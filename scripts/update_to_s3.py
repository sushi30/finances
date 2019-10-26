import os

import boto3
import click


@click.command
@click.argument("bucket")
@click.argument("file")
def upload_to_s3(bucket, file):
    boto3.resource("s3").Object(bucket, file).upload_file(file)


if __name__ == "__main__":
    upload_to_s3()
