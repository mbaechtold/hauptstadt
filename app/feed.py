import os

import httpx


def fetch_items():
    response = httpx.get(
        os.environ["FEED"],
        auth=(
            os.environ["USERNAME"],
            os.environ["PASSWORD"],
        ),
    )
    return response.json()
