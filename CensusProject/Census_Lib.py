import traceback
import os
from datetime import datetime
import logging
import sys
import pyodbc

def CheckLogFile():
    try:
        logFilesFolderPath = os.path.dirname(os.path.realpath(__file__))+"\\CensusDataLogFiles"
        logFileName = "Census_Log_File_" + str(datetime.now().date()) + ".txt"
        logFileFullPath = logFilesFolderPath +"\\"+ logFileName
        print(logFileFullPath)
        if os.path.isfile(logFileFullPath):
            return logFileFullPath
        else:
            open(logFileFullPath,"x")
            return logFileFullPath
    except:
        print(traceback.format_exc())
        sys.exit()

def InitializeLogging():
    try:
        logFile = CheckLogFile()
        logging.basicConfig(filename=logFile,   
            filemode='a',
            format='%(asctime)s %(name)-8s %(levelname)-8s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.DEBUG)
        return logging
    except:
        print(traceback.format_exc())
        sys.exit()

def InsertDataFrameToTable(df,parGet,parBlockGroup,parTract,parCounty,parState,parYear):
    server = 'gissql.nmads.lcl'
    database = 'OBAEGIS'
    username = 'OBAERESPEC'
    password = 'GIS#starlink23'
    cnxn = pyodbc.connect(driver='{SQL Server}', host=server, database=database,trusted_connection='yes', user=username, password=password)
    cursor = cnxn.cursor()

    # Create a Table(CensusData) If Not Exist.

    #sqlCreateTableQry = "IF OBJECT_ID(N'CENSUSDATA', N'U') IS NULL BEGIN CREATE TABLE CENSUSDATA(NAME VARCHAR(MAX) NULL, YEAR INT NULL, FIPS VARCHAR(MAX) NULL, VARIABLE VARCHAR(50) NULL,VALUE decimal(18, 0) NULL) END;"

    #cursor.execute(sqlCreateTableQry)
    #cnxn.commit()
    #cursor.close()
    cursor = cnxn.cursor()

    # Insert Dataframe into SQL Server:

    for index, row in df.iterrows():
        valName = row.NAME
        valYear = row.YEAR
        if parState != "":
            valFIPS = row.state
        if parCounty != "":
            valFIPS = valFIPS+row.county
        if parTract != "":
            valFIPS = valFIPS+"/"+row.tract
        if parBlockGroup != "":
            valFIPS = valFIPS+"/"+row.values[6]

        if len(parGet) > 1:
            for par in parGet:
                if par != "NAME":
                    valVariable = row[par]
                    cursor.execute("INSERT INTO OBAERESPEC.CENSUSDATA (NAME,YEAR,FIPS,VARIABLE,VALUE) values(?,?,?,?,?)",valName,valYear,valFIPS,par,valVariable)
        else:
            valVariable = row+"."+parGet[1]
            cursor.execute("INSERT INTO OBAERESPEC.CENSUSDATA (NAME,YEAR,FIPS,VARIABLE,VALUE) values(?,?,?,?,?)", valName,valYear,valFIPS,parGet[1],valVariable)
    cnxn.commit()
    cursor.close()