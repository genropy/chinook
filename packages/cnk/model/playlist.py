# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('playlist',legacy_name='main.Playlist',legacy_db='Chinook_Sqlite',pkey='playlistid',caption_field='name',name_long='playlist',name_plural='playlist')
        tbl.column('playlistid',dtype='I',name_long='playlistid',indexed=True,legacy_name='PlaylistId',unique=True)
        tbl.column('name',size='0:120',name_long='name',legacy_name='Name')
