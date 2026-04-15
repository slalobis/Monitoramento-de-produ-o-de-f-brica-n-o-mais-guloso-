lista = []          #Lista Vazia para armazenar dados novos
producao_total = 0  #variavel do total da produção
queda_producao = 0  #variavel da queda da produção

for i in range (16):          #Loop para pedir uma certa quantidade de informações desejadas
    valor_hora = i + 1
    producao = float(input(f"Digite a produção da hora {valor_hora}: "))     #input para colocar dados
    lista.append (producao)           #Adiciona a informação ao final da lista
    producao_total += producao        #Ele soma na produção total que igual a produção
    
media = producao_total / len(lista)      #Média da produção total
    
valor_hora_mais_produtiva = lista[0] #Pega os maiores valores da lista e conta como hora mais produtiva
hora_mais_produtiva = 1
valor_hora_menos_produtiva = lista[0]   #Pega os menores valores da lista e conta como hora menos produtiva
hora_menos_produtiva = 1

for i in range(len(lista)):       #Esse documenta a quantidade de queda da produção dos dados informados da lista produção
    if lista[i] > valor_hora_mais_produtiva:
        valor_hora_mais_produtiva = lista[i]
        hora_mais_produtiva = i + 1
    
    if lista[i] < valor_hora_menos_produtiva:
        valor_hora_menos_produtiva = lista[i]
        hora_menos_produtiva = i + 1
    
    if lista[i] < lista[i - 1]:
        queda_producao += 1
        
print("\n" + "="*30)
print(f"{'RELATÓRIO DE PRODUÇÃO':^30}")
print("="*30)
print(f"Tempo decorrido: {valor_hora} hora(s)")
print(f"Produção Total: {producao_total:>8.2f}")
print(f"Média por Hora: {media:>8.2f}")
print("-"*30)
print(f"Pico de Produção: Hora {hora_mais_produtiva} ({valor_hora_mais_produtiva})")
print(f"Menor Produção: Hora {hora_menos_produtiva} ({valor_hora_menos_produtiva})")
print(f"Quedas Registradas: {queda_producao}")
print("="*30)
