def obter_numeros():
    numeros = []
    for i in range(5):
        while True:
            try:
                numero = int(input(f"Digite o número {i+1}: "))
                numeros.append(numero)
                break  # Saímos do loop se a entrada for válida
            except ValueError:
                print("Por favor, insira um número inteiro válido.")
    return numeros

# Executando a função e exibindo a lista de números válidos
lista_numeros = obter_numeros()
print("Lista de números válidos inseridos:", lista_numeros)
