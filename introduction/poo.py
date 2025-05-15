# POO

# Class Exemplo
# Definindo a classe Pessoa
class Pessoa:
    # O método __init__ é o construtor que inicializa os atributos 'nome' e 'idade'
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo 'nome'
        self.idade = idade  # Atributo 'idade'

    # Método para exibir o nome e idade da pessoa
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos")

# Criando um objeto da classe Pessoa
pessoa1 = Pessoa("João", 30)

# Chamando o método para exibir as informações da pessoa
pessoa1.exibir_informacoes()

# Os pilares da Programação Orientada a Objetos (POO)

# 1. Encapsulamento
# O encapsulamento é o princípio que visa ocultar os detalhes internos de um objeto e expor apenas o necessário.
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor

    def get_saldo(self):
        return self.__saldo  # Método para acessar o saldo

conta = ContaBancaria(1000)
conta.depositar(500)
print(conta.get_saldo())  # 1500

# 2. Herança
# A herança permite que uma classe herde atributos e métodos de outra classe. 
class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

cachorro = Cachorro()
print(cachorro.falar())  # "Au au!"

gato = Gato()
print(gato.falar())  # "Miau!"

# 3. Polimorfismo
# O polimorfismo permite que objetos de diferentes classes sejam tratados de forma semelhante, normalmente usando o mesmo nome de método, mas com comportamentos diferentes, dependendo do tipo de objeto.
class Carro:
    def mover(self):
        return "O carro está se movendo"

class Bicicleta:
    def mover(self):
        return "A bicicleta está se movendo"

def movimentar_veiculo(veiculo):
    print(veiculo.mover())  # Polimorfismo em ação

carro = Carro()
bicicleta = Bicicleta()

movimentar_veiculo(carro)  # "O carro está se movendo"
movimentar_veiculo(bicicleta)  # "A bicicleta está se movendo"

# 4. Abstração
# Abstração é o conceito de esconder os detalhes complexos de implementação e mostrar apenas a interface ou funcionalidades essenciais.
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio ** 2

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

# Não podemos instanciar diretamente a classe Forma
# forma = Forma()  # Erro: Não pode instanciar classe abstrata

circulo = Circulo(5)
retangulo = Retangulo(4, 6)

print(circulo.area())  # 78.5
print(retangulo.area())  # 24



