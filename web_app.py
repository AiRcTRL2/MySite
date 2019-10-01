from flask import Flask, render_template, jsonify, send_from_directory
from MySite.py_modules.search import *
app = Flask(__name__)

# add favicon for website
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/search/<search_term>')
def search(search_term):
    print(search_term)
    search_db = find(search_term)

    if len(search_db) == 0:
        build(search_term)
    else:
        return jsonify(search_db)




if __name__ == "__main__":
    app.run(host='127.0.0.1',debug=True)