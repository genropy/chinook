#!/usr/bin/python
# -*- coding: UTF-8 -*-

def config(root,application=None):
    cnk = root.branch('Chinook music db')
    cnk.thpage('album',table='cnk.album')
    cnk.thpage('artist',table='cnk.artist')
    cnk.thpage('customer',table='cnk.customer')
    cnk.thpage('employee',table='cnk.employee')
    cnk.thpage('genre',table='cnk.genre')
    cnk.thpage('invoice',table='cnk.invoice')
    cnk.thpage('invoiceline',table='cnk.invoiceline')
    cnk.thpage('mediatype',table='cnk.mediatype')
    cnk.thpage('playlist',table='cnk.playlist')
    cnk.thpage('playlisttrack',table='cnk.playlisttrack')
    cnk.thpage('track',table='cnk.track')
