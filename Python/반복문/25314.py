byte = int(input())

print("long " * ((byte // 4) + 1) + "int") if byte % 4 > 0 else print("long " * (byte // 4) + "int")