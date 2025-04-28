from cryptography.fernet import Fernet

# Gera uma chave de sessão
key = Fernet.generate_key()
cipher = Fernet(key)

# Mensagem
texto = b"Mensagem Secreta!"

# Criptografar
texto_criptografado = cipher.encrypt(texto)
print("Criptografado:", texto_criptografado)

# Descriptografar
texto_original = cipher.decrypt(texto_criptografado)
print("Original:", texto_original)
