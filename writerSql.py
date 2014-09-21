__author__ = 'frasiek'
from iwriter import iwriter


class writerSql(iwriter):
    def __init__(self):
        self.queries = []
        self.mismatchFieldInstances = []

    def missingTable(self, message, missing_table, missing_fields):
        pkFields = []
        query = "CREATE TABLE `"+missing_table+"` ("
        for missing_field in missing_fields:
            if "PRI" in missing_fields[missing_field].info['COLUMN_KEY']:
                pkFields.append("`"+missing_fields[missing_field].info['COLUMN_NAME']+"`")
            nullV = " NOT NULL "
            if missing_fields[missing_field].info['IS_NULLABLE'].lower() == 'yes':
                nullV = " NULL "

            defaultV = ""
            if missing_fields[missing_field].info['COLUMN_DEFAULT'] is not None:
                defaultV = " DEFAULT '"+missing_fields[missing_field].info['COLUMN_DEFAULT']+"' "

            query += "`" + missing_fields[missing_field].info['COLUMN_NAME'] + "` "
            query += missing_fields[missing_field].info['COLUMN_TYPE'] + " "
            query += nullV + defaultV + " "+missing_field.info['EXTRA'] + ", "
        query = query[0:-2]
        if len(pkFields) > 0:
            query += "PRIMARY KEY ("+(", ".join(pkFields))+")"
        query += ")"
        self.queries.append(query)

    def reduntantTable(self, message, redundant_table):
        self.queries.append("DROP TABLE `"+redundant_table+"`")

    def missingField(self, message, table, missing_field, tableInfo, descHasPk):
        nullV = " NOT NULL "
        if missing_field.info['IS_NULLABLE'].lower() == 'yes':
            nullV = " NULL "

        defaultV = ""
        if missing_field.info['COLUMN_DEFAULT'] is not None:
            defaultV = " DEFAULT '"+missing_field.info['COLUMN_DEFAULT']+"' "

        dropPk = ''
        if descHasPk:
            dropPk = " , DROP PRIMARY KEY "

        self.queries.append("ALTER TABLE `"+table+"` ADD COLUMN `" +
            missing_field.info['COLUMN_NAME']+"` " +
            missing_field.info['COLUMN_TYPE']+" " +
            nullV +
            defaultV+" "+missing_field.info['EXTRA'] +
            dropPk + tableInfo.getPkSql(", ")
            )

    def redundantField(self, message, table, redundant_field):
        self.queries.append("ALTER TABLE `"+table+"` DROP COLUMN `"+redundant_field+"`")

    def mismatchField(self, message, table, source_field, tableInfo, descHasPk):
        if table+"_"+source_field.info['COLUMN_NAME'] in self.mismatchFieldInstances:
            return

        self.mismatchFieldInstances.append(table+"_"+source_field.info['COLUMN_NAME'])

        nullV = " NOT NULL "
        if source_field.info['IS_NULLABLE'].lower() == 'yes':
            nullV = " NULL "

        defaultV = ""
        if source_field.info['COLUMN_DEFAULT'] is not None:
            defaultV = " DEFAULT '"+source_field.info['COLUMN_DEFAULT']+"' "

        dropPk = ''
        if descHasPk:
            dropPk = " , DROP PRIMARY KEY "

        self.queries.append("ALTER TABLE `"+table+"` CHANGE COLUMN "+
            "`"+source_field.info['COLUMN_NAME']+"` "+
            "`"+source_field.info['COLUMN_NAME']+"` "+
            source_field.info['COLUMN_TYPE']+" "+
            nullV+
            defaultV+" "+source_field.info['EXTRA']+
            dropPk + tableInfo.getPkSql(", ")
            )
    def getText(self):
        return str(self.queries)

    def runSql(self, connection):
        for query in self.queries:
            connection.execute(query)