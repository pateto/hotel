
from __future__ import division, print_function, unicode_literals
# coding=utf-8
from django.contrib import admin
from django.contrib.admin.views.main import ChangeList


class ChangeListTotals(ChangeList):
    def get_results(self, *args, **kwargs):
        super(ChangeListTotals, self).get_results(*args, **kwargs)
        if hasattr(self.model_admin, 'list_totals'):
            self.aggregations = []
            list_totals = dict(self.model_admin.list_totals)
            for field in self.list_display:
                if field in list_totals:

                    # Change the value according to the list_display
                    value = 'price'

                    # Transform to str                       
                    sum_field = self.result_list.aggregate(agg=list_totals[field](value))['agg']
                    try:
                        sum_field_str = f'{sum_field:,}'.replace(',', '.')
                    except:
                        sum_field_str = sum_field

                    self.aggregations.append(sum_field_str)
                else:
                    self.aggregations.append('')


class ModelAdminTotals(admin.ModelAdmin):
    change_list_template = 'admin_totals/change_list_totals.html'

    def get_changelist(self, request, **kwargs):
        return ChangeListTotals
