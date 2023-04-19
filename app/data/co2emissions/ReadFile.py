import pandas as pd


def read_csv_from_url(url: str) -> pd.DataFrame:
    df = pd.read_csv(url)
    return df


if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/GreenfactAS/co2-dataset/main/CO2-emissions.csv"
    df = read_csv_from_url(url)
    print(df.head())
