numerique_message = [14, 21, 13, 5, 18, 15, 20, 1, 20, 9, 15, 14]

numerique_en_texte = ''.join(chr(num + 64) for num in numerique_message)
print(numerique_en_texte)