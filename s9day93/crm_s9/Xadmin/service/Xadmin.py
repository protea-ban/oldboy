from django.shortcuts import HttpResponse, render, redirect
from django.conf.urls import url
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from Xadmin.utils.page import Pagination
import copy
from django.db.models.fields.related import ForeignKey
from django.db.models.fields.related import ManyToManyField
from django.db.models import Q
from django.forms.boundfield import BoundField
from django.forms.models import ModelChoiceField


class ShowList(object):
    def __init__(self, config, data_list, request):
        self.config = config
        self.data_list = data_list
        self.request = request

        # 扩展分页类
        current_page = int(self.request.GET.get("page", 1))
        data_count = self.data_list.count()
        base_path = self.request.path
        self.pagination = Pagination(current_page, data_count, base_path, self.request.GET, per_page_num=10, pager_count=3)
        self.data_page = self.data_list[self.pagination.start: self.pagination.end]

        # 获取默认action
        self.actions = self.config.new_actions()

    def get_header(self):
        # 处理表头
        header_list = []

        # 为list_display的每个字段都添加相应的表头
        for field in self.config.new_display_list():

            # 字段为数据表自带
            if isinstance(field, str):
                # 默认list_display
                if field == '__str__':
                    val = self.config.model._meta.model_name.upper()
                else:
                    field_obj = self.config.model._meta.get_field(field)
                    val = field_obj.verbose_name
            # 字段为自添加函数
            else:
                # is_header判断是否在传表头时调用
                val = field(self.config, is_header=True)
            header_list.append(val)

        return header_list

    def get_body(self):
        # 处理表单数据的列表
        new_data_list = []

        for data_obj in self.data_page:
            temp = []
            for field in self.config.new_display_list():
                # 取数据对象相应的字段
                if callable(field):
                    val = field(self.config, data_obj)
                else:
                    try:
                        field_obj = self.config.model._meta.get_field(field)
                        if isinstance(field_obj, ManyToManyField):
                            # 获取字段值
                            ret = getattr(data_obj, field).all()
                            t = []
                            for obj in ret:
                                t.append(str(obj))
                            val = ",".join(t)
                        else:
                            val = getattr(data_obj, field)
                            # 如果是根据该字段进入编辑页面
                            if field in self.config.list_display_links:
                                _url = self.config.get_change_url(data_obj)
                                val = mark_safe("<a href='%s'>%s</a>" % (_url, val))
                    # 字段不存在时直接用名称
                    except Exception as e:
                        val = getattr(data_obj, field)

                temp.append(val)

            new_data_list.append(temp)

        return new_data_list

    def get_action_list(self):
        temp = []
        for action in self.actions:
            temp.append({
                "name": action.__name__,
                "short_description": action.short_description
            })

        return temp

    def get_filter_linktags(self):
        link_dic = {}

        for filter_field in self.config.filter_fields:
            params = copy.deepcopy(self.request.GET)
            cid = self.request.GET.get(filter_field, 0)
            filter_field_obj = self.config.model._meta.get_field(filter_field)

            # 根据字段不同类型获取该字段的数据
            if isinstance(filter_field_obj, ForeignKey) or isinstance(filter_field_obj, ManyToManyField):
                data_list = filter_field_obj.rel.to.objects.all()
            else:
                data_list = self.config.model.objects.all().values("pk", filter_field)

            temp = []

            # 处理  全部标签
            if params.get(filter_field):
                del params[filter_field]
                temp.append("<a href='?%s'>全部</a>" % params.urlencode())
            else:
                temp.append("<a class='active' href='#'>全部</a>")

            # 处理数据标签
            for obj in data_list:
                if isinstance(filter_field_obj, ForeignKey) or isinstance(filter_field_obj, ManyToManyField):
                    pk = obj.pk
                    text = str(obj)
                    params[filter_field] = pk
                else:
                    pk = obj.get("pk")
                    text = obj.get(filter_field)
                    params[filter_field] = text

                _url = params.urlencode()

                if cid == str(pk) or cid==text:
                    link_tag = "<a class='active' href='?%s'>%s</a>" % (_url, text)
                else:
                    link_tag = "<a href='?%s'>%s</a>" % (_url, text)

                temp.append(link_tag)

            link_dic[filter_field] = temp

        return link_dic


