contacts = {}

def add_contact():
    name = input("Hesaru: ").title()
    phone = input("Phone number: ")
    email = input("Email: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"✅ {name} add aythu!")

def view_contacts():
    if not contacts:
        print("📭 Yaavude contact illa!")
        return
    print("\n📒 Nimma Contacts:")
    print("=" * 30)
    for name, info in contacts.items():
        print(f"👤 {name}")
        print(f"   📞 {info['phone']}")
        print(f"   📧 {info['email']}")
        print("-" * 30)

def search_contact():
    name = input("Yaara hesaru search maadali? ").title()
    if name in contacts:
        print(f"\n👤 {name}")
        print(f"   📞 {contacts[name]['phone']}")
        print(f"   📧 {contacts[name]['email']}")
    else:
        print(f"❌ '{name}' contact sikkala!")

def delete_contact():
    name = input("Yaara hesaru delete maadali? ").title()
    if name in contacts:
        del contacts[name]
        print(f"🗑️ {name} delete aythu!")
    else:
        print(f"❌ '{name}' contact sikkala!")

def menu():
    print("\n📒 Contact Book")
    print("=" * 30)
    print("1. Contact add maadi")
    print("2. Ella contacts nodu")
    print("3. Contact search maadi")
    print("4. Contact delete maadi")
    print("5. Exit")

while True:
    menu()
    choice = input("\nOption aayke maadi (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("👋 Bye!")
        break
    else:
        print("⚠️ 1 to 5 maatra type maadi!")
