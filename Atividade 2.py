# 2) Um nutricionista precisa controlar a dieta para pacientes celíacos (intolerantes à glúten) e pacientes com intolerância à lactose. 
# Criar um programa onde o paciente deve digitar seu nome e em seguida responder se é celíaco (primeira pergunta) e se é 
# intolerante à lactose (segunda pergunta). Validar as respostas de SIM e NÃO para letras maiúsculas e minúsculas. 
# Em seguida coletar os dados de 3 alimentos, sendo digitado o nome do alimento, se ele contém glúten ou não e se ele contém lactose ou não. 
# Ao final, informar se o paciente pode comer os 3 alimentos digitados "Dieta adequada!" ou não pode "Dieta inadequada, 
# contém alimentos aos quais o paciente é intolerante!".

rel = 'sim'

nomeUsuario = input('Digite seu nome.')

eCeliaco = input('Você é celíaco?')

eIntolerante = input('Você é intolerante à lactose?')

alimentoUm = input('Digite o primeiro alimento.')

alimentoUmTemGluten = input('O alimento contém glúten?')

alimentoUmTemLactose = input('O alimento contém lactose?')

alimentoDois = input('Digite o segundo alimento.')

alimentoDoisTemGluten = input('O alimento contém glúten?')

alimentoDoisTemLactose = input('O alimento contém lactose?')

alimentoTres = input('Digite o terceiro alimento.')

alimentoTresTemGluten = input('O alimento contém glúten?')

alimentoTresTemLactose = input('O alimento contém lactose?')

if (eCeliaco=='não' and eIntolerante=='não'):
    
    print('{nomeUsuario} , a sua dieta está adequada!')
elif (eCeliaco==rel and eIntolerante=='não'):

  if (alimentoUmTemGluten==rel):

    print('{nomeUsuario} , a sua dieta não está adequada!')
  elif (alimentoDoisTemGluten==rel):

    print('{nomeUsuario} , a sua dieta não está adequada!')
  elif (alimentoTresTemGluten==rel):

    print('{nomeUsuario} , a sua dieta não está adequada!')
  else:

    print('{nomeUsuario} , a sua dieta está adequada!')
elif (eIntolerante==rel and eCeliaco=='não'):

  if (alimentoUmTemLactose==rel):

    print('{nomeUsuario} , a sua dieta não está adequada!')
  elif (alimentoDoisTemLactose==rel):
    
    print('{nomeUsuario} , a sua dieta não está adequada!')
  elif (alimentoTresTemLactose==rel):
    
    print('{nomeUsuario} , a sua dieta não está adequada!')
  else:

    print('{nomeUsuario} , a sua dieta está adequada!')
elif (eCeliaco==rel and eIntolerante==rel):

    print('{nomeUsuario} , a sua dieta não está adequada!')
