from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def email_validation(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError(_('Invalid email'))
        
    def create_user(self, email,first_name,last_name, password=None, **extra_fields):
        if not email:
            raise ValueError(_("This is a required field"))
        else:
            self.email_validation(email)
            cleaned_email = self.normalize_email(email)
            if not first_name:
                raise ValueError(_("This is a required field"))
            if not last_name:
                raise ValueError(_("This is a required field"))
            
            user = self.model(
                email=cleaned_email,
                first_name=first_name,
                last_name=last_name,
                **extra_fields
            )
            
            user.set_password(password)
            extra_fields.setdefault('is_staff', False)
            extra_fields.setdefault('is_superuser', False)
            user.save()
            
            return user
        
    def create_superuser(self, email, first_name, last_name=None, password=None, **extra_fields):
        if not email:
            raise ValueError(_("This is a required field"))
        else:
            self.email_validation(email)
            cleaned_email = self.normalize_email(email)
            if not first_name:
                raise ValueError(_("This is a required field"))

            user = self.model(
                email=cleaned_email,
                first_name=first_name,
                last_name=last_name,
                **extra_fields
            )

            user.set_password(password)
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
            
            user = self.create_user(email, first_name, last_name, password, **extra_fields)
            user.save()

            return user