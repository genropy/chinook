#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('employeeid')
        r.fieldcell('lastname')
        r.fieldcell('firstname')
        r.fieldcell('title')
        r.fieldcell('reportsto')
        r.fieldcell('birthdate')
        r.fieldcell('hiredate')
        r.fieldcell('address')
        r.fieldcell('city')
        r.fieldcell('state')
        r.fieldcell('country')
        r.fieldcell('postalcode')
        r.fieldcell('phone')
        r.fieldcell('fax')
        r.fieldcell('email')

    def th_order(self):
        return 'employeeid'

    def th_query(self):
        return dict(column='lastname', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('employeeid')
        fb.field('lastname')
        fb.field('firstname')
        fb.field('title')
        fb.field('reportsto')
        fb.field('birthdate')
        fb.field('hiredate')
        fb.field('address')
        fb.field('city')
        fb.field('state')
        fb.field('country')
        fb.field('postalcode')
        fb.field('phone')
        fb.field('fax')
        fb.field('email')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
