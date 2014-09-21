__author__ = 'frasiek'


class comparator(object):
    def compare(self, srcInfo, descInfo):
        results = []
        for src_table in srcInfo:
            if src_table not in descInfo:
                results.append('Table `'+src_table+'` not present in target DB')
                continue

            self.compare_fields(srcInfo[src_table].fields, descInfo[src_table].fields, results, src_table)

        for desc_table in descInfo:
            if desc_table not in srcInfo:
                results.append('Table `'+desc_table+'` not present in source DB')

        return results

    def compare_fields(self, srcFields, descFields, results, table):
        for field in srcFields:
            if field not in descFields:
                results.append('Table `'+table+'` field `'+field+'` not present in target DB')

            srcFields[field].compareWith(descFields[field], results, table)

        for field in descFields:
            if field not in srcFields:
                results.append('Table `'+table+'` field `'+field+'` not present in source DB')
