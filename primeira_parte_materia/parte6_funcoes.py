# Funções são blocos de códigos criados para serem chamados a qualquer momento do código, reduzindo redundâncias em códigos
# Por exemplo, você quer calcular a média de três alunos diferentes, mas repetir esse código três vezes seria redundante, então, é criada uma função

def nome_funcao():
    print("Bloco de código da função!")

# A palavra "def" seguida de um nome qualquer e parênteses é a maneira que se cria uma função.
# Porém, geralmente, os blocos de códigos de uma função não serão acessados sem serem chamados. Por isso, é necessário chamar a função da seguinte forma para executá-la:
nome_funcao() # -> Aqui, a função está sendo chamada, e o bloco de código dentro dela será executado

# Localização de variáveis (IMPORTANTE!)
# Variáveis criadas fora de uma função são chamadas de Variáveis Globais, e podem ser acessadas a qualquer momento no código
# Contudo, variáveis criadas dentro de uma função são as chamadas Variáveis Locais, e sua diferença é que só podem ser acessadas dentro da própria função

def funcao_exemplo():
    nova_variavel = "Essa é uma nova variável!"
    return nova_variavel

# Porém, utilizando "return" e colocando o nome de uma variável, a função retornará o valor que era local mas que agora poderá ser enviado para fora da função
# Para alocar o valor que a função está retornando, é necessário criar uma nova variável global

variavel_global = funcao_exemplo() # -> Nessa linha de código, a variável global criada recebe a string "Essa é uma nova variável!"
# Com isso, o valor que anteriormente era local, e só podia ser acessado dentro da função, se torna global e acessível

# Dentro dos parênteses de uma função, ficam os chamados Parâmetros
# Caso uma função precise dos valores de uma lista que é uma variável global para realizar alguma ação, essa lista deverá ser dada como parâmetro para a função

lista_numeros = [10, 20, 30, 40, 50]

# A seguinte função descobre o maior valor de uma lista qualquer, e retorna-o
def descobrir_maior(lista):
    maior = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    return maior

# Quando a função é criada solicitando um parâmetro (o que não é obrigatório, apenas necessário em alguns casos, como esse acima), o parâmetro deverá ser preenchido
# em sua chamada, como feito abaixo:

maior_global = descobrir_maior(lista_numeros)
# Acima, a variável global criada mais cedo, "lista_numeros", está sendo passada para a função como parâmetro, assumindo o lugar da variável "lista". O valor retornado está
# sendo armazenado na nova variável global criada: maior_global

# Exercício com funções
# Escreva um programa em Python para calcular as raízes de uma equação do segundo grau. O seu programa deverá ter uma função para calcular e retornar o
# valor do delta e também uma função para calcular e retornar as duas raízes da equação.

def calcular_delta(a, b, c):
    delta = b ** 2 - 4 * a * c
    return delta

def calcular_raizes(a, b, c, delta):
    raiz1 = (-1 * b + delta ** (1/2)) / 2 * a
    raiz2 = (-1 * b - delta ** (1/2)) / 2 * a
    return [raiz1, raiz2]

# Programa principal

print("Fórmula geral de uma equação de 2° grau: a * x² + b * x + c")
a = float(input("Insira o valor de 'a' da equação de segundo grau: "))
b = float(input("Insira o valor de 'b' da equação de segundo grau: "))
c = float(input("Insira o valor de 'c' da equação de segundo grau: "))

delta = calcular_delta(a, b, c)
raizes = calcular_raizes(a, b, c, delta)

print(f"O delta da equação dada é: {delta}")
print(f"As raízes da equação dada são: {raizes[0]} e {raizes[1]}")