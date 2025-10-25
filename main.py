from InquirerPy import prompt
from pathlib import Path
import sys


class ReadmeGenerator:
    def __init__(self):
        self.questions = [
            {"type": "input", "message": "Project Title:", "name": "project_title"},
            {"type": "input", "message": "description", "name": "description"},
            {"type": "input", "message": "Installation Instructions:", "name": "install_info"},
            {"type": "input", "message": "Usage Information:", "name": "usage_info"},
            {
                "type": "list",
                "message": "Which License would you like to choose?:",
                "name": "license",
                "choices": [
                    "Unlicensed / All Rights Reserved",
                    "MIT License",
                    "Apache License 2.0",
                    "GPL v3",
                    "BSD 3-Clause License",
                ],
            },
            {"type": "input", "message": "Author Name:", "name": "author_name"},
            {"type": "input", "message": "Contact Information:", "name": "contact_info"},
            {"type": "confirm", "message": "Confirm?", "name": "confirm"},
        ]

        self.license_texts = {
            "MIT License": "This project is licensed under the MIT License. See the LICENSE file for details.",
            "Apache License 2.0": "This project is licensed under the Apache License 2.0. See the LICENSE file for details.",
            "GPL v3": "This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the LICENSE file for details.",
            "BSD 3-Clause License": "This project is licensed under the BSD 3-Clause License. See the LICENSE file for details.",
            "Unlicensed / All Rights Reserved": "This project is not licensed. All rights reserved.",
        }

    def run(self):
        result = prompt(self.questions)

        if not result["confirm"]:
            sys.exit()

        script_path = Path(__file__)
        output_file_directory = script_path.resolve().parent
        output_file = output_file_directory / "README.md"

        with open(output_file, "w", encoding="utf-8") as file:
            print("\n\n") 

        if result["project_title"]:
            with open(output_file, "a", encoding="utf-8") as file:
                file.write(f'### {result["project_title"]}')

        if result["description"]:
            with open(output_file, "a", encoding="utf-8") as file:
                file.write("\n\n")
                file.write("## Description\n\n")
                file.write(f'{result["description"]}')
       
        if result["install_info"]:
            with open(output_file, "a", encoding="utf-8") as file:
                file.write("\n\n")
                file.write("## Installation Instructions\n\n")
                file.write(f'{result["install_info"]}')
    
        if result["usage_info"]:
            with open(output_file, "a", encoding="utf-8") as file:
                file.write("\n\n")
                file.write("## Usage Information\n\n")
                file.write(f'{result["usage_info"]}')

        with open(output_file, "a", encoding="utf-8") as file:
            file.write("\n\n")
            file.write("# License Information\n\n")
            file.write(self.license_texts.get(result["license"]))
   
        if result["author_name"]:
            with open(output_file, "a", encoding="utf-8") as file:
                file.write("\n\n")
                file.write("# Author\n\n")
                file.write(f'By {result["author_name"]}')

        if result["contact_info"]:
            with open(output_file, "a", encoding="utf-8") as file:
                file.write("\n\n")
                file.write("# Contact Information\n\n")
                file.write(f'By {result["contact_info"]}')


if __name__ == "__main__":
    generator = ReadmeGenerator()
    generator.run()



        






