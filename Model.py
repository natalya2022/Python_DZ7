def import_book(filename): # импорт информации из файла txt
    x = open(filename,'r',encoding='utf-8')
    return list(map(lambda x: x.rstrip('\n'), x.readlines()))

def append_record(main_book, name, number): # добавление записи в список
    main_book.append(name+' || '+number)
    
def find_record(main_book, x): # поиск записей в списке
    a = []
    for item in main_book:
        if item.find(x) != -1:
            a.append(item)
    return a

def export_book(main_book, filename):
    with open(filename,'w',encoding='utf-8') as f:
       for item in main_book:
        f.write(item+'\n')