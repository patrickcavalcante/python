# Personagem: Classe mãe 
# Heroi: controlado pelo usuario 
# Inimigo: adiversario do Usuario
import random

class Personagem: 
  def __init__(self, nome, vida, nivel):
    self.__nome = nome
    self.__vida = vida
    self.__nivel = nivel

  def get_nome(self):
    return self.__nome
  
  def get_vida(self):
    return self.__vida

  def get_nivel(self):
    return self.__nivel
  
  def exibir_detalhes(self):
    return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nLevel: {self.get_nivel()}"
  
  def receber_ataque(self, dano):
    self.__vida -= dano
    if self.__vida < 0:
      self.__vida = 0
  
  def atacar(self, alvo):
    dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
    alvo.receber_ataque(dano)
    print(f"{self.get_nome()} atacou o alvo {alvo.get_nome()} e causou {dano} de dano!")

  
class Heroi(Personagem):
  def __init__(self, nome, vida, nivel, habilidade):
    super().__init__(nome, vida, nivel)
    self.__habilidade = habilidade

  def get_habilidade(self):
   return self.__habilidade
  
  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"
  
  def atacar_especial(self, alvo):
    dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)
    alvo.receber_ataque(dano)
    print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} e causou {dano} de dano!")
  
class Inimigo(Personagem):
  def __init__(self, nome, vida, nivel, tipo):
    super().__init__(nome, vida, nivel)
    self.__tipo = tipo

  def get_tipo(self):
    return self.__tipo
  
  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n"

class Jogo:
  """Classe Orquestradora do Jogo"""
  def __init__(self):
    self.heroi = Heroi(nome="Herói", vida=100, nivel=5, habilidade="Perfurar")
    self.inimigo = Inimigo(nome="Lobo", vida=70, nivel=3, tipo="Normal")
  
  def iniciar_batalha(self):
    """Fazer gestão da batalha em turnos"""
    print("Iniciando Batalha!")
    while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0: 
      print("\nDetalhes dos Personagens:")
      print(self.heroi.exibir_detalhes())
      print(self.inimigo.exibir_detalhes())

      input("Pressione Enter para atacar...")
      escolha = input("Escolha (1 - Atack Normal, 2 - Atack Special): ")

      if escolha == "1":
        self.heroi.atacar(self.inimigo)
      elif escolha == "2":
        self.heroi.atacar_especial(self.inimigo)
      else: 
        print("Escolha Inválida, selecione uma opção valida")

      if self.inimigo.get_vida() > 0:
        self.inimigo.atacar(self.heroi)
    
    if self.heroi.get_vida() > 0:
      print("Parabéns, voce venceu a batalha!")
    else:
      print("Voce foi derrotado!")

jogo = Jogo()
jogo.iniciar_batalha()