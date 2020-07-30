import csv

# Записываем данные в файл
car_data = [['brand','price','year'],['Volvo',1.5,2007],['Lada',1.2,2010]]
with open('example.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(car_data)
print('Writing complete')