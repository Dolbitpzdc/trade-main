from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration
from django.http import JsonResponse
from django.http import HttpResponse

from django.contrib.auth.models import User
from accounts.models import *

import sqlite3

from django.contrib.auth import authenticate, login
import urllib


def moderViews(request):
    if checkAdmin(request):
        return render(request, 'admin/homeAdmin.html')
    else:
        return redirect("loginAdmin")

def moderForms(request):
    if checkAdmin(request):
        return render(request, 'admin/form-common.html')
    else:
        return redirect("loginAdmin")

def chat(request):
    if checkAdmin(request):
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()

        cur.execute("SELECT * FROM auth_user ")
        users = cur.fetchall()

        conn.close()

        return  render(request, 'admin/chat.html', {'users': users})
    else:
        return redirect("loginAdmin")

def charts(request):
    if checkAdmin(request):
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()

        cur.execute("SELECT * FROM auth_user ")
        users = cur.fetchall()

        cur.execute("SELECT * FROM accounts_buyer_individ") #выгрузка данных из таблицы accounts_buyer_individ
        accounts_buyer_individ = cur.fetchall()

        cur.execute("SELECT * FROM accounts_buyer_entity") #выгрузка данных из таблицы accounts_buyer_entity
        accounts_buyer_entity = cur.fetchall()

        cur.execute("SELECT * FROM accounts_provider_individ") #выгрузка данных из таблицы accounts_provider_individ
        accounts_provider_individ = cur.fetchall()

        cur.execute("SELECT * FROM accounts_provider_entity") #выгрузка данных из таблицы accounts_provider_entity
        accounts_provider_entity = cur.fetchall()

        cur.execute("SELECT * FROM accounts_paymentdetails ")
        accounts_paymentDetail = cur = fetchall()

        conn.close()

        return render(request, 'admin/charts.html', {'abi_users': accounts_buyer_individ,'abe_users': accounts_buyer_entity, 'api_users': accounts_provider_individ, 'ape_users': accounts_provider_entity, 'users': users, 'PD': accounts_paymentdetails})
    else:
        return redirect("loginAdmin")

def PymentDetail(request):
    if request.POST:
        data = urllib.parse.parse_qs(request.POST.get("data", ""))
        need_keys = ["email",  "expiration", "position"]

        if check_keys(need_keys, data):

            profile = PymentDetail()
            profile.email = data["email"][0]
            profile.expiration = data["expiration"][0]
            profile.position = data["position"][0]

            profile.save()

            return JsonResponse({'response': "Подписка оформлена!"}, status=200)

        else:
            return JsonResponse({'error': "Заполните все поля"}, status=400)


def tables(request):
    if checkAdmin(request):
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()

        cur.execute("SELECT * FROM accounts_buyer_individ") #выгрузка данных из таблицы accounts_buyer_individ
        accounts_buyer_individ = cur.fetchall()

        cur.execute("SELECT * FROM accounts_buyer_entity") #выгрузка данных из таблицы accounts_buyer_entity
        accounts_buyer_entity = cur.fetchall()

        cur.execute("SELECT * FROM accounts_provider_individ") #выгрузка данных из таблицы accounts_provider_individ
        accounts_provider_individ = cur.fetchall()

        cur.execute("SELECT * FROM accounts_provider_entity") #выгрузка данных из таблицы accounts_provider_entity
        accounts_provider_entity = cur.fetchall()

        cur.execute("SELECT * FROM auth_user") #выгрузка данных из таблицы auth_user
        users = cur.fetchall() #выгрузка данных в переменную

        conn.close()

        return render(request, 'admin/tables.html', {'abi_users': accounts_buyer_individ,'abe_users': accounts_buyer_entity, 'api_users': accounts_provider_individ, 'ape_users': accounts_provider_entity, 'users': users})
    else:
        return redirect("loginAdmin")

