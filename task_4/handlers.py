def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Not found."
        except IndexError:
            return "Enter user name."

    return inner



@input_error
def add_contact(args: list, contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def show_all(contacts: dict) -> None :
    print("Contacts:")
    for name, phone in contacts.items():
        print(f"{name} - {phone}")


@input_error
def show_phone( args: list, contacts: dict) -> str: 
    name = args[0]
    phone = contacts.get(name)
    if phone: 
        return f"{name} - {phone}"
    
    return f"{name} not found."


@input_error
def change_contact(args: list, contacts: dict) -> str:
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Does not have a contact by name: {name}."
