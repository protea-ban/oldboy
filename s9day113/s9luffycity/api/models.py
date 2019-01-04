from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
# Create your models here.

class Course(models.Model):
    """
    课程表
    """
    title = models.CharField(verbose_name="课程名称", max_length=32)
    course_img = models.CharField(verbose_name="课程图片", max_length=64)
    level_choices = (
        (1,'初级'),
        (2,'中级'),
        (3,'高级'),
    )
    level = models.IntegerField(verbose_name="课程难易程度", choices=level_choices)

    # 用于GenericForeignKey反向查询，不会生成表字段，切勿删除
    price_policy = GenericRelation("PricePolicy")
    period = models.PositiveIntegerField(verbose_name="建议学习周期(days)", default=7)

    def __str__(self):
        return self.title


class CourseDetail(models.Model):
    """
    课程详情表
    """
    course = models.OneToOneField(to='Course')
    slogon = models.CharField(verbose_name='口号', max_length=255)
    why = models.CharField(verbose_name='为什么要学？', max_length=255)
    recommend_course = models.ManyToManyField(verbose_name='推荐课程', to='Course', related_name='rc')

    def __str__(self):
        return "课程详情" + self.course.title


class Chapter(models.Model):
    """
    章节
    """
    num = models.IntegerField(verbose_name='章节')
    name = models.CharField(verbose_name='章节名称', max_length=32)
    course = models.ForeignKey(verbose_name='所属课程', to='Course')

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=64)

class UserToken(models.Model):
    user = models.OneToOneField(to="UserInfo")
    token = models.CharField(max_length=64)


class PricePolicy(models.Model):
    """价格与有课程效期表"""
    content_type = models.ForeignKey(ContentType)  # 关联course or degree_course
    object_id = models.PositiveIntegerField()

    #不会在数据库生成列，只用于帮助你进行添加和查询
    content_object = GenericForeignKey('content_type', 'object_id')


    valid_period_choices = (
        (1, '1天'),
        (3, '3天'),
        (7, '1周'), (14, '2周'),
        (30, '1个月'),
        (60, '2个月'),
        (90, '3个月'),
        (180, '6个月'), (210, '12个月'),
        (540, '18个月'), (720, '24个月'),
    )
    valid_period = models.SmallIntegerField(choices=valid_period_choices)
    price = models.FloatField()

    class Meta:
        unique_together = ("content_type", 'object_id', "valid_period")
        verbose_name_plural = "15. 价格策略"

    def __str__(self):
        return "%s(%s)%s" % (self.content_object, self.get_valid_period_display(), self.price)


# ########################### 优惠券 ################################
class Coupon(models.Model):
    """优惠券生成规则"""
    name = models.CharField(max_length=64, verbose_name="活动名称")
    brief = models.TextField(blank=True, null=True, verbose_name="优惠券介绍")
    coupon_type_choices = ((0, '立减券'), (1, '满减券'), (2, '折扣券'))
    coupon_type = models.SmallIntegerField(choices=coupon_type_choices, default=0, verbose_name="券类型")

    """
    通用：
        money_equivalent_value=100
        off_percent=null
        minimum_consume=0
    满减：
        money_equivalent_value=100
        off_percent=null
        minimum_consume=1000
    折扣：
        money_equivalent_value=0
        off_percent=79
        minimum_consume=0
    """
    money_equivalent_value = models.IntegerField(verbose_name="等值货币")
    off_percent = models.PositiveSmallIntegerField("折扣百分比", help_text="只针对折扣券，例7.9折，写79", blank=True, null=True)
    minimum_consume = models.PositiveIntegerField("最低消费", default=0, help_text="仅在满减券时填写此字段")

    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField("绑定课程", blank=True, null=True, help_text="可以把优惠券跟课程绑定")
    content_object = GenericForeignKey('content_type', 'object_id')

    quantity = models.PositiveIntegerField("数量(张)", default=1)
    open_date = models.DateField("优惠券领取开始时间")
    close_date = models.DateField("优惠券领取结束时间")
    valid_begin_date = models.DateField(verbose_name="有效期开始时间", blank=True, null=True)
    valid_end_date = models.DateField(verbose_name="有效结束时间", blank=True, null=True)
    coupon_valid_days = models.PositiveIntegerField(verbose_name="优惠券有效期（天）", blank=True, null=True,
                                                    help_text="自券被领时开始算起")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "31. 优惠券生成记录"

    def __str__(self):
        return "%s(%s)" % (self.get_coupon_type_display(), self.name)

    def save(self, *args, **kwargs):
        if not self.coupon_valid_days or (self.valid_begin_date and self.valid_end_date):
            if self.valid_begin_date and self.valid_end_date:
                if self.valid_end_date <= self.valid_begin_date:
                    raise ValueError("valid_end_date 有效期结束日期必须晚于 valid_begin_date ")
            if self.coupon_valid_days == 0:
                raise ValueError("coupon_valid_days 有效期不能为0")
        if self.close_date < self.open_date:
            raise ValueError("close_date 优惠券领取结束时间必须晚于 open_date优惠券领取开始时间 ")

        super(Coupon, self).save(*args, **kwargs)


class CouponRecord(models.Model):
    """优惠券发放、消费纪录"""
    coupon = models.ForeignKey("Coupon")
    number = models.CharField(max_length=64, unique=True)
    account = models.ForeignKey("UserInfo", verbose_name="拥有者")
    status_choices = ((0, '未使用'), (1, '已使用'), (2, '已过期'))
    status = models.SmallIntegerField(choices=status_choices, default=0)
    get_time = models.DateTimeField(verbose_name="领取时间", help_text="用户领取时间")
    used_time = models.DateTimeField(blank=True, null=True, verbose_name="使用时间")
    # order = models.ForeignKey("Order", blank=True, null=True, verbose_name="关联订单")  # 一个订单可以有多个优惠券

    class Meta:
        verbose_name_plural = "32. 用户优惠券"

    def __str__(self):
        return '%s-%s-%s' % (self.account, self.number, self.status)

