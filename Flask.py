import concurrent.futures
import os
from flask import Flask, jsonify
import logging

logging.basicConfig(format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
# logging.warning("is when this event was logged.")
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/")
def index() -> tuple:
    return (jsonify({"status": "up"}), 200)


@app.route("/healthz")
@app.route("/health")
def healthz() -> tuple:
    """
    healthz checkattempts to query and returns a dictionary of each health domain and its result

    Returns:
        result (dict): Flask HTTP Result of Healthcheck in the following format:
        {
            checkName (str): True/False (the result of the check)
        }
    """
    # Import check_endpoint function here

    # Define logger here

    healthz = {}
    executor_result = {}
    # Validate that my really cool server I rely on for my backend to work is functional
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        executor_result["reallyCoolServer"] = executor.submit(
            check_endpoint(),
            "reallyCoolServer",
            os.environ.get("really_cool_server", "http://really-cool-server:8181"),
        )
    if all(value for _, value in healthz.items()):
        return (jsonify(healthz), 200)
    else:
        logger.error(
            f"WARNING - health endpoint error when attempting to execute health check {healthz}"
        )
        return (jsonify(healthz), 500)


def check_endpoint():
    pass
