contact_book = {}
def add_contact(info):
    name = info["name"]
    del info["name"]
    contact_book[name] = info
    print(contact_book)

commands = "addcontact"

appIsOpen = True
while appIsOpen:
    command = input(">>> ")
    if not command in commands:
        continue
    if command == "addcontact":
        name = input("Name (required): ")
        age = input("Age: ")
        if age.isdigit():
            age = int(age)
        else:
            print("age must be a whole number")
            continue
        address = input("Address: ")
        gender = input("Gender :")
        if not gender in ["male", "female", "other"]:
            print('must be "male", "female", or "other"')
            continue
        add_contact({"name":name, "age":age, "address":address, "gender":gender})
    