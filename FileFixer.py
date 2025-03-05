# Display title, instructions, and accept user input for target file.
def title():
    print("Welcome to FileFixer")
    print("This program attempts to fix corrupted files.") 
    print("You can let the program make an educated guess or choose your desired file type manually")
    userSelection = input("Enter 1 for auto or 2 for manual mode: ")
    if userSelection == 1:
        autoFix()
    elif userSelection == 2:
        manualFix()
    else:
        print("That is not a recognized input, try again")

# Offer manual selection of desired file type conversion.
def manualFix():
    targetPath = input("Please enter the full path of your target: ")
    fileType = input("Please enter your desired file type without the '.' (case insensitive): ")


# Open file and examine magic bytes
def autoFix():
    targetPath = input("Please enter the full path of your target: ")

# Compare magice bytes to list of known formats and find closest match.

# Replace magic bytes with closest match.

# Save new copy seperately and preserve original.

# Return to intro for repeated execution as needed.