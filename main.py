from InquirerPy import inquirer

license = inquirer.select(
    message = "Which License would you like to choose?:",
    choices = ["MIT License", "Apache License 2.0", "GPL v3", "BSD 3-Clause License", "Unlicensed / All Rights Reserved"], ).execute()

print(license)

