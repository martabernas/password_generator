import string
import random
import json
import os.path


def main():
    answer = "y"
    filename = "./password_generator/saved_passwords.json"
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            saved_passwords = json.load(f)

    print("Hi, Marta. Welcome to PasswordGenerator!")
    decide(filename, saved_passwords)
    print("Bye bye!")


def manage_passwords(filename, saved_passwords):
    application_name = input("Give application name: ")
    overwrite = 'y'
    if application_name in saved_passwords:
        password = saved_passwords[application_name]
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
            decide(filename, saved_passwords)
            break
        elif overwrite == "n":
            break
        else:
            overwrite = input("Overwrite? Y/N: ").casefold()


def load_preferences(default_num):
    proper_nums = str(list(range(0, 11)))

    while True:
        print(f"Desired number (default {default_num}) of: ")
        num_of_letters_lowercase = input("* lowercase letters: ") or default_num
        num_of_letters_uppercase = input("* uppercase letters: ") or default_num
        num_of_digits = input("* digits: ") or default_num
        num_of_special_characters = input("* special characters: ") or default_num

        if num_of_letters_lowercase not in proper_nums or num_of_letters_uppercase not in \
                proper_nums or num_of_digits not in proper_nums or num_of_special_characters \
                not in proper_nums:
            print("Numbers must be integers in range from 0 to 10!")
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


def get_password(saved_passwords):
    application_name = input("Give application name: ")
    if application_name not in saved_passwords:
        print(f"Password to {application_name} was not found in saved passwords.")
    else:
        password = saved_passwords[application_name]
        print(f"Password to {application_name} is:  {password}")


def save_password(application_name, password, saved_passwords, filename):
    saved_passwords[application_name] = password
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(saved_passwords, f)
    print(f"Your password: {password} to {application_name} was saved in saved_password.json file"
          f"\n")


def decide(filename, saved_passwords):
    answer = input("What do you want to do: \n"
                   "- list all settled passwords (L),\n"
                   "- establish a new password (E), \n"
                   "- get single password? (G) \n"
                   "- exit? (X)\n").casefold()

    match answer:
        case "l":
            print(json.dumps(saved_passwords, indent=2))
            decide(filename, saved_passwords)
        case "e":
            manage_passwords(filename, saved_passwords)
            decide(filename, saved_passwords)
        case "g":
            get_password(saved_passwords)
            decide(filename, saved_passwords)
        case "x":
            return
        case _:
            print("Answer incorrect. \n")
            decide(filename, saved_passwords)


if __name__ == '__main__':
    main()
