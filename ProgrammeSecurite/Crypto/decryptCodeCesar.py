def decrypt_code_cesar(text, decal):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            is_uppercase = char.isupper()
            decalage = ord(char.lower()) - decal
            if decalage < ord('a'):
                decalage += 26
            decrypted_text += chr(decalage).upper() if is_uppercase else chr(decalage)
        else:
            decrypted_text += char
    return decrypted_text

text = input("Entrez le code à décrypter: ")
decrypted_messages = {decal: decrypt_code_cesar(text, decal) for decal in range(1, 26)}
print(decrypted_messages)