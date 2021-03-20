from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.db import models


class MainUserManager(BaseUserManager):


    def _create_user(self, email, password,**fields):
        if not email:
            raise  ValueError('Email must be set')
        email = self.normalize_email(email)
        user = self.model(email = email,**fields)
        user.set_password(password)
        user.save(using=self._db)

    def create_user(self, email ,password= None,**fields):
        fields.setdefault('is_uperuser', False)
        return self._create_user(email,password)

    def create_superuser(self,email,password,fields):
        fields.setdefault('is_superuser',True)
        fields.setdefault('is_staff',True)

        if fields.get('is_superuser') is not True:
            raise ValueError('is_superuser = True')
        return self._create_user(email,password,**fields)


class MainUser(AbstractBaseUser,PermissionsMixin)  :
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    date_joined =models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default=True)
    objects = MainUserManager

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    class Meta:
        ordering = ('firstName')
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def _str_(self):
        return self.first_name+ " "+ self.last_name