# API-workshop
Collection of all the APIs created by the team as part of the API workshop

## Instructions:
1. Create a virtual environment
2. To install dependenices of ```requirements.txt```:

```
pip install -r requirements.txt
```
3. To run the flask server:

``` 
python3 app.py
```

Open http://localhost:5000/ to view details for using all the API endpoints implemented.

4. To view swagger documentation of APIs:
Open http://{your_url}/swagger

### Steps to add more APIs:

* Create a .py file as `/apis/<api_name>.py` 
* Configure the API routes in the script.(Refer `/apis/test.py` . Don't forget to add the `/docs` endpoint)
* Import the Flask Blueprint object in `/apis/__init__.py` 
* Import and register the blueprints in `app.py` 

## Resources:

