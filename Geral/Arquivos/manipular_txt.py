# 'r' -> Usado somente para ler algo
# 'w' -> Usado somente pata escrever algo
# 'r+' -> Usado para ler e escrever algo
# 'a' -> Usado para acrescentar algo

# Ler e printar o que está no arquivo .txt

with open('email.txt', 'r', encoding='utf-8') as arquivo:
    email = arquivo.read()
print(email)

with open('email.txt', 'r', encoding='utf-8') as arquivo:
    mensagem = arquivo.readlines()
print(mensagem)

for linha in mensagem:
    if "@" in linha:
        print(linha)


# Escrever em um arquivo de texto

with open('senha.txt','w') as arquivo:
    arquivo.write("456789")

# Adiciona no arquivo
with open('email.txt','a') as arquivo:
    arquivo.write("\nmariajose@gmail.com")
