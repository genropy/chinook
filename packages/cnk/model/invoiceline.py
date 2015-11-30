# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('invoiceline',legacy_name='main.InvoiceLine',legacy_db='Chinook_Sqlite',pkey='invoicelineid',caption_field='invoicelineid',name_long='invoiceline',name_plural='invoiceline')
        tbl.column('invoicelineid',dtype='I',name_long='invoicelineid',indexed=True,legacy_name='InvoiceLineId',unique=True)
        tbl.column('invoiceid',dtype='I',name_long='invoiceid',indexed=True,legacy_name='InvoiceId',unique=False).relation('invoice.invoiceid',onDelete='raise')
        tbl.column('trackid',dtype='I',name_long='trackid',indexed=True,legacy_name='TrackId',unique=False).relation('track.trackid',onDelete='raise')
        tbl.column('unitprice',dtype='N',size='10,2',name_long='unitprice',legacy_name='UnitPrice')
        tbl.column('quantity',dtype='I',name_long='quantity',legacy_name='Quantity')
