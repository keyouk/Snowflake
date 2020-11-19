# Sample program to check CLIENT_SESSION_KEEP_ALIVE Parameter values

import snowflake.connector
import os

# Code to add Logging
import logging
logging.basicConfig(
    filename='/tmp/snowflake_python_connector.log',
    level=logging.INFO)


# Set your account and login information (replace the variables with
# the necessary values). Note that ACCOUNT might also require the
# region and cloud platform where your account is located, in the form of
# '<your_account_name>.<region_id>.<cloud_platform>' (e.g. 'xy12345.east-us-2.azure')
ACCOUNT = ''
USER = ''
PASSWORD = ''


# Connection with Keep Alive Enabled
con = snowflake.connector.connect(
  user=USER,
  password=PASSWORD,
  account=ACCOUNT,
  client_session_keep_alive=True # Toggle this parameter on and off
)


# KEEP ALIVE Parameter check using connection with keep_alive enabled/disabled
cur = con.cursor()
try:
    cur.execute("SHOW PARAMETERS LIKE '%CLIENT_SESSION_KEEP_ALIVE%'")
    for cursor in cur:
            print(cursor)
finally:
    cur.close()



# Closing the connection
con.close()