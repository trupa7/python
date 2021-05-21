import boto3
import ast
import json
from dynamodb_json import json_util as json

dynamodb_client = boto3.client(
    'dynamodb',
    region_name="us-east-2",
    aws_access_key_id="",
    aws_secret_access_key=""
)

TABLE_NAME = 'test'


def query_test_table(column_name,search_key):
    response = dynamodb_client.query(
        TableName="test",
        IndexName= column_name+"-index",
        KeyConditionExpression = column_name+"= :s",
        ExpressionAttributeValues= {
                                       ":s": {"S":search_key }
                                   }
    )

    return response['Items']


if __name__ == '__main__':
    # column_name = "service"
    # search_key = "s3"

    # column_name = "dnsname"
    # search_key = "mydata:aws"


    column_name = "type"
    search_key = "storage"
    results = query_test_table(column_name,search_key)
    for result in results:
        dynamodb_json = json.loads(result)
        print(dynamodb_json)
