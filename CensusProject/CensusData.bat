REM Extract NM state, county, tract, block group, place data for variables provided by Matt from ACS 5yr survey for 2015 to 2021
SET PythonPath="C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe"
SET ProjectPath="E:\RESPECPUB_ARPX_DoNotDelete\CensusProject\get_census_5year_data.py"
SET ProjectPath1="E:\RESPECPUB_ARPX_DoNotDelete\CensusProject\get_census_1year_data.py"

pushd %~dp0

%PythonPath% %ProjectPath% "get=NAME,DP02_0151PE,DP02_0152PE" "tract=*" "county=*" "state=35" "year=2015" "filename=ACS5_2015_NMStateData"
%PythonPath% %ProjectPath% "get=NAME,DP02_0151PE,DP02_0152PE" "tract=*" "county=*" "state=35" "year=2016" "filename=ACS5_2016_NMStateData"
%PythonPath% %ProjectPath% "get=NAME,DP02_0151PE,DP02_0152PE" "tract=*" "county=*" "state=35" "year=2017" "filename=ACS5_2017_NMStateData"
%PythonPath% %ProjectPath% "get=NAME,DP02_0151PE,DP02_0152PE" "tract=*" "county=*" "state=35" "year=2018" "filename=ACS5_2018_NMStateData"
%PythonPath% %ProjectPath% "get=NAME,DP02_0152PE,DP02_0153PE" "tract=*" "county=*" "state=35" "year=2019" "filename=ACS5_2019_NMStateData"
%PythonPath% %ProjectPath% "get=NAME,DP02_0153PE,DP02_0154PE" "tract=*" "county=*" "state=35" "year=2020" "filename=ACS5_2020_NMStateData"
%PythonPath% %ProjectPath% "get=NAME,DP02_0153PE,DP02_0154PE" "tract=*" "county=*" "state=35" "year=2021" "filename=ACS5_2021_NMStateData"


%PythonPath% %ProjectPath1% "get=NAME,DP02_0151PE,DP02_0152PE" "tract=" "county=*" "state=35" "year=2015" "filename=ACS1_2015_NMStateData"
%PythonPath% %ProjectPath1% "get=NAME,DP02_0151PE,DP02_0152PE" "tract=" "county=*" "state=35" "year=2016" "filename=ACS1_2016_NMStateData"
%PythonPath% %ProjectPath1% "get=NAME,DP02_0151PE,DP02_0152PE" "tract=" "county=*" "state=35" "year=2017" "filename=ACS1_2017_NMStateData"
%PythonPath% %ProjectPath1% "get=NAME,DP02_0151PE,DP02_0152PE" "tract=" "county=*" "state=35" "year=2018" "filename=ACS1_2018_NMStateData"
%PythonPath% %ProjectPath1% "get=NAME,DP02_0152PE,DP02_0153PE" "tract=" "county=*" "state=35" "year=2019" "filename=ACS1_2019_NMStateData"
%PythonPath% %ProjectPath1% "get=NAME,DP02_0153PE,DP02_0154PE" "tract=" "county=*" "state=35" "year=2020" "filename=ACS1_2020_NMStateData"
%PythonPath% %ProjectPath1% "get=NAME,DP02_0153PE,DP02_0154PE" "tract=" "county=*" "state=35" "year=2021" "filename=ACS1_2021_NMStateData"