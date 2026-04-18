# Imports
import sqlite3 as s3
import datetime as dt

import matplotlib.pyplot as plt


def main() -> None: 
    """Retrieve Data from Database and Graph by Riley Tutte"""

    # REQUEST DATA
    conn: s3.Connection = s3.connect("weather.db")
    cur: s3.Cursor = conn.cursor()

    rows: list = cur.execute("SELECT date, high, low FROM weather_data").fetchall()

    cur.close()
    conn.close()

    # PROCESS DATA
    dates: list[dt.datetime] = []
    highs: list[float] = []
    lows: list[float] = []

    for row in rows: 
        date: dt.datetime = dt.datetime.strptime(row[0], r"%Y-%m-%d")
        dates.append(date)
        highs.append(row[1])
        lows.append(row[2])

    # GRAPH DATA
    plt.plot(dates, highs, c="green")
    plt.plot(dates, lows, c="red")

    plt.title("Temperatures for Little Rock Weather Stations, AR")
    plt.xlabel("Date")
    plt.ylabel("Temperature (\u00b0F)")

    plt.legend(["High", "Low"], loc="upper left")
    plt.gcf().autofmt_xdate()

    plt.show()


if __name__ == "__main__":
    main()