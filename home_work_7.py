# 1 Вручную создать текстовый файл с данными (например, марка авто, модель авто, расход топлива, стоимость).

with open ('data_home.txt') as f:
    content = f.read()
    print(content)

# 2 Создать doc шаблон, где будут использованы данные параметры.
# 3 Автоматически сгенерировать отчет о машине в формате doc (как в видео 7.2).
import datetime
from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage



def get_context(model, mark, vol, price): # возвращает словарь аргуменов
    return {
        'model': model,
        'mark': mark,
        'vol': vol,
        'price': price,
    }


def from_template(model, mark, vol, price, template):
    template = DocxTemplate(template)
    context = get_context(model, mark, vol, price)  # gets the context used to render the document

    #img_size = Cm(15)  # sets the size of the image
    #acc = InlineImage(template, signature, img_size)

    #context['acc'] = acc  # adds the InlineImage object to the context
    template.render(context)

    template.save(model + '_' + str(datetime.datetime.now().date()) + '_home_work_7.docx')

def generate_report(model, mark, vol, price):
    template = 'home_work_7.docx'
    #signature = 'acc.png'
    document = from_template(model, mark, vol, price, template,)

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

generate_report('M5', 'BMW', '2.4', '1.5');

#4) Создать csv файл с данными.

import csv

car_data = [['brand', 'price', 'year'],['Volvo', 2.5, 2019],['BMW', 1.5, 2016],['Audi', 2.0, 2018]]
with open('data_model_home.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(car_data)
print('Writing complete!')

# 5) Создать json файл с данными.

import json

car_data = [['brand', 'price', 'year'],['Volvo', 2.5, 2019],['BMW', 1.5, 2016],['Audi', 2.0, 2018]]
dict_car_to_json = json.dumps(car_data)
with open('dict_car_to_json', 'w') as f:
    json.dump(car_data, f)