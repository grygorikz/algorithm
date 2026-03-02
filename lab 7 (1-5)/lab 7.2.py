count = 10
def change_value():
    global count   
    count = 20
print("do funkcii:", count)
change_value()
print("posle funkcii:", count)

#Глобальная переменная создаётся вне функции, она видна во всей программе и её можно изменить внутри функции с поомщью global.
#локальная переменная создаётся внутри функции и существует внутри неё.