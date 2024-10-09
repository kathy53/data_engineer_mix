import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "client_secret_cred.json", scope
)
client = gspread.authorize(credentials)
# open the GS
spreadsheet = client.open("data_nd_business")

with open("result.csv", "r") as f:
    content = f.read()

client.import_csv(spreadsheet.id, data=content)

# creating a new worksheet
date = datetime.today().strftime("%Y-%m-%d")
# worksheet = spreadsheet.add_worksheet(title=date)
