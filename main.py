dia = int(input())
mes = int(input())

fecha = float(str(mes) + "." + str(dia))

if fecha >= 3.21 and fecha <= 4.2:
    print("aries")
elif fecha >= 4.21 and fecha <= 5.2:
    print("tauro")
elif fecha >= 5.21 and fecha <= 6.21:
    print("geminis")
elif fecha >= 6.22 and fecha <= 7.22:
    print("cancer")
elif fecha >= 7.23 and fecha <= 8.22:
    print("leo")
elif fecha >= 8.23 and fecha <= 9.22:
    print("virgo")
elif fecha >= 9.23 and fecha <= 10.22:
    print("libra")
elif fecha >= 10.23 and fecha <= 11.22:
    print("escorpio")
elif fecha >= 11.23 and fecha <= 12.21:
    print("sagitario")
elif fecha >= 12.22 or fecha <= 1.20:
    print("capricornio")
elif fecha >= 1.21 and fecha <= 2.18:
    print("acuario")
elif fecha >= 2.19 and fecha <=3.2:
    print("piscis")
