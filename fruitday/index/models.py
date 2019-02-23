from django.db import models

# Create your models here.


class Users(models.Model):
    uphone = models.CharField(max_length=20, verbose_name='联系方式')
    upass = models.CharField(max_length=50, verbose_name='密码')
    uemail = models.EmailField(verbose_name='邮箱')
    uname = models.CharField(max_length=20, null=True, verbose_name='用户名')
    isActive = models.BooleanField(default=True, verbose_name='启用')

    def __str__(self):
        return self.uname

    class Meta:
        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class GoodsType(models.Model):
    title = models.CharField(max_length=30, verbose_name='类型名称')
    desc = models.TextField(null=True, verbose_name='类型描述')
    picture = models.ImageField(
        upload_to='static/upload/goodstype', verbose_name='类型图片')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'goodstype'
        verbose_name = '商品类型'
        verbose_name_plural = verbose_name


class Goods(models.Model):
    title = models.CharField(max_length=100, verbose_name='商品名称')
    price = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name='商品价格')
    spec = models.CharField(max_length=30, verbose_name='商品规格')
    picture = models.ImageField(
        upload_to='static/upload/goods', verbose_name='商品图片')
    isActive = models.BooleanField(default=True, verbose_name='销售中')
    goodsType = models.ForeignKey(GoodsType, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'goods'
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name
