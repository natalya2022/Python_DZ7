import Model
import Logger

bookfile = 'PhoneBook.txt'
main_book = Model.import_book(bookfile)
Logger.log_line(f'Запуск программы. Импортировано {len(main_book)} записей')
    
    
def book_append():
    Model.append_record(main_book, input('Введите ФИО => '), input('Введите номер телефона => '))
    Logger.log_line(f'Добавлена запись: {main_book[-1]}')

def book_search():
    search = Model.find_record(main_book, input('Введите значение для поиска => '))
    if len(search):
        print(search)
    else:
        print('Запись не найдена')
    Logger.log_line(f'Поиск. Найдено: {len(search)} записей')

def book_exit():
    Model.export_book(main_book, bookfile)
    Logger.log_line(f'Выход. Экспортировано {len(main_book)} записей\n')
    exit()
  
   
list_of_functions = [
    [book_exit,'Выход'],
    [book_append,'Добавление записи'],
    [book_search,'Поиск записи']
]
for num,item in enumerate(list_of_functions):
    print (num,item[1])
while True:
    a = int(input('Выберите вариант => '))
    if 0 <= a < len(list_of_functions):
        list_of_functions[a][0]()