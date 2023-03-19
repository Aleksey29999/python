from os import path

file_base = "base.txt"
# file_base = "homework/homework8/base.txt"
last_id = 0
all_data = []
index_id =0
index_surname=1
index_name = 2
index_patronymic=3
index_phone_number=4
count=0
if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

# Запись списка в файл 
def record_base(): 
    global all_data 
    with open(file_base, 'w', encoding="utf-8") as f:
        for all_data in all_data:
            f.write(all_data + '\n')

# запись файла в список
def read_records():
    global last_id, all_data
    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []

# просмотреть все
def show_all():
    if all_data:
        print(" ")
        print(*all_data, sep="\n")
        print(" ")
    else:
        print("Empty data")

# Добавить новый контакт
def add_new_contact():
    global last_id
    array = ["surname", "name", "patronymic", "phone_number"]
    string = ""
    for i in array:
        string += input(f"Enter {i} ") + " "
    last_id += 1

    with open(file_base, "a", encoding="utf-8") as f:
        f.write(f"{last_id} {string}\n")

# Импорт экспорт файлов менюшка 
def Exp_Imp():
    download = True
    while download:
        read_records()
        answer_files = input("Import/Exort files:\n"
                       "1. Import files\n"
                       "2. Export files\n"
                       "3. Exit\n")
        match answer_files:
            case "1":
                import_files()
            case "2":
                export_files()
            case "3":
                download = False
            case _:
                print("Try again!\n")

# экспорт файлов 
def export_files():
    global all_data
    base2 = input('введите имя файла: ')
    export_base=f"{base2}.txt"
    with open(export_base, 'w', encoding="utf-8") as f:
        for all_data in all_data:
            f.write(all_data + '\n')
    print("Файл экспортирован успешно \n")

# импорт файлов
def import_files():
    global all_data, file_base
    base2 = input('введите имя файла:.txt ',)
    import_base=open(base2,'r', encoding="utf-8")
    base = open(file_base,'w', encoding="utf-8")
    base.write(import_base.read()) 
    read_records()
    print("Файл импортирован успешно \n")

# удаление файлов по фамилии или именени
def Delete():
    global all_data , index_id, index_surname, contact, file_base, count
    Search_a_record()
    if count==1:
        input_id = input('введите номер id удаляемого контакта: ',)
        d=[]
        
        for i in range(len(all_data)):
            d=all_data[i].split(sep=' ')    
            if d[index_id]== input_id and (contact==d[index_surname] or contact==d[index_name]):
                all_data.pop(i)
                count= 0
                break       
        if count== 0:        
            print("\n Изменения контакта выполнены успешно \n")
            show_all()
            record_base()
            return all_data
        else:
            print("\n Нет такого Id \n")
            return 0    
    else:
        
        return 0

    # global all_data, last_id
    # element=[]
    # count=0
    # delit_people = str(input('введите Имя или Фамилию человека: ',))
    # for i in range(len(all_data)):
    #     element= all_data[i]
    #     for j in range(len(element)):
    #         if delit_people == element[j]:
    #             all_data.pop(i)
    #             count=1
    # show_all()
    # if count ==1:
    #     print("Удаление контакта " + delit_people + " прошло успешно \n")
    # else:
    #     print("Удаление контакта " + delit_people + " не выполнено  \n")
    #     return 0    
    # record_base()
    
# Внесение изменений- меню
def Change_menu():
    play = True
    while play:
        read_records()
        answer = input("Change:\n"
                       "1. Change surname\n"
                       "2. Change name\n"
                       "3. Change patronymic\n"
                       "4. Change phone number\n"
                       "5. Exit\n")
        match answer:
            case "1":
                Change_surname()
            case "2":
                Change_name()
            case "3":
                Change_patronymic()
            case "4":
                Change_phone_number()
            case "5":
                play = False
            case _:
                print("Try again!\n")

# поиск контакта
def Search_a_record():
    global all_data, last_id, contact, count  
    contact = input('введите контакт для поиска: ',)
    count=0
    for i in range(len(all_data)):
        for j in all_data[i].split(sep=' '):
            if contact == j:
                count = 1
                print(all_data[i])
    if count== 1:
        print('++++++++')
    else:
        print("Такого контакта не существует")
        count=0
        return 0   
    return all_data, count

# Изменение контакта
def Change(index):
    global all_data , index_id, index_surname, contact, file_base
    Search_a_record()
    if count==1:
        input_id = input('введите номер id изменяемого контакта: ',)
        new_contact = input('введите новое значение контакта: ',)
        all_data1 = []
        d=[]
        for i in range(len(all_data)):
            if all_data[i].split()[index_id]== input_id:
                d=all_data[i].split(sep=' ')
                for j in range(len(d)):
                    if index==j:
                        print(all_data[i].split(sep=' ')[j])
                        print() 
                        all_data1.append(new_contact)
                    else:
                        all_data1.append(d[j])
                all_data[i]=" ".join(map(str,all_data1))
             
        print("\n Изменения фамилии внесены успешно \n")
        show_all()
        record_base()
    else:
        return 0

# Изменение Фамилии
def Change_surname():
    global all_data , index_id, index_surname, contact, file_base, count
    index= index_surname
    Change(index)

# Изменение Имени
def Change_name():
    global all_data , index_id, index_name, contact, file_base, count
    index= index_name
    Change(index)

# Изменение номера отчества
def Change_patronymic():
    global all_data , index_id, index_patronymic, contact, file_base, count
    index = index_patronymic
    Change(index)  

# Изменение номера телефона
def Change_phone_number():
    global all_data , index_id, index_phone_number, contact, file_base, count
    index= index_phone_number
    Change(index)       

# менюшка
def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                Search_a_record()
            case "4":
                Change_menu()
            case "5":
                Delete()
            case "6":
                Exp_Imp()    
            case "7":
                play = False
            case _:
                print("Try again!\n")


main_menu()
