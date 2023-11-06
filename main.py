from classes import Name, Phone, Record, AddressBook, BirthDay, PhoneError, BDayError
from constants import TITLE, FILENAME, RED, BLUE, YELLOW, CYAN, GRAY, WHITE, RESET


book = AddressBook()


def user_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return f"{RED}not enough params{RESET}\n\tFormat: '<command> <name> <args>'\n\tUse 'help' for information"
        except KeyError:
            return f"{RED}Unknown name {args[0]}. Try another or use help{RESET}"
        except ValueError:
            return f"{RED}time data does not match format 'dd-mm-YYYY' (dd<=31, mm<=12){RESET}"
        except BDayError:
            return f"{RED}time data does not match format 'dd-mm-YYYY' (dd<=31, mm<=12) {RESET}"
        except PhoneError:
            return f"{RED}the phone number must contains only digits, format: '0671234567' or '+380671234567'{RESET}"
        except AttributeError:
            return f"{RED}phone number {args[1]} is not among the contact numbers of {args[0]} {RESET}"

    return inner


def get_record_or_error(name, book, return_error=False):
    name_rec = Name(name)
    rec = book.get(str(name_rec))
    if not rec:
        error_message = (
            f"{RED}contact {WHITE}{name}{RED} not found in address book{RESET}"
        )
        if return_error:
            return error_message
        else:
            return rec
    return rec


@user_error
def add_birthday(*args):
    return get_record_or_error(args[0], book).add_birthday((args[1]))


@user_error
def add_contact(*args):
    if get_record_or_error(args[0], book):
        return f"{RED}contact {Name(args[0])} already exist{RESET}\n\t{get_record_or_error(args[0], book)}\n\tUse 'add_phone' or 'change' command to add or change the phone"
    book.add_record(Record(args[0]))

    if len(args) > 1:
        if all([args[-1][2] == args[-1][5] == "-", len(args[-1]) == 10]):
            add_birthday(args[0], args[-1])
            args = args[:-1]
        add_phones(args[0], *args[1:])

    return f"contact {Name(args[0])} has been successfully added \n\t{get_record_or_error(args[0],book)}"


@user_error
def add_few_phones(rec, *args):
    result = ""
    for phone in args:
        rec.add_phone(phone)
        result += (
            f"phone number {Phone(phone)} has been added to {rec.name}'s contact list\n"
        )
    return result


@user_error
def add_phones(*args):
    rec = get_record_or_error(args[0], book)
    return add_few_phones(rec, *args[1:]) + f"\t{rec}"


@user_error
def change_name(*args):
    return book.change_name((args[0]), args[1])


@user_error
def change_phone(*args):
    return get_record_or_error(args[0], book).edit_phone(Phone(args[1]), Phone(args[2]))


@user_error
def del_phone(*args):
    return get_record_or_error(args[0], book).remove_phone(Phone(args[1]))


@user_error
def delete_record(*args):
    return book.delete_record(args[0])


@user_error
def name_find(*args):
    return book.find_name(args[0])


def search(*args):
    result = ""
    if not args:
        return f"{RED}searching string is required{RESET}"
    seek = args[0].lower()
    for name, record in book.data.items():
        if seek.isdigit():
            if record.seek_phone(seek):
                result += "\t" + str(record) + "\n"
        if seek in name.lower():
            result += "\t" + str(record) + "\n"
    if result:
        return f"data found for your request '{seek}': \n{result[:-1]}"
    else:
        return f"{RED}nothing was found for your request '{seek}'{RESET}"


def show_all(*args):
    pages = int(args[0]) if args else len(book.data)
    print(f"  === Address book ===")
    count = 0
    for _ in book.iterator(pages):
        for item in _:
            print(item)
            count += 1
        if count < len(book):
            input(f"  Press Enter for next page: ")
    return "  --- End of List ---"


