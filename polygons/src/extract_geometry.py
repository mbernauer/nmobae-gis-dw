#!/usr/bin/env python3

def main(infile, geo_level, year):
	df = gpd.read_file(infile)
	df['GEOLEVEL'] = geo_level
	df['year'] = year
	df = df[['year','GEOLEVEL','GEOID','geometry']]
	df.columns = ['year','geolevel', 'geoid', 'geometry']
	df[['year','geolevel','geoid','geometry']].to_csv(sys.stdout, index = False, header = False, sep = '\t')

if __name__ == '__main__':
	import sys
	if len(sys.argv) == 1:
		help = """usage: extract_polygons.py <infile> [TRACT|COUNTY|STATE]"""
		print(help)
		sys.exit()

	import geopandas as gpd
	main(sys.argv[1], sys.argv[2], sys.argv[3])
