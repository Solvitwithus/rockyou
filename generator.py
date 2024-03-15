def generate_passwords(first_input):
    # List of common passwords
    common_passwords = [
        "password",
        "123456",
        "qwerty",
        "abc123",
        "letmein",
        # Add more common passwords here
    ]

    # Generate passwords based on the first input
    passwords = [f"{first_input}{password}" for password in common_passwords]

    return passwords


def save_passwords_to_file(passwords):
    # Open file in write mode
    with open("passwords.txt", "w") as file:
        # Write each password to a new line
        file.write("\n".join(passwords))


# Prompt user for first input
first_input = input("Enter the first input: ")

# Generate passwords
passwords = generate_passwords(first_input)

# Save passwords to file
save_passwords_to_file(passwords)

print("Passwords generated and saved to passwords.txt file.")