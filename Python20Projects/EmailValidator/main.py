email = input("Enter your email: ")
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                print("Your email is valid")
            else:
                print("Your email is invalid")
        else:
            print("Your email is invalid")
else:
    print("Your email is invalid")
