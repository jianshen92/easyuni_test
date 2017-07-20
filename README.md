# Training Calender Editor

This project is built as part of EasyUni's django dev job application. Project is developed with Python 3.6 and Django 1.11.

## Getting Started

Clone the repository to your local workstation.

### Installing

Create a new virtual environment and activate it.

Install dependencies:
```
pip install -r requirements.txt
```

Run development server:
```
python manage.py runserver
```

## Database
SQLite was used as the project was never meant for production.

## Omitted Optimization
As this is a MVP, many aspects were omitted:
* UI/UX. No custom CSS files were included. Only basic bootstrap components.
* Class Based View for better code refactoring.
* A separate Model class for `Trainer`
* Dynamic Calender Month and Year
* Unique PDF for each Training Date/Location. I assumed the same pdf will be used for the same program.
* QuerySet optimization.

