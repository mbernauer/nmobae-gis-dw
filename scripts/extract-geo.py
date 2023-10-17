#!/usr/bin/env python3


# read shapefile as df
def main(year, geolevel, filename):
    df = gpd.read_file(filename)
    df['YEAR'] = year
    df['LEVEL'] = geolevel
    df[['YEAR','LEVEL','GEOID','geometry']].to_csv(sys.stdout, index = False)


if __name__ == '__main__':
    import sys

    # shapefile name
    help = "Usage: extract-geo.py <year> <geolevel> <shapefile>"
    args = sys.argv[1::]

    if len(args) != 3:
        print(help)
        sys.exit()

    import geopandas as gpd

    main(args[0], args[1], args[2])
