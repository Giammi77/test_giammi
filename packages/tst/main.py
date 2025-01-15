#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='tst package',sqlschema='tst',sqlprefix=True,
                    name_short='Tst', name_long='Tst', name_full='Tst')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
