from fastapi import FastAPI
app=FastAPI()
@app.get('/')
def hello():
    return{'message' : 'hello man chutiya hai kya sikh nahi aa paa rha kb se '}
