if __name__ == "__main__":
    hour, minute = map(int, input().split())

    if minute >= 45:
        print(f"{hour} {minute - 45}")
    elif hour == 0:
        print(f"{hour + 24 - 1} {minute + 60 - 45}")
    else:
        print(f"{hour - 1} {minute + 60 - 45}")
