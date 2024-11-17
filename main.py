login = input('Введите логин: ')
password_1 = input('Введите пароль: ')
password_2 = input('Пожалуйста, подтвердите ваш пароль: ')
if password_1 == password_2:
    print('Вы были успешно зарегистрированы в системе!')
else:
    print('Ваш пароль не совпадает')