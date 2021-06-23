# oic-person-name

A simple project to demonstrate oic development, testing etc.

## Requirements:

- create a simple table "person_name" and a pl/sql procedure that interacts with it.
- create a REST API to interact with this table
- write test cases to help with test driven development

## REST API Specifications:

- endpoint `personName` should take one parameter `sisid`. (e.g. GET https://...../personName/{sisid})
- GET request will only need the `{sisid}` parameter and no body and it should return
  a flat json object representing one record in that table for the given `sisid`:
  ```json
    GET https://...../personName/999111222
    {
        "sisid": "999111222",
        "surname": "Tester",
        "firstname": "Rose"
    }
  ```
- POST request should not have any parameter in the url. Instead the request payload should have `sisid`, `surname` and `firstname` as json:
  ```json
      POST https://...../personName
      {
          "sisid": 999111222,
          "surname": "Tester",
          "firstname": "Rose"
      }
  ```

## Workflow:

- write pytest script for the two requests specified above
- all tests would fail to begin with
- develop the database table and procedure or deploy them from this repo in `sql` directory (see instructions below)
- develop the integration or deploy it from this repo in `integration` directory
- update the host and basepath for the integration flow in config.ini, there is a sample file you can copy to get started
- run pytest to make sure integrations are working as expected

## deploy sql

```bash
git clone git@github.com:firozkabir/oic-person-name.git
cd sql
sqlplus username/password@database @deploy-objects.sql
```

## deploy integration artifact

- log into your OIC instance and import the par artifact found in integration directory
- configure the connection details and activate the integration flow

## install and configure and run test script

```bash
git clone git@github.com:firozkabir/oic-person-name.git
cd oic-person-name/pytest
virtualenv -p /usr/bin/python3 venv
pip3 install -r requirements.txt
cp config.ini.sample config.ini  # update parameters in config.ini
source venv/bin/activate
pytest -sv tests.py --html report.html
```
