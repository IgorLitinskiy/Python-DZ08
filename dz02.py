#Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
#Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
#для изменения и удаления данных.

def show_data(file_name: str):#Эта ф-ция показывает содержимое справочника
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            print(*line.split(';'), end='')

def new_data(file_name: str):#Добавляет строку в справочник
    with open(file_name, 'r+', encoding='utf-8') as data:
        record_id = 0
        for line in data:
            if line != '':
                record_id = line.split(';', 1)[0]
        print('Введите ФИО, № телефона')
        line = f'{int(record_id) + 1};' + ';'.join(input().split()[:5]) + ';\n'

def find_char():#Эта ф-ция ищет информацию в справочнике
    print('Выберите характеристику:')
    print('0 - id, 1 - фамилия, 2 - имя, 3 - отчество, 4 - номер, q - выйти')
    char = input()
    while char not in ('0', '1', '2', '3', '4', 'q'):
        print('Введены неверные данные')
        print('Выберите характеристику:')
        print('0 - id, 1 - фамилия, 2 - имя, 3 - отчество, 4 - номер, q - выйти')
        char = input()
    if char != 'q':
        inp = input('Введите значение\n')
        return char, inp
    else:
        return 'q', 'q'

def find_records(file_name: str, char, condition):#Эта ф-ция ищет информацию в справочнике
    if condition != 'q':
        printed = False
        with open(file_name, 'r', encoding='utf-8') as data:
            for line in data:
                if condition == line.split(';')[int(char)]:
                    print(*line.split(';'))
                    printed = True
        if not printed:
            print("Не найдено")
        return printed

def check_id_record(file_name: str, text: str):
    decision = input(f'Вы знаете id записи которую хотите {text}? 1 - да, 2 - нет, q - выйти\n')
    while decision not in ('1', 'q'):
        if decision != '2':
            print('Введены неверные данные')
        else:
            find_records(path, *find_char())
        decision = input(f'Вы знаете id записи которую хотите {text}? 1 - да, 2 - нет, q - выйти\n')
    if decision == '1':
        record_id = input('Введите id, q - выйти\n')
        while not find_records(file_name, '0', record_id) and record_id != 'q':
            record_id = input('Введите id, q - выйти\n')
        return record_id
    return decision

def confirmation(text: str):
    confirm = input()
    return confirm

def replace_record_line(file_name: str, record_id, replaced_line: str):
    replaced = ''
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            replaced += line
            if record_id == line.split(';', 1)[0]:
                replaced = replaced.replace(line, replaced_line)
    with open(file_name, 'w', encoding='utf-8') as data:
        data.write(replaced)

def change_records(file_name: str):#Изменяет данные
    record_id = check_id_record(file_name, 'изменить')
    if record_id != 'q':
        replaced_line = f'{int(record_id)};' + ';'.join(
            input('Введите ФИО, № телефона\n').split()[:4]) + '\n'
        confirm = confirmation('изменение')
        if confirm == 'y':
            replace_record_line(file_name, record_id, replaced_line)

def delete_records(file_name: str):#Удаляет данные
    record_id = check_id_record(file_name, 'удалить')
    replace_record_line(file_name, record_id, '')

path = 'book.txt'

try:                       
    file = open(path, 'r') 
except IOError:             
    print('Создан новый справочник -> book.txt ')
    file = open(path, 'w')
finally:                    
    file.close()

actions = {'1': 'список', '2':'запись', '3':'поиск', '4':'изменение', '5': 'удаление', 'q': 'выход'}

action = None
while action != 'q':
    print('Какое действие хотите совершить?', *[f'{i} - {actions[i]}' for i in actions])
    action = input()
    if action not in actions:
            print('Введены неверные данные')
    if action != 'q':
        if action == '1':
            show_data(path)
        elif action == '2':
            new_data(path)
        elif action == '3':
            find_records(path, *find_char())
        elif action == '4':
            change_records(path)
        elif action == '5':
            delete_records(path)