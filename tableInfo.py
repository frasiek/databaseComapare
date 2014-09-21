__author__ = 'frasiek'
from fieldInfo import fieldInfo

class tableInfo(object):
    def __init__(self, table_name):
        self.fields = {}
        self.table_name = table_name

    def add_field_info(self, info):
        self.fields[info['COLUMN_NAME']] = fieldInfo(info, self)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        ret = self.table_name+": \n"
        for field in self.fields:
            ret += "\t"+str(self.fields[field])+"\n"
        return ret

    def getPkSql(self, prefixIfHasPk = ''):
        pkFields = []
        for field in self.fields:
            if "PRI" in self.fields[field].info['COLUMN_KEY']:
                pkFields.append("`"+self.fields[field].info['COLUMN_NAME']+"`")

        if len(pkFields) > 0:
            return prefixIfHasPk+" ADD PRIMARY KEY ("+(", ".join(pkFields))+")"
        return ""

    def hasPk(self):
        pkFields = []
        for field in self.fields:
            if "PRI" in self.fields[field].info['COLUMN_KEY']:
                pkFields.append("`"+self.fields[field].info['COLUMN_NAME']+"`")

        return len(pkFields) > 0