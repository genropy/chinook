# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('genre',legacy_name='main.Genre',legacy_db='Chinook_Sqlite',pkey='genreid',caption_field='name',name_long='genre',name_plural='genre')
        tbl.column('genreid',dtype='I',name_long='genreid',indexed=True,legacy_name='GenreId',unique=True)
        tbl.column('name',size='0:120',name_long='name',legacy_name='Name')
