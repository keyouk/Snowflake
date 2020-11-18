#
# Snowflake Connector for Python Sample Program
#
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


# Connecting to Snowflake
con = snowflake.connector.connect(
  user=USER,
  password=PASSWORD,
  account=ACCOUNT,
)


# Creating a database, schema, and warehouse if none exists
con.cursor().execute("Select 1")


# Closing the connection
con.close()