import sys

def main():
    sys.stdout.write(str(len(list(sys.stdin.readline().split()))))

if __name__ == "__main__":
    main()