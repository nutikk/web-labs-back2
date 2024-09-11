from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/web")
def web():
    return """<!doctype html> 
        <html>
           <body> 
               <h1>web-сервер на flask</h1> 
           </body> 
           <a href = "/author">author</a>
        </html>"""

@app.route("/author")
def author(): 
    name = "Петерс Анна Алексеевна"
    group = "ФБИ-21"
    faculty = "ФБ"

    return """<!doctype html>
        <html>
            <body>
                <p>Студент: """ + name + """</p>
                <p>Группа: """ + group + """</p>
                <p>Факультет """ + faculty + """</p>
                <a href = "/web">web</a>
            </body>
        </html>"""
