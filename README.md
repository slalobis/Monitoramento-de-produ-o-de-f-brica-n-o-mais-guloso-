# Programa/Código em python de Monitoramento de produção de funcionários na fábrica
O programa feito tem a função de monitorar a produção dos funcionários da fábrica durante 16 horas que são registradas em valores. Além do programa guardar horários ele também pode calcular a produção total, fazer a média de produção por hora, identificar os horários mais produtivos e menos produtivos e também podendo detectar quedas na produção.
O que é utilizado nesse código
Lista, Loops, if's, .append e print

# Lista
Onde é armazenado os horários dos funcionarios, que quando eles batem o seu ponto é salvo na lista deixando assim todos os dados armazenados

lista = []

# Loops
O Loop é utilizado na lista para pedir sempre o novo horário a ser guardado pelo funcionário assim tendo acesso as 16 horas que são trabalhadas

 for i in range (16):          #Loop para pedir uma certa quantidade de informações desejadas
    producao = int(input("Digite a produção da hora "))     #input para colocar dados
    
# .Append
Trabalha junto com o loop, fazendo que todo horário armazenado sejá colocado como o ultimo na lista

  lista.append (producao)

# If's
If's foram usados para dizer as horas mais produtivas e menos produtivas, com um simples código (Se(if) produção for maior que hora_mais_produtiva, então hora_mais_produtiva é igual a produção. E se(if) produção for menor que hora_menos produtiva, então hora_menos_produtiva é igual a produção), assim obtendo 2 resultados para hora mais produtiva e menos produtiva

for producao in lista:                 
    if producao > hora_mais_produtiva:  
        hora_mais_produtiva = producao
    if producao < hora_menos_produtiva:  
        hora_menos_produtiva = producao
    
# Print
Para mostrar os resultados como:
Horas produzidas
Média de horas
Horas mais produtivas
Horas menos produtivas
Quantidade de quedas nos horários

Então com o código finalizado, funciona como o um sistema de monitoramento onde que toda vez que é batido o ponto um novo dado é armazenado, onde esse programa faz os calculos mostrados acima para dizer os horários do funcionário.
