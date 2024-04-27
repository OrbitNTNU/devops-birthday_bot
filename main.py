from slack_message import slack_send_message
import mysql.connector
from datetime import datetime
from dotenv import load_dotenv
import os 
from slack_sdk import WebClient

def main():
  load_dotenv()


  conn = mysql.connector.connect(
    host=os.environ.get("HOST"),
    port=os.environ.get("PORT"),  
    user=os.environ.get("USER"),
    password=os.environ.get("PASSWORD"),
    database=os.environ.get("DATABASE")
)

  cursor = conn.cursor()
  

  # Begin a transaction
  cursor.execute("START TRANSACTION")


  try:
      client = WebClient(os.environ.get("SLACK_APP_TOKEN"))
      response = client.users_list()
      # Execute SELECT query to fetch all rows from the Member table
      cursor.execute("SELECT activeStatus, name, birthday, slackID, birthdayBot FROM Member")
      
      # Fetch all rows
      rows = cursor.fetchall()
      print(rows)
      print(datetime.today().strftime("%m-%d"))
      
      #go through rows and see if birthday matches date 
      for row in rows:
          if row[0] == 1 and row[4] == 1 and row[2]:
              name_list = row[1].lower().split(" ")
              if row[2].strftime("%m-%d") == datetime.today().strftime("%m-%d"):
                slack_send_message(name_list, response, row[3])


  except Exception as e:
      # Rollback transaction if there's any error
      conn.rollback()
      print("Error:", e)

  finally:
      # Close cursor and connection
      cursor.close()
      conn.close()



if __name__ == "__main__":
  main()


