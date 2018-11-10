"""
自定义分页组件
"""
import copy
class Pagination(object):
    def __init__(self, data_num, current_page, url_prefix, params, per_page=10, max_show=3):
        """

        :param data_num:
        :param current_page:
        :param url_prefix:
        :param per_page:
        :param max_show:
        """
        self.data_num = data_num
        self.per_page = per_page
        self.max_show = max_show
        self.url_prefix = url_prefix
        # 传过来的参数
        self.params = copy.deepcopy(params)

        # 把页码数算出来
        self.page_num, more = divmod(data_num, per_page)
        if more:
            self.page_num += 1

        try:
            self.current_page = int(current_page)
        except Exception as e:
            self.current_page = 1
        # 如果URL传过来的页码数是负数,显示第一页
        if self.current_page <= 0:
            self.current_page = 1
        # 如果URL传过来的页码数超过最大页码数,显示最后一页
        elif self.current_page > self.page_num:
            self.current_page = self.page_num

        # 页码数的一半
        self.half_show = max_show // 2

        # 页码最左边显示多少
        if self.current_page - self.half_show <= 1:
            self.page_start = 1
            self.page_end = self.max_show
        # 如果右边越界
        elif self.current_page + self.half_show >= self.page_num:
            self.page_end = self.page_num
            self.page_start = self.page_num - self.max_show
        else:
            self.page_start = self.current_page - self.half_show
            # 页码最右边显示
            self.page_end = self.current_page + self.half_show


    @property
    def start(self):
        # print("current_page", self.current_page)
        # 数据从哪开始切
        return (self.current_page - 1) * self.per_page

    @property
    def end(self):
        # 数据切到哪
        return self.current_page * self.per_page

    def page_html(self):
        # 生成页码
        l = []
        # 加一个首页
        l.append('<li><a href="{}?page=1">首页</a></li>'.format(self.url_prefix))

        # 加一个上一页
        if self.current_page == 1:
            l.append('<li class="disabled"><a href="#"><<</a></li>')
        else:
            l.append('<li><a href="{}?page={}"><<</a></li>'.format(self.url_prefix, self.current_page-1))

        # 页码
        for i in range(self.page_start, self.page_end+1):
            self.params["page"] = i
            if i == self.current_page:
                tmp = '<li class="active"><a href="{0}?page={1}">{1}</a></li>'.format(self.url_prefix, i)
            else:
                tmp = '<li><a href="{0}?{1}">{2}</a></li>'.format(self.url_prefix, self.params.urlencode(), i)

            l.append(tmp)

        # 加一个下一页
        if self.current_page == self.page_num:
            l.append('<li class="disabled"><a href="#">>></a></li>')
        else:
            l.append('<li><a href="{}?page={}">>></a></li>'.format(self.url_prefix, self.current_page + 1))

        # 加一个尾页
        l.append('<li><a href="{}?page={}">尾页</a></li>'.format(self.url_prefix, self.page_num))





        return "".join(l)
