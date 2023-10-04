import json
import re
          
def parse_email_content(email_content):

    #Creates the body for the list
    info = {
        "ID": None,
        "Name": None,
        "Phone Number": None,
        "Latitude": None,
        "Longitude": None,
        "Uncertainty": None,
        "Time": None,
        "Update Interval": None
    }

    #Parses email content and stores it in the body
    for line in email_content.split("\n"):
        if line.startswith("ID:"):
            info["ID"] = line.split(":")[1].strip()
        elif line.startswith("NAME:"):
            info["Name"] = line.split(":")[1].strip()
        elif line.startswith("PHONE NUMBER:"):
            info["Phone Number"] = line.split(":")[1].strip()
        elif line.startswith("LATITUDE:"):
            info["Latitude"] = line.split(":")[1].strip()
        elif line.startswith("LONGITUDE:"):
            info["Longitude"] = line.split(":")[1].strip()
        elif line.startswith("UNCERTAINTY:"):
            info["Uncertainty"] = line.split(":")[1].strip()
        elif line.startswith("TIME"):
            time_match = re.search(r'\d{2}:\d{2}:\d{2}', line)
            if time_match:
                info["Time"] = time_match.group()
        elif line.startswith("SET TO UPDATE"):
            info["Update Interval"] = line.split(" ")[-2]

    print("PRINTING FROM SCRAPER: ", info)
    # WE WILL UPDATE DATABASE HERE
    return info


    

    
def handler(event, context):
    try: 
        parse_email_content(event)
        return {
      'statusCode': 200,
      'headers': {
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
      },
      'body': json.dumps('Hello from your new Amplify Python lambda!')
  }
   
    except:
        return {
      'statusCode': 400,
      'headers': {
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
      },
      'body': json.dumps("An Error Occured")
  }

        
  
