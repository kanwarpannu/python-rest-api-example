# python-rest-api-example

The code needs Python 3.11  
To run the code do following steps:  

1. Create env on mac:  
`python3.11 -m venv .venv`  

2. Activate env on mac:
`source .venv/bin/activate`

3. Install dependencies using following:
`pip install -r requirements.txt`

4. Start unicorn webserver to expose rest endpoint using:  
`uvicorn main:app --reload`

5. Now you can hit get endpoint `/` from local browser using url:  
`localhost:8000`