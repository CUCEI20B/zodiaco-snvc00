dia = int(input())
mes = int(input())

zodiaco = {1:[20, "capricornio", "acuario"], 2:[18, "acuario", "piscis"], 3:[20, "piscis", "aries"], 4:[20, "aries", "tauro"], 5:[20, "tauro", "geminis"], 6:[21, "geminis", "cancer"], 7:[22, "cancer", "leo"], 8:[22, "leo", "virgo"], 9:[22, "virgo", "libra"], 10:[22, "libra", "escorpio"], 11:[22, "escorpio", "sagitario"], 12:[21, "sagitario", "capricornio"]}

if dia <= zodiaco[mes][0]:
    signo = 1
else:
    signo = 2

print(zodiaco[mes][signo])