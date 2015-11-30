# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('track',legacy_name='main.Track',legacy_db='Chinook_Sqlite',pkey='trackid',caption_field='name',name_long='track',name_plural='track')
        tbl.column('trackid',dtype='I',name_long='trackid',indexed=True,legacy_name='TrackId',unique=True)
        tbl.column('name',size='0:200',name_long='name',legacy_name='Name')
        tbl.column('albumid',dtype='I',name_long='albumid',indexed=True,legacy_name='AlbumId',unique=False).relation('album.albumid',onDelete='raise')
        tbl.column('mediatypeid',dtype='I',name_long='mediatypeid',indexed=True,legacy_name='MediaTypeId',unique=False).relation('mediatype.mediatypeid',onDelete='raise')
        tbl.column('genreid',dtype='I',name_long='genreid',indexed=True,legacy_name='GenreId',unique=False).relation('genre.genreid',onDelete='raise')
        tbl.column('composer',size='0:220',name_long='composer',legacy_name='Composer')
        tbl.column('milliseconds',dtype='I',name_long='milliseconds',legacy_name='Milliseconds')
        tbl.column('bytes',dtype='I',name_long='bytes',legacy_name='Bytes')
        tbl.column('unitprice',dtype='N',size='10,2',name_long='unitprice',legacy_name='UnitPrice')

        tbl.aliasColumn('genre',relation_path='@genreid.name',name_long='Genre')
        tbl.aliasColumn('album',relation_path='@albumid.title',name_long='Album')
        tbl.aliasColumn('media',relation_path='@mediatypeid.name',name_long='Media')
