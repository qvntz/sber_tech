from dotenv import load_dotenv
import os
import boto3

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY', 1)
ACCESS_KEY = os.getenv('ACCESS_KEY', 1)
ENDPOINT_URL = os.getenv('ENDPOINT_URL', 1)

session = boto3.session.Session()


client = session.client(
    service_name="s3",
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    use_ssl=False,
    verify=False,
)


response = client.put_object(
    Body='hello.txt',
    Bucket='hackathon-ecs-38',
    Key='hash'
)
