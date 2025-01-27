# Capital Bikeshare Station Optimization

Capital Bikeshare is a bikeshare company that services the Washington DC metropolitan area. 

### Problem: Which stations are underperforming or overburdened?
Bikeshare systems often encounter challenges where certain stations are either underutilized or overburdened due to uneven demand patterns. This can lead to inefficiencies in resource allocation, such as bike shortages at high-demand locations or excess bikes at low-traffic stations.

This project includes an analysis of trip start and end stations to:

- **Identify High-Traffic Stations**: Pinpoint stations with consistently high demand to ensure they are adequately stocked with bikes and docking spaces.
- **Identify Low-Traffic Stations**: Locate underperforming stations to evaluate their suitability for relocation or removal.

### Data Source
Data is sourced courtesy of https://capitalbikeshare.com/system-data

2024 bikeshare data has been combined for this dataset and stored in AWS S3

You can access it via the link below

`!wget -O bikeshare_data.parquet "https://2024-bikeshare.s3.us-west-2.amazonaws.com/2024_bikeshare_data.parquet"`

### 📊 Dataset Description

The dataset used in this project contains key features related to individual rides in the District of Columbia metro area. 

Below is a breakdown of the dataset columns:

Column Name |	Description|
| ------ | ------ |
| booking_id	| Unique identifier for each booking. |
| started_at |	Date and time of the start of the ride. |
| ended_at	| Date and time of the end of the ride. |
| start_station_name	| Name of the station the ride began. |
| start_station_id	| Id of the station where the ride began. |
| end_station_name	| Name of the station the ride ended. |
| end_station_id | Id of the station where the ride ended. | 
| start_lat |  Starting lattitude where the ride began. |
| start_lng |  Starting longitude where the ride began. |
| end_lat |  Ending lattitude where the ride ended. |
| end_lng | Ending longitude where the ride ended. |

### 📈 Key Insights

- Many bikes are not locked at stations:
    The are a large number of bikes not being locked up at stations, especially more so when ending a trip. Meaning either there was no bike station available or it was full.

-  Time of day influence usage:
    Weekday evenings the hour of 5pm is the most used times for bikes.

-  Busiest Month:
    Trips steadily increased throughout the year reaching its peak in October, with over 700,000 trips taken.   

- Most Frequented Starting and Ending Station:
    The most frequently used station is  Columbus Circle / Union Station.

- Least Frequented Starting and Ending Station:
    The least frequently used station is Ring Rd & North Shore Dr.

### 🤖 Random Forest Model vs. XGBoost
|MAE |	MSE | R^2 | 
| ------ | ------ | ------ | 
| Random Forest | 0.09641000835% | 0.11119595421%| 99.84704785555573% |
| XGBoost	| 0.93672946095%	| 0.21088903304% |	99.7099161148% |

