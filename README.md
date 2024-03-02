# Steps

## Frontend

Execute the following in "/front":
`npm run dev`

This will not start the backend, so any interactions attempted with the flask server will fail

## Backend

First, compile the frontend (execute in "/front"):
`npm run build`

Next, run the python server (execute in "/"):
`py main.py`

Re-run the npm build if you change the front end. 