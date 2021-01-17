from django.db import models

# Create your models here.
# Create your models here.
class DBinfo(models.Model):
    # bookid : INTEGER型で、主キー
    id = models.IntegerField(primary_key=True)
    # 書名 : 文字列100桁
    title = models.CharField(max_length=100)
    # 著者
    name = models.CharField(max_length=30)
    #
    url=models.URLField(verbose_name='なんかのURL',null=True)

    email=models.EmailField(max_length=50,null=True)
    class Meta:
        verbose_name_plural = 'データベース'
    def __str__(self):
        return self.title
