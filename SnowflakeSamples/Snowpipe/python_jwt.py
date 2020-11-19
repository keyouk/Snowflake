import datetime
import json
import urllib
import threading
import jwt
import requests
from logging import getLogger
import time
import datetime
import os
from datetime import timedelta
from requests import HTTPError
import logging
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend
from jwt.algorithms import RSAAlgorithm
from cryptography.hazmat.primitives.asymmetric import dsa, rsa


# Please fill in these values in all caps
# After filling in these values, run $ Python3 python_jwt.py
ACCOUNT_NAME = ''
USERNAME = ''
RSA_PUB_KEY_FP = ''



private_key = """

"""


payload = {
  'iss': '{}.{}.{}'.format(ACCOUNT_NAME, USERNAME, RSA_PUB_KEY_FP),
  'sub': '{}.{}'.format(ACCOUNT_NAME, USERNAME),
  'iat': datetime.datetime.utcnow(),
  'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=360000) 
}

encoded_jwt_token = jwt.encode(
   payload,
   private_key,
   'RS256')

print(encoded_jwt_token)
