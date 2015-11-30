# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('employee',legacy_name='main.Employee',legacy_db='Chinook_Sqlite',pkey='employeeid',caption_field='lastname',name_long='employee',name_plural='employee')
        tbl.column('employeeid',dtype='I',name_long='employeeid',indexed=True,legacy_name='EmployeeId',unique=True)
        tbl.column('lastname',size='0:20',name_long='lastname',legacy_name='LastName')
        tbl.column('firstname',size='0:20',name_long='firstname',legacy_name='FirstName')
        tbl.column('title',size='0:30',name_long='title',legacy_name='Title')
        tbl.column('reportsto',dtype='I',name_long='reportsto',indexed=True,legacy_name='ReportsTo',unique=False).relation('employee.employeeid',onDelete='raise')
        tbl.column('birthdate',dtype='DH',name_long='birthdate',legacy_name='BirthDate')
        tbl.column('hiredate',dtype='DH',name_long='hiredate',legacy_name='HireDate')
        tbl.column('address',size='0:70',name_long='address',legacy_name='Address')
        tbl.column('city',size='0:40',name_long='city',legacy_name='City')
        tbl.column('state',size='0:40',name_long='state',legacy_name='State')
        tbl.column('country',size='0:40',name_long='country',legacy_name='Country')
        tbl.column('postalcode',size='0:10',name_long='postalcode',legacy_name='PostalCode')
        tbl.column('phone',size='0:24',name_long='phone',legacy_name='Phone')
        tbl.column('fax',size='0:24',name_long='fax',legacy_name='Fax')
        tbl.column('email',size='0:60',name_long='email',legacy_name='Email')
