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

        # 校验权限1(permission_list)
        # flag = False
        # permission_list = request.session.get("permission_list", [])
        # for permission in permission_list:
        #
        #     # 保障url完全匹配
        #     permission = "^%s$" % permission
        #
        #     ret = re.match(permission, current_path)
        #     if ret:
        #         flag = True
        #         break
        #
        # if not flag:
        #     return HttpResponse("没有权限访问")
        #
        # return None

        # 校验权限2(permission_dict)
        permission_dict = request.session.get("permission_dict")

        # 从字典中找到相关url信息进行校验并将权限允许的动作存到request中方便以后使用
        for permission in permission_dict.values():
            urls = permission['urls']
            for reg in urls:
                reg = "^%s$"%reg
                ret = re.match(reg, current_path)

                # 如果匹配到权限路径，将相关的动作存储到session中
                if ret:
                    request.actions = permission["actions"]
                    return None

            return HttpResponse("没有访问权限！")
