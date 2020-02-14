# Author: Jacob Gualtieri
# Date: 2/14/2020
# Password Reader - Verifies that a password meets requirements

def read_password(password, min_length):
    num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    special_char_list = ['!', '@', '#', '$', '%', '&', '*']
    num_count = 0
    special_char_count = 0
    if (not type(password) is str) or (not type(min_length) is int):
        raise TypeError("password must be a String, or min_length must be an int")
    if len(password) < min_length:
        return "Password must be at least " + str(min_length) + " characters long."
    for char in password:
        if char in num_list:
            num_count += 1
        elif char in special_char_list:
            special_char_count += 1
    if num_count < 1:
        return "Password must contain at least one number."
    if special_char_count < 1:
        return "Password must contain at least one special character."
    return "Password is okay!"

def main():
    password = input("New password: ")
    min_length = 8
    print(read_password(2, min_length))


main()
