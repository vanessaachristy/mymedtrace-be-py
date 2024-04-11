# Flask Server Setup Guide

This is a guide on setting up the MyMedtrace Flask Server. Flask is a lightweight web application framework that allows you to quickly build web applications.

## Prerequisites

- [Python 3](https://www.python.org/downloads/) installed
- [Pip](https://pip.pypa.io/en/stable/installation/) (usually comes with Python installation)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (optional but recommended for managing dependencies in a virtual environment)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/vanessaachristy/mymedtrace-be-py.git
    cd mymedtrace-be-py
    ```

2. **Create a virtual environment (optional but recommended)**:

    Creating a virtual environment helps manage dependencies in isolation.

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:

    Once you have activated your virtual environment (if using), install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Flask Server

1. **Set the Flask application**:

    Export the name of the Python file containing the Flask app as an environment variable:

    ```bash
    export FLASK_APP=app.py
    ```

    Replace `app.py` with the filename that contains your Flask app.

2. **Run the Flask development server**:

    Start the Flask server with the following command. This will start the server on the default port 3002. You can specify a different port using the `--port` option:

    ```bash
    flask run --port=3002
    ```

3. **Access the server**:

    Open a web browser and navigate to the server's URL, e.g., `http://127.0.0.1:3002/` if you specified a different port.

## Project Structure

Here's a typical structure for a Flask project:

- `app.py`: The main Python file containing the Flask application.
- `requirements.txt`: A list of dependencies required for the project.
- `templates/`: Directory containing HTML templates for the web application.
- `static/`: Directory containing static files such as CSS, JavaScript, and images.

## Additional Information

- **Debug mode**: You can run Flask in debug mode using the following command:

    ```bash
    flask run --debug
    ```

    This enables useful debugging features such as auto-reloading the server when changes are made and displaying detailed error messages in the browser.

- **Virtual environment**: When you're done with the project, deactivate the virtual environment (if used):

    ```bash
    deactivate
    ```

## Conclusion

That's it! You've successfully set up and run a Python Flask server. Now you can start building and experimenting with your web application. Adjust the repository URL and other details as needed for your specific project.

--- 

Adjust the project details as per your setup and share this README with your team or contributors for a smooth onboarding experience.
