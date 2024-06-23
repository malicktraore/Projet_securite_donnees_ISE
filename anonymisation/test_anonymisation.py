from anonymisation import mask_data, pseudonymize_data, delete_data, hash_data, substitute_data, generalize_data, randomize_data, encrypt_data, decrypt_data

# Exemple de masquage des données
print("Masquage des données :")
print(mask_data("123456789"))

# Exemple de pseudonymisation
print("\nPseudonymisation des données :")
print(pseudonymize_data("user@example.com"))

# Exemple de suppression
print("\nSuppression des données :")
print(delete_data("Some sensitive data"))

# Exemple de hachage
print("\nHachage des données :")
print(hash_data("Sensitive data"))

# Exemple de substitution
substitution_map = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 'u': 'ü'}
print("\nSubstitution des données :")
print(substitute_data("anonymisation", substitution_map))

# Exemple de généralisation
print("\nGénéralisation des données :")
print(generalize_data(12345, 10))

# Exemple de randomisation
print("\nRandomisation des données :")
print(randomize_data("random"))

# Exemple de cryptographie
print("\nCryptographie des données :")
encrypted = encrypt_data("Sensitive data")
print("Données chiffrées :", encrypted)
print("Données déchiffrées :", decrypt_data(encrypted))
