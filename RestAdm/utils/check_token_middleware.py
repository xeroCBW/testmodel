from uuid import uuid4
from django.http import HttpResponse, JsonResponse
from django.utils.deprecation import MiddlewareMixin
from jwt import InvalidSignatureError
from rest_framework.exceptions import ValidationError
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer, jwt_decode_handler
from rest_framework import status
import json
from django.http import QueryDict

class CheckTokenMiddleware(MiddlewareMixin):
    '''
    Django 1.4.x ---- Django 1.9.x
    每次请求时 判断 JWT 是否与 User.user_jwt 相等
    相等的话，说明没有以设备登录，且没有修改密码
    不相等，则说明异常设备登录，或修改了密码，修改用户的uuid并提示用户重新登录
    每次登录时记录更新JWT 为User 的一个属性user_jwt
    每次修改密码时 更新修改uuid
    '''

    def process_request(self,request):

        if request and request.user:
            user = getattr(request,'user')
            if len(user.username) and hasattr(user,'is_active') and not getattr(user,'is_active'):
                print('-----')
                return JsonResponse(data={'msg': '用户不可用请联系超级管理员', 'data': {}, 'code': 400},
                                    status=status.HTTP_400_BAD_REQUEST)


            # data = {
            #     'token': jwt_token.split()[1],  # [0] 是前缀，默认为JWT
            # }
            #
            # try:
            #     valid_data = VerifyJSONWebTokenSerializer().validate(data)
            #     user = valid_data['user']
            # except (InvalidSignatureError, ValidationError):
            #     # 找不到用户，说明token 不合法或者身份过期
            #     return JsonResponse(data={'msg': '身份已经过期或不合法，请重新登入','data':data,'code':401}, status=status.HTTP_401_UNAUTHORIZED)
            #
            # if user.user_secret != data['token']:
            #     user.user_secret = uuid4()
            #     user.save()
            #     return JsonResponse(data={'msg': '登录状态异常,请重新登入', 'data': data, 'code': 401},status=status.HTTP_401_UNAUTHORIZED)

    # def process_response(self, request, response):
    #     # 仅用于处理 login请求
    #
    #     print('-----')
    #
    #     pass
    #     # if request.path == '/user/login' and request.method == 'POST' and response.data.get('token'):
    #     #     data = response.data
    #     #     try:
    #     #         valid_data = VerifyJSONWebTokenSerializer().validate(data)
    #     #         user = valid_data['user']
    #     #         user.user_secret = valid_data['token']
    #     #         user.save()
    #     #     except(InvalidSignatureError, ValidationError):
    #     #         # 找不到用户，说明token 不合法或者身份过期
    #     #         return JsonResponse(data={'msg': '用户名或者密码错误,请重新登录','data':data,'code':400}, status=status.HTTP_400_BAD_REQUEST)
    #     #
    #     #     return response
    #     # else:
        #     return response

