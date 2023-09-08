# Usage: ./get_acs_variables.sh > CENSUS_CATALOG.txt
#
# Desc: Creates a single catalog file containing all available Census variables

# download product variables
curl -s https://api.census.gov/data/2021/acs/acs5/variables.json > tmp.detail
curl -s https://api.census.gov/data/2021/acs/acs5/subject/variables.json > tmp.subject 
curl -s https://api.census.gov/data/2021/acs/acs5/profile/variables.json > tmp.profile

# parse JSON and write to TSV
jq -rc '.variables | keys[] as $k | [$k, .[$k].label, .[$k].concept, .[$k].group] | @tsv' tmp.* | grep '^[SBDP]\{1,2\}[0-9]' | perl -lne '/^B/ && print "DETAIL\t$_"; /^D/ && print "PROFILE\t$_"; /^S/ && print "SUBJECT\t$_"'

# remove json
rm tmp.*
