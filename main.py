import os
names = []
with open("./Input/Names/invited_names.txt", 'r', encoding='utf-8') as file_names:
    for line in file_names:
        names.append(line.strip())
with open("./Input/Letters/starting_letter.txt", "r",encoding='utf-8') as letter:
    template = letter.read()
for name in names:
    letter_content = template.replace("[name]", name)
    letter_filename = f'letter_for_{name}.txt'
    letter_path = os.path.join("./Output/ReadyToSend", letter_filename)

    with open(letter_path, 'w', encoding='utf-8') as letter_file:
        letter_file.write(letter_content)