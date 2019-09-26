import requests

url = 'https://represent.opennorth.ca/'


def get_name_wards():
    ottawa_wards_request = requests.get(
        f'{url}/boundaries/?sets=ottawa-wards')
    ottawa_wards_json = ottawa_wards_request.json()
    # print(ottawa_wards_json['objects'])

    for x in ottawa_wards_json['objects']:
        print(x['name'])


def get_elections():
    ottawa_elections_request = requests.get(
        f'{url}/elections/')
    ottawa_elections_json = ottawa_elections_request.json()
    # print(ottawa_elections_json['objects'])

    for y in ottawa_elections_json['objects']:
        print(y['election_date'])


get_name_wards()
get_elections()
