#!/usr/bin/env python3
from kafka import KafkaConsumer
import configparser


def get_config(configfile='config.ini', section="DEFAULT"):
    config = configparser.ConfigParser()
    config.read(configfile)
    return config[section]


def main():
    print("*** start ***")

    config = get_config()
    consumer = KafkaConsumer(config['topic'],
                             bootstrap_servers=config['bootstrap_servers'],
                             client_id='some-consumer',
                             sasl_mechanism='PLAIN',
                             security_protocol='SASL_SSL',
                             sasl_plain_username=config['sasl_plain_username'],
                             sasl_plain_password=config['sasl_plain_password'])

    for message in consumer:
        print(message.value)

    print("=== end ===")


if __name__ == '__main__':
    main()
