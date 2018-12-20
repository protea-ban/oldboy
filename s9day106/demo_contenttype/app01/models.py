from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
# Create your models here.


class DegreeCourse(models.Model):
    """学位课程"""
    name = models.CharField(max_length=128, unique=True)
    course_img = models.CharField(max_length=255, verbose_name="缩略图")
    brief = models.TextField(verbose_name="学位课程简介", )


class Course(models.Model):
    """专题课程"""
    name = models.CharField(max_length=128, unique=True)
    course_img = models.CharField(max_length=255)

    # 不会在数据库生成列，只用于帮助你进行查询
    policy_list = GenericRelation("PricePolicy")


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