def grid(request):
    if checkAdmin(request):
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()
        cur.execute("SELECT * FROM accounts_buyer_entity") #выгрузка данных из таблицы accounts_buyer_entity
        accounts_buyer_entity = cur.fetchall()

        cur.execute("SELECT * FROM accounts_provider_entity ") #выгрузка данных из таблицы accounts_provider_entity
        accounts_provider_entity  = cur.fetchall()


        cur.execute("SELECT * FROM auth_user") #выгрузка данных из таблицы auth_user
        users = cur.fetchall() #выгрузка данных в переменную

        conn.close()

        return render(request, 'admin/grid.html', {'abi_users': accounts_buyer_entity,'ape_users': accounts_provider_entity , 'users': users})
    else:
        return redirect("loginAdmin")


def buttons(request):
    if checkAdmin(request):
        return render(request, 'admin/buttons.html')
    else:
        return redirect("loginAdmin")

def interface(request):
    if checkAdmin(request):
        return render(request, 'admin/interface.html')
    else:
        return redirect("loginAdmin")

def calendar(request):
    if checkAdmin(request):
        return render(request, 'admin/calendar.html')
    else:
        return redirect("loginAdmin")

#ОТЗЫВЫ
def error(request):
    if checkAdmin(request):
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()

        cur.execute("SELECT * FROM accounts_reviews")
        accounts_reviews = cur.fetchall()

        conn.close()

        return render(request, 'admin/error404.html', {'reviews': accounts_reviews})
    else:
        return redirect("loginAdmin")

def NewReview(request):
    if request.POST:
        data = urllib.parse.parse_qs(request.POST.get("data", ""))
        need_keys = ["name",  "email", "review"]

        if check_keys(need_keys, data):

            profile = reviews()
            profile.name = data["name"][0]
            profile.email = data["email"][0]
            profile.review = data["review"][0]

            profile.save()

            return JsonResponse({'response': "Спасибо! Отзыв отправлен!"}, status=200)

        else:
            return JsonResponse({'error': "Заполните все поля"}, status=400)


def loginAdmin(request):
        return render(request, 'admin/login.html')

