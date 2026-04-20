# Imports
import sqlite3 as s3
import datetime as dt

import matplotlib.pyplot as plt

def main() -> None: 
    """Retrieve Data from Database and Graph by Riley Tuttle"""

    # REQUEST DATA
    conn: s3.Connection = s3.connect("weather.db")
    cur: s3.Cursor = conn.cursor()

    rows: list = cur.execute("SELECT date, prcp FROM weather_data").fetchall()

    cur.close()
    conn.close()

    # PROCESS DATA
    dates: list[dt.datetime] = []
    precip: list[float] = []

    for row in rows: 
        date: dt.datetime = dt.datetime.strptime(row[0], r"%Y-%m-%d")
        dates.append(date)
        precip.append(row[1] * 10) # compensate for measurements in 10th of milimeters by multiplying by 10

    # GRAPH DATA
    plt.plot(dates, precip, c="blue")

    plt.title("Precipitation for Denver Airport Weather Stations, CO By Riley Tuttle")
    plt.xlabel("Date")
    plt.ylabel("Precipitation (mm)")

    plt.legend(["Precipitation"], loc="upper left")
    plt.gcf().autofmt_xdate()

    plt.show()


if __name__ == "__main__":
    main()