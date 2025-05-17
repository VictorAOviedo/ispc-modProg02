from datos import lista_dispositivos

def encender(dispositivo):
    for i, diccionario in enumerate(lista_dispositivos):
        if dispositivo == diccionario["nombre"]:
            lista_dispositivos[i]["estado"] = True       
            return f"El dispositivo {dispositivo} se encendio."
        
    return f"El dispositivo {dispositivo} no se encuentra."
           

def encender_luz_cocina_cafetera():
    print("Se encendieron la luz de la cocina y la cafetera")
    lista_dispositivos[0]["estado"] = True
    lista_dispositivos[1]["estado"] = True
