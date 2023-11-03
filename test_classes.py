from classes import Record, AddressBook
from constants import GREEN, RESET

# =============================================
#             test 1 (Classes)
# =============================================

if __name__ == '__main__':
    

    book = AddressBook()
    filename = 'book_test_1.bin'
    
    print(GREEN + "     створюємо новий контакт" + RESET)
    print(book.add_record(Record("tom", "0995648525", birthday="04-11-1986")))    
    
    print(GREEN + "     створюємо новий контакт, у якого тільки день народження" + RESET)
    print(book.add_record(Record("helen", birthday="23-11-1999")))
    
    print(GREEN + "     створюємо новий контакт, у якого є тільки ім'я" + RESET)
    print(book.add_record(Record("jerry")))
    
    print(GREEN + "     створюємо новій контакт в 3 дії" + RESET)
    name = "bill"
    phone = "0677977166"
    b_day = "27-10-1968"
    rec = Record(name, phone, b_day)
    print(book.add_record(rec))
    
    print(GREEN + "     намагаємось додати вже існуючий телефон" + RESET)
    result = rec.add_phone("0677977166")
    print(result)
    
    print(GREEN + "     додаємо другий телефон" + RESET)
    print(rec.add_phone("0933903357"))
    
    print(GREEN + "     намагаємося поміняти телефон на такий самий" + RESET)
    print(rec.edit_phone("0677977166", "+380677977166"))
    
    print(GREEN + "     міняємо номер телефона на інший" + RESET)
    print(rec.edit_phone("0677977166", "0997058845"))
    
    print(GREEN + "     намагаємося поміняти неіснуючий номер телефона" + RESET)
    print(rec.edit_phone("0671234567", "1234567809"))
    
    print(GREEN + "     намагаємося видалити неіснуючий номер телефона" + RESET)
    print(rec.remove_phone("0677977166"))

    print(GREEN + "     видаляємо один з номерів телефону" + RESET)
    print(rec.remove_phone("0997058845"))
    
    print(GREEN + "     додаємо ще один номер" + RESET)
    print(rec.add_phone("0677977166"))

    print(GREEN + "     шукаємо номер" + RESET)
    print(rec.find_phone("0677977166"))
    
    print(GREEN + "     шукаємо номер" + RESET)
    print(rec.find_phone("0933903357"))

    print(GREEN + "     шукаємо неіснуючий номер" + RESET)
    print(rec.find_phone("0677977444"))

    print(GREEN + "     додаємо новий контакт" + RESET)
    print(book.add_record(Record("ivan", "0671234567")))
    
    print(GREEN + "     додаємо новий контакт" + RESET)
    print(book.add_record(Record("mary", "0671234555", "5-11-2000")))
    
    print(GREEN + "     додаємо новий контакт" + RESET)
    print(book.add_record(Record("jill", "0672223344", birthday="03-11-2012")))
    
    print(GREEN + "     шукаємо контакт" + RESET)
    print(book.find_name("bill"))

    print(GREEN + "     шукаємо неіснуючий контакт" + RESET)
    print(book.find_name("john"))
    
    print(GREEN + "     перелік контактів до видалень контактів" + RESET)
    print("======= before delete =========")
    print(book)
    
    print(GREEN + "     зберігаємо контакти" + RESET)
    print(book.write_contacts_to_file(filename))
    
    print(GREEN + "     видаляємо 5 контактів" + RESET)
    print(book.delete_record("mary"))
    print(book.delete_record("tom"))
    print(book.delete_record("ivan"))
    print(book.delete_record("jill"))
    print(book.delete_record("bill"))

    print(GREEN + "     перелік контактів після видалень" + RESET)
    print("======== after delete ========")
    print(book)
    
    print(GREEN + "     відновлюємо контакти з файлу" + RESET)
    book = book.read_contacts_from_file(filename)
    
    print(GREEN + "     перелік контактів після відновлення (такий самий, як до видалення)" + RESET)
    print(GREEN + "     додано сортування контактів за алфавітом - відбувається під час читання файлу" + RESET)
    print("======== after restoring from a file ========")
    print(book)
    