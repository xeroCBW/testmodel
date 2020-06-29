from rest_framework import viewsets
from .models import *
from .serializers import *

class UserCourseViewSet(viewsets.ModelViewSet):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer


class UserAskViewSet(viewsets.ModelViewSet):
    queryset = UserAsk.objects.all()
    serializer_class = UserAskSerializer

class UserMessageViewSet(viewsets.ModelViewSet):
    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializer

class CourseCommentsViewSet(viewsets.ModelViewSet):

    queryset = CourseComments.objects.all()
    serializer_class = CourseCommentsSerializer