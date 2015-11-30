# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('playlisttrack',legacy_name='main.PlaylistTrack',legacy_db='Chinook_Sqlite',pkey='_multikey',caption_field='_multikey',name_long='playlisttrack',name_plural='playlisttrack')
        tbl.column('playlistid',dtype='I',name_long='playlistid',legacy_name='PlaylistId').relation('playlist.playlistid',onDelete='raise')
        tbl.column('trackid',dtype='I',name_long='trackid',indexed=True,legacy_name='TrackId',unique=False).relation('track.trackid',onDelete='raise')
        tbl.column('_multikey',name_long='_multikey')
