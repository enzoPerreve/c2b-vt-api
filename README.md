# C2B VT API

A FastAPI application for asset management.

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## Deployment with Docker

1. Build the Docker image:
   ```bash
   docker build -t c2b-vt-api .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 c2b-vt-api
   ```

## Deployment with Docker Compose

1. Run with Docker Compose:
   ```bash
   docker-compose up --build
   ```

## Deployment to Heroku

1. Install Heroku CLI and login.

2. Create a Heroku app:
   ```bash
   heroku create your-app-name
   ```

3. Push to Heroku:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   heroku git:remote -a your-app-name
   git push heroku main
   ```

## API Endpoint

- POST `/get-asset-id`: Accepts a list of items and returns asset codes based on Flow_code logic.

Example request:
```json
[{"Flow_code":"A","Main_asset_code":"15003997","Ordering_Client":"0001","Plant_code":"A","Asset_label":"A","quantity":1,"Inventory_Number":"T0000000030","WBS":"OPX/AA50476 .02.01","Supplier_code":9233,"Location_supplier":null,"Manufacturer":"COOPER","Location_supplier_Adress":"1010 Rue Ste Catherine Ouest","Postal_code":"H3B0H2","City":"Montreal","Country_Code":"CA","Supplier_name":"COOPER","Manufacturer_country":"FR"}]
```

Example response:
```json
[{"asset_code":"10000","sub_asset":"0"}]
```