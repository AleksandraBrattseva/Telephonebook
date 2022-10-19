from view import get_information as gi

info = gi()
def writing_scv():
    file = 'file.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')

def writing_txt():
    file = 'file.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Last name: {info[0]}\nFirst name: {info[1]}\nTelephone number: {info[2]}\nDescription: {info[3]}\n\n\n')

def creating():
    file = 'file.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'last name;first name;telephone number;description\n')