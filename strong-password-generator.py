import random  # Import the random module to select random characters
import time    # Import the time module (not used here, but commonly used for delays)
import os      # Import the os module to clear the console

def start():
    """
    Generates a secure random password.
    - Chooses a random length between 10 and 30.
    - Builds the password by randomly selecting characters from a predefined layout.
    Returns:
        A string representing the generated password.
    """
    # Choose a random password length between 10 and 30 characters
    length = random.randint(10, 30)

    # Define the set of allowed characters (letters, numbers, special symbols, accented letters)
    layout = (
        'Z$K8GDV7ÂY]HN5{PÈ?SÒQUÌ4"<ÍJ&Ê!6}_3RÁWBÓ)TÙ2OÇ>EC+À;[#-1F9XM%Ú0IÔ:Ã(,*ÉLA@^/.'
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"}{[]_+-/,;?. 1234567890:<>ÇÂÃÁÀÒÓÔÍÌÙÚÈÉÊ'
    )

    password = ''  # Initialize an empty string to accumulate the password characters

    # Loop 'length' times to build the password
    for _ in range(length):
        # Randomly pick one character from the layout
        char = random.choice(layout)
        # Append the chosen character to the password
        password += char

    return password  # Return the completed password


# Main program loop
while True:
    os.system('cls')  # Clear the console screen (Windows command)

    # Display the interactive menu and prompt the user for an option
    menu = int(input(
        "\n* Menu *\n"
        "1- Generate password\n"
        "2- Exit\n"
        "R: "
    ))

    # Validate input: continue prompting until the user enters 1 or 2
    while menu not in (1, 2):
        menu = int(input(
            "\n* Menu *\n"
            "Invalid option!\n"
            "1- Generate password\n"
            "2- Exit\n"
            "R: "
        ))

    if menu == 1:
        # If user chooses to generate a password, call the start() function
        print(f"Your password is:\n\n{start()}")

        # After showing the password, prompt the user to press "1" to return to the menu
        cont = int(input('\nType "1" to go back\nR: '))
        while cont != 1:
            cont = int(input('\nType "1" to go back\nR: '))
    else:
        # If user chooses 2, exit the program
        print('\nProgram terminated!')
        break  # Break out of the while loop and end execution
