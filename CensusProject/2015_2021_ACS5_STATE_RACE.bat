REM Extract NM state, county, tract, block group, place data for variables provided by Matt from ACS 5yr survey for 2015 to 2021

SET PythonPath="C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe"
SET ProjectPath="E:\RESPECPUB_ARPX_DoNotDelete\CensusProject\get_census_5year_data.py"
SET ProjectPath1="E:\RESPECPUB_ARPX_DoNotDelete\CensusProject\get_census_1year_data.py"

 

pushd %~dp0

 

%PythonPath% %ProjectPath% "dataset=acs/acs5" "get=NAME,B02001_001E" "block group=" "tract=" "county=" "state=35" "year=2021" "filename=2021_ACS5_STATE_RACE"
%PythonPath% %ProjectPath% "dataset=acs/acs5" "get=NAME,B02001_001E" "block group=" "tract=" "county=" "state=35" "year=2020" "filename=2020_ACS5_STATE_RACE"
%PythonPath% %ProjectPath% "dataset=acs/acs5" "get=NAME,B02001_001E" "block group=" "tract=" "county=" "state=35" "year=2019" "filename=2019_ACS5_STATE_RACE"
%PythonPath% %ProjectPath% "dataset=acs/acs5" "get=NAME,B02001_001E" "block group=" "tract=" "county=" "state=35" "year=2018" "filename=2018_ACS5_STATE_RACE"
%PythonPath% %ProjectPath% "dataset=acs/acs5" "get=NAME,B02001_001E" "block group=" "tract=" "county=" "state=35" "year=2017" "filename=2017_ACS5_STATE_RACE"
%PythonPath% %ProjectPath% "dataset=acs/acs5" "get=NAME,B02001_001E" "block group=" "tract=" "county=" "state=35" "year=2016" "filename=2016_ACS5_STATE_RACE"
%PythonPath% %ProjectPath% "dataset=acs/acs5" "get=NAME,B02001_001E" "block group=" "tract=" "county=" "state=35" "year=2015" "filename=2015_ACS5_STATE_RACE"
