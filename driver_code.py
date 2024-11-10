from enum import Enum
from src import Cargo, Loja, Funcionário, Instrumento, TipoEncordoamento, Guitarra, Baixo, Violão

# Craindo filiais
loja_1 = Loja("São Paulo", "Rio de Janeiro")
loja_2 = Loja("Rio de Janeiro", "São Paulo")

# Checando filiais existentes
print(Loja.lojas_existentes)

# Criando funcionários
funcionario_1 = Funcionário("Carlos Silva", "12345678900", 3000, Cargo(2))
funcionario_2 = Funcionário("Ana Souza", "09876543211", 3500, Cargo(4))

# Adicionando funcionários à loja
loja_1.adicionar_funcionário(funcionario_1)
loja_1.adicionar_funcionário(funcionario_2)

# Verificando quantidade de funcionários por cargo
print(loja_1.checar_funcionários_por_cargo())

# Criando instrumentos
guitarra = Guitarra("Fender", "Stratocaster", 1500, 6, "floyd rose")
baixo = Baixo("Ibanez", "SR300", 1200, 4, True)
violao = Violão("Yamaha", "C40", 500, 6, TipoEncordoamento(2))

# Adicionando instrumentos ao estoque da loja
loja_1.adicionar_instrumento(guitarra)
loja_1.adicionar_instrumento(baixo)
loja_1.adicionar_instrumento(violao)

# Consultando quantidade de instrumentos de cada tipo
print(loja_1.checar_estoque())

# Removendo um instrumento do estoque
loja_1.remover_instrumento(guitarra)

# Removendo um funcionário da loja
loja_1.remover_funcionário(funcionario_1)