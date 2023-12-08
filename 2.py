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


def validate_operator(operator):
    valid_operators = ("=", ">", "<", ">=", "<=")
    return operator in valid_operators


def validate_data_type(value, data_type):
    try:
        if data_type == "int":
            int(value)
        elif data_type == "str":
            str(value)
        else:
            return False
        return True
    except ValueError:
        return False


@app.route("/api/query", methods=["GET"])
def execute_query():
    try:
        # Get query parameters from the URL
        columns = request.args.getlist("column")
        values = request.args.getlist("value")
        operators = request.args.getlist("operator")
        data_types = request.args.getlist("data_type")

        if (
            len(columns) != len(values)
            or len(columns) != len(operators)
            or len(columns) != len(data_types)
        ):
            return jsonify(
                {
                    "error": "Mismatched number of columns, values, operators, and data types"
                }
            )

        # Construct the WHERE clause for the SQL statement
        where_clauses = []

        for col, val, op, data_type in zip(columns, values, operators, data_types):
            if validate_operator(op) and validate_data_type(val, data_type):
                if data_type == "str":
                    where_clauses.append(f"{col} {op} '{val}'")
                else:
                    where_clauses.append(f"{col} {op} {val}")
            else:
                return jsonify({"error": "Invalid operator or data type"})

        where_clause = " AND ".join(where_clauses)

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
