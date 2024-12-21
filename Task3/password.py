import random
import string

# Function to generate a random password
def generate_password(length, use_special_chars=True):
    # Define the characters to use in the password
    if use_special_chars:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits

    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Main function to prompt the user for input
def main():
    print("Welcome to the Password Generator!")

    # User input for password length
    length = int(input("Enter the desired length for your password: "))

    # User input to include special characters or not
    include_special = input("Do you want to include special characters (e.g. !, @, #, $)? (yes/no): ").lower()

    if include_special == 'yes':
        password = generate_password(length, use_special_chars=True)
    else:
        password = generate_password(length, use_special_chars=False)

    print(f"Your generated password is: {password}")

# Run the program
if __name__ == ("__main__"):
                main()