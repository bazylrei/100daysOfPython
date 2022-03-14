alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        if not letter in alphabet:
            encrypted_text += letter
            continue
        letter_index = alphabet.index(letter)
        encrypted_letter_index = (letter_index + shift) % (len(alphabet) - 1)
        encrypted_letter = alphabet[encrypted_letter_index]
        encrypted_text += encrypted_letter
    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)


if direction == "encrypt":
    print(encrypt(text, shift))
elif direction == "decrypt":
    print(decrypt(text, shift))
