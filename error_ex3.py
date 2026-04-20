filename = input("File hesaru enter maadi: ")

try:
    with open(filename, "r") as f:
        content = f.read()
        print(f"\n📄 File content:\n{content}")

except FileNotFoundError:
    print(f"❌ '{filename}' file sikkala!")

except PermissionError:
    print(f"❌ '{filename}' file open maadabarudu!")
