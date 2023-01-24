import uvicorn
from fastapi import FastAPI
from routes.api import router

app = FastAPI(
    title="Test Api",
    description='''This is a code snippet to store and retrieve files from Dropbox using the Dropbox API and FastAPI.

The first function, store_data(), takes a file provided by the user and stores it in a Dropbox account. The function 
begins by loading the Dropbox API and setting up the FastAPI application. It then uses the b64encode() method to convert
 the user-provided file into base64 encoding. Using the Dropbox API, the file is uploaded to the Dropbox account with 
 a key provided by the user.

The second function, get_data(), retrieves a file from the Dropbox account with a key provided by the user. It begins 
by loading the Dropbox API and setting up the FastAPI application. It then uses the b64decode() method to convert the 
file from base64 encoding. The file is then downloaded from the Dropbox account and written to a file with the key 
provided by the user.

Both functions return a message to the user indicating that the file was stored or retrieved successfully.''',
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Nikita Nozhenko",
        "url": "http://example.com/contact/",
        "email": "nikitanozhenko@gmail.com",
    },
    )

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(
        "start_app:app",
        host='localhost',
        port=8000,
        reload=True
    )