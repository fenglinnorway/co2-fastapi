from typing import List, Tuple, Dict, Union
from fastapi import FastAPI
from app.data.co2emissions import ReadFile
import pandas as pd

app = FastAPI()

DATA_URL = "https://raw.githubusercontent.com/GreenfactAS/co2-dataset/main/CO2-emissions.csv"


def get_data() -> pd.DataFrame:
    return ReadFile.read_csv_from_url(DATA_URL)


@app.get("/")
def read_root() -> Dict[str, str]:
    return {"Hello": "World"}


def get_top_n_sorted_by_column(n: int, column: str) -> List[Tuple[str, float]]:
    df = get_data()
    sorted_data = df.sort_values(by=column, ascending=False)
    top_n = sorted_data.head(n)
    return list(zip(top_n['Country'], top_n[column]))


@app.get("/top10")
def top_10_highest_per_capita_emissions() -> List[Tuple[str, float]]:
    return get_top_n_sorted_by_column(10, 'Percapita')


@app.post("/emissions")
def emissions_and_change_by_country_codes(country_codes: List[str]) -> List[Dict[str, Union[str, float]]]:
    df = get_data()
    filtered_data = df[df['Code'].isin(country_codes)]
    return filtered_data[['Country', 'Code', 'CO2Emissions', 'YearlyChange']].to_dict('records')


@app.get("/top10-life-expectancy")
def top10_life_expectancy() -> List[Tuple[str, float]]:
    return get_top_n_sorted_by_column(10, 'LifeExpectancy')


@app.post("/total-emissions")
def total_emissions_by_country_codes(country_codes: List[str]) -> float:
    df = get_data()
    filtered_data = df[df['Code'].isin(country_codes)]
    return filtered_data['CO2Emissions'].sum()