def help_page(*args):
    help_list = [TITLE]
    help_list.append(
        f"{YELLOW}add {CYAN}<name> <phone>{GRAY}*n {CYAN}<birthday>          {RESET} - add a new contact with a phone number(s) and birthday(optional)"
    )
    help_list.append(
        f"{GRAY}                                                (you can enter several phone numbers for a contact){RESET}"
    )
    help_list.append(
        f"{YELLOW}add_phone {CYAN}<name> <new_phone>{GRAY}*n           {RESET} - add the new phone number for an existing contact"
    )
    help_list.append(
        f"{GRAY}                                                (you can enter several phone numbers for a contact){RESET}"
    )
    help_list.append(
        f'{YELLOW}add_bd {CYAN}<name> <birthday>                 {RESET} - add the birthday data ("dd-mm-yyyy") for an existing contact'
    )
    help_list.append(
        f"{YELLOW}change_name {CYAN}<name> <new_name>            {RESET} - change the name for an existing contact"
    )
    help_list.append(
        f"{YELLOW}change_phone {CYAN}<name> <phone> <new_phone>  {RESET} - change the phone number for an existing contact"
    )
    help_list.append(
        f"{YELLOW}change_bd {CYAN}<name> <new_birthday>          {RESET} - change the phone number for an existing contact"
    )
    help_list.append(
        f"{YELLOW}delete_phone {CYAN}<name> <phone>              {RESET} - delete one phone number from an existing contact"
    )
    help_list.append(
        f"{YELLOW}delete_contact {CYAN}<name> <phone>            {RESET} - remove an existing contact"
    )
    help_list.append(
        f"{YELLOW}find {CYAN}<anything>                          {RESET} - search for any string (>= 3 characters) in the contact data"
    )
    help_list.append(
        f"{YELLOW}name {CYAN}<name>                              {RESET} - search record by the name"
    )
    help_list.append(
        f"{YELLOW}list {GRAY}<pages>                             {RESET} - show all contacts, {GRAY}<pages>(optional) - lines per page{RESET}"
    )
    help_list.append(
        f'{YELLOW}hello                                    {RESET} - "hello-string"'
    )
    help_list.append(
        f"{YELLOW}exit                                     {RESET} - exit from PhoneBook"
    )
    help_list.append(
        f"{YELLOW}help                                     {RESET} - this help-page"
    )
    return "\n".join(help_list)


def say_hello(*args):
    return "How can I help you?"


def say_good_bay(*args):
    print(book.write_contacts_to_file(FILENAME))
    exit("Good bye!")


def unknown(*args):
    return f"{RED}Unknown command. Try again{RESET}"


# =============================================
#                main
# =============================================


COMMANDS = {
    add_contact: ("add_record", "add", "add_contact", "+"),
    add_phones: ("add_phone", "phone_add"),
    change_phone: ("change_phone", "phone_change", "edit_phone"),
    del_phone: ("del_phone", "delete_phone"),
    delete_record: ("delete_record", "delete", "del"),
    add_birthday: ("add_birthday", "add_bd", "change_birthday", "change_bd"),
    change_name: ("change_name", "name_change"),
    name_find: ("name", "find_name"),
    search: ("search", "seek", "find"),
    help_page: ("help",),
    say_hello: ("hello", "hi"),
    show_all: ("show_all", "show", "list"),
    say_good_bay: ("exit", "good_bay", "by", "close", "end"),
}


def parser(text: str):
    for func, cmd_tpl in COMMANDS.items():
        for command in cmd_tpl:
            data = text.strip().lower().split()
            if len(data) < 1:
                break
            if data[0] == command:
                return func, data[1:]
    return unknown, []


def main():
    global book
    book = book.read_contacts_from_file(FILENAME)
    print("\n" + BLUE + TITLE + RESET + "\t\tType 'help' for information")
    while True:
        user_input = input(f"{YELLOW}>>>{RESET}").strip().lower()
        func, data = parser(user_input)
        print(func(*data))
        if func not in [
            say_good_bay,
            show_all,
            say_hello,
            help_page,
            search,
            name_find,
        ]:
            book.write_contacts_to_file(FILENAME)


if __name__ == "__main__":
    main()
