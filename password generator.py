import random
import string

def generate_password(length=12):
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Set the length of the password
password_length = 12  # You can change the length as needed

# Generate and print the password
password = generate_password(password_length)
print("Generated password:", password)
