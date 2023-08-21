"""
Реализовать телефонный справочник со следующими возможностями:
1.                   Вывод постранично записей из справочника на экран
2.                   Добавление новой записи в справочник
3.                   Возможность редактирования записей в справочнике
4.                   Поиск записей по одной или нескольким характеристикам
Требования к программе:
1.                   Реализация интерфейса через консоль (без веб- или графического интерфейса)
2.                   Хранение данных должно быть организовано в виде текстового файла, формат которого
                     придумывает сам программист
3.                   В справочнике хранится следующая информация: фамилия, имя, отчество,
                     название организации, телефон рабочий, телефон личный (сотовый)

"""

contacts_file = "contacts.txt"
page_size = 10


def paginate(records, page_size):
    """
    Разделить записи постранично.
    """
    return [records[i:i + page_size] for i in range(0, len(records), page_size)]


def display_page(page):
    """
    Вывести на экран одну страницу записей.
    """
    for contact in page:
        print(contact)
        print('-' * 30)


def display_contacts(records, page_size):
    """
    Вывести все записи из справочника постранично.
    """
    pages = paginate(records, page_size)

    current_page = 1
    total_pages = len(pages)

    while True:
        print(f"Страница {current_page}/{total_pages}")
        print('-' * 30)
        display_page(pages[current_page - 1])
        print('-' * 30)

        choice = input("Далее (d), Назад (b), В начало (f), В конец (e), Выйти в основное меню(q): ")

        if choice == 'd':
            if current_page < total_pages:
                current_page += 1
            else:
                print("Вы достигли конца справочника.")
        elif choice == 'b':
            if current_page > 1:
                current_page -= 1
            else:
                print("Вы достигли начала справочника.")
        elif choice == 'f':
            current_page = 1
        elif choice == 'e':
            current_page = total_pages
        elif choice == 'q':
            break
        else:
            print("Некорректный ввод. Пожалуйста, повторите попытку.")


def add_contact():
    """
    Добавить новую запись в справочник.
    """
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    organization = input("Введите название организации: ")
    work_phone = input("Введите рабочий телефон: ")
    personal_phone = input("Введите личный телефон: ")

    contact = f"{last_name},{first_name},{middle_name},{organization},{work_phone},{personal_phone}\n"

    with open(contacts_file, "a") as file:
        file.write(contact)

    print("Запись успешно добавлена!")


def edit_contact(records):
    """
    Редактировать запись в справочнике.
    """
    index = int(input("Введите номер записи, которую вы хотите отредактировать: ")) - 1

    if index < 0 or index >= len(records):
        print("Некорректный номер записи.")
        return

    contact = records[index]
    contact_fields = contact.split(',')

    print("Нажмите \"Enter\", если не хотите изменять характиристику")
    last_name = input(f"Фамилия ({contact_fields[0]}): ") or contact_fields[0]
    first_name = input(f"Имя ({contact_fields[1]}): ") or contact_fields[1]
    middle_name = input(f"Отчество ({contact_fields[2]}): ") or contact_fields[2]
    organization = input(f"Оргинизация ({contact_fields[3]}): ") or contact_fields[3]
    work_phone = input(f"Рабочий номер ({contact_fields[4]}): ") or contact_fields[4]
    personal_phone = input(f"Личный номер ({contact_fields[5]}): ") or contact_fields[5]

    new_contact = f"{last_name},{first_name},{middle_name},{organization},{work_phone},{personal_phone}"

    # заменяем старую запись на новую
    records[index] = new_contact

    with open(contacts_file, "w") as file:
        file.writelines(records)

    print("Запись успешно отредактирована.")


def search_criteria_dict():
    """
    Для выбора критериев и их значений при поиске.
    """
    search_criteria = dict()
    while True:
        print(f"\tМеню критериев для поиска.\n"
              f"0 - \tФалимилия\n"
              f"1 - \tИмя\n"
              f"2 - \tОтчество\n"
              f"3 - \tНазвание организации\n"
              f"4 - \tТелефон рабочий\n"
              f"5 - \tТелефон личный\n"
              f"6 - \tЗакончить добавлять критерии поиска\n")
        choice = int(input("Ввести цифру критерия: "))
        if choice == 0:
            param = input("Ввод значения критерия: ")
            search_criteria[choice] = param
        elif choice == 1:
            param = input("Ввод значения критерия: ")
            search_criteria[choice] = param
        elif choice == 2:
            param = input("Ввод значения критерия: ")
            search_criteria[choice] = param
        elif choice == 3:
            param = input("Ввод значения критерия: ")
            search_criteria[choice] = param
        elif choice == 4:
            param = input("Ввод значения критерия: ")
            search_criteria[choice] = param
        elif choice == 5:
            param = input("Ввод значения критерия: ")
            search_criteria[choice] = param
        elif choice == 6:
            break
        else:
            print("Некорректный ввод. Пожалуйста, повторите попытку.")
    return search_criteria


def search_records():
    """
    Поиск
    """
    search_count = input("Поиск по 1 или по нескольким характеристикам? (Введите: 1 или 2+): ")
    records = get_records()
    results = []
    if search_count == '1':

        search_criteria = input("Введите то, по чему хотите найти совпадения в справочнике: ")
        with open(contacts_file, "r") as file:
            for line in file:
                if search_criteria.lower() in line.lower():
                    results.append(line)

    elif search_count == '2+':
        records2 = []  # чтобы стал двумерным
        for record in records:
            elements = record.strip().split(',')
            records2.append(elements)
        search_criteria = search_criteria_dict()

        for record in records2:

            match = True  # флаг, который определяет, соответствия ли запись критериям поиска

            for key, value in search_criteria.items():
                if record[key] != value:
                    match = False
                    break
            if match:
                results.append(record)
    else:
        print("Некорректный ввод. Пожалуйста, повторите попытку.")
        search_records()
    if results:
        print("Результаты поиска:")
        print('-' * 30)
        for result in results:
            print(*result)
            print('-' * 30)
    else:
        print("Ничего не найдено.")


def show_menu():
    """
    Реализация меню справочника
    """
    print(f"Tелефонный справочник.\n\t\tМеню:\n"
          f"0 -\tВыход\n"
          f"1 -\tВывод постранично записей из справочника на экран\n"
          f"2 -\tДобавление новой записи в справочник\n"
          f"3 -\tВозможность редактирования записей в справочнике\n"
          f"4 -\tПоиск записей по одной или нескольким характеристикам")
    choice = input("Введите цифру: ")
    return int(choice)


def get_records():
    """
    Получения списка саписей
    """
    with open(contacts_file, "r") as file:
        records = file.readlines()

    return records


if __name__ == "__main__":
    running = True
    while running:
        choice = show_menu()

        if choice == 0:
            print("Выход из программы...")
            running = False
        elif choice == 1:
            records = get_records()
            display_contacts(records, page_size)
        elif choice == 2:
            add_contact()
        elif choice == 3:
            records = get_records()
            edit_contact(records)
        elif choice == 4:
            search_records()
        else:
            print("Неверный выбор. Попробуйте еще раз.")
