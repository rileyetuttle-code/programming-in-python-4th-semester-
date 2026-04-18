# Imports
import json

import requests as req

import my_token as mt


def main() -> None: 
    """Retrieve Data from Database and Graph by Riley Tutte"""

    # REQUEST DATA
    token: str = mt.TOKEN

    # Q variables
    base_url: str = "https://www.ncei.noaa.gov/cdo-web/api/v2/datasets?"

    query_url: list[str] = [
        base_url,

    ]

    request_url: str = "".join(query_url)
    r: req.Response = req.get(request_url, headers={"token":token})
    data_json: dict = json.loads(r.text)
    
    with open("view.json", "w") as f:
        f.write(json.dumps(r.json(), indent=4))

    # PROCESS DATA

    # GRAPH DATA


if __name__ == "__main__":
    main()