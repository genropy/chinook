#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('invoiceid')
        r.fieldcell('customerid')
        r.fieldcell('invoicedate')
        r.fieldcell('billingaddress')
        r.fieldcell('billingcity')
        r.fieldcell('billingstate')
        r.fieldcell('billingcountry')
        r.fieldcell('billingpostalcode')
        r.fieldcell('total')

    def th_order(self):
        return 'invoiceid'

    def th_query(self):
        return dict(column='billingaddress', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('invoiceid')
        fb.field('customerid')
        fb.field('invoicedate')
        fb.field('billingaddress')
        fb.field('billingcity')
        fb.field('billingstate')
        fb.field('billingcountry')
        fb.field('billingpostalcode')
        fb.field('total')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
