import boto3
import pandas as pd
from io import BytesIO

def fetch_csv_from_s3(bucket, key, aws_access_key_id=None, aws_secret_access_key=None, region_name=None):
    """
    Fetch CSV from S3 and return as pandas DataFrame.
    """
    s3 = boto3.client('s3',
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key,
                      region_name=region_name)
    obj = s3.get_object(Bucket=bucket, Key=key)
    return pd.read_csv(BytesIO(obj['Body'].read()))
