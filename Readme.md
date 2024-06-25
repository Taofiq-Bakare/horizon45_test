# Truck Management Application

## Overview
This project is a Django application for managing drivers and their assigned trucks. 
It includes the necessary models, API endpoints, and tests.

## Requirements

* Python 3.x
* PostgreSQL
* Pipenv

## Setup

Clone the repo

```bash
$ git clone git@github.com:Taofiq-Bakare/horizon45_test.git
$ cd horizon45_test

```

## Create a .env File

Create a `.env` file in the root of your project directory and add the following environment variables:

```bash
DB_NAME=your_db_name
DB_USERNAME=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port

```
If PostgreSQL environment variables are not set, the application will default to using SQLite.

## Install Dependencies

Install the required packages using Pipenv:

```bash
$ pipenv install
```
Run the command below to activate the environment.

```bash
$ pipenv shell
```

## Migrate the Database

Run the following commands to make and apply migrations:

```bash

$ python manage.py makemigrations
$ python manage.py migrate

```

## Running Tests

To run the unit tests for the application, use the following command:

```bash
$ python manage.py test
```


## Run the Server

Start the Django development server:

```bash
$ python manage.py runserver
```

## API Endpoints

List of Drivers

    URL: /domain/driver
    Method: GET
    Description: Returns a list of available drivers.
    Filters: You can filter drivers by email, mobile_number, language, and assigned truck number_plate.

Get Driver by ID

    URL: /domain/driver/<id>
    Method: GET
    Description: Returns a single driver by ID.

Create a Single Driver

    URL: /domain/driver
    Method: POST
    Description: Creates a single driver.
    Request Body:

```json
{
    "email": "Jadfmes144@example.com",
    "name": "James Smith",
    "mobile_number": 12343244567890,
    "city": "Example City",
    "district": "Example District",
    "language": "English",
    "assigned_truck": {
        "number_plate": "XYTdfT 11235",
        "registration_number": "TdfRTEG5668"
    }
}

```

Create Bulk Drivers

    URL: /domain/driver/bulk
    Method: POST
    Description: Creates multiple drivers.
    Request Body:

```json
[
    {
        "email": "Jadfs144@example.com",
        "name": "Ja Smith",
        "mobile_number": 12343244567890,
        "city": "Example City",
        "district": "Example District",
        "language": "English",
        "assigned_truck": {
            "number_plate": "XYTdfT 112035",
            "registration_number": "TdfRTEG56068"
        }
    },
    {
        "email": "driverdf1454@example.com",
        "name": "Peter A Smith",
        "mobile_number": 12343244567890,
        "city": "Example City",
        "district": "Example District",
        "language": "English",
        "assigned_truck": {
            "number_plate": "XXdfYT 11235",
            "registration_number": "TRRdfEG5668"
        }
    }
]

```
