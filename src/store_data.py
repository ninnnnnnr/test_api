import dropbox
from os import getenv
from dotenv import load_dotenv
from fastapi import APIRouter
from fastapi import File
from base64 import b64encode


load_dotenv()
router = APIRouter(
    prefix="/store",
    tags=["store"],
    responses={404: {"description": "Not found"}},
)

@router.put("/store_data/{key}")
def store_data(key: str, data: bytes = File(...)):
    '''Takes a file provided by the user and stores it in a Dropbox account. The function begins by loading the
    Dropbox API and setting up the FastAPI application. It then uses the b64encode() method to convert the
    user-provided file into base64 encoding. Using the Dropbox API, the file is uploaded to the Dropbox account
    with a key provided by the user.'''

    dbx = dropbox.Dropbox(getenv('DROPBOX_TOKEN'))
    data = b64encode(data)
    dbx.files_upload(data, '/' + key)
    return {'message': 'Data stored successfully in Dropbox'}