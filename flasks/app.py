from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from builtins import enumerate

app = Flask(__name__)

# Função para criar a tabela de eventos no banco de dados
def create_table():
    conn = sqlite3.connect('agenda.db')  # Conecta ao banco de dados ou cria um novo
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event TEXT,
            date TEXT,
            time TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_table()  # Chama a função para criar a tabela

@app.route("/")
def home():
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM events')
    agenda = cursor.fetchall()
    conn.close()
    return render_template("index.html", agenda=agenda, enumerate = enumerate)

@app.route("/add", methods=["POST"])
def add_event():
    event = request.form.get("event")
    date = request.form.get("date")
    time = request.form.get("time")

    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO events (event, date, time) VALUES (?, ?, ?)', (event, date, time))
    conn.commit()
    conn.close()

    return redirect(url_for("home"))

@app.route("/remove/<int:event_id>")
def remove_event(event_id):
    try:
        conn = sqlite3.connect('agenda.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM events WHERE id = ?', (event_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao remover evento: {e}")
    finally:
        conn.close()

    return redirect(url_for("home"))

@app.route("/mostrar/<int:event_id>")
def show_event(event_id):
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM events WHERE id = ?', (event_id,))
    event = cursor.fetchone()
    conn.close()

    if event is not None:
        return render_template("index.html", event=event)
    else:
        return "Evento não encontrado."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')