from django.shortcuts import render, redirect

# Create your views here.
from students.models import student
from students.form import PostForm

def listone(request): 
    try: 
        unit = student.objects.get(stdName="AAA") #讀取一筆資料
    except:
        errormessage = " (讀取錯誤!)"
    return render(request, "student/listone.html", locals())

def listall(request):  
    allStudents = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    return render(request, "student/listall.html", locals())

def post(request):
    # 判斷表單資料傳送方式
    if request.method == "POST":
        # 接收傳送資料
        mess = request.POST['stdName']
    else:
        mess = "表單資料尚未送出!"
    return render(request, "student/addstudent.html", locals())

def post1(request):
    if request.method == "POST":      #如果是以POST方式才處理
        stdName = request.POST['stdName'] #取得表單輸入資料
        stdID = request.POST['stdID']
        stdSex =  request.POST['stdSex']
        stdBirth =  request.POST['stdBirth']
        stdEmail = request.POST['stdEmail']
        stdPhone =  request.POST['stdPhone']
        stdAddress =  request.POST['stdAddress']
        #新增一筆記錄
        unit = student.objects.create(stdName=stdName, stdID=stdID, stdSex=stdSex, stdBirth=stdBirth, stdEmail=stdEmail, stdPhone=stdPhone, stdAddress=stdAddress) 
        unit.save()  #寫入資料庫
        return redirect('/hello')  
    else:
        mess = '請輸入資料(資料不作驗證)'
    return render(request, "student/addstudent1.html", locals())

def postform(request):
    # 新增PostForm表單物件
    stdform = PostForm()
    return render(request, "student/stdform.html", locals())