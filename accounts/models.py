from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربر")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    class Meta:
        db_table = "accounts"
        ordering = ["user__username"]
        verbose_name = "حساب کاربری"
        verbose_name_plural = "حساب‌های کاربری"
