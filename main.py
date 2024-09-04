from fastapi import FastAPI

app= FastAPI()

##definir un path
@app.get("/") #route directory, cuando alguien visite esto la funcion de abajo se llama 
def root():
    return {"Hello":"World"}
