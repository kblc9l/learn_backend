from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
