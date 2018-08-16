class myPage():
    def __init__(self, page_num, total_count, url_prefix, per_page=10, max_page=11):
        """

       :param page_num: 当前页码数
       :param total_count: 数据总数
       :param url_prefix: a标签href的前缀
       :param per_page: 每页显示多少条数据
       :param max_page: 页面上最多显示几个页码
       """
        self.url_prefix = url_prefix
        self.max_page = max_page
        self.per_page = per_page

        total_page, m = divmod(total_count, per_page)
        if m > 0:
            total_page += 1

        self.total_page = total_page

        try:
            page_num = int(page_num)
            # 如果输入页码数过大，默认跳到最后一页
            if page_num > total_page:
                page_num = total_page
        except Exception as e:
            page_num = 1

        self.page_num = page_num

        self.data_start = (page_num - 1) * 10
        self.data_end = page_num * 10

        # 1. 先实现一半一半
        max_page = 11
        # 10. 如果数据量少，页数也少
        if total_page < max_page:
            self.max_page = total_page
        half_max_page = max_page // 2
        page_start = page_num - half_max_page
        page_end = page_num + half_max_page

        # 2. 特殊情况一：页码前面出现负值
        if page_start < 1:
            page_start = 1
            page_end = self.max_page

        # 3. 特殊情况二：页码后面出现空白页
        if page_end >= total_page:
            page_start = total_page - self.max_page + 1
            page_end = total_page

        self.page_start = page_start
        self.page_end = page_end

    @property
    def start(self):
        return self.data_start

    @property
    def end(self):
        return self.data_end

    def page_html(self):
        page_html_list = []

        # 9. 解决在首页处点前一页
        if self.page_num == 1:
            page_html_list.append(
                '<li class="disabled"><a href="#"><span aria-hidden="true">&laquo;</span></a></li>')
        else:
            page_html_list.append(
                '<li><a href="{0}?pages={1}"><span aria-hidden="true">&laquo;</span></a></li>'.format(self.url_prefix,
                                                                                                      self.page_num - 1))

        # 4. 加上首页
        page_html_list.append('<li><a href="{}?pages=1">首页</a></li>'.format(self.url_prefix))

        for i in range(self.page_start, self.page_end + 1):
            # 11. 对当前页加上活动active样式类
            if i == self.page_num:
                temp = '<li class="active"><a href="{0}?pages={1}">{1}</a></li>'.format(self.url_prefix, i)
            else:
                temp = '<li><a href="{0}?pages={1}">{1}</a></li>'.format(self.url_prefix, i)
            page_html_list.append(temp)

        # 5. 加上尾页
        page_html_list.append('<li><a href="{0}?pages={1}">尾页</a></li>'.format(self.url_prefix, self.total_page))

        # 8. 解决最后一页时点后一页
        if self.page_num == self.total_page:
            page_html_list.append(
                '<li class="disabled"><a href="#" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>')
        else:
            page_html_list.append(
                '<li><a href="{0}?pages={1}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(
                    self.url_prefix,
                    self.page_num + 1))

        # 转成字符串
        page_html = "".join(page_html_list)
        return page_html
