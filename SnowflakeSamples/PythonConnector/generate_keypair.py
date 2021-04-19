from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dsa, rsa
from Cryptodome.PublicKey import RSA
import getpass
import snowflake.connector
import sys


# Please fill in these values in all caps
# After filling in these values, run $ Python3 python_jwt.py


ACCOUNT_NAME = input("Snowflake Account Name: ")
USERNAME = input("Snowflake Username (Must be AccountAdmin): ")
PASSWORD = getpass.getpass('Snowflake Password: ')



print("1. Generating Private and Public key using Python")
key = RSA.generate(2048)


pv_key = key.exportKey()
with open ("private.pem", "w") as prv_file:
    print("{}".format(pv_key.decode()), file=prv_file)


pb_key = key.publickey().exportKey()
with open ("public.pem", "w") as pub_file:
    print("{}".format(pb_key.decode()), file=pub_file)


print("COMPLETE: Private and Public keys created \n \n" )


print("2. Stripping Headers and New lines from PUBLIC KEY PEM File")
public_key_string = pb_key.decode()
stripped_public_key = ''.join(public_key_string.split('\n')[1:-1])

print(stripped_public_key)
print("\n \n")



#Connect to Snowflake to alter user to add key-pair
print("3. Connecting to Snowflake to add keypair to user")
WAREHOUSE = input("WAREHOUSE to use: ")
ctx = snowflake.connector.connect(
    user=USERNAME,
    password=PASSWORD,
    account=ACCOUNT_NAME,
    warehouse=WAREHOUSE,
    role='accountadmin',
)


cur = ctx.cursor()
try:
    cur.execute("ALTER USER {} SET rsa_public_key='{}'".format(USERNAME, stripped_public_key))
    cur.execute("desc user {}".format(USERNAME));
    cur.execute(
    	'''
		select "property", "value" from table(result_scan(last_query_id()))
  		where "property" = 'RSA_PUBLIC_KEY_FP';
  		'''
  		)
    
    for cursor in cur:
    	print("Created PUBLIC_KEY_FP")
    	print(cursor)


finally:
	print('Closing Current Connection and session. \n\n')
	cur.close()


print('4. Converting PEM Key to DER format')
with open("private.pem", "rb") as keyfile:
    # Load the PEM format key
    pemkey = serialization.load_pem_private_key(
        keyfile.read(),
        None,
        default_backend()
    )
    # Serialize it to DER format


DER_key = pemkey.private_bytes(
    serialization.Encoding.DER,
    serialization.PrivateFormat.TraditionalOpenSSL,
    serialization.NoEncryption()
)
print('COMPLETE: Coverted PEM Key to DER Format (Which Snowflake needs for connection) \n \n')


print("5. Connecting using Private key in DER Format")
ctx = snowflake.connector.connect(
    user=USERNAME,
    account=ACCOUNT_NAME,
    private_key=DER_key,
    warehouse=WAREHOUSE,
    role='accountadmin',
)

cur = ctx.cursor()
try:
    cur.execute("Select 1")
    for cursor in cur:
    	print(cursor)
    	print("CONNECTION WITH KEYPAIR SUCCESSFUL CONGRATS!!!!!! \n\n")

finally:
	cur.close()