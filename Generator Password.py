import random
import string

def generate_password(length):
    # Define the pool of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using random.choices for the specified length
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    try:
        # Prompt the user to specify the desired length of the password
        length = int(input("Enter the desired length of the password: "))
        
        # Check if the length is valid
        if length <= 0:
            print("Please enter a valid length for the password.")
        else:
            # Generate and display the password
            password = generate_password(length)
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the length of the password.")

if __name__ == "__main__":
    main()

