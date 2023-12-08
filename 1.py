from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Replace the connection details with your actual database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://your_user:your_password@your_server/your_database'
db = SQLAlchemy(app)

class YourTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_code = db.Column(db.String(50))
    job_type = db.Column(db.String(50))
    # Add other columns as needed

# Initialize the database
db.create_all()

@app.route('/api/query', methods=['GET'])
def execute_query():
    try:
        # Get query parameters from the URL
        app_code = request.args.get('app_code')
        job_type = request.args.get('job_type')

        # Construct the SQL query
        query = YourTable.query

        if app_code:
            query = query.filter_by(app_code=app_code)

        if job_type:
            query = query.filter_by(job_type=job_type)

        # Execute the SQL query
        result = query.all()

        # Convert the result to a JSON format
        result_json = [{'id': row.id, 'app_code': row.app_code, 'job_type': row.job_type} for row in result]

        return jsonify(result_json)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
