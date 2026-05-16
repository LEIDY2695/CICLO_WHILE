# Varibales

galones = 0.0
total_kilometros = 0.0
octanaje = 0
conteo_tanqueo = 0
conteo_octanaje = 0

programa_ejecutandose = True
primera_entrada = True

while programa_ejecutandose:
    galones_cargados_str = input()
    galones_cargados = float(galones_cargados_str)

    if primera_entrada and galones_cargados == 0:
        print("No data provided.")
        programa_ejecutandose = False
    elif galones_cargados == 0:
        programa_ejecutandose = False
    else:
        kilometros_recorridos_str = input()
        kilometros_recorridos = float(kilometros_recorridos_str)

        octanaje_valido = False    #controlar variable del octanaje
        octanaje = 0
    while not octanaje_valido:
        octanaje_str = input()   #valor sin texto
        octanaje = int(octanaje_str)   #valor entero

        if  81<= octanaje <=98:  #condicion que debe cumplir 
            octanaje_valido = True
        else:
            print("OCTANAJE INVALIDO")
        