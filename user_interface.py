from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import function as func
 
root = Tk()
list_of_data = []

def save():
    '''
    обрабатывается нажатие кнопки "Сохранить"
    '''
    list_of_data.append(entry_f.get()) # Фамилия
    list_of_data.append(entry_n.get()) # Имя
    list_of_data.append(entry_o.get()) # Отчество
    list_of_data.append(entry_tel.get()) # Телефон
    list_of_data.append(entry_about.get()) # Описание
    func.imp(list_of_data)
    entry_f.delete(0, END)
    entry_n.delete(0, END)
    entry_o.delete(0, END)
    entry_tel.delete(0, END)
    entry_about.delete(0, END)
    
def show():
    '''
    обрабатывается нажатие кнопки "Показать базу". В переменной текст должен быть список списков
    '''
    result = func.exp(entry_search.get())
    root = Tk()
    root.title('Телефонный справочник')
    title.configure(font = ('arial', 10, 'bold')) 
    title.grid(row = 0, column = 0, columnspan = 4)
    root.geometry("250x200")
    
    
    data_var = StringVar(value=result)
    listbox = Listbox(listvariable=data_var)
    listbox.pack(side=LEFT, fill=BOTH, expand=1)
    
    scrollbar = ttk.Scrollbar(orient="vertical", command=listbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    listbox["yscrollcommand"]=scrollbar.set
    
    root.mainloop()        
    return

def find():
    '''
    обрабатывается нажатие кнопки "Найти"
    '''
    # переменная для поиска 
    # entry_search.get()
    text, result = func.exp(entry_search.get())
    if result != "Данные отсутсвуют":
        # print(text,result)
        entry_f.insert(0, result[0])
        entry_n.insert(0, result[1])
        entry_o.insert(0, result[2])
        entry_tel.insert(0, result[3])
        entry_about.insert(0, result[4])
    else:
        messagebox.showinfo('Такой строки нет')
        
    # title = Label(root, text = 'Телефонный справочник')
    
# Нужно разобраться с функцией exp() она должна возвращать список списков или словарей
    
 
    
def selected(event):
    '''
    Функция получает выделенный объект из Combobox (выпадающего списка файловых расширений)
    '''
    global file_exp
    file_exp = drop_down.get()

root.title('Телефонный справочник')

title = Label(root, text = 'Телефонный справочник')
title.configure(font = ('arial', 10, 'bold')) 
title.grid(row = 0, column = 0, columnspan = 4)

hint = Label(root, text = 'Фамилия:')
hint.grid(row = 1, column = 0, ipadx=10, pady =10) 
entry_f = Entry(root)
entry_f.grid(row = 1, column = 1,columnspan = 1, ipadx=40, pady =10)

hint = Label(root, text = 'Имя:')
hint.grid(row = 2, column = 0, ipadx=0, pady =10)
entry_n = Entry(root)
entry_n.grid(row = 2, column = 1, columnspan = 1, ipadx=40, padx=10, pady =10)

hint = Label(root, text = 'Отчество:')
hint.grid(row = 3, column = 0, ipadx=10, pady =5)
entry_o = Entry(root)
entry_o.grid(row = 3, column = 1, columnspan = 1, ipadx=40, pady =5)

hint = Label(root, text = 'Телефон:')
hint.grid(row = 4, column = 0, ipadx=10, pady =10)
entry_tel = Entry(root)
entry_tel.grid(row = 4, column = 1, ipadx=10, pady =10)

hint = Label(root, text = 'Описание:')
hint.grid(row = 5, column = 0, ipadx=10, pady =10)
entry_about = Entry(root)
entry_about.grid(row = 5, column = 1, ipadx=40, pady =10)

but_search = Button(root, text = 'Найти', command = find)
but_search.grid(row = 7, column = 2, columnspan = 1, ipadx=10, pady =10)
entry_search = Entry(root)
entry_search.grid(row = 7, column = 0, columnspan = 2, ipadx=100, padx=10, pady =10, sticky=W)

but_save = Button(root, text = 'Сохранить', command=save)
but_save.grid(row = 8, column = 0, padx = 0, ipadx=10, pady =10)

but_show = Button(root, text = 'Показать базу', command=show)
but_show.grid(row = 8, column = 1, padx = 0, ipadx=10, pady =10)

but_exit = Button(root, text = 'Выход', command=exit)
but_exit.grid(row = 8, column = 2, ipadx=10, padx=10, pady =10)

level_list = ['csv', 'json']
file_exp = StringVar(value=level_list[1])
drop_down = ttk.Combobox(root, textvariable = file_exp, values = level_list, state="readonly")
drop_down.grid(row = 9, column = 1, columnspan=1, padx=10, pady=10)
drop_down.bind("<<ComboboxSelected>>", selected)

root.mainloop()