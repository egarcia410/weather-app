# Weather App
Reports location's current weather forecast, uses Dark Sky API and Google Maps Geocoding API

## Getting Started
1. Install [Python3](https://www.python.org/downloads/)

2. Clone Repository:

        $ git clone https://github.com/egarcia410/weather-app.git

3. Change Directory:

        $ cd weather-app

4. Install [VirtualWrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)

5. Create and Activate Virtualenv:

        $ mkvirtualenv -a `pwd` -p `which python3` INSERT_VIRTUALENV_NAME
    
6. Install Dependencies:

        $ pip install -r requirements.txt

7. Create `.env` File:

        $ touch .env

## Get Dark Sky API Secret Key
1. Register an account at [Dark Sky](https://darksky.net/dev)

2. Once registered, a secret key will be granted

3. Insert secret key inside the `.env` file:
```
SECRET_KEY=INSERT_YOUR_SECRET_KEY_HERE
```

## Getting Google Maps Geocoding API Key
1. Log into Google

2. Go to Google Cloud Platform [Dashboard](https://console.cloud.google.com/home/dashboard)

3. In side menu, click on `APIs & services`

4. In side menu, click on `Credentials`

5. Click on `Create credentials`

6. In dropdown menu, click on `API key`

7. In pop out menu, your API key will be displayed

    *You can **Restrict Key** and change **name*** 

8. Insert key inside the `.env` file:
```
KEY=INSERT_YOUR_KEY_HERE
```

9. Enable [Google Maps Geocoding API](https://console.cloud.google.com/apis/api/geocoding_backend/overview)

## Run Application
1. Inside project folder and activated Virtualenv:

        $ python app.py
