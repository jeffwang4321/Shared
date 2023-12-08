from flask import Flask, request, jsonify
import pymssql

app = Flask(__name__)

# Replace the connection details with your actual database connection
db_connection = pymssql.connect(
    server="your_server",
    user="your_user",
    password="your_password",
    database="your_database",
)
cursor = db_connection.cursor()


@app.route("/api/query", methods=["GET"])
def execute_query():
    try:
        # Get query parameters from the URL
        columns = request.args.getlist("column")
        values = request.args.getlist("value")

        if len(columns) != len(values):
            return jsonify({"error": "Mismatched number of columns and values"})

        # Construct the WHERE clause for the SQL statement
        where_clause = " AND ".join(
            [f"{col} = '{val}'" for col, val in zip(columns, values)]
        )

        # Use the constructed WHERE clause in the SQL statement
        sql_query = f"SELECT * FROM YourTable WHERE {where_clause}"

        # Execute the SQL query
        cursor.execute(sql_query)

        # Fetch the results
        result = cursor.fetchall()

        # You may want to process the result and convert it to a JSON format
        # For simplicity, we'll just return the result as is
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
