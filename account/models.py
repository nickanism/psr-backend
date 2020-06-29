from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.level = 5
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    
    is_active   = models.BooleanField(default=True)
    is_admin    = models.BooleanField(default=False)
    level       = models.IntegerField(default=1)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class Count(models.Model):
    user        = models.ForeignKey('User', on_delete=models.CASCADE, related_name='counts')
    date_time   = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'counts'