# Varibales

galones = 0.0
kilometros_recorridos = 0.0
octanaje = 0
conteo_tanqueo = 0
conteo_octanaje = 0

programa_ejecutandose = True
primera_entrada = True

while programa_ejecutandose:
    galones_cargados_str = input()
    galones_cargados = float(galones_cargados_str)

    if primera_entrada and galones_cargados == 0:
        print("No se Ingresaron Datos.")
        programa_ejecutandose = False
    elif galones_cargados == 0:
        programa_ejecutandose = False
    else:
        kilometros_recorridos_str = input()
        kilometros_recorridos = float(kilometros_recorridos_str)