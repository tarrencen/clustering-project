# Clustering Project

### Purpose: Determine if unsupervised ML clustering can be used to help predict log error in Zillow's ML regression model

### Data Dictionary
Feature	                                            Description

'bathroomcnt': 'baths'	                            Number of bathrooms in home including fractional bathrooms

'bedroomcnt': 'beds'	                            Number of bedrooms in home 

'buildingqualitytypeid': 'bldg_qual'	            Overall assessment of condition of the building from best (lowest) to worst (highest)
 
'calculatedbathnbr': 'calc_bath'	                Number of bathrooms in home including fractional bathroom

'calculatedfinishedsquarefeet': 'calc_fin_sqft'	    Calculated total finished living area of the home 

'finishedsquarefeet12': 'fin_sqft_12'	            Finished living area

'fips': 'county_name'	                            Federal Information Processing Standard -  see https://en.wikipedia.org/wiki/FIPS_county_code 

'fireplaceflag': 'has_firepl'	                    Is a fireplace present in this home 

'fullbathcnt': 'full_bath_ct'	                    Number of full bathrooms (sink, shower + bathtub, and toilet) present in home

'heatingorsystemdesc': 'heat_sys_desc'              Descriptor of type of home heating system

'heatingorsystemtypeid': 'heat_sys'	                Numeric designator for type of home heating system

'latitude': 'lat'	                                Latitude of the middle of the parcel multiplied by 10e6

'longitude': 'long'	                                Longitude of the middle of the parcel multiplied by 10e6

'parcelid': 'parcel_id'	                            Unique identifier for parcels (lots)

'poolcnt': 'has_pool'	                            Number of pools on the lot (if any

'propertylandusedesc': 'prop_land_desc'             Type of land use the property is zoned for

'propertylandusetypeid'	                            Numeric designator for property land use description

'regionidzip'	                                    Zip code in which the property is located

'roomcnt': 'room_ct'	                            Total number of rooms in the principal residence

'unitcnt': 'unit_ct	                                Number of units the structure is built into (i.e. 2 = duplex, 3 = triplex, etc...)

'yearbuilt': 'yr_blt'	                            The Year the principal residence was built

'taxvaluedollarcnt': 'tax_val'                      The total tax assessed value of the parcel

'property age*': 'prop_age'                         Engineered feature (2017 - 'yr_blt')

'logerror': 'log_err'                               log(Zestimate) - log(Sale price)



### Questions:

- Which variables are best suited for clustering?

- What do we gain by using clustering in our process?

- What effect does including more precise geolocation data have with respect to generating models?

- Are regression models built using clustering during the feature selection process better than those that do not have clustering involved?

### Procedure

- Acquire data via SQL query

- Wrangle data: Remove null values with drops or imputation, remove irrelevant or redundant columns, engineer features as needed

- Explore and do univariate analysis on clean df

- Split df into train/validate/test, isolate target ('log_err'), scale X splits

- Model clusters, and visualize plots with clusters incorporated

- Use conclusions from cluster analysis to inform regression model building

- Build and test regression models against target

- Report findings

# Findings:
In the purview of this project, ML clusters seem the most useful when employed as categorical variables. They served here as an aid in the regression model feature selection process, mostly in that they confirmed earlier conclusions about the features that may be the most effective in predicting a moving target like log error or tax assessed value.