import string
import random
import json
import os.path


def main():
    answer = "y"
    print("Hi, Marta. Welcome to GenPas!")

    while True:
        answer = input("Do you need a new password? Y/N: ").casefold()
        if answer == "y":
            filename = "./password_generator/saved_passwords.json"
            if os.path.exists(filename):
                with open(filename, "r") as f:
                    saved_passwords = json.load(f)
            else:
                saved_passwords = {}

            application_name = input("Give application name: ")

            manage_password(application_name, filename, saved_passwords)
        elif answer == "n":
            break
        else:
            pass


def manage_password(application_name, filename, saved_passwords):
    overwrite = 'y'
    if application_name in saved_passwords:
        password = get_password(application_name, saved_passwords)
        overwrite = input(f"Password to this application already exists: \n"
                          f"{password}\n"
                          f"Overwrite? Y/N: ").casefold()
    else:
        pass
    while True:
        if overwrite == "y":
            [num_of_letters_lowercase, num_of_letters_uppercase, num_of_digits,
             num_of_special_characters] = load_preferences(default_num="3")

            password = set_password(num_of_letters_lowercase, num_of_letters_uppercase,
                                    num_of_digits, num_of_special_characters)
            save_password(application_name, password, saved_passwords, filename)
            break
        elif overwrite == "n":
            break
        else:
            overwrite = input("Password to this application already exists. Overwrite? Y/N: ")


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

    return password


def get_password(application_name, saved_passwords):
    password = saved_passwords[application_name]
    return password


def save_password(application_name, password, saved_passwords, filename):
    saved_passwords[application_name] = password
    with open(filename, "w") as f:
        json.dump(saved_passwords, f)
    print(f"Your password: {password} to {application_name} was saved in saved_password.json file"
          f"\n")


if __name__ == '__main__':
    main()
