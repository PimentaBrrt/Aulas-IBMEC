# Existem duas estruturas de repetição: "while" e "for"
# Geralmente, "while" é utilizado quando o número de repetições do laço não é pré-definido, enquanto o "for" é utilizado quando sabe-se o número de repetições

# Começando pelo "while", assim como nas estruturas de seleção, é necessário dar um teste à função
# Uma tradução do "while" seria "enquanto". Então, enquanto uma condição X for verdadeira, o bloco de código continuará se repetindo

x = 10
y = 0
while x > y:
    print("Esse é um laço de repetição.")
    y = y + 5

# O laço acima se repetirá duas vezes, já que a partir da terceira execução, o teste será falso, já que Y será igual a X.

# É preciso cautela criando laços de repetição com while, já que caso é possível cair em um laço de fim indefinido, ou um laço infinito.

# Contadores em laços de repetição "while"

contador = 0
z = 1
while contador < 3:
    z = z * 3
    contador += 1 # -> contador += 1 é a mesma coisa do que contador = contador + 1

# O laço acima possui um contador. Ele definirá quantas vezes o laço se repetirá. Nesse caso, 3 vezes.

temporaria = 1
while True:
    print(f"Essa é a execução número {temporaria}")
    temporaria += 1
    if temporaria > 10:
        break

# No laço acima, o valor booleano "True" faz o while se repetir indefinidamente. Contudo, após 10 repetições, quando a variável temporaria atingir 11, o comando
# "break" será executado. Esse comando quebra um laço de repetição e segue executando o resto do código.


# Seguindo para o "for", esse método geralmente conta com um número limitado de repetições, e uma variável sempre é criada e tem seu valor alterado a cada repetição

for i in range(3):
    print(f"O valor de i nessa repetição é: {i}")

# A variável "i" criada no laço acima só é acessível durante esse laço de repetição. A função "range()" define um alcance.

# range(3) significa que o valor de i será 0 na primeira repetição, 1 na segunda e 2 na terceira. Lembrando que o range, caso não seja especificado, começa no 0 e termina
# um número antes do valor dado.

# Caso queira especificar, o range() deverá ser construído da seguinte forma: range({começo}, {fim}, {salto})
# Por exemplo, com range(1, 10, 2), ele começa em 1 e termina em 10, pulando de 2 em 2 valores.

# Exercício utilizando "while"
# Crie um programa que imprima a soma de todos os números pares entre 1 e 100.

# Definindo o contador e a variável que armazenará a soma
contador = 1
soma = 0

# Laço de repetição que checará se o resto de divisão de todos os números é 0. Um número para dividido por 2 tem resto 0, então caso essa condição seja verdadeira, o número é
# adicionado à soma

while contador <= 100:
    if contador % 2 == 0:
        soma = soma + contador
    contador += 1

# Imprimindo a soma

print(f"O valor da soma = {soma}")

# Mais um exercício utilizando "while"
# Crie um programa que receba o nome de 3 alunos e suas notas em 2 provas. O programa deverá calcular a média das notas e checar se o aluno passou de ano. A média é 6.

# Criando o contador
contador = 1

# Laço de repetição que pedirá o nome e as notas de um aluno, calculará a média e fará uma checagem com "if" para imprimir se o aluno foi aprovado ou reprovado
while contador <= 3:
    nome = input("Insira o nome do aluno: ")
    nota1 = float(input(f"Insira a nota do aluno {nome} na prova 1: "))
    nota2 = float(input(f"Insira a nota do aluno {nome} na prova 2: "))
    print("") # -> Essa impressão vazia foi feita apenas para dar um espaçamento no terminal. Ou seja, é puramente visual, e não é importante para o funcionamento do programa
    media = (nota1 + nota2) / 2
    if media >= 6:
        print(f"O aluno {nome} foi APROVADO. Média final: {media}")
    else:
        print(f"O aluno {nome} foi REPROVADO. Média final: {media}")
    print("")
    contador += 1

# Exercício utilizando "for"
# Crie um programa que imprima a tabuada de um número qualquer inserido pelo usuário

# Fazendo um "input()" para receber o valor que realizaremos a tabuada
valor = int(input("Insira o valor que terá a tabuada calculada: "))

# Um laço criado para se repetir de 0 até 10. Lembrando que o valor de "i" no último laço será o valor inserido no range - 1
# A cada repetição, imprimirá uma linha informando o valor, o número que está multiplicando e o resultado
for i in range(11):
    print(f"{valor} x {i} = {valor * i}")

# Exercício utilizando ambos, "while" e "for"
# Faça um programa em Python que leia um número inteiro e positivo e imprima todos os seus divisores (positivos e negativos).

# Input para o valor inteiro e positivo
valor = int(input("Insira um valor inteiro e positivo: "))

# Checando se o valor é de fato positivo. O while é utilizado para sempre pedir que o valor seja renovado caso seja negativo.
while valor < 0:
    valor = int(input("Valor inválido. Insira um valor positivo: "))

# Fazendo um laço de repetição "for" para checar os divisores
for i in range(valor * -1, valor + 1): # -> O valor * -1 é para testar com os valores negativos, e o valor + 1 para testar com o próprio valor
    if i != 0: # -> Por estar passando por valores positivos e negativos, essa estrutura de seleção impede uma divisão por 0, que quebraria o programa
        if valor % i == 0:
            print(i)