"""
File Export Utilities for SRT Translator
Handles file saving operations and user interactions for saving translated files
"""

import os
from datetime import datetime

def save_translated_file(translated_text, original_file, lang):
    """
    Save translated text to a new SRT file with timestamped filename
    
    Args:
        translated_text (str): The translated text content to save
        original_file (str): Path to the original source file
        lang (str): Target language code used for translation
    
    Returns:
        str: Path to the saved file if successful, None if failed
    
    Example:
        >>> save_translated_file("translated content", "movie.srt", "fa")
        "movie_fa_123045.srt"
    """
    try:
        # Extract filename and extension from original file
        name, ext = os.path.splitext(original_file)
        
        # Create new filename with language code and timestamp
        timestamp = datetime.now().strftime('%H%M%S')
        new_name = f"{name}_{lang}_{timestamp}{ext}"
        
        # Save file with UTF-8 encoding to support special characters
        with open(new_name, 'w', encoding='utf-8') as f:
            f.write(translated_text)
        
        print(f" File saved successfully: {new_name}")
        return new_name
        
    except PermissionError:
        print(" Permission denied: Cannot write to file")
        return None
    except Exception as e:
        print(f" Error saving file: {e}")
        return None

def ask_save_path(original_file, lang):
    """
    Prompt user for file save location with intelligent default naming
    
    Args:
        original_file (str): Path to the original source file
        lang (str): Target language code for translation
    
    Returns:
        str: User-selected file path with proper file extension
    
    Notes:
        - Automatically adds .srt extension if missing
        - Provides default naming convention: originalname_lang.srt
    """
    # Generate default filename using original name and language code
    name, ext = os.path.splitext(original_file)
    default_name = f"{name}_{lang}{ext}"
    
    print(f"\n Default save location: {default_name}")
    print("Enter custom filename or press Enter to accept default")
    
    # Get user input for filename
    user_input = input("New filename: ").strip()
    
    if user_input:
        # Ensure the filename has .srt extension
        if not user_input.endswith('.srt'):
            user_input += '.srt'
        return user_input
    else:
        # Use default filename if user presses Enter
        return default_name