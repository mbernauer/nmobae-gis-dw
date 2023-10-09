#!/usr/bin/bash
# Usage: census_variables.sh > output.tsv

get_vars () {
	YEAR=$1
	SURVEY=$2
	LABEL=$(echo $2 | tr '[:lower:]' '[:upper:]')
	curl -s "https://api.census.gov/data/$YEAR/acs/$SURVEY/profile/variables.json" | jq -r ".variables | keys[] as \$k | [$YEAR,\"US_CENSUS_$LABEL\",\$k,.[\$k].label]|@tsv" | grep '	DP'
}

for year in {2015..2021}; do
	for survey in {acs1,acs5}; do
		get_vars $year $survey
	done
done
