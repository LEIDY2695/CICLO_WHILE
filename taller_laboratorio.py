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
        octanaje = int(input())
        # Validacion del octanaje
        while octanaje < 81 or octanaje > 98:
            print("OCTANAJE INVALIDO")
            octanaje = int(input())
        # Calcular rendimiento 
        rendimiento = km / galones
        # Acumular datos
        total_km += km
        total_galones += galones
        total_tanqueos += 1
