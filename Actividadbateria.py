#Actividad bateria
bateria = 53
if bateria < 20:
    print("recargar")
elif bateria > 50:
    print("optimo")
elif bateria > 20:
    print("Normal")
elif bateria > 80:
    print("full")
    