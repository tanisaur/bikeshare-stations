# Capital Bikeshare Station Optimization

![](https://ehq-production-us-california.imgix.net/8e99a9b5c3a7d7b7f21e4de60a1590a0047dc1a0/original/1648656975/9d18f654954b781418520d665f59eeae_blob?1648656975-unsplash--undefined&auto=compress%2Cformat&)

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

- Many bikes are not locked at stations: <br>
    The are a large number of bikes not being locked up at stations, especially more so when ending a trip. Meaning either there was no bike station available or it was full.

-  Time of day influence usage: <br>
    Weekday evenings the hour of 5pm is the most used times for bikes.

-  Busiest Month: <br>
    Trips steadily increased throughout the year reaching its peak in October, with over 700,000 trips taken.   

- Most Frequented Starting and Ending Station: <br>
    The most frequently used station is  Columbus Circle / Union Station.

- Least Frequented Starting and Ending Station: <br>
    The least frequently used station is Ring Rd & North Shore Dr.

### 🤖 Random Forest Model vs. XGBoost
|------ |MAE |	MSE | R^2 | 
| ------ | ------ | ------ | ------ | 
| Random Forest | 0.09641000835% | 0.11119595421%| 99.84704785555573% |
| XGBoost	| 0.93672946095%	| 0.21088903304% |	99.7099161148% |

# Getting Started

### To replicate clone the Repository:
```
git clone https://github.com/tanisaur/bikeshare-stations.git
cd bikeshare-stations
```
### Install Pipenv
Ensure you have Pipenv installed on your system. If it’s not installed yet, you can install it using pip:
``` 
pip install pipenv
```

### Create Pipfile

Navigate to the directory where train.py and predict.py scripts are located and initialize a new Pipenv environment:

``` 
pipenv install
```

### Train Model

``` 
python train.py --data_path path/to/bikeshare_data.parquet
```

### Run the Flask app

``` 
python predict.py
 ```
## How to Build and Run the Docker Image

### Build the Docker Image
```
docker build -t flask-app .
```
### Run the Container
```
docker run -p 5000:5000 flask-app
```
