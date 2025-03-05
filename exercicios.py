### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
vendas = [
    {"quantidade": 10, "preco": 20.5},
    {"quantidade": 5, "preco": 15.0},
    {"quantidade": -1, "preco": 15.0},
    {"quantidade": 5, "preco": -115.0},
    {"quantidade": 5, "preco": 15.0},
    {"quantidade": 3, "preco": 10.0}
]

erros = [venda for venda in vendas if int(venda["quantidade"]) < 0 or int(venda["preco"]) <0]

# Exibir a lista com os erros
for erro in erros:
    print(erro)
    
### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# Lista de temperaturas
temperaturas = [10, 58, 22, 30, 15, 25, 5, 28, 20, 12]

# Classificar cada temperatura na lista
for temperatura in temperaturas:
    if temperatura <= 15:
        print(f"Temperatura {temperatura}: Baixa")
    elif 15 < temperatura <= 25:
        print(f"Temperatura {temperatura}: Normal")
    elif temperatura > 25:
        print(f"Temperatura {temperatura}: Alta")
    else:
        print(f"Temperatura {temperatura}: Incorreta!")

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

logs = [
    {"timestamp": "2021-06-23 10:01:00", "level": "ERROR", "message": "Falha na conexão"},
    {"timestamp": "2021-06-24 11:00:00", "level": "WARN", "message": "Tipo variável"},
    {"timestamp": "2021-06-25 12:00:00", "level": "WARN", "message": "Tipo variável"},
    {"timestamp": "2021-06-26 13:10:00", "level": "ERROR", "message": "Falha na conexão"},
    {"timestamp": "2021-06-27 14:31:00", "level": "ERROR", "message": "Falha na conexão"},
    {"timestamp": "2021-06-28 15:32:00", "level": "FATAL", "message": "timeout"},
    {"timestamp": "2021-06-29 16:00:00", "level": "ERROR", "message": "Falha na conexão"},
    {"timestamp": "2021-06-30 17:30:00", "level": "WARN", "message": "Tipo variável"}
]

erros = [log for log in logs if log["level"] == "ERROR"]

# Exibir a lista com os erros
for erro in erros:
    print(erro)

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
logs = [
    {"nome": "Vassa", "idade": "54", "profissao": "motorista"},
    {"nome": "Jones", "idade": "19", "profissao": "motoboy"},
    {"nome": "Fabio", "idade": "29", "profissao": "caixa"},
    {"nome": "Julio", "idade": "40", "profissao": "gerente"},
    {"nome": "Alfredo", "idade": "88", "profissao": "aposentado"},
    {"nome": "Gomes", "idade": "39", "profissao": "mecanico"},
    {"nome": "Enzo", "idade": "9", "profissao": "estudante"},
    {"nome": "Valentina", "idade": "7", "profissao": "estudante"}
]

erros = [log for log in logs if int(log["idade"]) >= 18 and int(log["idade"]) <= 65]

# Exibir a lista com os erros
for erro in erros:
    print(erro)

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
logs = [
    {'valor': 12000, 'hora': 7},
    {'valor': 9999, 'hora': 19},
    {'valor': 1000, 'hora': 0},
    {'valor': 122000, 'hora': 10}
]

erros = [log for log in logs if int(log["valor"]) >= 10000 or (int(log["hora"]) < 9 or int(log["hora"]) > 18 )]

# Exibir a lista com os erros
for erro in erros:
    print(erro)

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
from collections import Counter
import string

def contar_palavras(texto):
    # Normalizar o texto: converter para minúsculas e remover pontuações
    texto = texto.lower()
    texto = texto.translate(str.maketrans('', '', string.punctuation))

    # Dividir o texto em palavras
    palavras = texto.split()

    # Contar as ocorrências de cada palavra
    contagem = Counter(palavras)

    return contagem

# Exemplo de uso
texto = """
Olá, mundo! Este um exercício de Python. A linguagem python é mais utilizada do Mundo, e como utilizamos Python neste mundo.
"""

contagem = contar_palavras(texto)

# Exibir a contagem de cada palavra
for palavra, quantidade in contagem.items():
    print(f"'{palavra}': {quantidade} veze(s)")

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
def normalizar_lista(lista):
    # Encontrar o valor mínimo e máximo da lista
    minimo = min(lista)
    maximo = max(lista)

    # Normalizar cada valor da lista
    lista_normalizada = [(valor - minimo) / (maximo - minimo) for valor in lista]

    return lista_normalizada

# Exemplo de uso
lista = [10, 20, 30, 40, 50, 60] #Lista normalizada: [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
lista_normalizada = normalizar_lista(lista)

print("Lista original:", lista)
print("Lista normalizada:", lista_normalizada)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
def filtrar_dados_faltantes(lista_usuarios, campo): #Filtra os dicionários que não contêm o campo especificado.
    return [usuario for usuario in lista_usuarios if campo not in usuario]

# Exemplo de uso
lista_usuarios = [
    {"nome": "Mario", "idade": 25, "email": "mario@example.com"},
    {"nome": "Jose", "idade": 30},  # Campo 'email' faltando
    {"nome": "Alfredo", "email": "alfredo@example.com"},  # Campo 'idade' faltando
    {"nome": "Marcos", "idade": 35, "email": "marcos@example.com"},
    {"nome": "Maria"}  # Campos 'idade' e 'email' faltando
]

# Filtrar usuários que não têm o campo 'email'
usuarios_faltando_email = filtrar_dados_faltantes(lista_usuarios, "email")
print("Usuários sem email:", usuarios_faltando_email)

# Filtrar usuários que não têm o campo 'idade'
usuarios_faltando_idade = filtrar_dados_faltantes(lista_usuarios, "idade")
print("Usuários sem idade:", usuarios_faltando_idade)

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
# Lista de temperaturas
numbers = [10, 58, 22, 30, 15, 25, 5, 28, 20, 12]

# Classificar cada temperatura na lista
for number in numbers:
    if number  % 2 == 0 :
        print(f"Número {number} é par !")

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
def total_vendas_por_categoria(vendas): 

    total_por_categoria = {}

    for venda in vendas:
        categoria = venda['categoria']
        valor = venda['valor']

        # Adiciona o valor à categoria correspondente
        if categoria in total_por_categoria:
            total_por_categoria[categoria] += valor
        else:
            total_por_categoria[categoria] = valor

    return total_por_categoria

# Exemplo de uso
vendas = [
    {"categoria": "Eletrônicos", "valor": 1000.30},
    {"categoria": "Roupas", "valor": 1500.00},
    {"categoria": "Eletrônicos", "valor": 300.20},
    {"categoria": "Alimentos", "valor": 50.10},
    {"categoria": "Roupas", "valor": 1001.00},
    {"categoria": "Alimentos", "valor": 75.00},
]

resultado = total_vendas_por_categoria(vendas)

# Exibir o total de vendas por categoria
for categoria, total in resultado.items():
    print(f"Categoria: {categoria}, Total de Vendas: R$ {total:.2f}")

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.