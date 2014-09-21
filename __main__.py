"""
Comparing 2 mysql databases schema
"""
from db_connection import dbConnection
import configparser
from db_exception import dbException
import sys
from manager import manager
from comparator import comparator

class main(object):
    def __init__(self):
        #read config, create connections
        self.db_config = {}

        ini_parser = configparser.ConfigParser()
        ini_parser.read("config.ini", 'utf-8')
        for section in ini_parser.sections():
            self.db_config[section] = {}
            for option in ini_parser.options(section):
                self.db_config[section][option] = ini_parser.get(section,option)

        try:
            self.db_connection_from = dbConnection(self.db_config['source_db'])
            self.db_connection_to = dbConnection(self.db_config['target_db'])
        except dbException:
            sys.exit(1)

        self.informationParser = manager()

    def gatherInformation(self):
        self.db_info_from = self.informationParser.fetchInfo(self.db_connection_from)
        self.db_info_to = self.informationParser.fetchInfo(self.db_connection_to)

    def compare(self):
        comparator_obj = comparator()
        results = comparator_obj.compare(self.db_info_from, self.db_info_to)
        print(results)

if __name__ == "__main__":
    app = main()
    app.gatherInformation()
    app.compare()
