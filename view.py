def get_information():
    info = []
    last_name = input('Введите Фамилию: ')
    info.append(last_name)
    first_name = input('Введите Имя: ')
    info.append(first_name)
    telephone_number = input('Введите номер телефона: ')
    info.append(telephone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info