#4)Escreva um programa para ler 2 valores (considere que não serão informados valores iguais) e escrever o maior deles.

valor_um = float(input(f'Digite o primeiro valor.'))

valor_dois = float(input(f'Digite o segundo valor.'))

if valor_um == valor_dois:

    print ('Os números devem ser diferentes!')
elif valor_um>valor_dois:

    valor_maior = valor_um
    print (f'O valor maior é {valor_maior}.')
else:

    valor_maior = valor_dois
    print (f'O valor maior é {valor_maior}.')