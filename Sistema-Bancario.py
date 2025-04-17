
saldo = 1000.00
saques_diarios = 3
saques_diarios_realizados = 0
limite_de_saque = 500
saques = 0
depositos = 0
historico = []

while True:


 operacao = input("Digite a operacao desejada ").lower()

 if operacao == "sair":
    print("Programa encerrado")
    break
    

 elif operacao == "depositar":

    valor_de_deposito = float(input("Digite a valor a ser depositado "))

    if valor_de_deposito > 0:
        saldo += valor_de_deposito
        depositos += 1
        historico.append(f"Depósito: + R$ {valor_de_deposito:.2f}")

    else: 
       print("Somente depósitos maiores que R$ 00,00 são permitidos.")

 elif operacao == "sacar":

    valor_de_saque = float(input("Qual valor deseja sacar? "))

    exedeu_saque = saques_diarios_realizados >= saques_diarios 
    exedeu_limite = valor_de_saque > limite_de_saque
    sem_saldo = valor_de_saque > saldo

    if exedeu_saque:
        print("Limite de saques atingidos, tente novamente amanhã")

    elif exedeu_limite:
        print("Saque não autorizado, valor de R$ 500,00 exedido")

    elif sem_saldo:
        print("Saldo insuficiente")

    else:
        saldo -= valor_de_saque
        saques_diarios_realizados += 1
        saques += 1
        historico.append(f"Saque: - R$ {valor_de_saque:.2f}")
        print( f"Saque realizado, saldo restante: R$ {saldo:.2f}")
  
    
 elif operacao == "extrato":
        print("\n------------- EXTRATO -----------------")
        if historico:
            for item in historico:
                print(f"    {item}")
        else:
            print("    Nenhuma operação realizada.")
        print(f"    Saldo atual: R$ {saldo:.2f}")

else:
    print("Operação inválida")






   
           

