#!/usr/bin/env python3
import configparser
import requests
import json
from faker import Faker
import pytest
from random import randrange
from requests.models import HTTPBasicAuth


class PersonName:
    def __init__(self, sisid, surname, firstname):
        self.sisid = sisid
        self.surname = surname
        self.firstname = firstname

    def __eq__(self, other: object) -> bool:

        is_equal = False
        if (self.sisid == other.sisid) and (self.firstname == other.firstname) and (self.surname == other.surname):
            is_equal = True

        return is_equal


#global variables
faker = Faker()
pytest.person_name = PersonName(
    randrange(999), faker.last_name(), faker.first_name())


def get_config(configfile='config.ini', section="DEFAULT"):
    config = configparser.ConfigParser()
    config.read(configfile)
    return config[section]


def test_post_person_name():

    config = get_config()
    username = config['username']
    password = config['password']

    url = f"https://{config['host']}/{config['basepath']}/{pytest.person_name.sisid}"
    print(url)
    headers = {
        'Content-Type': 'application/json'
    }

    request_body = {
        'surname': pytest.person_name.surname,
        'firstname': pytest.person_name.firstname
    }

    response = requests.post(url, headers=headers,
                             data=json.dumps(request_body, indent=4),
                             auth=HTTPBasicAuth(
                                 config['username'], config['password'])
                             )
    assert response.status_code == 202


def test_get_person_name():

    config = get_config()
    username = config['username']
    password = config['password']

    url = f"https://{config['host']}/{config['basepath']}/{pytest.person_name.sisid}"

    response = requests.get(url,
                            auth=HTTPBasicAuth(
                                config['username'], config['password']))

    response_dict = response.json()
    assert response.status_code == 200
    response_person_name = PersonName(int(response_dict.get(
        'sisid')), response_dict.get('surname'), response_dict.get('firstname'))
    assert pytest.person_name == response_person_name
