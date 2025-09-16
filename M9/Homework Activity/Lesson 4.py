import random as r

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
while True:
    password_length = int(input("==========================\nEnter the number of characters you want for your password (minimum of 8 characters): "))
    if password_length < 8:
        print("==========================\nPassword length must be at least 8 characters. Please try again.")
        continue
    else:
        print("Your password is: ", ''.join(r.choices(chars, k=password_length)))
        print("Do you want to exit? (1=Yes, 2=No)")
        exit_choice = int(input())
        if exit_choice == 1:
            print('==========================\n')
            break
        else:
            continue
