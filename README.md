# Ebanx Take Home Test

Ebanx Take Home Test is a API implementation test developed in Python, with Clean Architecture Standard in mind.

It separates several layers for easing diferent changes without affecting the bigger part of the code.

It uses a simple SQLite database for the accounts managing.

## Installation

Use Python [virtualenv](https://virtualenv.pypa.io/en/latest/) to create one:

```bash
virtualenv -p python3 venv
```
Enter the virtual environment:
```bash
. venv/Scripts/activate
```
Install the requirements using [pip](https://pypi.org/project/pip/):
```bash
pip install -r requirements.txt
```
Install pre-commit dependencies:
```bash
pre-commit install
```
## Usage

Using [Flask](https://flask.palletsprojects.com/en/2.0.x/):

```bash
export FLASK_APP=run
flask run
```

The public URL for external testing was created using [ngrok](https://ngrok.com/). After following its installation process:
```bash
./ngrok http 5000
```
