# Importa os módulos necessários
import random
import string

# Pede ao usuário para escolher quantas letras, símbolos e números quer na senha
num_letters = int(input("How many letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like? "))
num_numbers = int(input("How many numbers would you like? "))

# Cria conjuntos de caracteres para letras, símbolos e números
letters = string.ascii_letters
symbols = string.punctuation
numbers = string.digits

# Inicializa uma lista vazia para armazenar os caracteres da senha
password_list = []

# Adiciona letras à lista
for _ in range(num_letters):
    password_list.append(random.choice(letters))

# Adiciona símbolos à lista
for _ in range(num_symbols):
    password_list.append(random.choice(symbols))

# Adiciona números à lista
for _ in range(num_numbers):
    password_list.append(random.choice(numbers))

# Embaralha a lista para misturar os caracteres
random.shuffle(password_list)

# Junta os caracteres para formar a senha
password = ''.join(password_list)

# Mostra a senha gerada
print("Your new password is: ", password)
