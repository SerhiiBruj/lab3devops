
import json
import boto3
import os

# Підключення до S3
s3 = boto3.client(
    "s3",
    region_name="us-east-1",
    endpoint_url=os.environ.get("AWS_ENDPOINT_URL_S3")
)


def handler(event, context):
    # Отримуємо назву S3 bucket
    bucket = os.environ["BUCKET_NAME"]

    try:
        # Читаємо файл із S3
        response = s3.get_object(
            Bucket=bucket,
            Key="items.json"
        )

        # Перетворюємо JSON на Python-об'єкт
        data = json.loads(response["Body"].read())

        # Повертаємо HTTP-відповідь
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(data)
        }

    except Exception as error:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "error": str(error)
            })
        }
