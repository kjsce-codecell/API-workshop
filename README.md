<div align="center">

# API-workshop

[![made-with-python](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

</div>

Collection of all the APIs created by the team as part of the API workshop conducted by [KJSCE CodeCell](https://github.com/kjsce-codecell). The architecture and working of APIs was explained and the students were guided to create their own APIs by the end of the workshop.

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

### Contributing

Open to `enhancements` & `bug-fixes`

### Note

The project was made as a resource for the participants of the workshop.
