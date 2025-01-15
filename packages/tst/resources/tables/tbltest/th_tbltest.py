#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method, metadata

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.cell('id', name='Id', width='143px')
        r.cell('numero_intero', name='Numero Intero', width='143px')
        r.cell('check', name='Check', width='81px')
        r.cell('validazione', calculated=True, format_isbutton='Validazione', format_buttonclass='buttonInGrid', text_align='center', width='8em',
                        _customGetter="""function(row) {
                                                if (row.check == true){
                                                    return '<span>&nbsp;</span>';
                                                }
                                                return
                                            }""",
                        format_onclick="""var row = this.widget.rowByIndex($1.rowIndex);
                                        genro.publish("valida",{pkey:row._pkey});""")

                        # TEST NON BUONO
                        # format_onclick="""var row = this.widget.rowByIndex($1.rowIndex);
                        #                 var idx = row._pkey;
                        #                 this.widget.sourceNode.setAttributeInDatasource('selectedId', row._pkey, null, row, true);
                        #                 var  s =this.widget.sourceNode.attr.selectedDataPath;
                        #                 genro.bp(true);
                        #                 var rowDataBag = new gnr.GnrBag(row);
                        #                 rowDataBag.popNode('_pkey');
                        #                 this.widget.sourceNode.setRelativeData('.currentSelectedPkeys',row._pkey);
                        #                 this.widget.sourceNode.setRelativeData('.selectionLength',1);
                        #                 this.widget.sourceNode.publish('onSelectedRow',{'idx':row,'selectedId':row._pkey,
                        #                 'grid':this,'selectedPkeys':null});
                        #                   genro.publish("valida",{pkey:row._pkey});""")

# CODICE PRESO DAL FRAMEWORK PER FARE UN TEST
# onSelectedRow:function(e,sourceNode,kw){
#         if(e.target.getAttribute('mv_main')=='false'){
#             var data = genro.getData(kw.sourcepath);
#             var r = e.target.parentElement.getAttribute('r');
#             if(r=='new'){
#                 return;
#             }
#             data.getNodeByValue('mv_main',true)._value.setItem('mv_main',false)
#             var newmain = data.getItem('#'+r);
#             newmain.setItem('mv_main',true);
#             genro.setData(kw.valuepath,newmain.getItem('mv_value'));
#             sourceNode.domNode.innerHTML = this.multivalueHtmlFromData(data);
#         }



#         1
#             if (this.sourceNode.attr.selectedDataPath) {
#             var selectedDataPath = null;
#             if (idx >= 0) {
#                 selectedDataPath = this.dataNodeByIndex(idx).getFullpath(null, true);
#             }
#             this.sourceNode.setAttributeInDatasource('selectedDataPath', selectedDataPath);
#         }
#         if (this.sourceNode.attr.selectedLabel) {
#             var selectedLabel = null;
#             if (idx >= 0) {
#                 var datanode = this.dataNodeByIndex(idx);
#                 selectedLabel = datanode ? this.dataNodeByIndex(idx).label : null;
#             }
#             this.sourceNode.setAttributeInDatasource('selectedLabel', selectedLabel);
#         }
#         var selattr = objectExtract(this.sourceNode.attr, 'selected_*', true);
#         var selectedPkeys = this.getSelectedPkeys();
#         var selectedRows = this.getSelectedRows();
#         var row = {};
#         var selectedId = null;
#         if(idx>=0){
#             row = this.rowByIndex(idx);
#             selectedId = this.rowIdentity(row);
#         }
#         for (var sel in selattr) {
#             this.sourceNode.setRelativeData(selattr[sel], arrayUniquify(selectedRows.map(r=>r[sel])).join(','));
#         }
#         if (this.sourceNode.attr.selectedIndex) {
#             this.sourceNode.setAttributeInDatasource('selectedIndex', ((idx < 0) ? null : idx));
#         }
#         if (this.sourceNode.attr.selectedPkeys) {
#             this.sourceNode.setAttributeInDatasource('selectedPkeys', selectedPkeys);
#         }
#         if (this.sourceNode.attr.selectedRowidx) {
#             this.sourceNode.setAttributeInDatasource('selectedRowidx', this.getSelectedRowidx().join(','));
#         }
#         if (this.sourceNode.attr.selectedNodes) {
#             var nodes = this.getSelectedNodes();
#             var selNodes;
#             if (nodes) {
#                 selNodes = new gnr.GnrBag();
#                 dojo.forEach(nodes,
#                     function(node) {
#                         selNodes.setItem(node.label, null, node.getAttr());
#                     }
#                 );
#             }
#             genro.setData(this.sourceNode.attrDatapath('selectedNodes'), 
#                             selNodes, {'count':selNodes?selNodes.len():0});
#         }
#         if(this.sourceNode.attr.selectedId) {
#             this.sourceNode.setAttributeInDatasource('selectedId', selectedId, null, row, true);
#         }
#         if(this.sourceNode.attr.selectedRowData){
#             var rowDataBag = new gnr.GnrBag(row);
#             rowDataBag.popNode('_pkey');
#             this.sourceNode.setAttributeInDatasource('selectedRowData', rowDataBag);
#         }
#         this.sourceNode.setRelativeData('.currentSelectedPkeys',selectedPkeys);
#         this.sourceNode.setRelativeData('.selectionLength',selectedPkeys?selectedPkeys.length:0);
#         this.sourceNode.publish('onSelectedRow',{'idx':idx,'selectedId':selectedId,
#                                                 'grid':this,'selectedPkeys':selectedPkeys});
#     },


    def th_order(self):
        return 'numero_intero'

    def th_query(self):
        return dict(column='numero_intero', op='contains', val='')


    def th_view(self, view):
        view.dataRpc(self.db.table('tst.tbltest').valida,
                    subscribe_valida=True)

        top_bar = view.top.bar.replaceSlots('advancedTools',
            'advancedTools,caricaRecord,dojo_connect')

        top_bar.caricaRecord.slotButton(label='Carica Record',
                                       ).dataRpc(self.db.table('tst.tbltest').creaRecord,
                                                                            _lockScreen=True,
                                                                            _onResult="""genro.publish("floating_message",{message:'Operazione completata', messageType:"message"});
                                                                                        """)
        top_bar.dojo_connect.slotButton('Dojo Connect',action="""console.log('Start dojo connect...');dojo.connect(dojo , 'publish', function(){console.log(arguments)})""")  
        
    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px',extendedQuery='*', virtualStore=False)#, grid_autoSelect=True)

    def th_top_upperbar(self, top):
        slotbar=top.slotToolbar('testo,*,sections@personali', childname='upper', _position='<bar')  # ,sections@sendingstatus,5
        slotbar.testo.div('15/01/25 Richiesta: nella vista della tbltest utilizzando il button nella row della griglia mi serve che oltre ad eseguire la rpc per la vidazione del record, venga automaticamente selezionata la row. Utilizzare il pulsante in alto a dx per generare i dati nella tabella se non presenti.')


    def th_sections_personali(self):
        return [dict(code='tutti', caption='Tutti'),
                dict(code='primi10', caption="Primi 10", condition="$numero_intero<10")]

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('numero_intero')
        fb.field('check')
        # fb.dataController("frm.form.goToRecord('2oa4Tz8_OAmuU5QBSM8hgQ');",frm=form, pippo='^pippo')


