"""
SRT Subtitle Translator
A tool for translating SRT subtitle files using Google Translate API
"""

import asyncio
from googletrans import Translator
import argparse
from exporter import save_translated_file, ask_save_path

# Global variable for text content
text = ""

def split_text_into_chunks(text, max_chunk_size=4500):
    """
    Split large text into smaller chunks for API processing
    
    Args:
        text (str): The input text to split
        max_chunk_size (int): Maximum size of each chunk (default: 4500 characters)
    
    Returns:
        list: List of text chunks
    """
    chunks = []
    current_chunk = ""
    
    # Split text into lines to preserve line breaks
    lines = text.split('\n')
    
    for line in lines:
        # Check if adding this line would exceed chunk size
        if len(current_chunk) + len(line) + 1 <= max_chunk_size:
            current_chunk += line + '\n'
        else:
            # Save current chunk and start new one
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = line + '\n'
    
    # Add the last chunk if it exists
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

async def translate_text(text, dest_lang='fa', src_lang='auto', max_chunk_size=4500):
    """
    Translate text by splitting into chunks and processing each chunk
    
    Args:
        text (str): Text content to translate
        dest_lang (str): Target language code (default: 'fa' for Persian)
        src_lang (str): Source language code (default: 'auto' for auto-detection)
        max_chunk_size (int): Maximum chunk size for API requests
    
    Returns:
        str: Translated text content
    """
    # Split text into manageable chunks
    chunks = split_text_into_chunks(text, max_chunk_size)
    
    translator = Translator()
    translated_chunks = []
    
    print(f"chunks count : {len(chunks)}")
    
    # Process each chunk individually
    for i, chunk in enumerate(chunks, 1):
        print(f" chunks translating {i} / {len(chunks)}...")
        
        try:
            # Translate the current chunk
            translation = await translator.translate(chunk, dest=dest_lang, src=src_lang)
            translated_chunks.append(translation.text)
        except Exception as e:
            # If translation fails, keep original text and show error
            print(f"error when translating chunk {i}: {e}")
            translated_chunks.append(chunk)  # Fallback to original text
    
    # Combine all translated chunks
    final_translation = '\n\n'.join(translated_chunks)
    return final_translation

def get_file(srt_path, lang):
    """
    Main function to read, translate, and save SRT file
    
    Args:
        srt_path (str): Path to the source SRT file
        lang (str): Target language for translation
    """
    print("processing (get file)...")
    
    # Read the source SRT file
    with open(srt_path, "r", encoding="utf-8") as txt:
        text = txt.read()
        
    # Translate the text content
    translated_text = asyncio.run(translate_text(text, dest_lang=lang))
    
    # Ask user for save location
    save_path = ask_save_path(srt_path, lang)
    
    # Save the translated file
    save_file = save_translated_file(translated_text, save_path, lang=lang)
    
    if save_file: 
        # File saved successfully
        print(f"srt saved in : {save_path}")
    else:
        # File save failed
        print("sorry. can not save this file")

if __name__ == "__main__": 
    # Get user input for file path and target language
    srt_path = input("enter srt path : ")
    lang = input("whats translate lang?(en, fa, ...) : ")
    
    # Start the translation process
    get_file(srt_path, lang)