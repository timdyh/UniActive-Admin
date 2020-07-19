import os

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse, HttpResponse, FileResponse
import json

from .models import Admin
from .models import Activity
from .models import Participate
from .models import Discuss
from .models import Users
from .models import Feedback
from .models import Favorite

from django.http import HttpResponseRedirect
from django.urls import reverse
import hashlib
from django.conf import settings
from django.http import StreamingHttpResponse
import time


def post_picture(request):
    if request.method == "POST":
        response = {}
        ticks = int(time.time())
        email = request.GET.get('email', None)
        image =request.FILES.get("image", None)
        if not image:
            response["success"] = False
            return JsonResponse(response)
        if not os.path.exists(settings.PICTURE_ROOT):
            os.makedirs(settings.PICTURE_ROOT)
        image_end = image.name.split('.')[-1]
        image_name = str(email) + '-' + str(ticks) + '.' + image_end
        destination = open(os.path.join(settings.PICTURE_ROOT, image_name), 'wb+')
        for chunk in image.chunks():
            destination.write(chunk)
        destination.close()
        response["success"] = True
        response['url'] = "http://114.115.134.188/api/get_picture/?file=" + image_name
        return JsonResponse(response)


@require_http_methods(["GET"])
def get_picture(request):
    filename = request.GET.get('file', None)
    file = open(os.path.join(settings.PICTURE_ROOT, filename), 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
    return response


def minidouyin_post_video(request):
    if request.method == "POST":
        response = {}
        ticks = int(time.time())
        student_id = request.GET.get('student_id', None)
        user_name = request.GET.get('user_name', None)
        cover_image =request.FILES.get("cover_image", None)
        video = request.FILES.get("video", None)
        if not cover_image or not video:
            response["success"] = False
            return JsonResponse(response)
        if not os.path.exists(settings.MEDIA_ROOT):
            os.makedirs(settings.MEDIA_ROOT)
        cover_image_end = cover_image.name.split('.')[-1]
        cover_image_name = str(student_id) + '-' + str(user_name) + '-' + str(ticks) + 'p.' + cover_image_end
        destination = open(os.path.join(settings.MEDIA_ROOT, cover_image_name), 'wb+')
        for chunk in cover_image.chunks():
            destination.write(chunk)
        destination.close()
        video_end = video.name.split('.')[-1]
        video_name = str(student_id) + '-' + str(user_name) + '-' + str(ticks) + 'v.' + video_end
        destination = open(os.path.join(settings.MEDIA_ROOT, video_name), 'wb+')
        for chunk in video.chunks():
            destination.write(chunk)
        destination.close()
        response["success"] = True
        # destination = open(os.path.join(settings.MEDIA_ROOT, 'record.txt'), 'a+')
        # record = str(student_id) + '-' + str(user_name) + '-' + str(ticks) + '\n'
        # destination.write(record)
        # destination.close()
        return JsonResponse(response)


@require_http_methods(["GET"])
def minidouyin_get_feed(request):
    filelist = os.listdir(settings.MEDIA_ROOT)
    filelist.sort()
    response = {}
    detaillist = []
    for i in range(0, len(filelist), 2):
        res = filelist[i].split('-')
        detail = {}
        detail['student_id'] = res[0]
        detail['user_name'] = res[1]
        detail['image_url'] = "http://114.115.134.188/api/minidouyin_get_file/?student_id=" + res[0] + \
                              "&user_name=" + res[1] + "&file=" + res[2].rstrip()
        res = filelist[i+1].split('-')
        detail['video_url'] = "http://114.115.134.188/api/minidouyin_get_file/?student_id=" + res[0] + \
                              "&user_name=" + res[1] + "&file=" + res[2].rstrip()
        detaillist.append(detail)
    response['feeds'] = detaillist
    response["success"] = True
    return JsonResponse(response)


"""
@require_http_methods(["GET"])
def minidouyin_get_file(request):
    def file_iterator(file, chunk_size=512):
        with open(file, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    filename = request.GET.get('file')
    student_id = request.GET.get('student_id', None)
    user_name = request.GET.get('user_name', None)
    filename = str(student_id) + '-' + str(user_name) + '-' + filename
    print(filename)
    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    print(filepath)
    response = StreamingHttpResponse(file_iterator(filepath))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
    print('attachment;filename="{0}"'.format(filename))
    return response
"""

@require_http_methods(["GET"])
def minidouyin_get_file(request):
    filename = request.GET.get('file', None)
    student_id = request.GET.get('student_id', None)
    user_name = request.GET.get('user_name', None)
    filename = str(student_id) + '-' + str(user_name) + '-' + filename
    #print(filename)
    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    #print(filepath)
    file = open(filepath, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
    #print('attachment;filename="{0}"'.format(filename))
    return response


def upload_file(request):
    if request.method == "POST": # 请求方法为POST时，进行处理
        myFile =request.FILES.get("image", None) # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join(settings.MEDIA_ROOT, myFile.name), 'wb+') # 打开特定的文件进行二进制的写操作
        # (os.path.join(settings.MEDIA_ROOT, myFile.name))
        for chunk in myFile.chunks(): # 分块写入文件
            destination.write(chunk)
        destination.close()
        return HttpResponse("upload over!")


@require_http_methods(["GET"])
def download_file(request):
    def file_iterator(file, chunk_size=512):
        with open(file, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    filename = request.GET.get('file')
    #print(filename)
    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    #print(filepath)
    response = StreamingHttpResponse(file_iterator(filepath))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
    #print('attachment;filename="{0}"'.format(filename))
    return response


@require_http_methods(["GET"])
def check_new(request):
    cur_version = request.GET.get('version', None)
    filelist = os.listdir(settings.RELEASE_ROOT)
    filelist.sort()
    filename = filelist[-1]
    # print(filename[:-4])
    new_version = filename[:-4].split('-')[1][1:]
    # print(new_version)
    response = {}
    if new_version > cur_version:
        response['success'] = True
        response['message'] = '当前最新版本是v' + str(new_version) +', 您是否下载？'
        response['url'] = 'http://114.115.134.188/api/download/'
    else:
        response['success'] = False
        response['message'] = '已经是最新版本'
        response['url'] = ''
    return JsonResponse(response)


@require_http_methods(["GET"])
def download(request):
    """
        def file_iterator(file, chunk_size=512):
        with open(file, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    filelist = os.listdir(settings.RELEASE_ROOT)
    # print(filelist)
    filelist.sort()
    # print(filelist)
    filename = filelist[-1]
    filepath = os.path.join(settings.RELEASE_ROOT, filename)
    response = StreamingHttpResponse(file_iterator(filepath))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
    return response
    """
    return HttpResponseRedirect('https://bhpan.buaa.edu.cn:443/link/91631D7AF775696E19C82DDC5F3DBFBB')


@require_http_methods(["GET"])
def show_users(request):
    response = {}
    try:
        userList = Users.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", userList))
        response['message'] = 'success'
        response["code"] = 1
    except Exception as e:
        response['message'] = str(e)
        response['code'] = 0
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_reviewedActivities(request):
    response = {}
    try:
        reviewedActList = Activity.objects.filter(act_status=0)
        response['list'] = json.loads(serializers.serialize("json", reviewedActList))
        response['message'] = 'success'
        response["code"] = 1
    except Exception as e:
        response['message'] = str(e)
        response['code'] = 0
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_passedActivities(request):
    response = {}
    try:
        passedActList = Activity.objects.filter(act_status=1)
        response['list'] = json.loads(serializers.serialize("json", passedActList))
        response['message'] = 'success'
        response["code"] = 1
    except Exception as e:
        response['message'] = str(e)
        response['code'] = 0
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_denyedActivities(request):
    response = {}
    try:
        denyedActList = Activity.objects.filter(act_status=2)
        response['list'] = json.loads(serializers.serialize("json", denyedActList))
        response['message'] = 'success'
        response["code"] = 1
    except Exception as e:
        response['message'] = str(e)
        response['code'] = 0
    return JsonResponse(response)


@require_http_methods(["GET"])
def get_feedback(request):
    response = {}
    try:
        feedbackList = Feedback.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", feedbackList))
        response['message'] = 'success'
        response["code"] = 1
    except Exception as e:
        response['message'] = str(e)
        response['code'] = 0
    return JsonResponse(response)


@require_http_methods(["GET"])
def get_actDetail(request):
    response = {}
    try:
        id = request.GET.get('id', None)
        activity = Activity.objects.filter(id=id)
        if len(activity) == 0:
            response['message'] = '活动不存在'
            response['code'] = 0
        else:
            response['message'] = '活动存在'
            response['code'] = 1
            response['list'] = json.loads(serializers.serialize("json", activity))
    except Exception as e:
        response['message'] = str(e)
        response['code'] = 0
    return JsonResponse(response)


@require_http_methods(["GET"])
def get_actDiscuss(request):
    response = {}
    try:
        id = request.GET.get('id', None)
        activity = Activity.objects.filter(id=id)
        if len(activity) == 0:
            response['message'] = '活动不存在'
            response['code'] = 0
        else:
            discussList = Discuss.objects.filter(act_id=id)
            response['message'] = '活动存在'
            response['code'] = 1
            response['list'] = json.loads(serializers.serialize("json", discussList))
    except Exception as e:
        response['message'] = str(e)
        response['code'] = 0
    return JsonResponse(response)


@require_http_methods(["GET"])
def discuss(request):
    response = {}
    try:
        disList = []
        passedActList = Activity.objects.filter(act_status=1)
        for act in passedActList:
            dList = Discuss.objects.filter(act_id=act.id)
            item = {'actName':act.name, 'actHolder': act.holder.email, 'introduction': act.introduction,
                    'discuss':json.loads(serializers.serialize("json", dList))}
            disList.append(item)
        response['list'] = disList
        response['message'] = 'success'
        response["code"] = 1
    except Exception as e:
        response['message'] = str(e)
        response['code'] = 0
    return JsonResponse(response)


@require_http_methods(["POST"])
def delete_discuss(request):
    try:
        disc_id = request.POST.get('disc_id', None)
        discuss = Discuss.objects.filter(disc_id=disc_id)
        if len(discuss) == 0:
            return JsonResponse({'code': 0, 'message': '讨论不存在'})
        else:
            Discuss.objects.filter(disc_id=disc_id).delete()
            return JsonResponse({'code': 1, 'message': '删除成功'})
    except Exception as e:
        print(e)
        return JsonResponse({'code': 0, 'message': '出现错误'})


@require_http_methods(["POST"])
def register(request):
    try:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        old = Admin.objects.filter(name=username)
        if len(old):
            return JsonResponse({'code': 0, 'message': '用户名已存在'})
        else:
            new_user = Admin.objects.create(name=username, password=hash_code(password))
            new_user.save()
            return JsonResponse({'code': 1, 'message': '注册成功'})
    except Exception as e:
        print(e)
        return JsonResponse({'code': 0, 'message': '注册失败'})


@require_http_methods(["POST"])
def login(request):
    try:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = Admin.objects.filter(name=username)
        if len(user) == 0:
            return JsonResponse({'code': 0, 'message': '用户不存在'})
        else:
            user = user[0]
            if user.password != hash_code(password):
                return JsonResponse({'code': 0, 'message': '用户名或密码错误'})
            else:
                return JsonResponse({'code': 1, 'message': '账号密码验证成功'})
    except Exception as e:
        return JsonResponse({'code': 0, 'message': '验证失败'})


@require_http_methods(["POST"])
def changepsw(request):
    try:
        username = request.POST.get('username', None)
        oldpsw = request.POST.get('oldpsw', None)
        password = request.POST.get('password', None)
        user = Admin.objects.filter(name=username)
        if len(user) == 0:
            return JsonResponse({'code': 0, 'message': '用户不存在'})
        else:
            user = user[0]
            if user.password != hash_code(oldpsw):
                return JsonResponse({'code': 0, 'message': '密码错误'})
            else:
                Admin.objects.filter(name=username).update(password=hash_code(password))
                return JsonResponse({'code': 1, 'message': '更新密码成功'})
    except Exception as e:
        return JsonResponse({'code': 0, 'message': '验证失败'})


@require_http_methods(["POST"])
def pass_activity(request):
    try:
        id = request.POST.get('id', None)
        activity = Activity.objects.filter(id=id)
        if len(activity) == 0:
            return JsonResponse({'code': 0, 'message': '活动不存在'})
        else:
            Activity.objects.filter(id=id).update(act_status=1)
            return JsonResponse({'code': 1, 'message': '更新成功'})
    except Exception as e:
        print(e)
        return JsonResponse({'code': 0, 'message': '出现错误'})


@require_http_methods(["POST"])
def deny_activity(request):
    try:
        id = request.POST.get('id', None)
        reject = request.POST.get('reject', None)
        activity = Activity.objects.filter(id=id)
        if len(activity) == 0:
            return JsonResponse({'code': 0, 'message': '活动不存在'})
        else:
            Activity.objects.filter(id=id).update(act_status=2, reject=reject)
            return JsonResponse({'code': 1, 'message': '更新成功'})
    except Exception as e:
        print(e)
        return JsonResponse({'code': 0, 'message': '出现错误'})


@require_http_methods(["POST"])
def change_user_status(request):
    try:
        email = request.POST.get('email', None)
        user = Users.objects.filter(email=email)
        if len(user) == 0:
            return JsonResponse({'code': 0, 'message': '用户不存在'})
        else:
            user = user[0]
            Users.objects.filter(email=email).update(status=(1-user.status))
            return JsonResponse({'code': 1, 'message': '更新成功'})
    except Exception as e:
        print(e)
        return JsonResponse({'code': 0, 'message': '出现错误'})


def hash_code(s):
    h = hashlib.sha256()
    h.update(s.encode())
    return h.hexdigest()
