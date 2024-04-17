def main():
    while True:
        fraction = input("Enter the fraction (X/Y) indicating fuel level in the tank: ")
        try:
            percentage = convert(fraction)
            print(f"The tank is {gauge(percentage)}")
            break
        except (ValueError, ZeroDivisionError) as e:
            print(e)


def convert(fraction):
    try:
        X, Y = map(int, fraction.split('/'))
        if X > Y:
            raise ValueError("X cannot be greater than Y")
        if Y == 0:
            raise ZeroDivisionError("Y cannot be 0")
        percentage = round((X / Y) * 100)
        return min(max(0, percentage), 100)
    except ValueError:
        raise ValueError("Invalid input format. Please provide X/Y format as input.")
    except ZeroDivisionError:
        raise ZeroDivisionError("Denominator Y cannot be zero.")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
