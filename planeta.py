class Planeta:
    def __init__(self, nombre, masa, radio, distancia_al_sol, tiene_vida=False):
        self.nombre = nombre
        self.masa = masa
        self.radio = radio
        self.distancia_al_sol = distancia_al_sol
        self.tiene_vida = tiene_vida

    def calcular_densidad(self):
        pi =  3.1415926535   # estoy usando los primeros 10 digitos xd
        volumen = (4 / 3) * pi * (self.radio ** 3)
        densidad = self.masa / volumen
        return densidad

    def es_planeta_exterior(self):
        if self.distancia_al_sol > 5.2:
            return True
        else:
            return False
        
    def __str__(self):
        if self.es_planeta_exterior():
            tipo = "Exterior"
        else:
            tipo = "Interior"
        return "Planeta: " + str(self.nombre) + " | Densidad: " + str(self.calcular_densidad()) + " kg/m3 | Tipo: " + tipo

# ejemplos de uso que me dio la IA, esta usa el __init__ del inicio para darle los datos que necesita

tierra = Planeta("Tierra", 5.972e24, 6371000, 1.0, True)
print(tierra)

jupiter = Planeta("Jupiter", 1.898e27, 69911000, 5.204, False)
print(jupiter)