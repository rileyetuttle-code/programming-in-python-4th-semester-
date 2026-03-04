import re

import requests as rq


def main() -> None:
    url: str = "https://www.wikipedia.org/wiki/Python_(programming language)" 
    headers: dict = {"User-Agent": "rtuttle1@atu.edu"}

    response: rq.Response = rq.get(url, headers = headers)
    print(response.status_code)

    page_content: str = response.text
    # print(page_content)

    pattern: str = r"[0-3]?[0-9] [A-Z][a-z]+ [0-9]{4}"
    results: list[str] = re.findall(pattern, page_content)

    print(results)




main()