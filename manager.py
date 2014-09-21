__author__ = 'frasiek'
from tableInfo import tableInfo


class manager(object):

    def fetchInfo(self, connection):
        db_name = connection.get_db_name()

        table_info_raw = connection.get_all("SELECT * FROM `COLUMNS` WHERE `TABLE_SCHEMA` = %(db_name)s",{'db_name': db_name})
        db_info = {}
        for field in table_info_raw:
            if field['TABLE_NAME'] not in db_info:
                db_info[field['TABLE_NAME']] = tableInfo(field['TABLE_NAME'])
            db_info[field['TABLE_NAME']].add_field_info(field)
        return db_info