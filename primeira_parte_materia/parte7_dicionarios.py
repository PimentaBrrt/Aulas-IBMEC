# Primeiramente, o que é um dicionário?
# Assim como listas, dicionários são uma maneira de armazenar valores em uma variável
# O conceito diferencial dos dicionários é que os elementos vêm em pares: O primeiro elemento é a chave e o segundo, o valor

# Para criar um dicionário, utilizamos chaves, e eles seguem a seguinte formtação para inserir a chave e o elemento:
dicionario = {"Chave1": "Valor1", "Chave2": "Valor2", "Chave3": "Valor3"}

# Também é possível criar um funcionário com a função dict() -> Pouco utilizado, mas colocando aqui por precaução
outro_dicionario = dict(Chave1="Valor1", Chave2="Valor2", Chave3="Valor3")

# Para acessar o valor 1, é necessário inserir o nome da variável com o nome da chave entre colchetes
print(dicionario["Chave1"]) # -> Essa linha de comando irá imprimir "Valor1", que é o valor atribuído à chave "Chave1"

# Para criar um novo par chave-valor dentro de um dicionário, é simples, como fiz abaixo:
dicionario["Chave4"] = "Valor4"
# Acima, nos referimos à chave4, uma nova chave, que antes era inexistente. Depois, inserimos um valor à ela

# Para remover um par chave-valor do dicionário, podemos utilizar a função pop com o nome da chave
dicionario.pop("Chave4")

# É preciso citar a semelhança de um Dataframe (Estrutura do Pandas que se consiste em uma tabela com dados) e um dicionário
# Um dicionário contendo listas como valor para as chaves nada mais é do que uma tabela

dicionario_tabela = {
    "Coluna_Nome": ["Marcelo", "Ângela", "Carlos"],
    "Coluna_Sobrenome": ["Mendes", "Rocha", "Campos"],
    "Coluna_Idade": [22, 46, 19]
}

# O dicionário acima possui 3 linhas e 3 colunas
# Cada chave possui uma lista, formando uma coluna, na qual os índices da lista (começando em 0) indicam a linha
# Para acessar um valor específico desse dicionário, é necessário citar o nome da chave e o índice do elemento

print(dicionario_tabela["Coluna_Nome"][0]) # -> Imprimirá o valor "Marcelo"
print(dicionario_tabela["Coluna_Idade"][2]) # -> Imprimirá o valor 19

# Para adicionarmos novos valores, podemos utilizar o método .insert(), inserindo primeiro próximo índice da lista e depois o valor
dicionario_tabela["Coluna_Nome"].insert(3, "Joana")
dicionario_tabela["Coluna_Sobrenome"].insert(3, "Mello")
dicionario_tabela["Coluna_Idade"].insert(3, 25)

# Acima, inseri no índice 3 (que ainda não tinha valores em nenhuma das listas) as informações sobre uma nova pessoa
print(dicionario_tabela) # -> Testando se a pessoa "Joana" foi inserida

# Exercício exemplo de dicionários

# Escreva um programa em python que leia um conjunto de palavras fornecidas pelo usuário da aplicação. O programa deverá
# imprimir as palavras fornecidas agrupadas por tamanho.

print("")
# Criando o dicionário
dic_palavras = {}

# Obtendo a sequência de palavras
palavras = input("Insira as palavras desejadas separadas por vírgula: ")
palavras = palavras.split(",") # -> Transforma o texto em uma lista de palavras
tam_palavras = []

# Retirando os caracteres de espaço
for i in range(len(palavras)):
  palavras[i] = palavras[i].strip()

# Pegando o tamanho de todas as palavras
for i in range(len(palavras)):
  if len(palavras[i]) not in tam_palavras:
    tam_palavras.append(len(palavras[i]))

# Colocando a lista "tam_palavras" em ordem crescente
for i in range(len(tam_palavras)):
  for j in range(len(tam_palavras) - 1):
    if tam_palavras[j] > tam_palavras[j + 1]:
      auxiliar = tam_palavras[j]
      tam_palavras[j] = tam_palavras[j + 1]
      tam_palavras[j + 1] =  auxiliar

# Criando as colunas
for i in range(len(tam_palavras)):
  dic_palavras[f"{tam_palavras[i]}"] = []

# Inserindo as palavras nas respectivas colunas
for i in range(len(palavras)):
    dic_palavras[f"{len(palavras[i])}"].append(palavras[i])

print("")
print(dic_palavras)