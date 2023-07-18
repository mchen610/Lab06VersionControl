def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode(num_string):
    encoded = ""
    for i in range(len(num_string)):
        encoded += str((int(num_string[i])+3)%10)
    return encoded

def decode(encoded_password):
    pass

def main():
    encoded_password = ""
    while True:
        print_menu()
        choice = int(input("Please enter an option: "))
        if choice == 1:
            encoded_password = input("Please enter your password to encode: ")
            encoded_password = encode(encoded_password)
            print("Your password has been encoded and stored!")
        elif choice == 2:
            if len(encoded_password) == 0:
                print("The password does not exist")
            else:
                print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}")
        elif choice == 3:
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()