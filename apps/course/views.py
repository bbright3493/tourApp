#coding=utf-8

from django.shortcuts import render
from django.views.generic.base import View
from .models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from user_operation.models import UserFavorite, CourseComments, UserCourse
from django.http import HttpResponse

# Create your views here.
class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        courses = courses.order_by('-add_time')
        hot_courses = courses.order_by('click_num')[:3]
        cur_page = 'course'
        sort = request.GET.get('sort','')
        if sort:
            if sort == 'hot':
                courses = courses.order_by('click_num')
            elif sort == 'students':
                courses = courses.order_by('students')
            else:
                pass

        courses_nums = courses.count()

        #对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(courses, 6, request=request)
        course_page = p.page(page)

        return render(request, 'course-list.html',{
            'all_courses':course_page,
            'hot_courses':hot_courses,
            'cur_page':cur_page

        })


class CourseDetailView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course.click_num += 1
        course.save()

        has_fav_course = False
        has_fav_org = False

        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=int(course.id), fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=int(course.org.id), fav_type=2):
                has_fav_org = True

        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:1]
        else:
            relate_courses = []
        return render(request, 'course-detail.html',{
            'course':course,
            'relate_courses':relate_courses,
            'has_fav_course':has_fav_course,
            'has_fav_org':has_fav_org,
            })

class CourseVideoView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course_resource = CourseResource.objects.filter(course=course)
        cur_page = 'video'
        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_user_courses = UserCourse.objects.filter(user_id__in==user_ids)
        course_ids = [user_course.course.id for user_course in all_user_courses]
        relate_courses = Course.objects.filter(id__in=course_ids).order_by('-click_num')[:5]

        return render(request, 'course-video.html', {
            'course':course,
            'course_resource':course_resource,
            'cur_page':cur_page,
            'user_courses':relate_courses,
        })

class CourseCommentsView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course_comments = CourseComments.objects.filter(course=course)
        course_resource = CourseResource.objects.filter(course=course)
        cur_page = 'comment'
        return render(request, 'course-comment.html', {
            'course':course,
            'course_comments':course_comments,
            'course_resource':course_resource,
            'cur_page':cur_page,
            })


class AddComment(View):
    def post(self, request):
        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        comment = request.POST.get('comment', '')
        course_id = request.POST.get('course_id', 0)
        if course_id > 0 and comment:
            course_comment = CourseComments()
            course = Course.objects.get(id=int(course_id))
            course_comment.comments = comment
            course_comment.course = course
            course_comment.user = request.user
            course_comment.save()
            return HttpResponse('{"status":"success", "msg":"评论成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"评论失败"}', content_type='application/json')
