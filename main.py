password = input("Enter Password: ")

has_upper = False
has_lower = False
has_number = False
has_special = False

for i in password:

    if i.isupper():
        has_upper = True

    elif i.islower():
        has_lower = True

    elif i.isdigit():
        has_number = True

    else:
        has_special = True


if (
len(password) >= 8
and has_upper
and has_lower
and has_number
and has_special
):
    print("Strong Password")

elif len(password) >= 8:
    print("Medium Password")

else:
    print("Weak Password")