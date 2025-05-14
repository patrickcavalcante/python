def show_menu():
  print("\n--- Menu da Agenda ---")
  print("1. Adicionar contato")
  print("2. Ver contatos")
  print("3. Editar contato")
  print("4. Marcar/desmarcar favorito")
  print("5. Ver contatos favoritos")
  print("6. Apagar contato")
  print("7. Sair")

def add_contact(contacts):
  name = input("Nome: ")
  phone = input("Telefone: ")
  email = input("Email: ")
  favorite = input("É favorito? (s/n): ").lower() == 's'
  contact = {
    "name": name,
    "phone": phone,
    "email": email,
    "favorite": favorite
  }
  contacts.append(contact)
  print(f"Contato '{name}' adicionado com sucesso!")
  return

def list_contacts(contacts):
  if not contacts:
    print("Nenhum contato encontrado.")
    return
  print("\n--- Lista de Contatos ---")
  for index, contact in enumerate(contacts, start=1):
    fav = "⭐" if contact["favorite"] else ""
    print(f"{index}. {contact['name']} - {contact['phone']} - {contact['email']} {fav}")
  return

def edit_contact(contacts):
  list_contacts(contacts)
  index = int(input("Digite o número do contato que deseja editar: ")) - 1
  if 0 <= index < len(contacts):
    name = input("Novo nome (deixe vazio para manter): ")
    phone = input("Novo telefone (deixe vazio para manter): ")
    email = input("Novo email (deixe vazio para manter): ")
    if name:
      contacts[index]["name"] = name
    if phone:
      contacts[index]["phone"] = phone
    if email:
      contacts[index]["email"] = email
    print("Contato atualizado com sucesso.")
  else:
    print("Índice inválido.")
  return

def toggle_favorite(contacts):
  list_contacts(contacts)
  index = int(input("Digite o número do contato para marcar/desmarcar favorito: ")) - 1
  if 0 <= index < len(contacts):
    contacts[index]["favorite"] = not contacts[index]["favorite"]
    status = "favorito" if contacts[index]["favorite"] else "não favorito"
    print(f"Contato agora está marcado como {status}.")
  else:
    print("Índice inválido.")
  return

def list_favorites(contacts):
  favorites = [c for c in contacts if c["favorite"]]
  if not favorites:
    print("Nenhum contato favorito.")
  else:
    print("\n--- Contatos Favoritos ---")
    for i, contact in enumerate(favorites, start=1):
      print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']} ⭐")
  return

def delete_contact(contacts):
  list_contacts(contacts)
  index = int(input("Digite o número do contato que deseja apagar: ")) - 1
  if 0 <= index < len(contacts):
    name = contacts[index]["name"]
    del contacts[index]
    print(f"Contato '{name}' apagado com sucesso.")
  else:
    print("Índice inválido.")
  return

contacts = []

while True:
  show_menu()
  choice = input("Escolha uma opção: ")

  if choice == "1":
    add_contact(contacts)
  elif choice == "2":
    list_contacts(contacts)
  elif choice == "3":
    edit_contact(contacts)
  elif choice == "4":
    toggle_favorite(contacts)
  elif choice == "5":
    list_favorites(contacts)
  elif choice == "6":
    delete_contact(contacts)
  elif choice == "7":
    print("Programa encerrado.")
    break
  else:
    print("Opção inválida. Tente novamente.")
