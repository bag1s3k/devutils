# Frankfurter API URL Builder

This project provides a simple Python utility class to generate URLs for the [Frankfurter Currency API](https://frankfurter.dev/). It is designed to separate the URL construction logic from the actual HTTP requests, making it easy to use in both synchronous and asynchronous environments.

## Project Structure

* `main.py`: The core class that builds the API endpoints.
* `test.py`: Example script showing how to fetch data using `requests` and `httpx`.
* `requirements.txt`: Necessary packages for the main class.
* `requirements-dev.txt`: Packages required for testing and async support.

## Installation

To install the basic requirements for the class:
```bash
pip install -r requirements.txt
```

To only clone this project branch use: 
```bash
git clone -b frankfurter_api --single-branch https://github.com/bag1s3k/devutils.git
```

To only download specific file in **Windows powershell**
```bash
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/bag1s3k/devutils/main/frankfurter_api/main.py" -OutFile "main.py"
```