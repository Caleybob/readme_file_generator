from InquirerPy import prompt, inquirer
from pathlib import Path

script_path = Path(__file__)

output_file_directory = script_path.resolve().parent

output_file = output_file_directory / "README.md"

with open(output_file, 'w') as file:
    file.write('some text')

questions  = [

    {"type": "input", "message": "Project Title:", "name": "project_title"},

    {"type": "input", "message": "description", "name": "description"},

    {"type": "input", "message": "Installation Instructions:", "name": "install_info"},

    {"type": "input", "message": "Usage Information", "name": "usage_info"},
    
    {
        "type": "list",
        "message": "Which License would you like to choose?:", "name": "license",
        "choices": ["MIT License", "Apache License 2.0", "GPL v3", "BSD 3-Clause License", "Unlicensed / All Rights Reserved"],
    },

    {"type": "input", "message": "Author Name:", "name": "author_name"},

    {"type": "input", "message": "Contact Information:", "name": "contact_info"},

     {"type": "confirm", "message": "Confirm?"},
]  


result = prompt(questions)
print(f'Project Title: {result["project_title"]}')
print(f'Description: {result["description"]}')
print(f'Installation Instructions: {result["install_info"]}')
print(f'Usage Information {result["usage_info"]}')
print(f'License: {result["license"]}')
print(f'Author: {result["author_name"]}')
print(f'Contact information: {result["contact_info"]}')






