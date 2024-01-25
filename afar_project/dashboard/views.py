from django.shortcuts import render
from django.http import request
import pandas as pd
import os

# Create your views here.
def dashboard(request):
    table_of_summary = dashboard_summary_of_assets(request)
    yearly_table=yearly_summary(request)
    context = {'table': table_of_summary,
               'yearly': yearly_table}
    return render(request, "Dashboard.html", context)

def dashboard_summary_of_assets(request):
    file_path ='csv_path/sample/asset_register.xlsx'
     # Replace with the actual file path
    df = pd.read_excel(file_path)
    list_primary=df[['Category','Expected life']].drop_duplicates()
    list_primary=list_primary.dropna()
    list_count=list_primary['Category']
    total =0
    table=pd.DataFrame(columns=['Category','Number'])
    for i in list_count:
        j = df[df['Category'] == i].shape[0]
        new_row = pd.DataFrame({'Category': [i], 'Number': [j]})
        table = pd.concat([table, new_row], ignore_index=True)
        total += j
    new_list=pd.merge(table,list_primary,on='Category',how='left')
    new_row = pd.DataFrame({'Category': "TOTAL " , 'Number': [total]})
    table = pd.concat([new_list, new_row], ignore_index=True)
    table=table.fillna(' ')
    table_of_summary=table.to_html(index=False)
    return table_of_summary


def yearly_summary(request):
    file_path ='csv_path/sample/asset_register.xlsx'
    df = pd.read_excel(file_path)
    list_primary=df['Financial Year']
    list_primary=list_primary.drop_duplicates().dropna()
    table=pd.DataFrame(columns=['Financial Year','Number'])
    total=0
    for i in list_primary:
        j = df[df['Financial Year'] == i].shape[0]
        new_row = pd.DataFrame({'Financial Year': [i], 'Number': [j]})
        table = pd.concat([table, new_row], ignore_index=True)
        total += j
    new_list=table
    last_line=pd.DataFrame([{"Financial Year":'TOTAL','Number': total}])
    table = pd.concat([new_list, last_line], ignore_index=True).to_html(index=False)
    return table