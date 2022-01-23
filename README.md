# LSB Steganography utility
### SImple utility for encoding and decoding text inside images using LSB method.

## Installation
```bash
pip3 install -r requirements.txt
```

### Usage
Decoding:
```bash
steganography.py -m decode -i input.png
```
Encoding:
```bash
  steganography.py -m encode -o output.png -p Hello -i input.jpg
```

