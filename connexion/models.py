from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self, email, prenom=None, nom=None, gsm=None, password=None, is_active=True, is_staff=False,
                    is_admin=False, is_joueur=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            email=self.normalize_email(email),
            prenom=prenom,
            nom=nom,
            gsm=gsm,
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.active = is_active
        user_obj.admin = is_admin
        user_obj.estjoueur = is_joueur
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, prenom=None, nom=None, gsm=None, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            prenom=prenom,
            nom=nom,
            gsm=gsm,
        )
        return user

    def create_superuser(self, email, prenom=None, nom=None, gsm=None, password=None):
        user = self.create_user(
            email,
            password=password,
            nom=nom,
            gsm=gsm,
            is_staff=True,
            is_admin=True,
            prenom=prenom,
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) #staff no superuser
    admin = models.BooleanField(default=False) #superuser
    nom = models.CharField(max_length=255, blank=True, null=True)
    prenom = models.CharField(max_length=255, blank=True, null=True)
    gsm = PhoneNumberField(blank=True, null=True)
    estjoueur = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return "%s %s" % (self.nom, self.prenom)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_joueur(self):
        return self.estjoueur


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.email} Profile'


class Joueur(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    entrainements = models.IntegerField(default=0)
    matchs = models.IntegerField(default=0)
    titularisations = models.IntegerField(default=0)
    buts = models.IntegerField(default=0)
    jaune = models.IntegerField(default=0)
    rouge = models.IntegerField(default=0)


    def __str__(self):
        return "%s %s" % (self.user.nom, self.user.prenom)






