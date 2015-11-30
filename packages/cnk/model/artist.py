# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('artist',legacy_name='main.Artist',legacy_db='Chinook_Sqlite',pkey='artistid',caption_field='name',name_long='artist',name_plural='artist')
        tbl.column('artistid',dtype='I',name_long='artistid',indexed=True,legacy_name='ArtistId',unique=True)
        tbl.column('name',size='0:120',name_long='name',legacy_name='Name')
