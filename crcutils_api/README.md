# Currency API URL Builder (crcutils)

This project provides a simple Python utility class to generate URLs for the [Frankfurter Currency API](https://frankfurter.dev/). It is designed to separate the URL construction logic from the actual HTTP requests, making it easy to use in both synchronous and asynchronous environments.

## Project Structure

* `main.py`: The core class that builds the API endpoints.
* `test.py`: Example script showing how to fetch data using `requests` and `httpx`.

## Installation

1. Activate venv
2. Install package

When is package stored locally
```bash
pip install -e C:\example\subfolder\
```

To install the basic requirements for the class:
```bash
pip install "git+https://github.com/bag1s3k/devutils.git#subdirectory=crcutils_api"
```

To only clone this project branch use: 
```bash
git clone -b crcutils_api --single-branch https://github.com/bag1s3k/devutils.git@crcutils_api
```

## Usage
* `import crcutils` or `from crcutils import CurrencyAPI`