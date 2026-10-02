class Automovil:
    def __init__(self, marca, modelo, velocidad_max, nivel_combustible, ano_fabricacion):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_max = velocidad_max
        self.nivel_combustible = nivel_combustible
        self.ano_fabricacion = ano_fabricacion

    # Propiedad ano_fabricacion
    @property
    def ano_fabricacion(self):
        return self._ano_fabricacion

    @ano_fabricacion.setter
    def ano_fabricacion(self, valor):
        if valor >= 1886 and valor <= 2026:
            self._ano_fabricacion = valor
        else:
            raise ValueError("El año de fabricacion debe estar entre 1886 y 2026.")

    # Propiedad nivel_combustible
    @property
    def nivel_combustible(self):
        return self._nivel_combustible

    @nivel_combustible.setter
    def nivel_combustible(self, valor):
        if valor >= 0.0 and valor <= 100.0:
            self._nivel_combustible = float(valor)
        else:
            raise ValueError("El nivel de combustible debe estar entre 0.0 y 100.0.")

    # Propiedad velocidad_max
    @property
    def velocidad_max(self):
        return self._velocidad_max

    @velocidad_max.setter
    def velocidad_max(self, valor):
        if valor > 0:
            self._velocidad_max = float(valor)
        else:
            raise ValueError("La velocidad maxima debe ser mayor a 0.")