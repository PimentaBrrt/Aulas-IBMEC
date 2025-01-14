# Definindo uma variável

x = 10

# Acima, estou criando uma variável "x". Para atribuir um valor à ela, eu coloco o sinal de = e coloco um valor depois. Esse valor pode ser um texto, um número
# ou até mesmo uma outra função. O nome de uma variável deve sempre começar com letra minúscula, não ter espaço e nem hífen

# Tipos de dados primitivos

string = "Olá!" # -> Uma string (str) é um texto qualquer
inteiro = int(10) # -> Um inteiro (int) é um número inteiro, positivo ou negativo
decimal = float(0.5) # -> Um número float é um número decimal
booleano = True # -> Uma varável booleana pode ser definida como True ou False

complexos = complex(2, 3) # -> Um número complexo pode ser definido através da função complex(), lido nesse caso como 2 + 3i
vazio = None # -> Tipo especial de dado que representa a ausência de valor

# Operações básicas em Python

a = 10
b = 5

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
exponenciacao =  a ** b
raiz = a ** (1 / b)
resto_divisao = a % b # -> Explicado em detalhes na parte 2
divisao_inteira = a // b # -> Explicado em detalhes na parte 2

# Exemplo de exercício (calculando área e perímetro de um triângulo)

# Pedindo para o usuário inserir o valor da base e da altura através da função "input()" e armazenando nas variáveis "base" e "altura"

base = float(input("Insira a base do triângulo: "))
altura = float(input("Insira a altura do triângulo: "))

# Realizando as operações e armazenando os resultados nas variáveis "area" e "perimetro" considerando um triângulo equilátero

area = base * altura / 2
perimetro = base * 3

# Imprimindo a variável "area" para o usuário no terminal através da função "print()"

print(area)

# Também é possível inserir texto, separando o por vírgula da variável para imprimi-la depois

print("O perímetro do triângulo equilátero é:", perimetro)

# Formatando um print utilizando a função "format()"

e = 10.5559
print("Imprimindo a variável 'e' com apenas duas casas decimais: ", format(e, ".2f"))

# Também é possível definir variáveis das seguintes formas

a = b = 2
a, b, c = 1, 2, 3