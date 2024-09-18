from modelo.Pessoa import Viagem

pessoa_Vinicius = Viagem("Vinicius Rosa", "Brasil", "Canada")
pessoa_Luiza = Viagem("Luiza Ribeiro", "Brasil", "Reino Unido")
pessoa_Samuel = Viagem("Samuel Wingert", "Alemanha", "Estados Unidos")
pessoa_Gustavo = Viagem("Gustavo Apolinario", "Argentina", "Italia")
pessoa_Luanna = Viagem("Luanna Rodrigues", "Brasil", "Venezuela")
pessoa_Estefan = Viagem("Estefan Xavier", "Brasil", "Japão")
pessoa_Sonia = Viagem("Sonia de Assis", "Japão", "Brasil")

pessoa_Luanna.alterar_estado()
pessoa_Estefan.receber_Distancia("LATAM", 35)
pessoa_Estefan.receber_Distancia("AZUL", 32)
pessoa_Estefan.receber_Distancia("GOL", 28)

def main():
    Viagem.listar_viagens()

if __name__ == "__main__":
    main()