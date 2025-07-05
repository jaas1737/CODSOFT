import random
import string

def generate_password(length):
    chars=string.ascii_letters+string.digits+string.punctuation
    passw=''.join(random.choice(chars) for i in range(length))
    return passw

def main():
    print("=== Password Generator ===")
    try:
        leng=int(input("Enter the desired password length: "))
        if leng<= 0:
            print("Password length must be greater than 0.")
            return
        passw=generate_password(leng)
        print("Generated Password:", passw)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
