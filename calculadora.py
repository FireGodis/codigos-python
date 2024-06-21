
import os

def limpar():
    # Verifica o sistema operacional
    if os.name == 'nt':  # Se for Windows
        os.system('cls')
    else:  # Se for Unix ou MacOS
        os.system('clear')



def adicao (x, y):

    return x + y
def subtracao(x, y):
    
    return x - y

def multiplicacao(x, y):
   
    return x * y

def divisao(x, y):
   
    if y == 0:
        return "Não é possivel fazer divisão por zero"
    return x / y
    


def calculadora():
    programa = 1
    limpar()

    while(programa != 0):
         print("Selecione a operação:")
         print("1. Adição")
         print("2. Subtração")
         print("3. Multiplicação")
         print("4. Divisão")

         escolha = input("Digite numero 1/2/3/4: ")

         if escolha in(['1', '2', '3', '4']):
             limpar()

             num1 = float(input("Digite o primeiro numero: "))
             
             num2 = float(input("Digite o segundo numero: "))
             limpar()
             if escolha == '1':
                 
                 print(f"{num1} + {num2} = {adicao(num1, num2)}")
    
             elif escolha == '2':
                 
                 print(f"{num1} + {num2} = {subtracao(num1, num2)}")

             elif escolha == '3':
                 
                 print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")

             elif escolha == '4':
                 
                 print(f"{num1} / {num2} = {divisao(num1, num2)}")

         else:
             limpar()
             print("essa não é uma resposta válida")

     
         programa = int(input("Deseja continuar no programa? 0 para sair/1 para ficar: "))
         limpar()
    
       
   
   



if __name__ == "__main__":
    calculadora()