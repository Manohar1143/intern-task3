import random
import string

def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    
    while True:
        try:
            length = int(input("Enter the desired length for your password (minimum 6): "))
            if length < 6:
                print("Password length should be at least 6 characters. Please try again.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    
    
    password = generate_password(length)
    
    
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
