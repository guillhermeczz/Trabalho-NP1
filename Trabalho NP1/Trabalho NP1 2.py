def calcular_salario_vendedor():
    try:
        unidades_vendidas = int(input("Digite a quantidade de unidades vendidas: "))

        salario_fixo = 151.00
        comissao_por_unidade = 3.00

        salario_total = salario_fixo + (unidades_vendidas * comissao_por_unidade)

        print(f"\nO salário total do vendedor é: R$ {salario_total:.2f}")
    
    except ValueError:
        print("\nErro: Por favor, insira um número inteiro válido para as unidades vendidas.")

calcular_salario_vendedor()