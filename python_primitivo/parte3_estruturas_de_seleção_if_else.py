# Estruturas de seleção são utilizadas para executar um bloco de código caso um teste seja verdadeiro

# Checando se a variável x é igual a 10 e executando um print caso seja

x = 10
if x == 10:
    print("x é 10")

# Ao realizar testes, há diferentes sinais para comparar uma variável e outro valor

if x > 10:
    print("X é maior que 10")

if x >= 10:
    print("X é maior ou igual a 10")

if x < 10:
    print("X é menor que 10")

if x <= 10:
    print("X é menor ou igual a 10")

if x != 10:
    print("X é diferente de 10")

# É possível realizar múltiplos testes em uma estrutura if utilizando "and" e "or"

# Utilizando o operador "and", ambos os testes devem ser verdadeiros para o bloco de código ser executado
if x > 10 and x < 20:
    print("X é um valor entre 10 e 20")

# Utilizando o operador "or", se um dos testes for verdadeiro, o bloco de código será executado
if x == 10 or x == 20:
    print("X é igual a 10 ou igual a 20")

# É possível, após uma estrutura "if", utilizar o elif faz outro teste em uma outra linha de código, que se for verdadeiro, rodará outro bloco de texto
# Pensar no if como "se" e elif como "e se" é uma boa forma de visualizar a relação entre essas estruturas

if x == 10:
    print("X é 10")
elif x == 15:
    print("X é 15")

# No caso acima, se x for igual a 10, ele imprime que x é 10, e se for igual a 15, imprime que x é 15

# Por fim há a estrutura de seleção "else", que complementa o "if" e "elif". O caso "else" executa um bloco de código caso todos os testes anteriores forem falsos
# Ou seja, o "else" pode ser traduzido como "senão"
# if (se) o primeiro teste for verdadeiro, é rodado o bloco do "if". Elif (e se) os conseguintes testes forem verdadeiros, é rodado o bloco do "elif" que for verdadeiro.
# else (senão), ou seja, se o "if" e todos "elifs" forem falsos, o código do "else" será executado.

if x == 10:
    print("X é 10")
elif x == 15:
    print("X é 15")
else:
    print("X é diferente de 10 e diferente de 15")

# Exemplo de exercício
# Crie um programa que leia três valores de lados de um triângulo e descubra se o triângulo é equilátero, isósceles ou escaleno


# Recebendo os valores dos lados e criando a variável que armazenará o tipo de triângulo
lado1 = float(input("Insira o primeiro lado: "))
lado2 = float(input("Insira o segundo lado: "))
lado3 = float(input("Insira o terceiro lado: "))
tipo_triangulo = ""

# Checando o tipo de triângulo com if, elif e else
if lado1 == lado2 and lado2 == lado3:
    tipo_triangulo = "Equilátero"
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    tipo_triangulo = "Escaleno"
else:
    tipo_triangulo = "Isósceles"

# Imprimindo no console o tipo de triângulo
print("O tipo de triângulo inserido é:", tipo_triangulo)