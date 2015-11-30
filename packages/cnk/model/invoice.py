# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('invoice',legacy_name='main.Invoice',legacy_db='Chinook_Sqlite',pkey='invoiceid',caption_field='billingaddress',name_long='invoice',name_plural='invoice')
        tbl.column('invoiceid',dtype='I',name_long='invoiceid',indexed=True,legacy_name='InvoiceId',unique=True)
        tbl.column('customerid',dtype='I',name_long='customerid',indexed=True,legacy_name='CustomerId',unique=False).relation('customer.customerid',onDelete='raise')
        tbl.column('invoicedate',dtype='DH',name_long='invoicedate',legacy_name='InvoiceDate')
        tbl.column('billingaddress',size='0:70',name_long='billingaddress',legacy_name='BillingAddress')
        tbl.column('billingcity',size='0:40',name_long='billingcity',legacy_name='BillingCity')
        tbl.column('billingstate',size='0:40',name_long='billingstate',legacy_name='BillingState')
        tbl.column('billingcountry',size='0:40',name_long='billingcountry',legacy_name='BillingCountry')
        tbl.column('billingpostalcode',size='0:10',name_long='billingpostalcode',legacy_name='BillingPostalCode')
        tbl.column('total',dtype='N',size='10,2',name_long='total',legacy_name='Total')
