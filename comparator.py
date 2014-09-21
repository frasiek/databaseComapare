__author__ = 'frasiek'
from iwriter import iwriter

class comparator(object):
    def __init__(self, writer=iwriter()):
        self.writer = writer

    def compare(self, srcInfo, descInfo):
        for src_table in srcInfo:
            if src_table not in descInfo:
                self.writer.missingTable('Table `'+src_table+'` not present in target DB', src_table, srcInfo[src_table].fields)
                continue

            self.compare_fields(srcInfo[src_table].fields, descInfo[src_table].fields, self.writer, src_table, srcInfo[src_table], descInfo[src_table].hasPk())

        for desc_table in descInfo:
            if desc_table not in srcInfo:
                self.writer.reduntantTable('Table `'+desc_table+'` not present in source DB', desc_table)

        return self.writer

    def compare_fields(self, srcFields, descFields, results, table, srcTableObj, descHasPk):
        for field in srcFields:
            if field not in descFields:
                self.writer.missingField('Table `'+table+'` field `'+field+'` not present in target DB', table, srcFields[field], srcTableObj, descHasPk)
            else:
                srcFields[field].compareWith(descFields[field], results, table, descHasPk)

        for field in descFields:
            if field not in srcFields:
                self.writer.redundantField('Table `'+table+'` field `'+field+'` not present in source DB', table, field)