class ModelXadmin(object):
    # 存放要显示哪些字段的列表
    list_display = ["__str__", ]
    list_display_links = []
    model_class = None
    search_fields = []
    actions = []
    filter_fields = []

    def __init__(self, model, site):
        self.model = model
        self.site = site

    def extra_url(self):
        return []

    def patch_delete(self, request, queryset):
        queryset.delete()

    patch_delete.short_description = "批量删除"

    def new_actions(self):
        temp = []
        temp.append(ModelXadmin.patch_delete)
        temp.extend(self.actions)

        return temp

    def new_display_list(self):
        """
        新的展示列表，增加了能够点击编辑的数据字段
        :return: 新的展示列表
        """
        temp = []
        temp.append(ModelXadmin.check)
        temp.extend(self.list_display)
        if not self.list_display_links:
            temp.append(ModelXadmin.edit)
        temp.append(ModelXadmin.deletes)
        return temp

    def get_add_url(self):
        """
        返回添加数据的url
        :return:
        """

        model_name = self.model._meta.model_name
        app_label = self.model._meta.app_label

        _url = reverse("%s_%s_add"%(app_label, model_name))

        return _url

    def get_list_url(self):
        """
        返回展示数据的url
        :return:
        """

        model_name = self.model._meta.model_name
        app_label = self.model._meta.app_label

        _url = reverse("%s_%s_list" % (app_label, model_name))

        return _url

    def get_change_url(self, obj):
        """
        返回编辑数据的url
        :param obj: 要编辑的数据对象
        :return:
        """

        model_name = self.model._meta.model_name
        app_label = self.model._meta.app_label

        _url = reverse("%s_%s_change" % (app_label, model_name), args=(obj.pk,))

        return _url

    def get_delete_url(self, obj):
        """
        返回删除数据的url
        :param obj:要删除的数据对象
        :return:
        """

        model_name = self.model._meta.model_name
        app_label = self.model._meta.app_label

        _url = reverse("%s_%s_delete" % (app_label, model_name), args=(obj.pk,))

        return _url

    def get_modelform_class(self):
        if not self.model_class:
            from django.forms import ModelForm
            class ModelFormDemo(ModelForm):
                class Meta:
                    model = self.model
                    fields = "__all__"

            return ModelFormDemo
        else:
            return self.model_class

    def get_search_conditon(self, request):
        key_words = request.GET.get("q", "")
        self.key_words = key_words
        search_connection = Q()
        if key_words:
            search_connection.connector = "or"
            for field in self.search_fields:
                search_connection.children.append((field + "__contains", key_words))

        return search_connection

    def get_filter_condition(self, request):
        filter_condition = Q()

        for filter_field, val in request.GET.items():
            if filter_field in self.filter_fields:
                filter_condition.children.append((filter_field, val))

        return filter_condition

    def edit(self, obj=None, is_header=False):

        # 用在传表头的时候
        if is_header is True:
            return "操作"

        url = self.get_change_url(obj)
        return mark_safe('<a href="'+url+'">编辑</a>')

    def deletes(self, obj=None, is_header=False):

        # 用在传表头的时候
        if is_header is True:
            return "操作"

        url = self.get_delete_url(obj)
        return mark_safe('<a href="'+url+'">删除</a>')

    def check(self, obj=None, is_header=False):

        # 用在传表头的时候
        if is_header is True:
            return mark_safe('<input id="choice" type="checkbox">')
            # return "操作"

        return mark_safe('<input class="choice_item" name="selected_pk" value="%s" type="checkbox">'%obj.pk)

    def list_view(self, request):

        if request.method == "POST":
            action = request.POST.get("action")
            selected_pk = request.POST.getlist("selected_pk")
            action_func = getattr(self, action)
            queryset = self.model.objects.filter(pk__in=selected_pk)
            action_func(request, queryset)

        # 所有的数据
        data_list = self.model.objects.all()
        # 数据表的名称
        model_name = self.model._meta.model_name

        # 获取search的Q对象
        search_connection = self.get_search_conditon(request)

        # 获取filter的Q对象
        filter_connection = self.get_filter_condition(request)

        # 筛选数据
        data_list = self.model.objects.filter(search_connection).filter(filter_connection)

        # 构建ShowList列表
        showlist = ShowList(self, data_list, request)

        # 添加url
        add_url = self.get_add_url()
        return render(request, "list_view.html", locals())

    def add_view(self, request):
        ModelFormDemo = self.get_modelform_class()
        form = ModelFormDemo()

        # 实现pop功能
        for bfield in form:
            # 字段对象
            # print(bfield.field)
            # print(type(bfield.field))    # 字段类型
            # print("name", bfield.name)  # 字段名

            if isinstance(bfield.field, ModelChoiceField):
                # 如果是一对多或多对多字段，需要pop功能
                bfield.is_pop = True

                # print(bfield.name, "=====>", bfield.field.queryset.model)

                # bfield.field.queryset.model是所关联的模型表
                related_model_name = bfield.field.queryset.model._meta.model_name
                related_app_label = bfield.field.queryset.model._meta.app_label

                _url = reverse("%s_%s_add"%(related_app_label, related_model_name))
                bfield.url = _url+"?pop_res_id=id_%s"%bfield.name




        # 从前端传回数据
        if request.method == "POST":
            form = ModelFormDemo(request.POST)
            # 通过校验，保存并返回到查看页面
            if form.is_valid():
                obj = form.save()

                pop_res_id = request.GET.get("pop_res_id")

                # 按pop方式打开，返回到之前添加页面
                if pop_res_id:
                    res = {"pk":obj.pk, "text": str(obj), "pop_res_id":pop_res_id}
                    return render(request, "pop.html", {"res": res})

                # 如果不是经过pop打开，按正常方式返回
                else:
                    return redirect(self.get_list_url())

            # 没通过校验,直接返回到添加页面，此时保留的是填写好的表单
            return render(request, "add_view.html", locals())

        return render(request, "add_view.html", locals())

    def change_view(self, request, id):
        data_obj = self.model.objects.filter(pk=id).first()
        ModelFormDemo = self.get_modelform_class()
        # 从前端传回数据
        if request.method == "POST":
            form = ModelFormDemo(request.POST, instance=data_obj)
            # 通过校验，保存并返回到查看页面
            if form.is_valid():
                form.save()
                return redirect(self.get_list_url())

            # 没通过校验,直接返回到添加页面，此时保留的是填写好的表单
            return render(request, "change_view.html", locals())

        form = ModelFormDemo(instance=data_obj)

        return render(request, "change_view.html", locals())

    def delete_view(self, request, id):
        url = self.get_list_url()

        if request.method == "POST":
            self.model.objects.filter(pk=id).first().delete()
            return redirect(url)

        return render(request, "delete_view.html", locals())

    def get_urls2(self):
        """
        二级分发url函数
        :return: 代表操作url的列表
        """
        temp = []

        model_name = self.model._meta.model_name
        app_label = self.model._meta.app_label

        temp.append(url(r"^add/", self.add_view, name="%s_%s_add" % (app_label, model_name)))
        temp.append(url(r"^(\d+)/delete/", self.delete_view, name="%s_%s_delete" % (app_label, model_name)))
        temp.append(url(r"^(\d+)/change/", self.change_view, name="%s_%s_change" % (app_label, model_name)))
        temp.append(url(r"^$", self.list_view, name="%s_%s_list" % (app_label, model_name)))

        # 分配url时增加额外的对某个表的url
        temp.extend(self.extra_url())

        return temp

    @property
    def urls2(self):
        return self.get_urls2(), None, None


class XadminSite(object):
    def __init__(self):
        self._registry = {}

    def get_urls(self):
        temp = []

        for model, admin_class_obj in self._registry.items():
            app_name = model._meta.app_label
            mode_name = model._meta.model_name

            temp.append(url(r'^{}/{}/'.format(app_name, mode_name), admin_class_obj.urls2))
        return temp

    @property
    def urls(self):
        return self.get_urls(), None, None

    def register(self, model, admin_class=None, **options):
        if not admin_class:
            admin_class = ModelXadmin

        self._registry[model] = admin_class(model, self)


site = XadminSite()
