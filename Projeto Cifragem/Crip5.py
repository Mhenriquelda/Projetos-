def criptografa(frase, chave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    frase_criptografada = ''

    for char in frase:
        if char.isalpha():
            posição = alfabeto.find(char.lower())
            nova_posição = (posição + chave) % len(alfabeto)
            if char.isupper():
                frase_criptografada += alfabeto[nova_posição].upper()
            else:
                frase_criptografada += alfabeto[nova_posição]
        else:
            frase_criptografada += char

    return frase_criptografada


def descriptografa(frase, chave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    frase_descriptografada = ''

    for char in frase:
        if char.isalpha():
            posição = alfabeto.find(char.lower())
            nova_posição = (posição - chave) % len(alfabeto)
            if char.isupper():
                frase_descriptografada += alfabeto[nova_posição].upper()
            else:
                frase_descriptografada += alfabeto[nova_posição]
        else:
            frase_descriptografada += char

    return frase_descriptografada


print("Escolha uma opção:")
print("1 - Criptografar uma frase")
print("2 - Descriptografar uma frase")

opcao = int(input("Digite o número da opção desejada: "))

if opcao == 1:
    sentenca = input('Insira uma frase para criptografar: ')
    numero = int(input('Digite um número para ser a chave: '))
    cripto = criptografa(sentenca, numero)
    print('Frase criptografada: ', cripto)

elif opcao == 2:
    sentenca = input('Insira uma frase criptografada: ')
    numero = int(input('Digite o número da chave usada na criptografia: '))
    descripto = descriptografa(sentenca, numero)
    print('Frase descriptografada: ', descripto)

else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")
