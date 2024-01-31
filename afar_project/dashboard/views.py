from django.shortcuts import render
from django.http import request
import pandas as pd

# Create your views here.
def dashboard(request):
    return render(request,"Dashboard.html")

def dashboard_summary_of_assets(request):
    file_path = 'csv_path/sample/asset_register.xlsx'  # Replace with the actual file path
    df = pd.read_excel(file_path)
    list_primary=df['Category'].drop_duplicates()
    list_primary=list_primary.dropna()
    total =0
    table=pd.DataFrame(columns=['Category','Number'])
    for i in list_primary:
        j = df[df['Category'] == i].shape[0]
        new_row = pd.DataFrame({'Category': [i], 'Number': [j]})
        table = pd.concat([table, new_row], ignore_index=True)
        total += j
    new_row = pd.DataFrame({'Category': "Total Number of Assets is" , 'Number': [total]})
    table = pd.concat([table, new_row], ignore_index=True)
    table_of_summary=table
    context={"summary_table":table_of_summary}
    return render (request,"Dashboard.html",context)