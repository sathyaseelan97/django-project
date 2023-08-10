from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'django_page','number':100}
    return render(request,'basic_app/index.html',context=context_dict)

def other(request):
    num = {'test_list':[1,2,3,4]}
    return render(request,'basic_app/other.html',context=num)

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')