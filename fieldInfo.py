__author__ = 'frasiek'


class fieldInfo(object):
    def __init__(self, info, parentTableObj):
        self.info = self.filter(info)
        self.parentTableObj = parentTableObj

    def filter(self, info):
        miningful = {}
        for name in info:
            if name in ['COLUMN_NAME', 'COLUMN_DEFAULT', 'IS_NULLABLE', 'COLUMN_TYPE',
                        'COLLATION_NAME', 'COLUMN_KEY', 'EXTRA']:
                miningful[name] = info[name]
        return miningful

    def compareWith(self, destInfo, results, table, descHasPk):
        for spec in self.info:
            if self.info[spec] != destInfo.info[spec]:
                results.mismatchField(
                    'Table `' + table + '` field `' + self.info['COLUMN_NAME'] + '` different in target DB [' +
                    self.info[spec] + ' != ' + destInfo.info[spec] + ']', table, self, self.parentTableObj, descHasPk)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.info['COLUMN_NAME'] + " [" + self.info['COLUMN_TYPE'] + "]"