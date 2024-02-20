import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime 
from slack_message import slack_send_message


# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1AH9PcCXHhbTZposjvSBgbrs1rxUgOtCT_B9DOG3UGf4"
SAMPLE_RANGE_NAME = "A:C"


def main():
  creds = None
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    values = result.get("values", [])

    if not values:
      print("No data found.")
      return
    
    today = datetime.datetime.today().strftime("%m-%d")
   
    for i, row in enumerate(values):
      if row: # if row is not empty, format birthday correctly and compare
        if i==0:
          continue

        date_with_year = row[2].split("-")
        birthday = "-".join(date_with_year[1:])
        if birthday == today:
          slack_send_message(name=f"{row[0]} {row[1]}")

  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()



# CRONTAB KODEN: 0 12 * * * 