# Download Census polygons
Code used to retrieve Census polygons

State, County, Tract, and Block Groups are returned for the state of New Mexico.

```
# to run
make all
```
Once complete you should have `geometries.tsv` file which contains the following columns

```
year		Year the geometry applies
geolevel	Geographic level (e.g. STATE, COUNTY, TRACT, BLOCKGROUP)
geoid		FIPS geo id
geometry	polygon
```
