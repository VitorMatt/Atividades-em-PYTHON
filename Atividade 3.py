# 3) Faça um programa que solicite o salário e os anos de serviço de um funcionário. 
# Se ele tiver mais de 5 anos de serviço, dê um bônus de 5% sobre o salário.

bonus_salario = 5

salario_usuario = 1000

anos_trabalhados = 4

valor_bonus = bonus_salario * salario_usuario / 100

salario_com_bonus = salario_usuario + valor_bonus

if anos_trabalhados > 5:
    
    print(f'Parabéns! Você ganhou um bônus de 5% no seu salário.\nSalário mensal: R$ {salario_usuario}\nValor bônus: +R$ {valor_bonus} (5%)\nSalário final com bônus: R$ {salario_com_bonus}')
else:

    print('Você ainda não tem bônus para receber!')
