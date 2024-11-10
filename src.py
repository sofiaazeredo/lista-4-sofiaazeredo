from enum import Enum

class TipoEncordoamento(Enum):
    NYLON = 1
    AÇO = 2

class Cargo(Enum):
    ESTAGIÁRIO = 1
    ATENDENTE = 2
    CAIXA = 3
    GERENTE = 4
    DONO_DE_FRANQUIA = 5
    
class Funcionário:
    def __init__(self,
                 nome_completo : str,
                 documento : int,
                 salário : float,
                 cargo : Cargo,
                 loja_atual = None):
        self.nome_completo = nome_completo
        self.documento = documento
        self.salário = salário
        self.cargo = cargo
        self.loja_atual = loja_atual

    def __str__(self):
        return self.nome_completo
        
class Instrumento:
    def __init__(self, 
                 marca : str, 
                 modelo : str, 
                 preço : float,
                 numero_de_cordas : int):
        self.marca = marca
        self.modelo = modelo
        self.preço = preço
        self.numero_de_cordas = numero_de_cordas
        
class Guitarra(Instrumento):
    def __init__(self, 
                 marca : str, 
                 modelo : str, 
                 preço : float,
                 numero_de_cordas : int,
                 ponte : str):
        super().__init__(marca, modelo, preço, numero_de_cordas)
        self.ponte = ponte
    
class Baixo(Instrumento):
    def __init__(self, 
                 marca : str, 
                 modelo : str, 
                 preço : float,
                 numero_de_cordas : int,
                 ativo : bool):
        super().__init__(marca, modelo, preço, numero_de_cordas)
        self.ativo = ativo

class Violão(Instrumento):
    def __init__(self, 
                 marca : str, 
                 modelo : str, 
                 preço : float,
                 numero_de_cordas : int,
                 tipo_encordoamento : TipoEncordoamento):
        super().__init__(marca, modelo, preço, numero_de_cordas)
        self.tipo_encordoamento = tipo_encordoamento

class Loja:
    lojas_existentes = []
    
    def __init__(self, 
                 localização : str, 
                 loja_mais_próxima : str
                 ):
        self.localização = localização
        self.loja_mais_próxima = loja_mais_próxima
        self.quadro_de_funcionários = []
        self.instrumentos_da_loja = []
        self.estoque = {}
        Loja.lojas_existentes.append(str(self))
    
    def __str__(self):
        return self.localização
    
    def checar_estoque(self):
        self.estoque = {"Violão": 0, "Guitarra": 0, "Baixo": 0}
        for instrumento in self.instrumentos_da_loja:
            if isinstance(instrumento, Violão):
                self.estoque["Violão"] += 1
            elif isinstance(instrumento, Guitarra):
                self.estoque["Guitarra"] += 1
            elif isinstance(instrumento, Baixo):
                self.estoque["Baixo"] += 1

        return self.estoque
    
    def checar_funcionários_por_cargo(self):
        funcionarios_por_cargo = {cargo: 0 for cargo in Cargo}
        
        for funcionario in self.quadro_de_funcionários:
            funcionarios_por_cargo[funcionario.cargo] += 1
            
        return funcionarios_por_cargo
            
    def remover_funcionário(self, funcionário : Funcionário):
        self.quadro_de_funcionários.remove(funcionário)
        funcionário.loja_atual = None
    
    def adicionar_funcionário(self, funcionário : Funcionário):
        self.quadro_de_funcionários.append(funcionário)
        funcionário.loja_atual = self
     
    def remover_instrumento(self, instrumento : Instrumento):
        self.instrumentos_da_loja.remove(instrumento)
        
    def adicionar_instrumento(self, instrumento : Instrumento):
        self.instrumentos_da_loja.append(instrumento)