# Varibales

total_km = 0
total_galones = 0
mejor_rendimiento = 0
total_tanqueos = 0
tanqueos_extras = 0

# Primer ingreso de galones
galones = float(input())

# Caso especial
if galones == 0:
    print("No data provided.")
else:
    #Ciclo principal
    while galones != 0:
        # Kilometros recorridos
        km = float(input())
        # Octanaje
        octanaje = float(input())

        while octanaje < 81 or octanaje > 98 or octanaje != int(octanaje):
            print("OCTANAJE INVALIDO")
            octanaje = float(input())

        octanaje = int(octanaje)
        # Calcular rendimiento 
        rendimiento = km / galones
        # Acumular datos
        total_km += km
        total_galones += galones
        total_tanqueos += 1

# Actualizado por Laura

        if rendimiento > mejor_rendimiento:
            mejor_rendimiento = rendimiento
            # contar gasolina extra
        if octanaje >= 90:
            tanqueos_extras += 1

        #pedir nuevos galones
        galones = float(input())

        #calculos finales               
        promedio = total_km / total_galones
        porcentaje_extras = (tanqueos_extras / total_tanqueos) * 100

    # Salida (Output)
    print(f"AVG: {promedio:.2f}")
    print(f"BEST: {mejor_rendimiento:.2f}")
    print(f"EXTRA: {porcentaje_extras:.2f}")

    