import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json


# google sheets setup
scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
credtails = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(credtails)
sheet = client.open("232-database")
entries = sheet.worksheet("Sheet1")

print(entries.get_all_records())
