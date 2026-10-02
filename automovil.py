class Automovil:
    def __init__(self, marca, modelo, velocidad_max, nivel_combustible, ano_fabricacion):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_max = velocidad_max
        self.nivel_combustible = nivel_combustible
        self.ano_fabricacion = ano_fabricacion

    @property
    def ano_fabricacion(self):
        return self._ano_fabricacion

    @ano_fabricacion.setter
    def ano_fabricacion(self, valor):
        if valor >= 1886 and valor <= 2026:
            self._ano_fabricacion = valor
        else:
            raise ValueError("El año de fabricacion debe estar entre 1886 y 2026.")

    @property
    def nivel_combustible(self):
        return self._nivel_combustible

    @nivel_combustible.setter
    def nivel_combustible(self, valor):
        if valor >= 0.0 and valor <= 100.0:
            self._nivel_combustible = float(valor)
        else:
            raise ValueError("El nivel de combustible debe estar entre 0.0 y 100.0.")

    @property
    def velocidad_max(self):
        return self._velocidad_max

    @velocidad_max.setter
    def velocidad_max(self, valor):
        if valor > 0:
            self._velocidad_max = float(valor)
        else:
            raise ValueError("La velocidad maxima debe ser mayor a 0.")

    def tiempo_llegada(self, distancia_km):
        tiempo = distancia_km / self.velocidad_max
        return tiempo

    def __str__(self):
        return "Automovil: " + str(self.marca) + " " + str(self.modelo) + " (" + str(self.ano_fabricacion) + ") | Vel Max: " + str(self.velocidad_max) + " km/h | Combustible: " + str(self.nivel_combustible) + "%"


# ejemplo de uso de la IA
auto1 = Automovil("Toyota", "Corolla", 180.0, 50.0, 2020)
print(auto1)

distancia = 360.0
print("Tiempo para recorrer " + str(distancia) + " km: " + str(auto1.tiempo_llegada(distancia)) + " horas")

# Prueba de validacion con try/except
try:
    auto1.ano_fabricacion = 1800
except ValueError as error:
    print("Error capturado correctamente: " + str(error))