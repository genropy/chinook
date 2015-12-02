# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('album',legacy_name='main.Album',legacy_db='Chinook_Sqlite',pkey='albumid',caption_field='title',name_long='album',name_plural='album')
        tbl.column('albumid',dtype='I',name_long='albumid',indexed=True,legacy_name='AlbumId',unique=True)
        tbl.column('title',size='0:160',name_long='title',legacy_name='Title')
        tbl.column('artistid',dtype='I',name_long='artistid',indexed=True,legacy_name='ArtistId',unique=False).relation('artist.artistid',onDelete='raise')
        tbl.aliasColumn('artist_name', relation_path='@artistid.name', name_long='Artist')
