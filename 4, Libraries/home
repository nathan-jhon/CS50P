import sys
import pyfiglet

try:
    if len(sys.argv) == 1:
        user = input("Input: ")
        print(pyfiglet.figlet_format(user))
    elif sys.argv[1].startswith("-") and sys.argv[1] not in ["-f", "--font"]:
        print("Invalid option. Please provide valid input.")
        sys.exit(1)
    elif sys.argv[1] in ["-f", "--font"] and len(sys.argv) >= 3:
        user = input("Input: ")
        print(pyfiglet.figlet_format(user, font=sys.argv[2]))
    else:
        user = sys.argv[1]
        print(pyfiglet.figlet_format(user))
except IndexError:
    print("Usage: python figlet.py [OPTION] [TEXT]")
    print("Options:")
    print("  -f, --font FONT     Specify font for text conversion")
