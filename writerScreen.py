__author__ = 'frasiek'
from iwriter import iwriter


class writerScreen(iwriter):
    def __init__(self):
        self.messages = []

    def missingTable(self, message, missing_table, missing_fields):
        self.messages.append(message)

    def reduntantTable(self, message, redundant_table):
        self.messages.append(message)

    def missingField(self, message, table, missing_field, srcTableObj, descHasPk):
        self.messages.append(message)

    def redundantField(self, message, table, redundant_field):
        self.messages.append(message)

    def mismatchField(self, message, table, source_field, srcTableObj, descHasPk):
        self.messages.append(message)

    def getText(self):
        return str(self.messages)