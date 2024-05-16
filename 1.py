
price = input("Введите цену товара:") #цена товара
weight = input("Введите вес товара:") #вес товар
submitted = input("Сумма средств клиента:") #количество денег
change = float(submitted) - (float(price) * float(weight)) #сдача
print("Чек")
print('Цена товара:',price,"Р.За КГ.")
print('Вес товара:',weight,"КГ.")
print("Сумма покупки:",(float(price) * float(weight)),"Р.")
print("Внесёная Сумма:",submitted,"Р.")
print("Сдача:",change,"Р.")

