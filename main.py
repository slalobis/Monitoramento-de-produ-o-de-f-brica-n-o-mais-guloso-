lista = []              #Uma lista Vazia para armazenar os dados da produção
producao_total = 0        #As duas variaveis uma de soma e a outra um contador de vezes que a produção caiu
queda_producao = 0

for i in range (16):       #Loop de 16 para as horas
    producao = int(input("Digite a produção da hora "))   #Aqui ele pede a produção do Usuário
    lista.append (producao)       #Adiciona o valor que foi colocado acima

    producao_total += producao    #Faz a Soma na produção total

    media = producao_total / len(lista)    #Calcula a média

    hora_mais_produtiva = lista[0]    #Esses 2 definem os valores iniciais (primeiro valor da lista)
    hora_menos_produtiva = lista[0]

for i in lista:
    if producao > hora_mais_produtiva:
        hora_mais_produtiva = producao

    if producao < hora_menos_produtiva:
        hora_menos_produtiva = producao

for i in range(1, len(lista)):
    if lista[i] < lista[i - 1]:
        queda_producao += 1

print(f"Produção total foi de: {producao_total}")
print(f"A média da produção foi de: {media}")
print(f"A hora mais produtiva foi: {hora_mais_produtiva}")
print(f"A hora menos produtiva foi: {hora_menos_produtiva}")
