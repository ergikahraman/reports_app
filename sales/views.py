
from re import template
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Sale
from .forms import SalesSearchForms
import pandas as pd


# Create your views here.

def home_view(request):
    sales_df = None
    form = SalesSearchForms(request.POST or None)

    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        print(date_from, date_to, chart_type)

        qs = Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from) # lte: ilgili tarihten küçük
        #qs = Sale.objects.filter(created__date=(date_from, date_to))

        if len(qs)> 0:
            sales_df = pd.DataFrame(qs.values())

            sales_df =sales_df.to_html()
            print(sales_df)
        else:
            print('no data')

    #obj = Sale.objects.get(id=1)
    #print(qs)
    #print(obj)
    # print(qs.values())
    # print (qs.values_list())
    # print('####')

        
        

    # df2 = pd.DataFrame(qs.values_list())
    # print(df1)
    
    context = {
        
        'form': form,
        'sales_df': sales_df,
    }

    return render (request, 'sales/home.html', context) # (request, 'sales/home.html', {'h': hello}) bu kısımda {'x':...} '' arasına yazdığımız ifadeyi main.html içerisinde {{'x'}} şeklinde yazdığımızda web sitesinde yayınlayabiliyoruz.

class SaleListView (ListView):
    model = Sale
    template_name = 'sales/main.html' # eşittir işaretine dikkat
    # context_object_name = 'qs'( burada qs isimli context oluşturup main.html içerisindeki for dögüsüne yazıyoruz. (liste mantığı)) fakat bunun yerine main içerisinde object_list kavramını kullandık daha basit

class SaleDetailView (DetailView):
    model = Sale
    template_name = "sales/detail.html"










'''

eğer class değilde fonksiyon mantığıyla list ve detail işlemlerini gerçekleştirirsek def yapısı aşağıdaki gibi olmalı

def sale_list_view(request):
    qs = Sale.object.all()
    return render (request, 'sales/main.html', {'qs':qs})

def sale_detail_view (request, **kwargs):
    pk = kwargs.get('pk')
    obj = Sale.object.get(pk=pk)
    # or
    # obj = get_object_or_404(Sale, pk=pk)
    return render( request, 'sales/detail.html', {'object':obj})



eğer class değilde fonksiyon mantığıyla list ve detail işlemlerini gerçekleştirirsek url yapısı aşağıdaki gibi olmalı

in the urls:
path('sales/', sale_list_view, name='list'),
path('sales/<pk>/', sale_detail_view, name='detail'),


'''



