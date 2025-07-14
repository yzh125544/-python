from validator_collection import validators, errors

def main():
    email = input("Email: ")

    try:
        validators.email(email, allow_empty=False)
        print("Valid")
    except (errors.InvalidEmailError, ValueError):
        print("Invalid")

if __name__ == "__main__":
    main()
