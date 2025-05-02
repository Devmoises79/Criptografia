# 🔐 Criptografia Simples com Python (Fernet)

Este é um exemplo prático de criptografia e descriptografia de mensagens usando a biblioteca `cryptography` com o algoritmo **Fernet**. Ele mostra como gerar uma chave, criptografar uma mensagem e depois recuperar o texto original.

## 📌 Funcionalidades

- Geração de chave secreta (chave simétrica)
- Criptografia de uma mensagem (em bytes)
- Descriptografia usando a mesma chave

## 🧠 Conceito

O algoritmo **Fernet** implementa criptografia simétrica segura baseada em AES, com:

- Confidencialidade (criptografia)
- Autenticidade (assinatura da mensagem)

Tudo isso de forma simples e segura.

## 🚀 Como executar

1. Instale a biblioteca necessária:

```bash
pip install cryptography
```

# Execute o script: #

python criptog.py
Você verá no terminal a mensagem criptografada e, em seguida, o texto original descriptografado.

## 📄 Exemplo de saída ##


´´´bash
Criptografado: b'gAAAAABl...'
Original: b'Mensagem Secreta!'
´´´

## 📁 Arquivo principal 
criptog.py: script contendo todo o código de criptografia e descriptografia.

## 📚 Tecnologias e bibliotecas
cryptography: biblioteca segura e moderna de criptografia para Python.

## ⚠️ Observações
A chave gerada com Fernet.generate_key() é única a cada execução.

Não é possível recuperar a mensagem se a chave for perdida.

Sempre guarde a chave em local seguro se for usá-la em sistemas reais.

## 🔐 Segurança
Este script é apenas um exemplo educacional. Para aplicações reais, use boas práticas de gerenciamento de chaves e segurança.
