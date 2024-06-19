#Actividad temperatura
temperatura = int(input('Que grados hace hoy? '))
if temperatura < 20:
    if temperatura < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
elif temperatura < 30:
    print('Nivel naranja')
else:
    print('Nivel rojo')

