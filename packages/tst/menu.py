# encoding: utf-8
class Menu(object):
    def config(self,root,**kwargs):
        auto = root.branch(u"auto")
        auto.thpage(u"!!Tbl Test", table="tst.tbltest")
