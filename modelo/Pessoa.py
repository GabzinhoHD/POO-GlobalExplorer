from modelo.Distancia import Distancia

class Viagem:
    viagens = []
    def __init__(self, nome, pais_Origem, pais_Destino):
        self._nome = nome.upper()
        self._pais_Origem = pais_Origem.title()
        self._pais_Destino = pais_Destino.title()
        self._distancia = []
        self._ativo = False
        Viagem.viagens.append(self)

    def __str__(self):
        return f"{self.nome} | {self.pais_Origem} | {self.pais_Destino} | {self.ativo}"

    @classmethod
    def listar_viagens(cls):
        print("""𝔊𝔩𝔬𝔟𝔞𝔩 𝔈𝔵𝔭𝔩𝔬𝔯𝔢𝔯""")
        print("‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗")
        print(f"{"Nome Viajante".ljust(20)} | {"Pais de Origem".ljust(20)} | {"Pais de destino".ljust(20)} | {"Status".ljust(20)} | {"Tempo Medio da viagem"}")
        print("‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗")
        for viagem in cls.viagens:
            print(f"{viagem._nome.ljust(20)} | {viagem._pais_Origem.ljust(20)} | {viagem._pais_Destino.ljust(20)} | {viagem.ativo.ljust(20)} | {viagem.media_Tempo}")

    @property
    def ativo(self):
        return "☆ Parada" if self._ativo else "★ Em andamento"

    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_Distancia(self, companhia, tempo):
        distancia = Distancia(companhia, tempo)
        self._distancia.append(distancia)

    @property
    def media_Tempo(self):
        if not self._distancia:
            return 0 
        soma_tempo = sum(Distancia._tempo for Distancia in self._distancia)
        quantidade_Companhias = len(self._distancia)
        media = round(soma_tempo / quantidade_Companhias, 1)
        return media

