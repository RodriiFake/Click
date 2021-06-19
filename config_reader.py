# -*- coding: utf-8 -*-
import configparser
from os import path

CONFIG_FILE = "click.conf"


class ClickConfiguration:
    def __init__(self):
        self.__configuration_parse = configparser.ConfigParser()
        absolute_file_path = path.join(path.abspath(path.dirname(__file__)), CONFIG_FILE)
        self.__configuration_parse.read(absolute_file_path)

    @property
    def postgres_host(self):
        return self.__configuration_parse.get(section='postgres', option='host')

    @property
    def postgres_user(self):
        return self.__configuration_parse.get(section='postgres', option='user')

    @property
    def postgres_password(self):
        return self.__configuration_parse.get(section='postgres', option='password')

    @property
    def postgres_database(self):
        return self.__configuration_parse.get(section='postgres', option='database')

    @property
    def postgres_port(self):
        return self.__configuration_parse.get(section='postgres', option='port')
