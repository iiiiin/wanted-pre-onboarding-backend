from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.core.validators import MinLengthValidator, RegexValidator

# Create your models here.

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("The Email field must be set")
#         # email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.CharField(
#         verbose_name='email address',
#         max_length=255,
#         primary_key=True,
#         validators=[RegexValidator(regex='.*@{1}.*',
#                                    message='Enter a valid email address.')])
    
#     password = models.CharField(max_length=128, verbose_name='password',
#                                 validators=[MinLengthValidator(limit_value=8,
#                                                                message='Enter password over 8')])

#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'

#     def __str__(self):
#         return self.email
    

class Post(models.Model):
    postnum = models.AutoField(primary_key=True)
    content = models.TextField()
    title = models.CharField(max_length=255)
    # email = models.ForeignKey("CustomUser",on_delete=models.CASCADE, db_column="email")
    
    def __str__(self):
        return self.title