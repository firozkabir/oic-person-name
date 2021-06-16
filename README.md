# oic-person-name

A simple project to demonstrate oic development, testing etc.

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
pip3 instasll -r requirements.txt
cp config.ini.sample config.ini  # update parameters in config.ini
source venv/bin/activate
pytest -sv tests.py --html report.html
```
