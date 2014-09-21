__author__ = 'frasiek'
import pymysql
from db_exception import dbException


class dbConnection(object):
    def __init__(self, config):
        self.host = config['host']
        self.user = config['user']
        self.passwd = config['passwd']
        self.db_name = config['db_name']
        self.port = config['port']

        try:
            self.connection = pymysql.connect(host=self.host, port=int(self.port), user=self.user, passwd=self.passwd, db='INFORMATION_SCHEMA')
        except pymysql.err.OperationalError as e:
            print(str(e))
            raise dbException()

    def get_db_name(self):
        return self.db_name

    def get_all(self, query, query_dict = None):
        cur = self.connection.cursor()
        cur.execute(query,query_dict)
        raw_results = cur.fetchall()
        results = []
        for row in raw_results:
            tmp = {}
            i = 0
            for value in row:
                tmp[cur.description[i][0]] = value
                i += 1
            results.append(tmp)
        return results