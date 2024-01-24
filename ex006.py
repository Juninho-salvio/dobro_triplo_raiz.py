# Crie um algoritmo que leia um número e mostre o seu dobro, triplo
# e raiz quadrada
n1 = int(input('Digite um numero: '))
print(type(n1))

d = n1 * 2
t = n1 * 3
r = n1 ** (1/2) # tem que ter parenteses primeiro.

print('o numero é {}, \n seu dobro {}, \n seu triplo {}, \n raiz quadrada \033[4;35m{:.2f}\033[m' .format(n1, d, t, r))
