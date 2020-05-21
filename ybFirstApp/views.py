from django.shortcuts import render
from django.http import HttpResponse,Http404
# Create your views here.

def login_demo(request):
    if request.method == 'GET':
        return render(request,'login.html')

def home(request):
    return render(request, 'home.html')

def demo(request):
    return render(request, 'demo.html')

def sonpage(request):
    context = {
        "ads": ["selenium", "appnium", "requests"]
    }
    return render(request, 'sonpage.html', context)

def personalview(request):
    context = {
        "name": "CS小菜鸡",
        "n_name": "小菜鸡",
        "age": 20,
        "fancy": ["python", "django", "pytest"],
        "blog": {
            "url": "https://www.cnblogs.com/yoyoketang/",
            "img": "https://pic.cnblogs.com/avatar/1070438/20161126151035.png"
        },
        "html": "<h3>这是一段html标签</h3>",
        "hello": "Hello,World!"
    }

    class Myblog():
        def __init__(self):
            self.name = "CS小菜鸡",
            self.age = 20
        def guanzhu(self):
            return 100
        def fensi(self):
            return 1000
    myblog = Myblog()    #类的实例
    context["myblog"] = myblog
    return render(request,"personal.html", context=context)

def navlist(request):
    name_list = [
        {
            "type": "科普读物",
            "value": ["宇宙知识", "百科知识", "科学世界", "生物世界"]
        },
        {
            "type": "计算机/网络",
            "value": ["Java", "Python", "C语言"]
        },
        {
            "type": "建筑",
            "value": ["标准/规范", "室内设计", "建筑科学", "建筑文化"]
        }
    ]
    context = {"name_list": name_list}
    return render(request,"navigationbar.html",context)