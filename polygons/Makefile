export PATH := $(PATH):$(PWD)/src/

all: download clean

download:
	@echo "Downloading data..."
	@get_geometry_from_census.sh 2019 > 2019.tsv
	@get_geometry_from_census.sh 2020 > 2020.tsv
	@get_geometry_from_census.sh 2021 > 2021.tsv
	@get_geometry_from_census.sh 2022 > 2022.tsv

clean:
	@echo 'year	geolevel	geoid	geometry' > geometries.tsv
	@cat 20*.tsv > geometries.tsv
	@rm 20*.tsv
	@rm 20*.zip
	@echo "Done!"
