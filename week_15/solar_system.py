# Imports
import csv
import datetime as dt

import astroquery.jplhorizons as aqj
import astropy.time as apt


# Constants
AU: int = 149597870700  # meters


# Classes
class Body: 
    """Represents a single planet, moon, or star."""


class SolarSystem: 
    """Manages the collection of all bodies and updates their physics."""

    def __init__(self, date: dt.datetime, filename: str) -> None: 
        self.bodies: list[Body] = []
        self.date: dt.datetime = date

        self.load_bodies(filename)

    def load_bodies(self, filename: str) -> None: 
        """Reads a CSV and fetches live API data for each planet."""
        with open(filename, "r") as file_obj: 
            csv_reader: csv.DictReader = csv.DictReader(file_obj)

            for row in csv_reader: 
                body: Body | None = self.fetch_body(row)

    def fetch_body(self, row: dict) -> Body | None: 
        """Reaches out to JPL Horizons for a specific planet's velocity and position."""
        body_id: int = int(row["body_id"])
        tbd_time: apt.Time = apt.Time(self.date)

        vectors: dict = aqj.Horizons(id=body_id, location="@Sun", epochs=tbd_time.jd1).vectors()

        return Body(
            body_id,
            row["name"],
            float(row["mass"]),
            row["color"],
            row["pixel_radius"],
            vectors["x"][-1] * AU,
            vectors["y"][-1] * AU,
            vectors["vx"][-1] * AU / 24,
            vectors["vy"][-1] * AU / 24,
        )