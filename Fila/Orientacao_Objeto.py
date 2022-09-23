class Carro:
    # CARACTERÍSTICAS DE CARROS:  (ATRIBUTOS)
    # PRIMEIRO DEFINIMOS OS ATRIBUTOS DA CLASSE  # lista de atributos de objetos da classe carro...
    ano = 0
    modelo = ""
    marca = ""
    combustivel = ""
    km = 0
    cor = ""
    velocidade = 0
    #  Método Construtor - É um método que é chamado toda vez que "instanciamos" um objeto da classe

    def __init__(self, ano, modelo, marca, combustivel, km, cor) -> None:
        self.ano = ano
        self.modelo = modelo
        self.marca = marca
        self.combustivel = combustivel
        self.km = km
        self.cor = cor

    def acelerar(self, tempo, aceleracao):
        self.velocidade = aceleracao * tempo

    def parar(self):
        self.velocidade = 0

    def capivara(self):
        print(f"Dados do veiculo")
        print(f"O modelo do veículo é: {self.modelo}")
        print(f"O ano do veículo é: {self.ano}")
        print(f"Sua cor: {self.cor}")
        print(f"O Combustível: {self.combustivel}")
        print(f"Seu km: {self.km}")
        print(f"Sua velocidade:{self.velocidade}")


fusca = Carro(1977, "Fusca", "Volkswagen", "gasolina", 50000, "preto")
# velocidade 0
fusca.capivara()
fusca.acelerar(10, 10)
# velocidade 100
fusca.capivara()
fusca.parar()
# velocidade 0
fusca.capivara()