def checkAdmin(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return True
        else:
            return False
    else:
        return False


#ПРОВЕРКА НА АВТОРИЗАЦИЮ В ПАНЕЛЕ АДМИНИСТРИРОВАНИЯ
def log_inAdmin(request):
    if request.POST:
        if not request.user.is_authenticated:
            username = password = ''

            email=request.POST.get("email")
            password=request.POST.get("password")

            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    if user.is_superuser:
                        login(request, user)
                        return JsonResponse({'response': "Авторизован.", "code": 200}, status=200)
                    else:
                        return JsonResponse({'error': "Пользователь не имеет прав.", "code": 401}, status=401)
                else:
                    return JsonResponse({'error': "Пользователь не активен.", "code": 401}, status=401)
            else:
                return JsonResponse({'error': "Неправильный логин или пароль.", "code": 401}, status=401)
        else:
            return JsonResponse({'error': "Вы уже авторизованы.", "code": 400}, status=400)

#Изменение статуса пользователя
def activeUser(request):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute("UPDATE auth_user SET is_active=1 WHERE id=?", [request.GET.get("id", "0")]) #оьновить данные в таблице auth_user поле is_active  равному единице где id  равен чему-то

    conn.commit()
    conn.close()
    return redirect("tables")

def deactiveUser(request):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute("UPDATE auth_user SET is_active=0 WHERE id=?", [request.GET.get("id", "0")]) #оьновить данные в таблице auth_user поле is_active равному нулю где id  равен чему-то

    conn.commit() #сохранение данных
    conn.close() #закрытие соединения
    return redirect("tables")

def changeActive(request):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute("SELECT * FROM accounts_buyer_individ") #выгрузка данных из таблицы accounts_buyer_individ
    accounts_buyer_individ = cur.fetchall()

    cur.execute("SELECT * FROM auth_user") #выгрузка данных из таблицы auth_user
    users = cur.fetchall() #выгрузка данных в переменную

    conn.close()

    return render(request, 'changeActive.html', {'abi_users': accounts_buyer_individ, 'users': users})

def changeActiveInfo(request, id_user="0"):
    if id_user == "0":
        return HttpResponse("Неверный ID.")
    else:
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()

        cur.execute("SELECT * FROM accounts_buyer_individ WHERE user_id=?", id_user) #выгрузка данных из таблицы accounts_buyer_individ где user_id равен чему-то
        account_buyer_individ = cur.fetchall()

        if len(account_buyer_individ) == 0:
            conn.close()
            return HttpResponse("Данный пользователь не найден.")
        else:
            cur.execute("SELECT * FROM auth_user WHERE id=?", id_user)
            user_basic = cur.fetchall()

            conn.close()

            return render(request, 'changeActiveInfo.html', {'user': account_buyer_individ[0], 'user_basic': user_basic[0]})


def home(request):
    if request.user.is_authenticated:
        return redirect('home_accaunt')
    else:
        return render(request, 'home.html')





#для поставщика (физ.лицо)
def register_p_ind(request):
    return render(request, 'login_provider_individ.html')
    # if request.method == "POST":
    #     form = UserRegistration(request.POST);
    #     form.get()
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username');
    #         return redirect('home')
    # else:
    #     form = UserRegistration()
    # return render(request, 'registration.html', {'form': form})

#для поставщика (юр.лицо)
def register_p_ent(request):
    return render(request, 'login_provider_entity.html')

#для заказчика (физ.лицо)
def register_z_ind(request):
    return render(request, 'login_buyer_individ.html')

#для заказчика (юр.лицо)
def register_z_ent(request):
    return render(request, 'login_buyer_entity.html')

def registrationAdmin(request):
    if checkAdmin(request):
        if request.POST:
            data = urllib.parse.parse_qs(request.POST.get("data", ""))
            need_keys = ["last_name", "first_name", "middle_name",  "email", "password"]

            if check_keys(need_keys, data):
                user = User.objects.create_user(username=data["email"][0],email=data["email"][0], password=data['password'][0])
                user.save()

                profile = new_person()
                profile.user = user
                profile.first_name = data["first_name"][0]
                profile.last_name = data["last_name"][0]
                profile.middle_name = data["middle_name"][0]

                profile.save()


                return JsonResponse({'response': "Регистрация прошла успешно! Ожидайте подтверждение администратора", "code": 200}, status=200)
    else:
        return JsonResponse({'error': "Иди нахуй", "code": 401}, status=401)


def registration(request, type_reg="undefined"):
    if request.POST:
        if not request.user.is_authenticated:
            if type_reg == "undefined":
                return JsonResponse({'error': "Отсутствует тип регистрации.", "code": 400}, status=400)

            if type_reg == "buyer_individ":
                data = urllib.parse.parse_qs(request.POST.get("data", ""))
                need_keys = ["last_name", "first_name", "middle_name", "kind_of_activity", "VAT_payer", "count_of_outlets", "trading_area", "address_1", "address_2", "address_3", "email", "phone", "delivery", "deferment_of_payment", "certificate_of_registration", "payment_form", "short_desc"]

                if check_keys(need_keys, data):
                    user = User.objects.create_user(username=data["email"][0],email=data["email"][0], password='nullPass')
                    user.save()

                    profile = buyer_individ()
                    profile.user = user
                    profile.first_name = data["first_name"][0]
                    profile.last_name = data["last_name"][0]
                    profile.middle_name = data["middle_name"][0]
                    profile.kind_of_activity = data["kind_of_activity"][0]
                    profile.VAT_payer = data["VAT_payer"][0]
                    profile.count_of_outlets = data["count_of_outlets"][0]
                    profile.trading_area = data["trading_area"][0]
                    profile.address = data["address_1"][0] + ", " + data["address_2"][0] + ", " + data["address_3"][0]
                    profile.phone = data["phone"][0]
                    profile.delivery = data["delivery"][0]
                    profile.deferment_of_payment = data["deferment_of_payment"][0]
                    profile.certificate_of_registration = data["certificate_of_registration"][0]
                    profile.payment_form = data["payment_form"][0]
                    profile.short_desc = data["short_desc"][0]

                    profile.save()


                    return JsonResponse({'response': "Регистрация прошла успешно! Ожидайте подтверждение администратора", "code": 200}, status=200)

                else:
                    return JsonResponse({'error': "Заполните все поля, это привлечёт больше клиентов.", "code": 400}, status=400)

            elif type_reg == "buyer_entity":
                data = urllib.parse.parse_qs(request.POST.get("data", ""))
                need_keys = ["name","last_name", "first_name", "middle_name","position" , "kind_of_activity", "VAT_payer", "count_of_outlets", "trading_area", "address_1", "address_2", "address_3", "email", "phone", "inn", "short_desc"]

                if check_keys(need_keys, data):

                    user = User.objects.create_user(username=data["email"][0],email=data["email"][0], password='glass onion')
                    user.save()

                    profile = buyer_entity()
                    profile.user = user
                    profile.name = data["name"][0]
                    profile.first_name = data["first_name"][0]
                    profile.last_name = data["last_name"][0]
                    profile.middle_name = data["middle_name"][0]
                    profile.position = data["position"][0]
                    profile.kind_of_activity = data["kind_of_activity"][0]
                    profile.VAT_payer = data["VAT_payer"][0]
                    profile.count_of_outlets = data["count_of_outlets"][0]
                    profile.trading_area = data["trading_area"][0]
                    profile.address = data["address_1"][0] + ", " + data["address_2"][0] + ", " + data["address_3"][0]
                    profile.phone = data["phone"][0]
                    profile.inn = data["inn"][0]
                    profile.short_desc = data["short_desc"][0]
                    profile.save()

                    return JsonResponse({'response': "Регистрация прошла успешно! Ожидайте подтверждение администратора", "code": 200}, status=200)

                else:
                    return JsonResponse({'error': "Заполните все поля, это привлечёт больше клиентов.", "code": 400}, status=400)

            elif type_reg == "provider_individ":
                data = urllib.parse.parse_qs(request.POST.get("data", ""))
                need_keys = ["last_name", "first_name", "middle_name", "kind_of_activity", "VAT_payer", "address_1", "address_2", "address_3", "email", "phone", "delivery", "deferment_of_payment", "certificate_of_registration", "min_order", "warranty", "availability_of_certificates" "short_desc"]

                # if check_keys(need_keys, data):
                user = User.objects.create_user(username=data["email"][0],email=data["email"][0], password='glass onion')
                user.save()

                profile = provider_individ()
                profile.user = user
                profile.first_name = data["first_name"][0]
                profile.last_name = data["last_name"][0]
                profile.middle_name = data["middle_name"][0]
                profile.kind_of_activity = data["kind_of_activity"][0]
                profile.VAT_payer = data["VAT_payer"][0]
                profile.address = data["address_1"][0] + ", " + data["address_2"][0] + ", " + data["address_3"][0]
                profile.phone = data["phone"][0]
                profile.delivery = data["delivery"][0]
                profile.deferment_of_payment = data["deferment_of_payment"][0]
                profile.certificate_of_registration = data["certificate_of_registration"][0]
                profile.min_order = data["min_order"][0]
                profile.warranty = data["warranty"][0]
                profile.availability_of_certificates = data["availability_of_certificates"][0]
                profile.short_desc = data["short_desc"][0]

                profile.save()

                return JsonResponse({'response': "Регистрация прошла успешно! Ожидайте подтверждение администратора", "code": 200}, status=200)

                # else:
                #     return JsonResponse({'error': "Заполните все поля, это привлечёт больше клиентов.", "code": 400}, status=400)

            elif type_reg == "provider_entity":
                data = urllib.parse.parse_qs(request.POST.get("data", ""))
                need_keys = ["name","last_name", "first_name", "middle_name", "position", "kind_of_activity", "VAT_payer", "address_1", "address_2", "address_3", "email", "phone", "delivery", "deferment_of_payment", "min_order", "warranty", "inn", "availability_of_certificates" "short_desc"]

                # if check_keys(need_keys, data):
                user = User.objects.create_user(username=data["email"][0],email=data["email"][0], password='glass onion')
                user.save()

                profile = provider_entity()
                profile.user = user
                profile.name = data["name"][0]
                profile.first_name = data["first_name"][0]
                profile.last_name = data["last_name"][0]
                profile.middle_name = data["middle_name"][0]
                profile.position = data["position"][0]
                profile.kind_of_activity = data["kind_of_activity"][0]
                profile.VAT_payer = data["VAT_payer"][0]
                profile.address = data["address_1"][0] + ", " + data["address_2"][0] + ", " + data["address_3"][0]
                profile.phone = data["phone"][0]
                profile.delivery = data["delivery"][0]
                profile.deferment_of_payment = data["deferment_of_payment"][0]
                profile.min_order = data["min_order"][0]
                profile.warranty = data["warranty"][0]
                profile.availability_of_certificates = data["availability_of_certificates"][0]
                profile.inn = data["inn"][0]
                profile.short_desc = data["short_desc"][0]

                profile.save()


                return JsonResponse({'response': "Регистрация прошла успешно! Ожидайте подтверждение администратора", "code": 200}, status=200)

                # else:
                #     return JsonResponse({'error': "Заполните все поля, это привлечёт больше клиентов.", "code": 400}, status=400)


            elif type_reg == "new_person":
                data = urllib.parse.parse_qs(request.POST.get("data", ""))
                need_keys = ["last_name", "first_name", "middle_name",  "email", "password"]

                if check_keys(need_keys, data):
                    user = User.objects.create_user(username=data["email"][0],email=data["email"][0], password=data['password'][0])
                    user.save()

                    profile = new_person()
                    profile.user = user
                    profile.first_name = data["first_name"][0]
                    profile.last_name = data["last_name"][0]
                    profile.middle_name = data["middle_name"][0]

                    profile.save()


                    return JsonResponse({'response': "Регистрация прошла успешно! Ожидайте подтверждение администратора", "code": 200}, status=200)
                else:
                    return JsonResponse({'error': "Заполните все поля, это привлечёт больше клиентов.", "code": 400}, status=400)

            else:
                return JsonResponse({'error': "Неизвестный тип регистрации", "code": 400}, status=400)



        else:
            return JsonResponse({'error': "Вы уже авторизованы.", "code": 400}, status=400)


#Функция проверки ключей
def check_keys(keys, data):
    for key in keys:
        if not key in data:
            return False
    return True


#вход
def log_in(request):
    if request.POST:
        if not request.user.is_authenticated:
            username = password = ''

            email=request.POST.get("email")
            password=request.POST.get("password")

            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return JsonResponse({'response': "Авторизован.", "code": 200})
                else:
                    return JsonResponse({'error': "Пользователь не активен.", "code": 401}, status=401)
            else:
                return JsonResponse({'error': "Неправильный логин или пароль.", "code": 401}, status=401)
        else:
            return JsonResponse({'error': "Вы уже авторизованы.", "code": 400}, status=400)

#страница после входа
def accaunt_home(request):
    return render(request, 'home_accaunt.html')

def bay(request):
    return render(request, 'bay.html')

def rates(request):
    return render(request, 'rates.html')

def help(request):
    return render(request, 'help.html')
