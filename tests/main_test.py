from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_top_10_highest_per_capita_emissions():
    response = client.get("/top10")
    assert response.status_code == 200
    assert len(response.json()) == 10


def test_emissions_and_change_by_country_codes():
    country_codes = ["CAN", "LUX", "EST"]
    response = client.post("/emissions", json=country_codes)
    assert response.status_code == 200
    assert len(response.json()) == len(country_codes)


def test_top10_life_expectancy():
    response = client.get("/top10-life-expectancy")
    assert response.status_code == 200
    assert len(response.json()) == 10


def test_total_emissions_by_country_codes():
    country_codes = ["CAN", "LUX", "EST"]
    response = client.post("/total-emissions", json=country_codes)
    assert response.status_code == 200
    assert isinstance(response.json(), float)
