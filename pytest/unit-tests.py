#!/usr/bin/env python3
import configparser
import requests
import json
from faker import Faker
import pytest
from random import randrange
from requests.models import HTTPBasicAuth
import logging
import urllib
import time


class PersonName:
    def __init__(self, sisid, surname, firstname):
        self.sisid = sisid
        self.surname = surname
        self.firstname = firstname

    def __str__(self):
        return f"sisid: {self.sisid}, surname: {self.surname}, firstname: {self.firstname}"

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

    url = f"https://{config['host']}/{config['basepath']}"
    print(url)

    headers = {
        'Content-Type': 'application/json'
    }

    request_body = {
        'firstname': pytest.person_name.firstname,
        'surname': pytest.person_name.surname,
        'sisid': pytest.person_name.sisid


    }
    try:
        response = requests.post(url, headers=headers,
                                 data=json.dumps(request_body, indent=4),
                                 auth=HTTPBasicAuth(
                                     config['username'], config['password'])
                                 )

    except Exception as e:
        print(e)

    print(pytest.person_name.sisid)
    print(pytest.person_name.surname)
    print(pytest.person_name.firstname)
    assert response.status_code == 202


def test_run_procedure():

    config = get_config()
    username = config['username']
    password = config['password']

    url = f"https://{config['host']}/{ urllib.parse.quote( config['runpath'] ) }"

    response = requests.post(url,
                             auth=HTTPBasicAuth(
                                 config['username'], config['password'])
                             )

    assert response.status_code == 204


def test_get_person_name():
    print(' waiting 15 seconds for kafka scheduled run to complete')
    time.sleep(15)

    config = get_config()
    username = config['username']
    password = config['password']
    print(pytest.person_name.sisid)

    url = f"https://{config['host']}/{config['basepath']}/{pytest.person_name.sisid}"

    response = requests.get(url,
                            auth=HTTPBasicAuth(
                                config['username'], config['password']))

    response_dict = response.json()
    assert response.status_code == 200
    response_person_name = PersonName(response_dict.get(
        'sisid'), response_dict.get('surname'), response_dict.get('firstname'))

    print(response_person_name)
    #assert pytest.person_name == response_person_name
