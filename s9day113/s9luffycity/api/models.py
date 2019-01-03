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
