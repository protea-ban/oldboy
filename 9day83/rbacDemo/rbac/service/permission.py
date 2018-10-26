def initial_session(user, request):
    # 将用户权限列表存入session
    # 取出登录用户的权限url并去重
    # permissions = models.Role.objects.filter(user=user_obj).values("permissions__url").distinct()
    # permissions = user.roles.all().values("permissions__url").distinct()
    # permission_list = []
    # for item in permissions:
    #     permission_list.append(item["permissions__url"])
    #
    # request.session["permission_list"] = permission_list

    # 方案2
    permissions = user.roles.all().values("permissions__url", "permissions__group_id", "permissions__action").distinct()

    # 以字典的形式存储动作信息，此种方式能够存储更多内容
    permission_dict = {}
    for item in permissions:
        gid = item.get('permissions__group_id')

        # 以group id为键，如果是第一次则赋值，其他则添加
        if not gid in permission_dict:
            permission_dict[gid] = {
                "urls": [item["permissions__url"], ],
                "actions": [item["permissions__action"], ]
            }

        else:
            permission_dict[gid]["urls"].append(item["permissions__url"])
            permission_dict[gid]["actions"].append(item["permissions__action"])

    request.session["permission_dict"] = permission_dict
