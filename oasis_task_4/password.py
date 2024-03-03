import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    # Create a list of characters based on user preferences
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    # Check if any character types were selected
    if not characters:
        print("No character types selected.")
        return None
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Get user input for password criteria
    try:
        length = int(input("Enter password length: "))
        use_letters = input("Use letters? (y/n): ").lower() == 'y'
        use_numbers = input("Use numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Use symbols? (y/n): ").lower() == 'y'
        
        # Generate and display the password
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input! Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
