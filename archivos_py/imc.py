def IMC():
    #? Entrada de variables:

    w = float(input('Peso del usuario:\r\n'))
    h = float(input('Altura del usuario:\r\n'))

    #? Cálclulo de IMC:

    imc = w / pow(h,2)

    #? Comparativa de rangos y salida de resultados:

    print('Su Indice de masa corporal es: ',imc)

    if 0 < imc < 18.5:
        print('Usted esta en infrapeso')

    elif 18.5 <= imc <= 24.9:
        print('Usted esta en su peso ideal')

    elif 24.9 < imc <= 29.9:
        print('Usted esta en sobrepeso')

    else:
        print('Usted tiene obesidad')

IMC()