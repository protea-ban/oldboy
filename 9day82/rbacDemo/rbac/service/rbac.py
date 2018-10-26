from django.utils.deprecation import MiddlewareMixin
import re
from django.shortcuts import HttpResponse, redirect


class ValidPermissionMiddleware(MiddlewareMixin):

    def process_request(self, request):

        # 当前路径
        current_path = request.path_info

        # 校验是否为白名单
        valid_url_list = ["/login/", "/reg/", "/admin/.*"]
        for item in valid_url_list:
            ret = re.match(item, current_path)
            if ret:
                return None

        # 校验是否登录
        if not request.session.get("user_id"):
            return redirect('/login/')

        # 校验权限
        flag = False
        permission_list = request.session.get("permission_list", [])
        for permission in permission_list:

            # 保障url完全匹配
            permission = "^%s$" % permission

            ret = re.match(permission, current_path)
            if ret:
                flag = True
                break

        if not flag:
            return HttpResponse("没有权限访问")

        return None
