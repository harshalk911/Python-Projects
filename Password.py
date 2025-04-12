def strength():
    password = (input("Enter a Password: "))
    result = {}

    if len(password) >= 8:
        result["Length"] = True

    digit = False
    uppercase = False

    for item in password:
        if item.isdigit():
            digit = True

    for i in password:
        if i.isupper():
            uppercase = True

    result["Digits"] = digit
    result["Uppercase"] = uppercase

    if all(result.values()):
        return "Strong Password"

    else:
        print("Weak Password!"'\n',"Password should contain at least 8 characters, 1 uppercase and 1 number")
        return "Weak Password"


while True:

    value = strength()

    if value.startswith("Weak"):
        continue
    else:
        print("Strong Password")
        break
print("Your Password is set up")