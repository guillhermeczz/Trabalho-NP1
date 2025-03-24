def calcular_novo_salario():
    try:
        # Entrada de dados
        salario_atual = float(input("Digite o seu salário atual: R$ "))
        percentual_aumento = float(input("Digite o percentual de aumento (%): "))

        # Processamento
        aumento = salario_atual * (percentual_aumento / 100)
        novo_salario = salario_atual + aumento

        # Saída de dados
        print(f"\nSeu aumento será de: R$ {aumento:.2f}")
        print(f"Seu novo salário será: R$ {novo_salario:.2f}")
    
    except ValueError:
        print("\nErro: Por favor, insira valores numéricos válidos.")

# Chamada da função
calcular_novo_salario()
