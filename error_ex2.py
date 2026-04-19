my_list = [10, 20, 30, 40, 50]

try:
    index = int(input("Index enter maadi (0-4): "))
    result = my_list[index] + "hello"

except IndexError:
    print("❌ Index list range alli illa!")

except TypeError:
    print("❌ Number mattu string add maadabarudu!")

finally:
    print("✅ Program complete!")
