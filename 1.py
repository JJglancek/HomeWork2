name = input("Введите цену товара:") #цена товара
name1 = input("Введите вес товара:") #вес товар
name2 = input("Сумма средств клиента:") #количество денег
name3 = float(name2) - (float(name) * float(name1)) #сдача
print("Чек")
print('Цена товара:',name,"Р.За КГ.")
print('Вес товара:',name1,"КГ.")
print("Сумма покупки:",(float(name) * float(name1)),"Р.")
print("Внесёная Сумма:",name2,"Р.")
print("Сдача:",name3,"Р.")

