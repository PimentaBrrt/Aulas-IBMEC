# O python possui duas operações especiais: o resto de divisão e a divisão inteira

a = 10
b = 2

# Resto de divisão -> faz o cálculo da divisão de a por b, porém, o resultado é o resto da divisão
resultado = a % b

# Exemplo de dois casos
resultado1 = 10 % 2 # -> O resultado dessa conta é 0, pois o resto da divisão de 10 por 2 é 0
resultado2 = 12 % 5 # -> O resultado dessa conta é 2, pois o resto da divisão de 12 por 5 é 2

print("Resultado de 10 % 2:", resultado1)
print("Resultado de 12 % 5:", resultado2)

# Divisão inteira -> faz o cálculo da divisão de a por b, porém, o resultado é apenas o quociente puro, ignorando o resto da divisão
resultado = a // b

# Exemplo de dois casos
resultado1 = 10 // 2 # -> O resultado dessa conta é 5, pois o quociente da divisão de 10 por 2 é 5
resultado2 = 16 // 5 # -> O resultado dessa conta é 3, pois o quociente da divisão de 16 por 5 é 3. O resto dessa divisão, que é 1, é ignorado

print("Resultado de 10 // 2:", resultado1)
print("Resultado de 16 // 5:", resultado2)

# Exemplo de exercício utilizando resto de divisão e divisão inteira

# O desafio é fazer um programa que leia um valor de três dígitos. O programa deverá exibir o valor da dezena do número informado.

# Lendo um valor inteiro digitado pelo usuário
numero = int(input("Insira um valor contendo três digitos: "))

# Utilizando divisão inteira e resto de divisão para separar o digito do meio dos outros dois
passo1 = numero // 10 # -> Primeiro, o número sofre uma divisão inteira por 10. Ex: 568 // 10 = 56 (O resto 8 é ignorado)
dezena = passo1 % 10 # -> Depois, o número sofre outra divisão, na qual apenas o resto será retornado. Ex: 56 % 10 = 6 (O quociente 5 é ignorado)

print("O valor da casa de dezena do número", numero, "é:", dezena)

# Utilizando o print(f) para formatar uma impressão

print(f"O valor da casa de dezena do número {numero}, inserido pelo usuário, é: {dezena}") # -> colocando o "f", é possível escrever trazendo as variáveis entre chaves