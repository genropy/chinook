# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('mediatype',legacy_name='main.MediaType',legacy_db='Chinook_Sqlite',pkey='mediatypeid',caption_field='name',name_long='mediatype',name_plural='mediatype')
        tbl.column('mediatypeid',dtype='I',name_long='mediatypeid',indexed=True,legacy_name='MediaTypeId',unique=True)
        tbl.column('name',size='0:120',name_long='name',legacy_name='Name')
