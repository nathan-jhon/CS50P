# Define the main function
def main():
    # Prompt the user for input and strip leading/trailing whitespace
    greeting = input("Enter your greeting: ").strip()
    # Print the result of the value function
    print(value(greeting))

# Define the value function
def value(greeting):
    # Convert the greeting to lowercase and check conditions
    if greeting.lower().startswith("hello"):
        # Return 0 if the greeting starts with "hello"
        return 0
    elif greeting.lower().startswith("h"):
        # Return 20 if the greeting starts with "h" but not "hello"
        return 20
    else:
        # Return 100 for all other cases
        return 100

# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function
    main()

