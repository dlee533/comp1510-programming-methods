def main():
    print(23/0)

    print("IndexError"[10])
    print("IndexError"[-20])

    print(int("TypeError"))
    print(2 + "TypeError")

if __name__ == "__main__":
    main()