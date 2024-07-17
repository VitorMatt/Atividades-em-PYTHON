# 1) Seu sonho é construir uma piscina. Para cada metro quadrado, são necessários 120 azulejos. 
# O cálculo de área em metros quadrados, é feito multiplicando a largura pelo comprimento. 
# Digitar os valores (em metros) da largura e comprimento que deseja a piscina. 
# Mostrar na tela a quantidade de azulejos que devem ser comprados e o valor total a ser pago, 
# sendo que uma caixa de azulejo com 60 unidades custa R$45,50.

azulejos_por_cada_metro_quadrado = 120
valor_sessenta_unidades_azulejo = 45.5
unidades_azulejos_por_caixa = 60

comprimento_pscina = float(input(f'Qual o comprimento da pscina?'))

largura_pscina = float(input(f'Qual a largura da pscina?'))

area_pscina = comprimento_pscina * largura_pscina

valor_unidade_azulejo = valor_sessenta_unidades_azulejo / unidades_azulejos_por_caixa

quantidade_azulejos_necessários = area_pscina * azulejos_por_cada_metro_quadrado


valor_total = quantidade_azulejos_necessários * valor_unidade_azulejo

quantidade_azulejos_necessários = round(quantidade_azulejos_necessários)

valor_total = round(valor_total)

print(f'Quantidade de azulejos necessários: {quantidade_azulejos_necessários}\nValor total à ser pago: R$ {valor_total}')








