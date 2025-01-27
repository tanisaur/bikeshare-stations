# Capital Bikeshare Station Optimization

Capital Bikeshare is a bikeshare company that services the Washington DC metropolitan area. 

### Problem: Which stations are underperforming or overburdened?
Bikeshare systems often encounter challenges where certain stations are either underutilized or overburdened due to uneven demand patterns. This can lead to inefficiencies in resource allocation, such as bike shortages at high-demand locations or excess bikes at low-traffic stations.

This project includes an analysis of trip start and end stations to:

- **Identify High-Traffic Stations**: Pinpoint stations with consistently high demand to ensure they are adequately stocked with bikes and docking spaces.
- **Identify Low-Traffic Stations**: Locate underperforming stations to evaluate their suitability for relocation or removal.

### Data Source
Data is sourced courtesy of https://capitalbikeshare.com/system-data

2024 bikeshare data has been combined for this dataset and store in AWS S3

`!wget -O bikeshare_data.parquet "https://2024-bikeshare.s3.us-west-2.amazonaws.com/2024_bikeshare_data.parquet"`



