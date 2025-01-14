# Listas são variáveis utilizadas para armazenar múltiplos elementos, diferente de variáveis normais, que armazenam apenas um elemento

lista = [1, 2, 3, 4, 5]

# A variável acima é uma lista contendo cinco valores
# Cada valor de uma lista contém um índice. Esse índice sempre começa em 0. Ou seja, na variável acima, no índice 0, está o valor 1. E no índice 1, o valor 2.

lista = list((1, 2, 3, 4, 5))

# Também é possível utilizar o método acima para criar uma lista, com a função list()

lista_string = list("Teste") # -> Gerará a seguinte lista: ["T", "e", "s", "t", "e"]

# Inserir uma string na função list(), será criada uma lista com um caracter do texto em cada índice, como visto acima

# É possível acessar um elemento específico da lista, indicando o índice em que ele está armazenado após o nome da variável entre colchetes
indice_0_lista = lista[0] # -> Pegando o valor 1, que está no índice 0 da lista [1, 2, 3, 4, 5]

# É possível visualizar o tamanho de uma lista utilizando a função len()

len(lista) # -> A lista possui 5 valores dentro dela, logo seu tamanho é 5

# As listas possuem diversos métodos que permitem modificá-las, listados a seguir

lista.append(6) # -> Insere um elemento no final da lista
# A lista iria de [1, 2, 3, 4, 5] para [1, 2, 3, 4, 5, 6]

lista.pop() # -> O método .pop() sem nenhum parâmetro remove o último elemento de uma lista
# A lista iria de [1, 2, 3, 4, 5, 6] para [1, 2, 3, 4, 5]

lista.pop(0) # -> O método .pop() com um parâmetro especificado irá excluir o valor que estiver no índice do número dado, nesse caso, excluirá o valor do índice 0
# A lista iria de [1, 2, 3, 4, 5] para [2, 3, 4, 5]

lista.insert(0, 1) # -> O método .insert() insere um valor em um índice especificado. O primeiro valor dado ao método é o índice, e o segundo é o elemento que será armazenado
# A lista iria de [2, 3, 4, 5] para [1, 2, 3, 4, 5]

lista.remove(1) # -> O método .remove() remove o valor especificado em sua primeira ocorrência. Então, o valor 1 será removido da lista na primeira vez que aparece.
# A lista iria de [1, 2, 3, 4, 5] para [2, 3, 4, 5]

lista.index(2) # -> O método .index() indica o índice em que está um valor dado como parâmetro.
# Como a lista está no formato [2, 3, 4, 5], esse método retornaria o valor 0, pois é o índice em que está o valor 2 na lista

sum(lista) # -> Por fim, temos a função sum(), que somará todos os valores presentes na lista.
# A lista possui os valores [2, 3, 4, 5], logo, essa função retornará 14

# Exercício utilizando listas -> Um pouco mais avançado
# Escreva um programa em python que leia o nome de cada produto comercializado por um vendedor, a respectiva quantidade em estoque e o valor unitário. O programa deverá:
# a) Imprimir o nome do produto mais caro (considerar mais de um produto com mesmo valor).
# b) Imprimir o valor total (em reais) de cada produto armazenado.
# c) Imprimir o valor total (em reais) armazenado em estoque.

# Criando as listas para armazenar os valores e a variável de soma do preço total de todos os produtos em estoque
produto = []
estoque = []
preco = []
val_tot_prod = []
mais_caros = []

# Perguntado quantos produtos distintos o usuário colocará para utilizar esse valor no laço de repetição
quant_prods = int(input("Insira quantos tipos de produtos serão inseridos: "))

# Laço de repetição "for" para armazenar nas listas, através do .append(), os valores pedidos
for i in range(quant_prods):
    produto.append(input("Insira o nome do produto: "))
    estoque.append(int(input(f"Insira a quantidade de estoque do produto '{produto[i]}': ")))
    preco.append(float(input(f"Insira o preço de cada unidade do produto '{produto[i]}': ")))
    val_tot_prod.append(preco[i] * estoque[i])

# Laço de repetição "for" para descobrir o maior preço de um produto
maior = 0
for i in range(len(preco)):
    if preco[i] > maior:
        maior = preco[i]

# Laço de repetição "for" para descobrir os produtos que tem o valor do maior preço e inseri-los em uma lista
for i in range(len(produto)):
    if preco[i] == maior:
        mais_caros.append(produto[i])

# Impressão de todos os dados coletados e processados

# Imprimindo o nome do(s) produto(s) mais caro(s)
print("")
if len(mais_caros) == 1:
    print(f"O produto mais caro é {mais_caros[0]}")
else:
    print(f"Os produtos mais caros são: ")
    for i in range(len(mais_caros)):
        print({mais_caros[i]}, end="") # -> o atributo end="" serve apenas para a impressão continuar na mesma linha em todas as repetições do loop
print("")

for i in range(len(produto)):
    print(f"O valor total armazenado em estoque do produto {produto[i]} é: {val_tot_prod[i]}")
print("")

print(f"O valor total armazenado em estoque na loja é: {sum(val_tot_prod)}")