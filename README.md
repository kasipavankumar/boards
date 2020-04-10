# Discuss Boards

## Responsive discussion forums built with Django.

[![Build Status](https://travis-ci.org/code-plus-coffee/boards.svg?branch=master)](https://travis-ci.org/code-plus-coffee/boards)

Online discussion forums to discuss about programming & technology related topics. You can create an account and get involved with the discussions.

## Usage

In case you want to consume the code or contribute to this repository, you might want to run this locally on your computer. Follow the steps below to do so:

### Requirements

1. [Python 3.7](https://www.python.org/downloads/)
2. [pipenv](https://github.com/pypa/pipenv)

```bash
# Install pipenv
1. pip install pipenv

# Create a directory called boards
2. mkdir boards

# cd to it
3. cd boards

# Clone this repository
3. git clone https://github.com/code-plus-coffee/boards.git

# After cloning, your project structure should be:
# boards        ← Outer directory
#   → boards    ← Root directory of the project

# cd one level back to boards
4. cd ..

# Create an virutal environment
5. virtualenv .

# Activate the virtual environment
6. \scripts\activate

# cd to project's root directory
7. cd boards

# Install the dependencies using requirements.txt
8. pip install -r requirements.txt

# Start the local development server
# Default: localhost:8000 or 127.0.0.1:8000
9. python manage.py runserver
```

## Credits

This project is fully based on the tutorial provided at [SimpleIsBetterThanComplex](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/). I would like to thank [@vitorfs](https://github.com/vitorfs) for comprehensive & informative tutorial.

`Code Plus Coffee • 2020`
