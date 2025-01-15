# encoding: utf-8
from gnr.core.gnrdecorator import public_method

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('tbltest', pkey='id', name_long='Tbl Test', name_plural='Tbl Test',caption_field='numero_intero')
        self.sysFields(tbl)
        
        tbl.column('numero_intero', dtype='I', name_long='Numero Intero')
        tbl.column('check', dtype='B', name_long='Check')

    @public_method
    def creaRecord(self):
        for i in range(10000):
            nr=self.newrecord()
            nr['numero_intero']=i
            self.insert(nr)
            self.db.commit()

    @public_method
    def valida(self,pkey=None,*args,**kwargs):
        with self.recordToUpdate(id=pkey) as r:
            r['check']=True
        self.db.commit()
        site = getattr(self.db.application,'site',None)
        if site and site.currentPage:
            cp=site.currentPage
            # SOLO PER DEBUG
            cp.clientPublish('floating_message',message=pkey)
        


