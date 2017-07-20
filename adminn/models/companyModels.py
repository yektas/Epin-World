from django.db import connection

from utility.cursorutil import dictfetchall


class CompanyEventClass():
    def __init__(self, request_object):
        self.request_object = request_object
        self.cursor = connection.cursor()

    def __del__(self):
        self.cursor.close()

    def create_company(self, cname):

        if self.check_company(cname) is False:
            self.cursor.execute("INSERT INTO company (company_name) VALUES ( '{}' )".format(str(cname)))
            self.cursor.execute("COMMIT;")
            return True
        else:
            return False

    def check_company(self, cname):

        self.cursor.execute("SELECT company_name FROM company WHERE company_name='{}' ".format(cname))
        company = dictfetchall(self.cursor)
        if len(company) <= 0:
            return False
        else:
            return True

    def list_company(self):

        self.cursor.execute("SELECT company_name FROM company ORDER BY created_date DESC ")
        company = dictfetchall(self.cursor)
        if len(company) <= 0:
            return False
        else:
            return company

    def delete_company(self, cname):

        if (self.check_company(cname)):
            try:
                self.cursor.execute("START TRANSACTION;")
                self.cursor.execute(
                    "delete from game where company_id = (select id from company where company_name = '{}')".format(
                        str(cname)))
                self.cursor.execute("delete from company where company_name = '{}' ".format(str(cname)))
                self.cursor.execute("commit;")
                return True
            except:
                return False
        else:
            return False
