#5) Você é um ciclista profissional e pretende participar da competição "Volta à Ilha de Bike", revezamento em equipes, 
#com equipes de 4 integrantes. O percurso tem um total de 140km, sendo dividido em 4 partes: Trecho 1 Av. Beira-Mar até 
#Cachoeira do Bom Jesus (30km), Trecho 2 Cachoeira do Bom Jesus até Lagoa da Conceição (45km), Trecho 3 Lagoa da Conceição até 
#Pântano do Sul (30km), Trecho 4 Pântano do Sul até Av. Beira-Mar (35km). Criar um programa que recebe o nome da equipe, 
#em seguida o nome de cada um dos 4 integrantes e o tempo em horas que gastou pedalando o seu trecho. Ao final mostrar a 
#velocidade média de cada trecho e a velocidade média geral (total dos 4 trechos) com duas casas após a vírgula. Se a velocidade 
#média geral ficar abaixo de 15km/h mostrar uma mensagem "Desempenho pode melhorar bastante!", caso a velocidade média fique de 15 a 18km/h 
#mostrar uma mensagem "Desempenho bom, mas ainda pode melhorar!" e se a média ficar acima de 18km/h 
#mostrar uma mensagem "Desempenho excelente. Parabéns!"

percurso_total = 140
percurso_trecho_um = 30
percurso_trecho_dois = 45
percurso_trecho_tres = 30
percurso_trecho_quatro = 35
limite_media_baixa = 15
limite_media_alta = 18

nome_equipe = input('Digite o nome da sua equipe.')

nome_integrante_um = input('Digite o nome do primeiro integrante.')

nome_integrante_dois = input('Digite o nome do segundo integrante.')

nome_integrante_tres = input('Digite o nome do terceiro integrante.')

nome_integrante_quatro = input('Digite o nome do quarto integrante.')

tempo_total_gasto = float(input(f'Quantas horas durou o percurso inteiro?'))

tempo_gasto_trecho_um = float(input(f'Quantas horas durou o primeiro trecho?'))

tempo_gasto_trecho_dois = float(input(f'Quantas horas durou o segundo trecho?'))

tempo_gasto_trecho_tres = float(input(f'Quantas horas durou o terceiro trecho?'))

tempo_gasto_trecho_quatro = float(input(f'Quantas horas durou o quarto trecho?'))

velocidade_media_trecho_um = percurso_trecho_um / tempo_gasto_trecho_um

velocidade_media_trecho_dois = percurso_trecho_dois / tempo_gasto_trecho_dois

velocidade_media_trecho_tres = percurso_trecho_tres / tempo_gasto_trecho_tres

velocidade_media_trecho_quatro = percurso_trecho_quatro / tempo_gasto_trecho_quatro

velocidade_media_geral = percurso_total / tempo_total_gasto

velocidade_media_trecho_um = round(velocidade_media_trecho_um)
velocidade_media_trecho_dois = round(velocidade_media_trecho_dois)
velocidade_media_trecho_tres = round(velocidade_media_trecho_tres)
velocidade_media_trecho_quatro = round(velocidade_media_trecho_quatro)
velocidade_media_geral = round(velocidade_media_geral)

if (velocidade_media_geral<limite_media_baixa):

    print(f'Desempenho equipe {nome_equipe}\nVelocidade média no trecho 1: {velocidade_media_trecho_um}km/h\nVelocidade média no trecho 2: {velocidade_media_trecho_dois}km/h\nVelocidade média no trecho 3: {velocidade_media_trecho_tres}km/h\nVelocidade média no trecho quatro: {velocidade_media_trecho_quatro}km/h\nVelocidade média geral: {velocidade_media_geral}km/h\nDesempenho pode melhorar bastante!')
elif velocidade_media_geral>=limite_media_baixa and velocidade_media_geral<=limite_media_alta:

    print(f'Desempenho equipe {nome_equipe}\nVelocidade média no trecho 1: {velocidade_media_trecho_um}km/h\nVelocidade média no trecho 2: {velocidade_media_trecho_dois}km/h\nVelocidade média no trecho 3: {velocidade_media_trecho_tres}km/h\nVelocidade média no trecho quatro: {velocidade_media_trecho_quatro}km/h\nVelocidade média geral: {velocidade_media_geral}km/h\nDesempenho bom, mas ainda pode melhorar!')
else:

    print(f'Desempenho equipe {nome_equipe}\nVelocidade média no trecho 1: {velocidade_media_trecho_um}km/h\nVelocidade média no trecho 2: {velocidade_media_trecho_dois}km/h\nVelocidade média no trecho 3: {velocidade_media_trecho_tres}km/h\nVelocidade média no trecho quatro: {velocidade_media_trecho_quatro}km/h\nVelocidade média geral: {velocidade_media_geral}km/h\nDesempenho excelente. Parabéns!')