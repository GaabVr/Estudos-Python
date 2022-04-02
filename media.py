#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
n1 = float(input('Entre com a nota:'))
n2 = float(input('Entre com a nota:'))
n3 = float(input('Entre com a nota:'))
n4 = float(input('Entre com a nota:'))
media = (n1 + n2 + n3 + n4) / 4
print('Sua media é', media)
if media >= 7:
    print('Aprovado!')
else:
    print('Reprovado!')


