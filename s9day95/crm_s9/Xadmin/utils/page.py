"""
自定义分页组件

"""


class Pagination(object):
    def __init__(self, current_page, all_count, base_url,params, per_page_num=8, pager_count=11, ):
        """
        封装分页相关数据
        :param current_page: 当前页
        :param all_count:    数据库中的数据总条数
        :param per_page_num: 每页显示的数据条数
        :param base_url: 分页中显示的URL前缀
        :param pager_count:  最多显示的页码个数
        """

        try:
            current_page = int(current_page)
        except Exception as e:
            current_page = 1

        if current_page < 1:
            current_page = 1

        self.current_page = current_page

        self.all_count = all_count
        self.per_page_num = per_page_num

        self.base_url = base_url

        # 总页码
        all_pager, tmp = divmod(all_count, per_page_num)
        if tmp:
            all_pager += 1
        self.all_pager = all_pager

        self.pager_count = pager_count  # 最多显示页码数
        self.pager_count_half = int((pager_count - 1) / 2)

        import copy
        params = copy.deepcopy(params)
        params._mutable = True
        self.params = params  # self.params : {"page":77,"title":"python","nid":1}


    @property
    def start(self):
        return (self.current_page - 1) * self.per_page_num


    @property
    def end(self):
        return self.current_page * self.per_page_num


    def page_html(self):
        # 如果总页码 < 11个：
        if self.all_pager <= self.pager_count:
            pager_start = 1
            pager_end = self.all_pager + 1
        # 总页码  > 11
        else:
            # 当前页如果<=页面上最多显示(11-1)/2个页码
            if self.current_page <= self.pager_count_half:
                pager_start = 1
                pager_end = self.pager_count + 1

            # 当前页大于5
            else:
                # 页码翻到最后
                if (self.current_page + self.pager_count_half) > self.all_pager:
                    pager_start = self.all_pager - self.pager_count + 1
                    pager_end = self.all_pager + 1

                else:
                    pager_start = self.current_page - self.pager_count_half
                    pager_end = self.current_page + self.pager_count_half + 1

        page_html_list = []
        self.params["page"] = 1
        first_page = '<li><a href="%s?%s">首页</a></li>' % (self.base_url, self.params.urlencode(),)
        page_html_list.append(first_page)

        if self.current_page <= 1:
            prev_page = '<li class="disabled"><a href="#">上一页</a></li>'
        else:
            self.params["page"] = self.current_page - 1
            prev_page = '<li><a href="%s?%s">上一页</a></li>' % (self.base_url, self.params.urlencode(),)

        page_html_list.append(prev_page)

        for i in range(pager_start, pager_end):
            #  self.params  : {"page":77,"title":"python","nid":1}

            self.params["page"] = i  # {"page":72,"title":"python","nid":1}
            if i == self.current_page:
                temp = '<li class="active"><a href="%s?%s">%s</a></li>' % (self.base_url, self.params.urlencode(), i,)
            else:
                temp = '<li><a href="%s?%s">%s</a></li>' % (self.base_url, self.params.urlencode(), i,)
            page_html_list.append(temp)

        if self.current_page >= self.all_pager:
            next_page = '<li class="disabled"><a href="#">下一页</a></li>'
        else:
            self.params["page"] = self.current_page + 1
            next_page = '<li><a href="%s?%s">下一页</a></li>' % (self.base_url, self.params.urlencode(),)
        page_html_list.append(next_page)

        self.params["page"] = self.all_pager
        last_page = '<li><a href="%s?%s">尾页</a></li>' % (self.base_url, self.params.urlencode(),)
        page_html_list.append(last_page)

        return ''.join(page_html_list)





# class Pagination(object):
#
#     def __init__(self, data_num, current_page, url_prefix,params, per_page=10, max_show=4):
#         """
#         进行初始化.
#         :param data_num: 数据总数
#         :param current_page: 当前页
#         :param url_prefix: 生成的页码的链接前缀
#         :param per_page: 每页显示多少条数据
#         :param max_show: 页面最多显示多少个页码
#         """
#         self.data_num = data_num
#         self.per_page = per_page
#         self.max_show = max_show
#         self.url_prefix = url_prefix
#
#         # 把页码数算出来
#         self.page_num, more = divmod(data_num, per_page)
#         if more:
#             self.page_num += 1
#
#         try:
#             self.current_page = int(current_page)
#         except Exception as e:
#             self.current_page = 1
#             # 如果URL传过来的页码数是负数
#         if self.current_page <= 0:
#             self.current_page = 1
#             # 如果URL传过来的页码数超过了最大页码数
#         elif self.current_page > self.page_num:
#             self.current_page = self.page_num  # 默认展示最后一页
#
#         # 页码数的一半 算出来
#         self.half_show = max_show // 2
#
#         # 页码最左边显示多少
#         if self.current_page - self.half_show <= 1:
#             self.page_start = 1
#             self.page_end = self.max_show
#         elif self.current_page + self.half_show >= self.page_num:  # 如果右边越界
#             self.page_end = self.page_num
#             self.page_start = self.page_num - self.max_show
#         else:
#             self.page_start = self.current_page - self.half_show
#             # 页码最右边显示
#             self.page_end = self.current_page + self.half_show
#
#
#         import copy
#         self.params=copy.deepcopy(params) # {"page":"12","title_startwith":"py","id__gt":"5"}
#
#
#
#     @property
#     def start(self):
#         # 数据从哪儿开始切
#         return (self.current_page - 1) * self.per_page
#
#     @property
#     def end(self):
#         # 数据切片切到哪儿
#         return self.current_page * self.per_page
#
#     def page_html(self):
#         # 生成页码
#         l = []
#         # 加一个首页
#         l.append('<li><a href="{}?page=1">首页</a></li>'.format(self.url_prefix))
#         # 加一个上一页
#         if self.current_page == 1:
#             l.append('<li class="disabled" ><a href="#">«</a></li>'.format(self.current_page))
#         else:
#             l.append('<li><a href="{}?page={}">«</a></li>'.format(self.url_prefix, self.current_page - 1))
#
#
#
#         # {"page":"12","title_startwith":"py","id__gt":"5"}  #  "page=12&title_startwith=py&id__gt=5"
#
#
#         print(self.params.urlencode())
#         for i in range(self.page_start, self.page_end + 1):
#             self.params["page"]=i #  # {"page":"7","title_startwith":"py","id__gt":"5"}  #  "page=7&title_startwith=py&id__gt=5"
#             if i == self.current_page:
#                 tmp = '<li class="active"><a href="{0}?page={1}">{1}</a></li>'.format(self.url_prefix, i)
#             else:
#                 tmp = '<li><a href="{0}?{1}">{2}</a></li>'.format(self.url_prefix, self.params.urlencode(),i)
#             l.append(tmp)
#
#
#
#
#
#
#
#         # 加一个下一页
#         if self.current_page == self.page_num:
#             l.append('<li class="disabled"><a href="#">»</a></li>'.format(self.current_page))
#         else:
#             l.append('<li><a href="{}?page={}">»</a></li>'.format(self.url_prefix, self.current_page + 1))
#         # 加一个尾页
#         l.append('<li><a href="{}?page={}">尾页</a></li>'.format(self.url_prefix, self.page_num))
#         return "".join(l)
