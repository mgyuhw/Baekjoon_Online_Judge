def multiplication(x, y):
    return int(x) * int(y)

if __name__ == "__main__":
    a = input()
    b = list(map(int, str(input())))
    result = map(multiplication, a, b) # 수정 필요
    print(list(result))