from django.shortcuts import render

# Create your views here.

def index(request):
    datas = {

    }
    return render(request, 'index.html', datas)

def blog(request):
    datas = {

    }
    return render(request, 'blog.html', datas) 

def blog_details(request):
    datas = {

    }
    return render(request, 'blog-details.html', datas)

def about_us(request):
    datas = {

    }
    return render(request, 'about-us.html', datas)    

def contact(request):
    datas = {

    }
    return render(request, 'contact.html', datas)

def main(request):
    datas = {

    }
    return render(request, 'main.html', datas)    

def speaker(request):
    datas = {

    }
    return render(request, 'speaker.html', datas)

def schedule(request):
    datas = {

    }
    return render(request, 'schedule.html', datas)                   