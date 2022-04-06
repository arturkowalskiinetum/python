from database import Database
from os import getenv
from dotenv import load_dotenv
from flask import Flask, request, jsonify
app = Flask(__name__)
load_dotenv()


@app.route('/setup')
def setup_database():
    db_name = getenv('DB_NAME')
    db = Database(db_name)
    db.initialize('CREATE TABLE docs (id INTEGER PRIMARY KEY AUTOINCREMENT, body TEXT)')
    return 'Database Initialized'

@app.route('/health')
def get_health():
    db_name = getenv('DB_NAME')
    db = Database(db_name)
    return db.info


@app.route('/doc', methods=['POST'])
def create():
    req = request.get_json()
    db_name = getenv('DB_NAME')
    db = Database(db_name)
    body = req['body']

    query = 'INSERT INTO docs (body) VALUES (?)'
    db.create(query, body)
    return 'Insertion complete'

@app.route('/doc/<doc_id>', methods=['PUT'])
def create():
    req = request.get_json()
    db_name = getenv('DB_NAME')
    db = Database(db_name)
    id = req['id']
    body = req['body']

    query = 'INSERT INTO docs (id,body) VALUES (?,?)'
    db.create(query, id,body)
    return 'Insertion complete'

@app.route('/doc')
def read():
    db_name = getenv('DB_NAME')
    db = Database(db_name)
    query = 'SELECT * FROM docs'
    docs = db.readall(query)
    return jsonify(docs)

@app.route('/doc/<doc_id>')
def read(doc_id):
    db_name = getenv('DB_NAME')
    db = Database(db_name)
    query = 'SELECT body FROM docs WHERE id=?'
    doc = db.read(query, (doc_id))
    return jsonify(doc)


@app.route('/doc/<doc_id>', methods=['PUT'])
def update(doc_id):
    req = request.get_json()
    db_name = getenv('DB_NAME')
    db = Database(db_name)
    body = req['body']
    query = 'UPDATE docs SET body=? WHERE id=?'
    db.update(query, (body, doc_id))
    return 'Updated successfully'


@app.route('/doc/<doc_id>', methods=['DELETE'])
def delete(doc_id):
    db_name = getenv('DB_NAME')
    db = Database(db_name)
    query = 'DELETE FROM docs WHERE id=?'
    db.delete(query, (body_id,))
    return 'Deleted successfully'
