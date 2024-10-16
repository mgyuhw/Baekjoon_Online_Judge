if __name__ == "__main__":
    a = int(input())
    b = input()
    c = reversed(list(b))

    for y in c:
        print(a * int(y))

    print(a * int(b))
    