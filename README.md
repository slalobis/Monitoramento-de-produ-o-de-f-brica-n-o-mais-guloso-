# Análise de Produção por Hora

Este projeto em Python realiza a coleta e análise de dados de produção ao longo de 16 horas, fornecendo métricas importantes como total produzido, média, maior e menor produção, além da quantidade de quedas ao longo do período.

# Funcionalidades

O programa executa as seguintes tarefas:

Solicita ao usuário a produção de 16 horas consecutivas
Armazena os dados em uma lista

Calcula:

📈• Produção total
📊• Média da produção
🔝• Hora mais produtiva
🔻• Hora menos produtiva
⚠️• Quantidade de quedas na produção
🧠• Lógica do Programa

Coleta de dados
Um loop (for) solicita 16 valores de produção ao usuário.
Cada valor é armazenado em uma lista.
Cálculo da produção total e média
A produção total é acumulada a cada entrada.
A média é calculada com base na soma total e quantidade de dados.
Identificação de extremos
O programa percorre a lista para identificar:
Maior valor (hora mais produtiva)
Menor valor (hora menos produtiva)
Contagem de quedas
Compara cada valor com o anterior
Conta quantas vezes a produção diminuiu

🖥️ Exemplo de Uso
Digite a produção da hora 10
Digite a produção da hora 15
Digite a produção da hora 12
...

Saída esperada:
A produção total foi de: 200
A média da produção é de: 12.5
A hora mais produtiva teve o valor de: 20
A hora menos produtiva teve o valor de: 5
A quantidade de quedas de produção foi de: 6

📦 Requisitos
Python 3.18

▶️ Como executar
Salve o código em um arquivo, por exemplo: producao.py
Execute no terminal:
python producao.py
