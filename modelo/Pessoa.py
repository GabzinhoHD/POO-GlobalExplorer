class Viagem:
    viagens = []
    def __init__(self, nome, pais_Origem, pais_Destino):
        self.nome = nome
        self.pais_Origem = pais_Origem
        self.pais_Destino = pais_Destino
        self._ativo = False
        Viagem.viagens.append(self)

    def __str__(self):
        return f"{self.nome} | {self.pais_Origem} | {self.pais_Destino} | {self.ativo}"

    def listar_viagens():
        print("""𝔊𝔩𝔬𝔟𝔞𝔩 𝔈𝔵𝔭𝔩𝔬𝔯𝔢𝔯""")
        print("‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗")
        print(f"{"Nome Viajante".ljust(20)} | {"Pais de Origem".ljust(20)} | {"Pais de destino".ljust(20)} | {"Status"}")
        print("‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗")
        for viagem in Viagem.viagens:
            print(f"{viagem.nome.ljust(20)} | {viagem.pais_Origem.ljust(20)} | {viagem.pais_Destino.ljust(20)} | {viagem.ativo.ljust(20)}")

    @property
    def ativo(self):
        return "☆ Parada" if self._ativo else "★ Em andamento"


pessoa_Vinicius = Viagem("Vinicius", "Brasil", "Canada")
pessoa_Luiza = Viagem("Luiza Ribeiro", "Brasil", "Reino Unido")
pessoa_Samuel = Viagem("Samuel Wingert", "Alemanha", "Estados Unidos")
pessoa_Gustavo = Viagem("Gustavo Apolinario", "Argentina", "Italia")
pessoa_Luanna = Viagem("Luanna Rodrigues", "Brasil", "Venezuela")
pessoa_Estefan = Viagem("Estefan Xavier", "Brasil", "Japão")
pessoa_Sonia = Viagem("Sonia de Assis", "Japão", "Brasil")

Viagem.listar_viagens()
