#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='cnk package',sqlschema='cnk',sqlprefix=True,
                    name_short='Cnk', name_long='Chinook music db', name_full='Cnk')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
