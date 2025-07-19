def text_to_binary(text):
    return ' '.join(format(ord(c), '08b') for c in text)

def binary_to_text(binary_str):
    try:
        return ''.join([chr(int(b, 2)) for b in binary_str.split()])
    except ValueError:
        return "[Message binaire invalide]"
