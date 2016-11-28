from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.views.generic import FormView
from .forms import LoginUserForm, RegisterUserForm,ForgetPasswordForm,ChangePasswordForm,ResetPasswordForm
from django.core.mail import send_mail, EmailMultiAlternatives
from myapps.users.forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from django.core.mail import EmailMultiAlternatives
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from myapps.users.models import CustomUser
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import update_session_auth_hash
# Create your views here.


'''登录用户的类，验证登录用户和密码是否正确，如果正确，就进入到home(首页)里面
如果不正确的话，就会重置这个页面'''
@csrf_exempt
class LoginView(FormView):
    template_name = 'user/welcome.html'     # 指定登录成功后跳转渲染的模板文件
    form_class = LoginUserForm              # 指定使用的是哪个form
    def post(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
        if user is not None:									##重定向到一个登录成功页面
            login(request,user)
            return HttpResponseRedirect(reverse('home'))

        else:
            return render(request, 'user/welcome.html')

    '''退出登录,django封装的logout会自动删除掉session'''
    def logout(request):
        logout(request)
        return HttpResponseRedirect('/login')

'''注册用户'''
class RegisterView(FormView):
    # template_name = 'user/register.html'
    # form_class = RegisterUserForm
    def register(request):
        if request.method == 'POST':
            # username = request.POST.get('username', '')                        # 用户名
            password = request.POST.get('password', '')                        # 密码
            confirm_password = request.POST.get('confirm_password', '')        # 确认密码
            # email = request.POST.get('email', '')                              # 邮箱
            # agree = request.POST.get('agree','')                               # 同意协议
            register_data = CustomUser(
                username=request.POST.get('username', ''),                      # 用户名
                company=request.POST.get('company', ''),                        # 公司名称
                password=make_password(request.POST.get('password', '')),       # 密码
                phone=request.POST.get('phone', ''),                            # 手机号
                email=request.POST.get('email', ''),                            # 邮箱
                url=request.POST.get('url', ''),                                # 公司网址
            )
            # 确定用户名在数据库中有没有，因为是使用用户名登录，所以要保证用户名唯一性
            ajax_username = request.POST.get('a')                                 #获取ajax传过来的用户名
            ajax_email =request.POST.get('b')                                     #获取ajax传过来的邮箱名
            username_count = CustomUser.objects.filter(username=ajax_username).count()    # 传进来的用户名是否有同名的
            email_count = CustomUser.objects.filter(email=ajax_email).count()        # 传进来的邮箱是否有重复的
            if username_count == 0 and password == confirm_password and email_count == 0:
                register_data.save()
                return HttpResponseRedirect(reverse('login'))
            elif username_count != 0 and ajax_username != "":
                context = {'register_username':'a'}
                return JsonResponse(context)
            elif email_count != 0 and ajax_email != "":
                context = {'register_email':'b'}
                return JsonResponse(context)
            else:
                return HttpResponse("该邮箱已经存在，请输入新的邮箱")
        return render(request,'user/register.html')


'''当用户忘记密码的时候，点击忘记密码，需要输入邮箱，另外输入的邮箱必须在数据库中存在，否则邮件会发不出去，因为输入的邮箱
会和数据库里的邮箱匹配。而且查出其对应的用户名'''
class ForgetPasswordView(FormView):
    template_name = 'user/forgetpassword.html'
    form_class = ForgetPasswordForm

    def forget_password(request):
        if request.method == 'POST':
            email_data = request.POST.get('a')
            username_count = CustomUser.objects.filter(email=email_data).count()
            if username_count == 0:
                context = {'receive_email':'a'}
                return JsonResponse(context)
            else:
                username_data = CustomUser.objects.filter(email=email_data).values('username')[0]
                username = username_data.get('username')
                subject, form_email, to = '重置密码', '2463011462@qq.com', email_data
                text_content = '点击链接进入系统主页'
                html_content = u'<b>激活重置密码链接</b><a href="http://127.0.0.1:8000/resetpassword/'+username+'"> http://127.0.0.1:8000/resetpassword/ </a>'
                msg = EmailMultiAlternatives(subject, text_content, form_email, [to])
                msg.attach_alternative(html_content, 'text/html')
                msg.send()
                context = {'b':'b'}
                return JsonResponse(context)
        return render(request,'user/forgetpassword.html')

'''修改个人资料信息,现在需求改为一旦注册完毕，用户名和邮箱都不可以再次修改。'''
class PersonalData(FormView):
        def personal_data(request):
            now_user = request.user
            personal_data = CustomUser.objects.filter(username=now_user)
            now_user_id = request.user.id
            if request.method == 'POST':
                '''获取当前表单提交的数据'''
                # username=request.POST.get('username')
                company=request.POST.get('company')
                contacts=request.POST.get('contacts')
                phone=request.POST.get('phone')
                # email=request.POST.get('email')
                url=request.POST.get('url')
                '''根据当前用户的id，查出当前用户的信息'''
                old_user_data = CustomUser.objects.get(pk=now_user_id)
                '''把新提交的数据赋值给原来用户的字段，最后保存'''
                # old_user_data.username = username
                old_user_data.company = company
                old_user_data.contacts = contacts
                old_user_data.phone = phone
                # old_user_data.email = email
                old_user_data.url = url
                old_user_data.save()
            return render(request,'user/changepassword.html',locals())
'''用户修改密码，首先要验证用户输入的旧密码是否匹配，然后在把新密码存进数据库里面'''
@csrf_exempt
class ChangePasswordView(FormView):
    def change_password(request):
        user = request.user                         # 获取当前登录用户是哪个用户
        oldpassword = request.POST.get('a')         # 获得前端传过来的旧密码
        newpassword = request.POST.get('b')         # 获得前端传过来的新密码
        if user.check_password(oldpassword):        # 判断前端传过来的密码是否正确，如果正确，返回一个值
            user.set_password(newpassword)          # 把前端输入的新密码加密放进数据库里面
            user.save()
            update_session_auth_hash(request,user)  # 更新session，因为原来的session存放的是旧密码
            context={'a':'a'}
            return JsonResponse(context)
        else:
            context={'b':'b'}
            return JsonResponse(context)
        """
        now_user_id = request.user.id
        if request.method == 'POST':
            oldpassword = request.POST.get('a')
            newpassword = make_password(request.POST.get('b'))
            #'''验证当前登录用户输入的密码是否是数据库里存放的密码'''
            personal_data = CustomUser.objects.filter(id=now_user_id)
            #'''方法一  这种方法是采用的check_password方法，如果验证成功的话，返回的是True，否则返回False'''
            new_user_id = request.user.id
            sqlpassword = CustomUser.objects.filter(id=new_user_id).values('password')[0]
            password = sqlpassword.get('password')
            testauth = check_password(oldpassword,password)

            #'''方法二  这种验证方法是采用的类似登录的方法验证，如果获得的user不是None的话，则说明当前用户的密码验证正确'''
            user = authenticate(username=request.user,password=oldpassword)

            if testauth is True:
                old_user_data = CustomUser.objects.get(pk=now_user_id)
                old_user_data.password = newpassword
                old_user_data.save()
                update_session_auth_hash(request,old_user_data)
                context={'a':'a'}
                return JsonResponse(context)
            else:
                context = {'b':'b'}
                return JsonResponse(context)
            """
        return render(request,'user/changepassword.html')


'''重置密码'''
class ResetPasswordView(FormView):
    template_name = 'user/resetpassword.html'
    # form_class = ResetPasswordForm

    def reset_password(request,username):
        reqpath =request.path
        reset_user = reqpath[15:]
        return render(request,'user/resetpassword.html',locals())
    def subit_newpassword(request):
        newpasssword = make_password(request.GET.get('a',''))     # 输入的新密码的值
        reset_user = request.GET.get('c','')                      # 当前重置密码的用户
        old_user_data = CustomUser.objects.get(username=reset_user)
        old_user_data.password = newpasssword
        old_user_data.save()
        return render(request,'user/welcome.html')