from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    password = models.CharField(max_length=100, verbose_name="رمز عبور")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "account"
        ordering = ["name"]
        verbose_name = "حساب کاربری"
        verbose_name_plural = "حساب‌های کاربری"