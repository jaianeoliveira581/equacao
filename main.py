import math
import time

def calcular_equacao1():

    a = float(input("DIGITE O VALOR DA CONSTANTE A: "))
    b = float(input("DIGITE O VALOR DA CONSTANTE B: "))
    print('Lembrando que a equação do primeiro grau é: y = ', a, ". x", b)
    raiz = (-b)/a
    print('O valor de x para que y seja 0 é: ', raiz ) 
    print('')
    yield raiz


def bhaskara(a, b, c):
            delta = (b**2) - (4*a*c)
            x1 = (((-1)*b) + (delta**0.5))/(2*a)
            x2 = (((-1)*b) - (delta**0.5))/(2*a)
            if delta == 0:
                print()
                print("Nossa equação do 2º Grau: ", a, ".x²", b, ".x", c, "= 0")
                print("Como Delta = 0, temos um único valor de raiz (X1 = x2): ", x1)
            elif delta > 0:
                print()
                print("Nossa equação do 2º Grau: ", a, ".x²", b, ".x", c, "= 0")
                print("Como Delta > 0, temos dois valores distintos de raízes: ", x1, "e", x2)
            else:
                print()
                print("Nossa equação do 2º Grau: ", a, ".x²", b, ".x", c, "= 0")
                print("Como Delta < 0, não temos raízes reais!")
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))
            
            yield bhaskara(a, b, c)


def Menu():
    while True:
       
        print(f'{'-'*20}Calculando equações do 1º e 2º Grau {'-'*20}\n')
        print('1. para calcular equação do 1º grau.')
        print('2. para calcular equação do 2º grau.')
        print('3. para sair do programa.\n')
        opcao = (input('Escolha uma opção:'))
        print('Carregando opção...')
        time.sleep(2)

        if opcao == '3':
            print('Saindo do programa...')
            time.sleep(2)

        elif opcao == '1':
            print ('Carregando dados para calcular equação do 1º Grau')
            time.sleep(2)
            print(f'o resultado da equação do primeiro grau é: {calcular_equacao1()}.\n')
            break
        elif opcao =='2':
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))
            print(f'O resultado da equação do segundo grau é:  {bhaskara(a,b,c)}')
            time.sleep(2)
            


if __name__ == "__main__":
    Menu()