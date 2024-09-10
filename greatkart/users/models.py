from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password):
        if not email:
            raise ValueError('User must have an email')
        if not username:
            raise ValueError("User must have a usernmae")
        if not password:
            raise ValueError("User must have a password")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(first_name, last_name, username, email, password)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True

        user.save(using=self.db)
        
        return user

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)
    
    date_joined = models.DateTimeField(auto_now_add=True)
    last_joined = models.DateTimeField(auto_now=True)
    
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        """
        Does the user have a specific permission?
        
        Args:
            perm: The permission to check.
            obj: The object to check the permission against.
            
        Returns:
            bool: Whether the user has the permission.
        """
        # Simplest possible answer: Yes, admin user has all permissions
        return self.is_admin

    
    def has_module_perms(self, add_label):
        """
        Does the user have permissions to view the app `add_label`?
        
        Args:
            add_label: The label of the application to check.
            
        Returns:
            bool: Whether the user has permissions to view the application.
        """
        # Simplest possible answer: Yes, the user has access to all apps.
        return True