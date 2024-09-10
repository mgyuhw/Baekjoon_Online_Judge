if __name__ == "__main__":
    num_list = input().split()
    a, b, c = map(int, num_list)

    if a == b == c:
        print(10000 + (a * 1000))
    elif a == b or a == c:
        print(1000 + (a * 100))
    elif b == c:
        print(1000 + (c * 100))
    else:
        print(int(max(num_list)) * 100)
