import string
import random

def main():
    print("Hi, Marta. Welcome to GenPas!")
    application_name = input("Give application name: ")
    set_password(application_name)

def set_password(application_name):
    letters_uppercase = list(string.ascii_uppercase)
    letters_lowercase = list(string.ascii_lowercase)
    digits = list(string.digits)
    special_characters = list(string.punctuation)
    new_password = 'Y'
    proper_nums = str(list(range(0, 11)))
    default_num = "3"

    while True:
        if new_password == 'Y' or new_password == 'y':
            password = []
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

            password.extend(random.choices(letters_lowercase, k=int(num_of_letters_lowercase)))
            password.extend(random.choices(letters_uppercase, k=int(num_of_letters_uppercase)))
            password.extend(random.choices(digits, k=int(num_of_digits)))
            password.extend(random.choices(special_characters, k=int(num_of_special_characters)))

            random.shuffle(password)
            password = ''.join(password)
            print(f"Your password: {password}\n")
            new_password = input("Do you need a new password? Y/N:")

        elif new_password == 'N' or new_password == 'n':
            break
        else:
            new_password = input("Do you need a new password? Y/N:")

        with open("no_password_at_all.txt", "w") as passwords_file:
            passwords_file.write(f"{application_name}: {password}")


if __name__ == '__main__':
    main()