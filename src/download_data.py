import dropbox
from os import getenv
from dotenv import load_dotenv
from fastapi import APIRouter
from base64 import b64decode


load_dotenv()
router = APIRouter(
    prefix="/download",
    tags=["download"],
    responses={404: {"description": "Not found"}},
)


@router.get("/get_data/{key}")
def get_data(key: str):
    '''Retrieves a file from the Dropbox account with a key provided by the user. It begins by loading the Dropbox
    API and setting up the FastAPI application. It then uses the b64decode() method to convert the file from base64
    encoding. The file is then downloaded from the Dropbox account and written to a file with the key provided
    by the user.'''

    dbx = dropbox.Dropbox(getenv('DROPBOX_TOKEN'))
    _, res = dbx.files_download("/" + key)
    file = b64decode(res.content)
    with open(key, 'wb') as f:
        f.write(file)
    return f"filename:{key} successfully downloaded"