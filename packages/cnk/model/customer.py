# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('customer',legacy_name='main.Customer',legacy_db='Chinook_Sqlite',pkey='customerid',caption_field='firstname',name_long='customer',name_plural='customer')
        tbl.column('customerid',dtype='I',name_long='customerid',indexed=True,legacy_name='CustomerId',unique=True)
        tbl.column('firstname',size='0:40',name_long='firstname',legacy_name='FirstName')
        tbl.column('lastname',size='0:20',name_long='lastname',legacy_name='LastName')
        tbl.column('company',size='0:80',name_long='company',legacy_name='Company')
        tbl.column('address',size='0:70',name_long='address',legacy_name='Address')
        tbl.column('city',size='0:40',name_long='city',legacy_name='City')
        tbl.column('state',size='0:40',name_long='state',legacy_name='State')
        tbl.column('country',size='0:40',name_long='country',legacy_name='Country')
        tbl.column('postalcode',size='0:10',name_long='postalcode',legacy_name='PostalCode')
        tbl.column('phone',size='0:24',name_long='phone',legacy_name='Phone')
        tbl.column('fax',size='0:24',name_long='fax',legacy_name='Fax')
        tbl.column('email',size='0:60',name_long='email',legacy_name='Email')
        tbl.column('supportrepid',dtype='I',name_long='supportrepid',indexed=True,legacy_name='SupportRepId',unique=False).relation('employee.employeeid',onDelete='raise')
