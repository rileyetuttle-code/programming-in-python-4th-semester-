# Imports
import json
import _sqlite3 as s3

import requests as req

import my_token as mt


def main() -> None: 
    """Retrieve Data from Database and Graph by Riley Tuttle"""

    # REQUEST DATA
    token: str = mt.TOKEN

    # Q variables
    base_url: str = "https://www.ncei.noaa.gov/cdo-web/api/v2/data?"
    dataset_id: str = "GHCND"
    station_id: str = "GHCND:USW00003017"
    datatype_id: str = "PRCP,TMAX,TMIN"
    start_date: str = "2025-01-01"
    end_date: str = "2025-12-31"
    units: str = "standard"
    limit: int = 1000
    offset: int = 1

    data: dict[str, dict] = {}

    while True:
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

        with open("view.json", "w") as f:
            f.write(json.dumps(r.json(), indent=4))

        # PROCESS DATA
        if "results" not in data_json or len(data_json["results"]) == 0:
            break

        for item in data_json["results"]:
            date: str = item["date"].split("T")[0]

            if data.get(date) is None: 
                data[date] = {"PRCP": None, "TMAX": None, "TMIN": None}

            if item["datatype"] == "TMAX":
                data[date]["TMAX"] = item["value"]
            elif item["datatype"] == "TMIN":
                data[date]["TMIN"] = item["value"]
            elif item["datatype"] == "PRCP":
                data[date]["PRCP"] = item["value"]

        offset += 1000

    # STORE DATA
    conn: s3.Connection = s3.connect("weather.db")
    cur: s3.Cursor = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS weather_data")
    cur.execute("CREATE TABLE weather_data (date TEXT, prcp REAL, high REAL, low REAL)")

    for date, values in data.items():
        command: str = "INSERT INTO weather_data (date, prcp, high, low) VALUES (?, ?, ?, ?)"
        cur.execute(command, (date, values["PRCP"], values["TMAX"], values["TMIN"]))

    conn.commit()

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()