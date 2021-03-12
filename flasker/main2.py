from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Y"


@app.route('/choice/<planet_name>')
def bootstrap(planet_name):
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" 
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Колонизация</title>
                          </head>
                          <body>
                            <h1>Мое предложение: {planet_name}</h1>
                            <h2>Эта планета близка к Земле;</h2>
                            <div class="alert alert-primary" role="alert">
                                Человечество вырастает из детства.
                            </div>
                            <div class="alert alert-success" role="alert">
                                Человечеству мала одна планета.
                            </div>
                            <div class="alert alert-info" role="alert">
                                Мы сделаем обитаемыми безжизненные пока планеты.
                            </div>
                            <div class="alert alert-warning" role="alert">
                                И начнем с {planet_name}
                            </div>
                            <div class="alert alert-danger" role="alert">
                                Присоединяйся!
                            </div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.1.1')