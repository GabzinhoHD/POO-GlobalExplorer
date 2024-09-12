class Viagem:
    def __init__(self, nome, pais_Origem, pais_Destino):
        self.nome = nome
        self.pais_Origem = pais_Origem
        self.pais_Destino = pais_Destino
        self.ativo = False

    def __str__(self):
        return f"{self.nome} | {self.pais_Origem} | {self.pais_Destino} | {self.ativo}"



pessoa_Vinicius = Viagem("Vinicius", "Brasil", "Canada")
pessoa_Luiza = Viagem("Luiza Ribeiro", "Brasil", "Alemanha")

Viagens = [pessoa_Luiza, pessoa_Vinicius]

print(pessoa_Vinicius)
print(pessoa_Luiza)

