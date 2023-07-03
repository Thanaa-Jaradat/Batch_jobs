from flask import Flask, request, jsonify, redirect
from sqlalchemy import create_engine, Column, Integer, DateTime, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
# Create an engine that connects to the SQLite database specified by the URL
engine = create_engine("sqlite:///database.db")
# Create a session factory using the engine to bind sessions to the database
Session = sessionmaker(bind=engine)
#Create a new session object
session = Session()
# Create a base class for declarative models to inherit from
Base = declarative_base()

# Define a class named Batch that inherits from Base
class Batch(Base):
    __tablename__ = 'batch'
    batch_number = Column(Integer, primary_key=True, unique=True)
    submitted_at = Column(DateTime)
    nodes_used = Column(Integer)

#Create all the tables defined in the declarative base
Base.metadata.create_all(engine)
#Establish a connection to the database using the engine
connection = engine.connect()

#Define a route handler for the root URL ("/")
#The handler function returns a redirect response to the specified URL
@app.route('/')
def redirect_main_page():
    return redirect("http://localhost:5000/batch_jobs", code=302)

#Define a route handler for the URL ("/batch_jobs")
#The handler function returns json response according to attched query parameters in the URL
@app.route('/batch_jobs', methods = ['GET'])
def filter():
    # extract query parameters from the request if they exist
    min_nds = request.args.get('min_nodes')
    max_nds = request.args.get('max_nodes')
    submitted_before = request.args.get('submitted_before')
    submitted_after = request.args.get('submitted_after')
    request_link = request.url
    # Check each query parameter value (if exists) and modifying the query text accordingly.
    if min_nds is None and max_nds is None and submitted_before is None and submitted_after is None:
        return "No params were selected"
    query_text = "SELECT * FROM batch WHERE"
    # Dictionary that holds the values of the query parameters to be passed to the SQL query text
    params_dict = dict()
    if min_nds is not None:
        query_text += " nodes_used >= :min_nodes"
        params_dict['min_nodes'] = int(min_nds)
    if max_nds is not None:
        if not query_text == "SELECT * FROM batch WHERE":
            query_text += " AND"
        query_text += " nodes_used <= :max_nodes"
        params_dict['max_nodes'] = int(max_nds)
    if submitted_after is not None:
        if not query_text == "SELECT * FROM batch WHERE":
            query_text += " AND"
        query_text += " submitted_at >= :submitted_after"
        params_dict['submitted_after'] = submitted_after
    if submitted_before is not None:
        if not query_text == "SELECT * FROM batch WHERE":
            query_text += " AND"
        query_text += " submitted_at <= :submitted_before"
        params_dict['submitted_before'] = submitted_before
    query = text(query_text)
    #Querying the database and fetching the result records
    results = connection.execute(query, params_dict).fetchall()
    batch_data = []
    for i, batch in enumerate(results):
        record = {'batch_number': batch.batch_number, 'submitted_at': batch.submitted_at, 'nodes_used': batch.nodes_used}
        item = {"type": "batch_jobs", "id": str(i + 1), "attributes": record}
        batch_data.append(item)
    result_dict = {"links": {"self": request_link}, "data": batch_data}
    return jsonify(result_dict)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
