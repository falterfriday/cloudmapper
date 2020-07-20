import urllib
import os
import json
import logging


def query_aws(account, query, region=None):
    if not region:
        file_name = "account-data/{}/{}.json".format(account.name, query)
    else:
        if not isinstance(region, str):
            region = region.name
        file_name = "account-data/{}/{}/{}.json".format(account.name, region, query)
    if os.path.isfile(file_name):
        return json.load(open(file_name))
    else:
        return {}


def get_parameter_file(region, service, function, parameter_value):
    file_name = "account-data/{}/{}/{}/{}".format(
        region.account.name,
        region.name,
        "{}-{}".format(service, function),
        urllib.parse.quote_plus(parameter_value),
    )

    print("FILE_NAME: " + file_name)

    file_exists = os.path.isfile(file_name)
    print("FILE_EXISTS: " + str(file_exists))

    file_size = os.path.getsize(file_name)
    print("FILE_SIZE: " + str(file_size))

    if not os.path.isfile(file_name):
        return None
    if os.path.getsize(file_name) <= 4:
        return None

    # Load the json data from the file
    return json.load(open(file_name))
