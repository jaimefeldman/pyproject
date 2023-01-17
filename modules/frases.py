import random, json

class frases:
    def __init__(self):
        # Abriendo el archivo json.
        f = open("modules/frases.json")

        # devolviendo un objeto json como diccionario.
        data = json.load(f)

        # iternado sobre el diccionario devuelto.
        self.listado_frases = data['frases']
        #print("listado_frases es un:",type(listado_frases))
                
        # cerrando el archivo.
        f.close()

    def una_frase(self):
        return self.listado_frases[random.randrange(0, len(self.listado_frases))]
    
    
