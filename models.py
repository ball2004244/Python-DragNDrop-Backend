from pydantic import BaseModel
from typing import Dict

'''
This file define the request and response body for the API.
'''


class CodeRequest(BaseModel):
    filename: str
    code: Dict[str, str]


class CLIRequest(BaseModel):
    command: str
