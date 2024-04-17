def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    d = 0
    while d < len(s):
        if not s[d].isalpha():
            if s[d] == "0":
                return False
            else:
                break
        d += 1

    if any(c in ['.', ' ', '!', '?'] for c in s):
        return False

    return True

if __name__ == "__main__":
    main()

