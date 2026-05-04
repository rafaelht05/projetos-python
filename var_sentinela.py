#Exemplo de uso da Variável Sentinela

while true:
    comando = input("Digite um comando - Para parar, digite 'Sair'")

if comando == "Sair":
    break
print(f"Executado:{comando}")
