print("---------------------------------------")
print("Bem-vindo ao seu Jogo de Adivinhação")
print("---------------------------------------")

numero_secreto=76

chute_usuario = input("Digite seu chute:")
print("O número que você chutou foi:", chute_usuario)
chute= int (chute_usuario)

if(numero_secreto==chute):
    print("Você acertou o núemero Secreto :)")

else:
    print("Você errou :( \n Tente Novamente...")

print("------------")
print("Fim de Jogo!")
print("------------")
