
class SautDeTemps:
    def __init__(self, intervalle: int):
        self.intervalle = intervalle


class SautDeTempsSecondes(SautDeTemps):
    def __init__(self, intervalle: int):
        super().__init__(intervalle)
        self.seconds = intervalle


class SautDeTempsMinutes(SautDeTemps):
    def __init__(self, intervalle: int):
        super().__init__(intervalle)
        self.seconds = intervalle * 60


class SautDeTempsHeures(SautDeTemps):
    def __init__(self, intervalle: int):
        super().__init__(intervalle)
        self.seconds = intervalle * 3600
