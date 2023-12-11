from flask import Flask, jsonify
import os
import requests
import concurrent.futures

app = Flask(__name__)


def check_endpoint(check_name, endpoint_url):
    """
    Performs a simple health check by making a GET request to the specified endpoint.

    Args:
        check_name (str): Name of the health check.
        endpoint_url (str): URL of the endpoint to be checked.

    Returns:
        bool: True if the health check is successful, False otherwise.
    """
    try:
        response = requests.get(endpoint_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return True
    except requests.RequestException:
        # Log the error or handle it as needed
        app.logger.error(f"Health check failed for {check_name} at {endpoint_url}")
        return False


@app.route("/")
def index():
    return jsonify({"status": "up"}), 200


@app.route("/healthz")
@app.route("/health")
def healthz():
    healthz = {}
    executor_result = {}

    # Validate that my really cool server I rely on for my backend to work is functional
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        executor_result["reallyCoolServer"] = executor.submit(
            check_endpoint,
            "reallyCoolServer",
            os.environ.get("really_cool_server", "http://really-cool-server:8181"),
        )

    # Get results from executor
    for check_name, future in executor_result.items():
        healthz[check_name] = future.result()

    if all(value for _, value in healthz.items()):
        return jsonify(healthz), 200
    else:
        app.logger.error(
            f"WARNING - health endpoint error when attempting to execute health check {healthz}"
        )
        return jsonify(healthz), 500


if __name__ == "__main__":
    app.run(debug=True)
