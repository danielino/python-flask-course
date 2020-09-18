---
title: Corso Flask
theme: sky
revealOptions:
    transition: 'fade'
---

# Corso Flask

* Introduzione
* Prima applicazione flask
* Metodi HTTP
* Estensioni
* Database SQL ORM

---

## Introduzione a Flask

Flask è un micro-framework per python

* Facile da utilizzare
* Facile da configurare
* RESTful
* Testabile

---

### Flask Hello-World

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

app.run()
```

---

### Metodi HTTP

```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    pass

@app.route("/", methods=["POST"])
def post():
    # curl -X POST -d "username=test" http://localhost:5000/
    data = request.data 
    print(data['username'])

app.run()
```

---

### Templates

Flask dispone di un linguaggio di templating che permette di avere dei file statici con dei placeholder per i dati dinamici.

- elaborazione del template
- sostituzione dei placeholder
- render della pagina html completa

----

#### Backend

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
```

----

#### Template

definiamo il layout di base

```jinja2
# base.html
<\!doctype html>
<title>{% block title %}{% endblock %} - Flaskr</title>
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<nav>
    <h1>Flaskr</h1>
    <ul>
        {% if g.user %}
        <li><span>{{ g.user['username'] }}</span>
        <li><a href="{{ url_for('auth.logout') }}">Log Out</a>
        {% else %}
        <li><a href="{{ url_for('auth.register') }}">Register</a>
        <li><a href="{{ url_for('auth.login') }}">Log In</a>
        {% endif %}
    </ul>
</nav>
<section class="content">
    <header>
        {% block header %}{% endblock %}
    </header>
    {% for message in get_flashed_messages() %}
        <div class="flash">{{ message }}</div>
    {% endfor %}
    {% block content %}{% endblock %}
</section>
```

----

estendiamo il layout di base per la pagina `index.html` route("/")

```jinja2
# index.html
{% extends 'base.html' %}
{% block content %}
    <h3> My Index Page </h3>
{% endblock %}
```

---

### Estensioni

* Flask-Admin
* Flask-Cache
* Flask-OpenID
* Flask-Mail
* Flask-SQLAlchemy
* Flask-MongoAlchemy
* Flask-WTF
* Flask-Uploads


---

### Database SQL ORM

```bash
$ pip install flask-sqlalchemy
```

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app  = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/mydb.sqlite'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

def main():
    # provvede a creare il database se non esiste
    db.create_all()

    u = User(username="test", password="secret", email="test@exampple.com")
    try:
        db.session.add(u)
        db.session.commit()
    except:
        db.session.rollback()
    
main()

----

```python
u = User(username="test", password="secret", email="test@exampple.com")

# insert
db.session.add(u)
db.session.commit()

# query
User.query.all()
User.query.filter_by(username="test").first()

# delete
db.session.delete(u)
db.session.commit()

#  update
u.password = 'test'
db.session.commit()
```




```