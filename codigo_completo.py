import os
import time

#informações gerais da conta
saldo = 0
limite = 500
extrato = []
limite_saques = 3

#funcao deposito

def depositar(valor):
    global saldo
    float(valor)
    saldo += valor
    extrato.append(f'Deposito: {valor}')
    print('Operação Concluida')
    
#funcao saque 

def sacar(valor):
    global limite_saques
    global saldo
    float(valor)
    if limite_saques > 0 and valor <= limite:
        if saldo >= valor:
            saldo -= valor
            extrato.append(f'Saque: {valor}')
            print('Operação Concluida')
            limite_saques -= 1
        else:
            print('Saldo Insuficiente')
    else:
        if limite_saques == 0 and valor > limite:
            print('Saque Não Concluido! Limite de Saques e Limite de Saque Ultrapassado.')
        elif limite_saques == 0:
            print('Saque Não Concluido! Limite de Saques Ultrapassado.')
        elif valor > limite:
            print('Saque Não Concluido! Valor Acima do Limite Permitido')
            
#funcao extrato

def ver_extrato():
    if len(extrato) != 0:
        print('\n---Extrato da Conta---\n')
        for operacoes in extrato:
            print(operacoes)
            
        print(f'Saldo Atual de: R${saldo:.2f}\n')
        print('-----------------------')
    else:
        print('Não foram realizadas movimentações')
            
#menu

while True:

    print('''
    
        ----- BANCO -----
          1- Depositar
          2-  Sacar  
          3- Extrato 
          4-  Sair
        -----------------
''')

    opcao = int(input('Digite o código da Operação: '))
    
    if opcao == 1:
        os.system('clear')
        valor_deposito = float(input('Digite o valor para deposito: '))
        depositar(valor_deposito)
        time.sleep(2)
    elif opcao == 2:
        os.system('clear')
        valor_saque = float(input('Digite o valor para sacar: '))
        sacar(valor_saque)
        time.sleep(2)
    elif opcao == 3:
        os.system('clear')
        ver_extrato()
        time.sleep(5)
    elif opcao == 4:
        os.system('clear')
        print('Obrigado! Operações encerradas')
        break
    else:
        os.system('clear')
        print('Opção Invalida! Digite uma opção valida')
        time.sleep(2)