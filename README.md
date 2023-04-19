# CO2 Emissions FastAPI Project

This project is a FastAPI-based RESTful API that provides data on countries' CO2 emissions, yearly changes, per capita emissions, and life expectancy.

## Overview

The project consists of the following main components:

- FastAPI: A modern Python web framework for building APIs.
- pandas: A data manipulation and analysis library used to process the CSV data.

The API provides the following endpoints:

- `/`: A simple "Hello, World" endpoint.
- `/top10`: Returns the top 10 countries with the highest per capita CO2 emissions.
- `/emissions`: Accepts a list of country codes and returns the CO2 emissions and yearly change for each country.
- `/top10-life-expectancy`: Returns the top 10 countries with the highest life expectancy.
- `/total-emissions`: Accepts a list of country codes and returns the total CO2 emissions for the specified countries.

## How to Run

1. Install the required packages:

```bash
pip install fastapi uvicorn pandas
```

## Run the FastAPI application:


```
uvicorn main:app --reload
```

Visit the default FastAPI documentation at http://127.0.0.1:8000/docs to interact with the API.

## How to Test


Install the required testing packages:

```bash
pip install fastapi[testing] pytest
```

Run the tests using pytest:

```bash
pytest
```

pytest will discover and run the test functions in the main_test.py file.