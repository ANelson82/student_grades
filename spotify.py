import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime import sqlite3

DATABASE_LOCATION = "sqlite://my_played_tracks.sqlite"
USER_ID = "sparat1k"
TOKEN = "BQBc82wpH_6ekljb0R0glWQJ46d2PYDQDs6kntzlDf0k2EjO2ZCwgMjfOFf1ihpNL2eqY80mzlkt2yYzqgdzzYhCMNoCA2L0MZKWWZirqfhuAUVwGZLze2SPqXKvX3_FKP2nnrGngBIdzw"

## these are some comments that I want to make
if __name__ == "__main__":
    headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json"
        "Authorization" : "Bearer {token}".format(token=TOKEN)
    }

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta*(days=1)
