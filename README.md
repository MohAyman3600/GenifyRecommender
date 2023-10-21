# Genify Flask API Integration

Flask API for integrating with a Machine Learning Model and serves it to the User Interface

## Description

This is a Flask API that serves a machine-learning model. It uses MongoDB as a database, marshmallow for schema validation, Flask-RESTful for serialization, Flask-Testing for testing, token authentication, Swaggger for documentation, logging module for logging.

## Installation

1. Clone the repository
2. Install the required packages using `pip install -r requirements.txt`
3. Start the application using `flask run`

## Usage

The API has the following endpoints:

- `/api/users`: allows you to create, edit, get, list users.
- `/api/predictions`: allows you to make predictions using the machine learning model

To access the endpoints, you need to authenticate using a token. You can get a token by sending a POST request to `/api/token` with your credentials.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
