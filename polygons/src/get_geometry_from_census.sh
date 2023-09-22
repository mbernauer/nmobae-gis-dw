#!/usr/bin/env bash

function main () {
	YEAR=$1
	curl -s "https://www2.census.gov/geo/tiger/TIGER${YEAR}/STATE/tl_${YEAR}_us_state.zip" -o ${YEAR}_STATE.zip
	curl -s "https://www2.census.gov/geo/tiger/TIGER${YEAR}/COUNTY/tl_${YEAR}_us_county.zip" -o ${YEAR}_COUNTY.zip
	curl -s "https://www2.census.gov/geo/tiger/TIGER${YEAR}/TRACT/tl_${YEAR}_35_tract.zip" -o ${YEAR}_TRACT.zip
	./src/extract_geometry.py ${YEAR}_STATE.zip STATE ${YEAR} | perl -F'\t' -lane 'print if $F[2] =~ /^35/' 
	./src/extract_geometry.py ${YEAR}_COUNTY.zip COUNTY ${YEAR} | perl -F'\t' -lane 'print if $F[2] =~ /^35/' 
	./src/extract_geometry.py ${YEAR}_TRACT.zip TRACT ${YEAR} | perl -F'\t' -lane 'print if $F[2] =~ /^35/'
}

if [[ $# -ne 1 ]]; then
	echo "Usage: get_geometry_from_census.sh <year>"
	exit 1
fi
main $1
