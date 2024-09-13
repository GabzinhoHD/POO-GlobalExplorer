class Viagem:
    viagens = []
    def __init__(self, nome, pais_Origem, pais_Destino):
        self.nome = nome
        self.pais_Origem = pais_Origem
        self.pais_Destino = pais_Destino
        self.ativo = False
        Viagem.viagens.append(self)

    def __str__(self):
        return f"{self.nome} | {self.pais_Origem} | {self.pais_Destino} | {self.ativo}"

    def listar_viagens():
        for viagem in Viagem.viagens:
            print(f"{viagem.nome} | {viagem.pais_Origem} | {viagem.pais_Destino}")



pessoa_Vinicius = Viagem("Vinicius", "Brasil", "Canada")
pessoa_Luiza = Viagem("Luiza Ribeiro", "Brasil", "Reino Unido")
pessoa_Samuel = Viagem("Samuel Wingert", "Alemanha", "Estados Unidos")
pessoa_Gustavo = Viagem("Gustavo Apolinario", "Argentina", "Italia")
pessoa_Luanna = Viagem("Luanna Rodrigues", "Brasil", "Venezuela")
pessoa_Estefan = Viagem("Estefan Xavier", "Brasil", "Japão")

Viagem.listar_viagens()
