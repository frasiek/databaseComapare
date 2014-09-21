__author__ = 'frasiek'


class fieldInfo(object):
    def __init__(self, info):
        self.info = self.filter(info)

    def filter(self, info):
        miningful = {}
        for name in info:
            if name in ['COLUMN_NAME', 'COLUMN_DEFAULT', 'IS_NULLABLE', 'DATA_TYPE', 'COLUMN_TYPE',
                        'COLLATION_NAME', 'COLUMN_KEY', 'EXTRA']:
                miningful[name] = info[name]
        return miningful

    def compareWith(self, destInfo, results, table):
        for spec in self.info:
            if self.info[spec] != destInfo.info[spec]:
                results.append('Table `'+table+'` field `'+self.info['COLUMN_NAME']+'` different in target DB ['+
                               self.info[spec]+' != '+destInfo.info[spec]+']')

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.info['COLUMN_NAME']+" ["+self.info['COLUMN_TYPE']+"]"