import requests
import pandas as pd
import sys,os
from Census_Lib import *

 
#Initializing the Log File.

logging  = InitializeLogging()
logging.info("--------------------Fetching Census Data For ACS1 Process Started--------------------\n")

storageDir = os.path.dirname(os.path.realpath(__file__))
storageDir = storageDir + "\\CensusDataOutputFiles"

if not os.path.exists(storageDir):
    # Create a new directory because it does not exist
    os.makedirs(storageDir)
    print(f"The new directory {storageDir} is created to store the output csv files.")
    logging.info("The new directory {storageDir} is created to store the output csv files.")

argv = sys.argv
# argv.append("get=NAME,DP02_0153PE,DP02_0154PE")
# argv.append("tract=*")
# argv.append("county=001")
# argv.append("state=34")
# argv.append("year=2021")
# argv.append("filename=TestOutputFile")

HOST = 'https://api.census.gov/data'
dataset = ''
predicates = {}

for arg in argv:
    if arg.split('=')[0] == 'dataset':
        print(f"{arg.split('=')[0]} parameter value:{arg.split('=')[1]}")
        logging.info(f"{arg.split('=')[0]} parameter value:{arg.split('=')[1]}")
        if not arg.split('=')[1]:
            print("Please enter dataset parameter.")
            sys.exit(arg.split('=')[0])
        else:
            dataset = arg.split('=')[1]
    if arg.split('=')[0] == 'get':
        print(f"{arg.split('=')[0]} parameter value:{arg.split('=')[1]}")
        if arg.split('=')[1] == "":
            print("Please enter get parameter.")
            logging.info("Please enter get parameter.")
            sys.exit(arg.split('=')[0])
        else:
            predicates["get"] = arg.split('=')[1]
            parGet = arg.split('=')[1].split(',')

    if arg.split('=')[0] == 'block group':
        print(f"{arg.split('=')[0]} parameter value:{arg.split('=')[1]}")
        logging.info(f"{arg.split('=')[0]} parameter value:{arg.split('=')[1]}")
        if not arg.split('=')[1] == "":
            predicates["for"] = "block group:"+arg.split('=')[1]
            parBlockGroup = arg.split('=')[1]
        else:
            parBlockGroup = ''

    if arg.split('=')[0] == 'tract':
        print(f"{arg.split('=')[0]} parameter value:{arg.split('=')[1]}")
        logging.info(f"{arg.split('=')[0]} parameter value:{arg.split('=')[1]}")
        if not arg.split('=')[1] == "":
            if "for" in predicates and not predicates["for"] == "":
                predicates["in"] = "tract:"+arg.split('=')[1]
            else:
                predicates["for"] = "tract:"+arg.split('=')[1]
            parTract = arg.split('=')[1]
        else:
            parTract = ''

    if arg.split('=')[0] == 'county':
        print(f"{arg.split('=')[0]} parameter value:{arg.split('=')[1]}")
        logging.info(f"{arg.split('=')[0]} parameter value:{arg.split('=')[1]}")
        if not arg.split('=')[1] == "":
            if "for" in predicates and not predicates["for"] == "":
                predicates["in"] = "county:"+arg.split('=')[1]
            else:
                predicates["for"] = "county:"+arg.split('=')[1]
            parCounty = arg.split('=')[1]
        else:
            parCounty = ''

               
    if arg.split('=')[0] == 'state':
        print(f"{arg.split('=')[0]} parameter value:{arg.split('=')[1]}")
        logging.info(f"{arg.split('=')[0]} parameter value:{arg.split('=')[1]}")
        if not arg.split('=')[1] == "":
            if "in" in predicates and not predicates["in"] == "":
                predicates["in"] = "state:"+arg.split('=')[1] +" "+ predicates["in"]
            else:
                if "for" in predicates and not predicates["for"] == "":
                    predicates["in"] = "state:"+arg.split('=')[1]
                else:
                    predicates["for"] = "state:"+arg.split('=')[1]
            parState = arg.split('=')[1]

           
    if arg.split('=')[0] == 'year':
        print(f"{arg.split('=')[0]} parameter value:{arg.split('=')[1]}")
        logging.info(f"{arg.split('=')[0]} parameter value:{arg.split('=')[1]}")
        if not arg.split('=')[1]:
            print("Please enter year parameter.")
            sys.exit(arg.split('=')[0])
        else:
            year = arg.split('=')[1]
            parYear = arg.split('=')[1]

   
    if arg.split('=')[0] == 'filename':
        print(f"{arg.split('=')[0]} parameter value:{arg.split('=')[1]}")
        logging.info(f"{arg.split('=')[0]} parameter value:{arg.split('=')[1]}")
        if not arg.split('=')[1]:
            print("Please enter filename parameter.")
            sys.exit(arg.split('=')[0])
        else:
            storageDir = storageDir + "\\" + arg.split('=')[1] + ".csv"


base_url = "/".join([HOST,year,dataset])
predicates["key"] = '577fb555542f6a41c4765b88d9e848ce5ef12c5f'

             
print(base_url)
logging.info(base_url)
print(predicates)
logging.info(predicates)
responce = requests.get(base_url,params=predicates)

print(responce.status_code)
logging.info("Responce Status Code:"+str(responce.status_code))

 
if responce.status_code == 200:
    #Displaying Responce in Table Format.
    df = pd.DataFrame(responce.json()[1:],columns=responce.json()[0])
    df['YEAR'] = year
    #df['county'] = df['county'].astype(str)
    # df.county = df.county.apply('="{}"'.format)
    # df.tract = df.tract.apply('="{}"'.format)
    # df.state = df.state.apply('="{}"'.format)
    #df.county = df.county.astype("str")
    #print(df.to_string())

    # inserting data into table.
    InsertDataFrameToTable(df,parGet,parBlockGroup,parTract,parCounty,parState,parYear)


    df.to_csv(storageDir, index=False)
    print(f"Ouput file generated sucessfully in the following location:{storageDir}")
    logging.info(f"Ouput file generated sucessfully in the following location:{storageDir}"+"\n")
    #print(responce.text)
else:
    print(responce.text)
    logging.info("Error Info:"+responce.text+"\n")
logging.info("--------------------Fetching Census Data For ACS1 Process Completed--------------------\n")