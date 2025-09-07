
# SubtitleSync Translator

Translator of str files using googletrans API with Large File Support


## What It Does

- Translates SRT subtitle files
- Handles large files by splitting into chunks  
- Supports any language Google Translate supports
- Simple command line interface

## Usage

1. Run the script
2. Enter path to your SRT file
3. Enter target language code (e.g. 'fa' for Persian)
4. Get your translated SRT file

## Language Codes

| Language | Code |
|----------|------|
| Persian | fa |
| English | en |
| Spanish | es |
| French | fr |
| German | de |
| Arabic | ar |
| Turkish | tr |

## Requirements

- Python 3.7+
- googletrans package

```bash
pip install googletrans==4.0.0-rc1
```

## Project Structure

```
srt-translator/
├── main.py          # Main translation script
├── exporter.py      # File handling utilities
└── README.md        # This file
```

## Limitations

- Requires internet connection
- Subject to Google Translate API limits
- Large files may take some time

## License

MIT