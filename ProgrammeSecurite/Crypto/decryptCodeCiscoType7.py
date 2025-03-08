def dechiffrer_type7(mot_de_passe_chiffre):
    # La clé XOR utilisée par Cisco pour le chiffrement de type 7
    cle_xor = 0x5F

    # Le mot de passe chiffré commence par un en-tête fixe de 2 octets
    if mot_de_passe_chiffre[:2] != '07':
        raise ValueError("Ce n'est pas un mot de passe chiffré de type 7 valide")

    # Extraire la partie chiffrée du mot de passe
    partie_chiffree = mot_de_passe_chiffre[2:]

    # Déchiffrer le mot de passe
    mot_de_passe_dechiffre = []
    for i in range(0, len(partie_chiffree), 2):
        # Convertir chaque paire de chiffres hexadécimaux en un entier
        caractere_chiffre = int(partie_chiffree[i:i+2], 16)
        # XOR avec la clé pour déchiffrer
        caractère_déchiffré = caractere_chiffre ^ cle_xor
        # Ajouter le caractère déchiffré au résultat
        mot_de_passe_dechiffre.append(chr(caractère_déchiffré))

    # Joindre la liste de caractères en une chaîne
    return ''.join(mot_de_passe_dechiffre)

# Exemple d'utilisation
mot_de_passe_chiffre = '07025017705B3907344E'
mot_de_passe_dechiffre = dechiffrer_type7(mot_de_passe_chiffre)
print("Mot de passe déchiffré :", mot_de_passe_dechiffre)
