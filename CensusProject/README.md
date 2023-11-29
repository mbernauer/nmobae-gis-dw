# Developing a GIS Data Warehouse using Census Data
Contact: Raghuveer (raghuveer.kalluri@respec.com)

# Purpose
This repo contains scripts for downloading Census data (e.g. Census Data Profile tables) and loading them into the OBAE GIS Data Warehouse. The Census data currently available include approximately 570 metrics accessible within the Census Data Profile product. The purpose of this data warehouse is to expose relevant Census data in away that is conducive to analysis, reporting, and geospatial analysis.

# GIS DW Data Model
The GIS DW leverages a _star_ model in which there is a core fact table containing all of the "facts" available for each geography/time point. This fact table has foreign keys that point to two dimension tables which store metadata relating to _concepts_ and _geographies_. Concepts are Census variables such as "Number of households with internet acccess" and are stored in the `concepts` table. Geographies represent the spatial regions described by the concepts such as block groups, tracts, counties, and states. Currently, the DW conains only those geographies belonging to the Census hierarchy (i.e. state > counties > tracts > block groups) and contains facts from the ACS-5 year survey from present day back to 2015.

The figure below shows the data model which can also be accessed/modified [here](https://dbdiagram.io/d/OBAE-GIS-DW-65241608ffbf5169f054ae66). From the ERD you'll notice that the fact table (`geofacts`) is stored in long form as entity-attribute-value tuples (i.e attributes describing a particular geography are stored across multiple rows vs multiple columns). This has several advantages including a much simpler table structure since we need 4 columns (`cid`, `gid`, `year`, `value`) to capture _any_ number of attributes. This is partuclarly useful when the number of attributes may change over time (e.g. if we were to bring in additional meaures from another Census product or data provider).
![GIS DW Data Model](./assets/OBAE\ GIS\ DW.png)

# GIS DE Data Mart
One of the primary objectives of the GIS DW is to support work related to assessing and improving Digital Equity across the state of New Mexico. With this in mind, a logical next step would be to develop a Digital Equity datamart which stores and exposes only those measures related to Digital Equity. Exposing these measures in the form of a datamart ensures future analysts and application developers can easily find these measures.

There are a number of different schemas that the Digital Equity datamart could leverage. For example, we could store each attribute as a seperate column which may be most familar to other analysts. This approach has a few advantages; 1) familiarity since most data consumers are used to consuming data in tabular format; 2) integration with applicaitons sugh as ArcGIS which expect tabular data. One downside of this approach is that the number of columns can quickly become large; for example ther are roughly 170 variables across the Census Detail and Data Profile tables that may be relevant to Digital Equity. Furthermore, the number of columns will change anytime additional data are added which may have negative effects on any downtream applications that happent be consuming data from this table. To address these issues we may want to leverage an EAV type schema similar to the one used by the `geofacts` table. Under this schema we store all attributes describing a partuclar geography as rows. This means we can store an infinite number of attributes with a finite number of columns. This dramatically simplifies the table structure while still serving a convenient storage locaiton for digital equity related measures.

An example EAV schema for the Digital Equity data mart can be seen in the table below.

| Column        | Data Type | Description                                                                            |
| ---           | ---       | ---                                                                                    |
| gid           | int       | Geo ID and foreign key into geographies table                                          |
| cid           | int       | Concept ID and foreign key into concepts table                                         |
| year          | int       | Year the variable was measured (e.g. 2021)                                             |
| fips          | varchar   | FIPS code for the geography                                                            |
| geolevel      | varchar   | Describes the geographic level of the attribute (e.g. blockgroup, tract, county, state |
| desc          | varachar  | Describes the concept (e.g. Estimate!!Total:!!No Internet Access                       |
| value         | float     | Numerical value for the concept (e.g. 27,348)                                          |
| geography     | geography | Polygon describing the geography (e.g. county boundary)                                |

# Variables to Include in the Digital Equity Datamart

A list of relavent variables available from the Census can be found in the `census-variables` directory of this repository. Specifically, `de-detail.tsv` lists approximately 120 variables available from the Census Detail tables while `de-profile.tsv` lists ~ 60 additional variables from the Data Profile tables. Additional variables identified from the CTC County Profiles and the Community Learning Network can be seen in the Data Inventory [here](https://nmgov.sharepoint.com/sites/DoIT-NMOBAEGIS/_layouts/15/Doc.aspx?sourcedoc={dd2ed41d-4215-421b-9b96-fd3163077ae2}&action=edit&wd=target%28Apps%20-%20Design.one%7C48c8e629-b4a1-4a56-9fe7-2970735903ce%2F%2A%2A~~APP%20County%20Profiles~~%7C2299a225-55a7-4c67-b32f-01f24dba5646%2F%29&wdorigin=NavigationUrl)

# Related Reading
1. Additional documentation describing the GIS DW: [here](https://nmgov.sharepoint.com/sites/DoIT-NMOBAEGIS/_layouts/15/Doc.aspx?sourcedoc={dd2ed41d-4215-421b-9b96-fd3163077ae2}&action=edit&wd=target%28Data-Analysis.one%7Ce8f2a4f9-00e4-4f8a-977d-12e1f2f9e90a%2FData%20Model%20Concept%20%20Outline%7Cd1c84b93-90c6-4356-933d-1e74b317a209%2F%29&wdorigin=NavigationUrl) 
2. Additional Digital Equity varaibles from CTC and Community Learning Network: [here](https://nmgov.sharepoint.com/sites/DoIT-NMOBAEGIS/_layouts/15/Doc.aspx?sourcedoc={dd2ed41d-4215-421b-9b96-fd3163077ae2}&action=edit&wd=target%28Apps%20-%20Design.one%7C48c8e629-b4a1-4a56-9fe7-2970735903ce%2F%2A%2A~~APP%20County%20Profiles~~%7C2299a225-55a7-4c67-b32f-01f24dba5646%2F%29&wdorigin=NavigationUrl)
3. Recommended CTC key performance indicators for tracking Digital Equity initiatives: [here](https://nmgov.sharepoint.com/sites/DoIT-NMOBAEGIS/_layouts/15/Doc.aspx?sourcedoc={dd2ed41d-4215-421b-9b96-fd3163077ae2}&action=edit&wd=target%28Data-Analysis.one%7Ce8f2a4f9-00e4-4f8a-977d-12e1f2f9e90a%2F%2A%2A~~%20DATA%20%20Digital%20Equity%20~~%7C31e78a93-7f6d-4a40-a393-9a26f40abf4c%2F%29&wdorigin=NavigationUrl)
