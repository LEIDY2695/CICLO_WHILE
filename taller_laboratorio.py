# Problematica : Se necesita analizar el historial de tanquoeos para conocer la eficiencia del consumo del combustible y verificar la calidad de la gasolina utilizada. 
# Se requiere calcular el rendimiento promedio, identificar el mejor rendimiento registrado y determinar el porcentaje de tanqueos que utilizaron gasolina de octanaje alto (90 o más).   

# Solucion : Desarrollar un algoritmo que permita registrar varios tanqueos. (Hasta que se ingrese 0 galones). 
# Para cada tanqueo, se solicitará la cantidad de galones, los kilómetros recorridos y el octanaje de la gasolina. 
# El algoritmo calculará el rendimiento de cada tanqueo, acumulará los datos necesarios para calcular el rendimiento promedio.
# identificará el mejor rendimiento registrado y contará cuántos tanqueos utilizaron gasolina de octanaje alto. 
# Al finalizar la entrada de datos, se mostrará el rendimiento promedio, el mejor rendimiento y el porcentaje de tanqueos con gasolina de octanaje alto.

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

    