def main():
    greeting = input("Enter your greeting: ").strip()
    print(value(greeting))

def value(greeting):
    if greeting.lower().startswith("hello"):
        return 0
    elif greeting.lower().startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()

