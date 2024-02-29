import json
import random

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/list_prof/<typeL>')
def list_prof(typeL: str):
    profs = ''' менеджер по продажам,
                продавец-консультант,
                водитель,
                бухгалтер,
                программист, разработчик программного обеспечения,
                врач,
                инженер,
                повар,
                упаковщик и комплектовщик,
                слесарь,
                сантехник'''.strip().split(',')
    return render_template('prof_list.html', title='Список профессий для полёта на Марс', profs=profs, typeL=typeL, )


# @app.route('/')
# def practice():
#     return render_template('my_first_template.html')


@app.route('/distribution')
def distribution():
    l = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бил']
    return render_template('distribution.html', title='По каютам!', l=l)


@app.route('/table')
def table():
    color = '#afaafa'
    age = 22
    return render_template('table.html', title='Цвет каюты', color=color, age=age)


urls = ['static/image/mars1.jpg',
        'static/image/mars2.jpg',
        'static/image/mars3.jpg']


@app.route('/galery', methods=['GET', 'POST'])
def galery():
    if request.method == 'POST':
        f = request.files['file']
        with open(f'static/image/mars{len(urls) - 3}.png', 'wb') as img_file:
            img_file.write(f.read())
        urls.append(f'static/image/mars{len(urls) - 3}.png')

    return render_template('galery.html', title='Галерея с добавлением', urls=urls)


with open('templates/crew.json', 'r') as file:
    crew_data = json.load(file)
    crew_members = crew_data['crew_members']


@app.route('/member')
def random_crew_member():
    random_member = random.choice(crew_members)
    return render_template('profile.html', random_crew_member=random_member)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
