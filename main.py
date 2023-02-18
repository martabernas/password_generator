import string
import random


def print_hi(name):
    letters_lowercase = list(string.ascii_lowercase)
    letters_uppercase = list(string.ascii_uppercase)
    digits = list(string.digits)
    special_characters = list(string.punctuation)
    new_password = 'Y'
    proper_nums = str(list(range(0, 11)))
    default_num = "3"

    print("Hi, Marta. Welcome to GenPas!")
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
            print(f"Your password: {''.join(password)}")
            new_password = input("Do you need a new password? Y/N:")

        elif new_password == 'N' or new_password == 'n':
            break
        else:
            new_password = input("Do you need a new password? Y/N:")


if __name__ == '__main__':
    print_hi('PyCharm')
