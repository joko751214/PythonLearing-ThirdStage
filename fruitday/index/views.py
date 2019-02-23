from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *

# Create your views here.


# def login_views(request):
	# 判斷request.method是get還是post
	# if request.method == 'GET':
	# 	#判斷 id 和 uphone 是否都存在於 COOKIES 中
	# 	cookies = request.COOKIES
	# 	if 'id' in cookies and 'uphone' in cookies:
	# 		return HttpResponse('歡迎:'+cookies['uphone'])
	# 	return render(request,'login.html')
	# else:
	# 	uphone = request.POST.get('uphone','')
	# 	upwd = request.POST.get('upwd','')
	# 	# if uphone and upwd:
	# 	# 	users = Users.objects.filter(uphone=uphone,
	# 	# 		upass=upwd)
	# 	# 	if users:
	# 	# 		return HttpResponse('登錄成功!!')
	# 	# 	else:
	# 	# 		errMsg = "手機號或密碼不正確"
	# 	# 		return render(request,'login.html',
	# 	# 			locals())
	# 	if uphone and upwd:
	# 		users = Users.objects.filter(uphone=
	# 			uphone)
	# 		if users:
	# 			u = users[0]
	# 			if upwd == u.upass:
	# 				resp = HttpResponse('登錄成功')
	# 				#將用戶id,uname保存進cookie
	# 				if 'isSave' in request.POST:
	# 					resp.set_cookie('id',u.id,
	# 						60*60*24*365)
	# 					resp.set_cookie('uphone',u.uphone,
	# 						60*60*24*365)
	# 					return resp
	# 				else:
	# 					return HttpResponse('登錄成功')
	# 			else:
	# 				errMsg = "對不起,輸入的密碼不正確"
	# 				return render(request,'login.html',
	# 				locals())
	# 		else:
	# 			errMsg = '對不起,手機號碼不存在'
	# 			return render(request,'login.html',
	# 				locals())
	# 	else:
	# 		errMsg = '手機號或密碼不能為空'
	# 		return render(request,'login.html',
	# 			locals())

def login_views(request):
	if request.method == 'POST':
		# 執行登錄的驗證判斷
		uphone = request.POST.get('uphone','')
		upwd = request.POST.get('upwd','')
		uList = Users.objects.filter(uphone=uphone,upass=upwd)
		if uList:
			# 登錄成功
			# 聲明一個響應對象
			resp = HttpResponseRedirect('/index/')
			# 將手機號碼存進session
			request.session['uphone'] = uphone
			# 判斷是否需要存進cookie
			if 'isSave' in request.POST:
				resp.set_cookie('uphone',uphone,3600*24*365)
			return resp

		else:
			# 登錄失敗
			errMsg = '手機號或密碼不正確'
			return render(request,'login.html',locals())
	else:
		# GET請求
		# 判斷是否處於已登錄狀態(session中是否有值)
		if 'uphone' in request.session:
			return HttpResponseRedirect('/index/')
		else:
			# 未處於登錄狀態
			# 判斷曾經是否登錄過(cookies中是否有值)
			if 'uphone' in request.COOKIES:
				# 曾經登錄過,取出值,存進session
				uphone = request.COOKIES['uphone']
				request.session['uphone'] = uphone
				return HttpResponseRedirect('/index/')
			else:
				# 不曾登錄過
				return render(request,'login.html')


def index_views(request):
	return render(request,'index.html')



def register_views(request):
	# 判斷request.method 得到用戶的意圖
	if request.method == 'GET':
		return render(request,'register.html')
	else:
		# 實現註冊操作
		uphone = request.POST.get('uphone','')
		upwd = request.POST.get('upwd','')
		uname = request.POST.get('uname','')
		uemail = request.POST.get('uemail','')

		if uphone and upwd and uname and uemail:
			#先判斷uphone的值是否存在
			u = Users.objects.filter(uphone=uphone)
			if u:
				errMsg = "手機號碼已存在"
				return render(request,
					'register.html',locals())
			else:
				Users.objects.create(uphone=uphone,
					upass=upwd,uname=uname,
					uemail=uemail)
				return HttpResponse('註冊成功')
		else:
			return HttpResponse('數據不能為空')

