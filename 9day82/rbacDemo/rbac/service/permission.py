def initial_session(user, request):
    # 将用户权限列表存入session
    # 取出登录用户的权限url并去重
    # permissions = models.Role.objects.filter(user=user_obj).values("permissions__url").distinct()
    permissions = user.roles.all().values("permissions__url").distinct()
    permission_list = []
    for item in permissions:
        permission_list.append(item["permissions__url"])

    request.session["permission_list"] = permission_list
