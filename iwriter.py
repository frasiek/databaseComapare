__author__ = 'frasiek'


class iwriter(object):
    def missingTable(self, message, missing_table, missing_fields):
        pass

    def reduntantTable(self, message, redundant_table):
        pass

    def missingField(self, message, table, missing_field, srcTableObj, descHasPk):
        pass

    def redundantField(self, message, table, redundant_field):
        pass

    def mismatchField(self, message, table, source_field, srcTableObj, descHasPk):
        pass

    def getText(self):
        pass