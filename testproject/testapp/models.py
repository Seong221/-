from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self,username, password=None):
        common_user = self.model(username=username)
        common_user.set_password(password)
        common_user.save(using=self._db)
        return common_user
    
    def create_staff(self,username,password=None):
        staff_user=self.model(username=username)
        staff_user.is_staff=True
        staff_user.set_password(password)
        staff_user.save(using=self.db)
     
        return staff_user

    def create_superuser(self, username, password=None):
      
        #extra_fields.setdefault('is_staff', True)
        admin_user=self.model(username=username)
        admin_user.is_superuser=True
        admin_user.set_password(password)
        admin_user.save(using=self.db)
        #admin_user=super().create_superuser(username,password,**extra_fields)
        return admin_user


class CustomUser(AbstractUser):
    is_active=models.BooleanField(default=True)
    #is_admin=models.BooleanField(default=False)
    objects=CustomUserManager()

   
    def has_perm(self, perm,obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)