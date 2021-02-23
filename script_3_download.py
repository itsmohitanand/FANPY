from forpy import download_era5_single

download_dir = '/data/compoundx/era_5_single/'
var = 'total_cloud_cover'


for year in range(1979,2018):
    download_era5_single(var=var, download_dir = download_dir, year=year) 