# Imports
import json
import _sqlite3 as s3

import requests as req

import my_token as mt


def main() -> None: 
    """Retrieve Data from Database and Graph by Riley Tutte"""

    # REQUEST DATA
    token: str = mt.TOKEN

    # Q variables
    base_url: str = "https://www.ncei.noaa.gov/cdo-web/api/v2/data?"
    dataset_id: str = "GHCND"
    station_id: str = "GHCND:USW00003952"
    datatype_id: str = "TMAX,TMIN"
    start_date: str = "2025-01-01"
    end_date: str = "2025-12-31"
    units: str = "standard"
    limit: int = 1000
    offset: int = 1

    query_url: list[str] = [
        base_url,
        f"datasetid={dataset_id}&",
        f"stationid={station_id}&",
        f"datatypeid={datatype_id}&",
        f"startdate={start_date}&",
        f"enddate={end_date}&",
        f"units={units}&",
        f"limit={limit}&",
        f"offset={offset}",
    ]

    request_url: str = "".join(query_url)
    r: req.Response = req.get(request_url, headers={"token":token})
    data_json: dict = json.loads(r.text)

    # PROCESS DATA
    data: dict[str, dict] = {}

    for item in data_json["results"]:
        date: str = item["date"].split("T")[0]

        if data.get(date) is None: 
            data[date] = {"TMAX": None, "TMIN": None}

        if item["datatype"] == "TMAX":
            data[date]["TMAX"] = item["value"]
        elif item["datatype"] == "TMIN":
            data[date]["TMIN"] = item["value"]

    # STORE DATA
    conn: s3.Connection = s3.connect("weather.db")
    cur: s3.Cursor = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS weather_data")
    cur.execute("CREATE TABLE weather_data (date TEXT, high REAL, low REAL)")

    for date, values in data.items():
        command: str = "INSERT INTO weather_data (date, high, low) VALUES (?, ?, ?)"
        cur.execute(command, (date, values["TMAX"], values["TMIN"]))

    conn.commit()

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()