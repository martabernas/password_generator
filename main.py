import string
import random
import json
import os.path


def main():
    new_password = "y"
    print("Hi, Marta. Welcome to GenPas!")
    accepted_answers = ["y", "Y", "N", "n"]
    overwrite = 'y'

    while new_password == "y" or new_password == "Y":
        filename = "./password_generator/saved_passwords.json"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                saved_passwords = json.load(f)
        else:
            saved_passwords = {}

        application_name = input("Give application name: ")

        if application_name in saved_passwords:
            overwrite = input("Password to this application already exists. Overwrite? Y/N: ")
        else:
            pass
        while True:
            if overwrite == "y" or overwrite == "Y":
                [num_of_letters_lowercase, num_of_letters_uppercase, num_of_digits,
                 num_of_special_characters] = load_preferences(default_num="3")

                password = set_password(num_of_letters_lowercase, num_of_letters_uppercase,
                                        num_of_digits, num_of_special_characters)
                save_password(application_name, password, saved_passwords, filename)
                break
            elif overwrite == "n" or overwrite == "N":
                break
            else:
                overwrite = input("Password to this application already exists. Overwrite? Y/N: ")

        while True:
            new_password = input("Do you need a new password? Y/N: ")
            if new_password in accepted_answers:
                break


def load_preferences(default_num):
    while True:
        proper_nums = str(list(range(0, 11)))
        print(f"Desired number (default {default_num}) of: ")
        num_of_letters_lowercase = input("* lowercase letters: ") or default_num
        num_of_letters_uppercase = input("* uppercase letters: ") or default_num
        num_of_digits = input("* digits: ") or default_num
        num_of_special_characters = input("* special characters: ") or default_num

        if num_of_letters_lowercase not in proper_nums or num_of_letters_uppercase not in \
                proper_nums or num_of_digits not in proper_nums or num_of_special_characters \
                not in proper_nums:
            print("Numbers must be integers in range from 0 to 10!")
            continue
        else:
            break

    return num_of_letters_lowercase, num_of_letters_uppercase, num_of_digits, \
        num_of_special_characters


def set_password(num_of_letters_lowercase, num_of_letters_uppercase, num_of_digits,
                 num_of_special_characters):
    letters_uppercase = list(string.ascii_uppercase)
    letters_lowercase = list(string.ascii_lowercase)
    digits = list(string.digits)
    special_characters = list(string.punctuation)

    password = []

    password.extend(random.choices(letters_lowercase, k=int(num_of_letters_lowercase)))
    password.extend(random.choices(letters_uppercase, k=int(num_of_letters_uppercase)))
    password.extend(random.choices(digits, k=int(num_of_digits)))
    password.extend(random.choices(special_characters, k=int(num_of_special_characters)))

    random.shuffle(password)
    password = ''.join(password)

    print(f"Your password: {password}\n")
    return password


def save_password(application_name, password, saved_passwords, filename):
    saved_passwords[application_name] = password
    with open(filename, "w") as f:
        json.dump(saved_passwords, f)


if __name__ == '__main__':
    main()
