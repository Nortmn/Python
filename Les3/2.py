def my_func(surname, name, year, city, email, telephone):
    return ' '.join([surname, name, year, city, email, telephone])


print(my_func(surname='Иванов', name='Иван', year='1998', city='Москва', email='ivanov@gmail.com',
              telephone='8-999-000-99-99'))
