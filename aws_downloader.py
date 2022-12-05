import boto3
import json
import urllib.request
# import iris
import pandas
import netCDF4
from netCDF4 import Dataset


sqs = boto3.client('sqs',region_name='eu-west-2', aws_access_key_id='', aws_secret_access_key='')

messages = sqs.receive_message(QueueUrl='https://sqs.eu-west-2.amazonaws.com/124406878548/MetOffice_AWS')


[message] = messages['Messages']


notification = json.loads(message['Body'])

print(notification)

s3_object = json.loads(notification['Message'])

# print(s3_object['key'])
# exit()

def download_data(sns_message):
	url = "https://s3.eu-west-2.amazonaws.com/" + sns_message['bucket'] + "/" + sns_message['key']
	urllib.request.urlretrieve(url, sns_message['key'])

a = download_data(s3_object)

# [data] = iris.load(s3_object['key'])
print(a)

# conda create -n iris -c conda-forge iris

#read nc file using netCDF4
ncfile = Dataset('./68c84185b78ea7f826a96c795741c398ec2dd1e3.nc')
varaibles = list(ncfile.variables.keys())

print(varaibles)