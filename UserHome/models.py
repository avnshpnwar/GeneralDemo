from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.
class user_account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_no = models.PositiveIntegerField(db_index=True)
    account_name = models.CharField(max_length=20, validators=[MinLengthValidator(4, message='Length has to be 4'),])
    
    class Meta:
        unique_together = (('user', 'account_no', 'account_name'),)
        
    def __str__(self):
        return str(self.account_no)
    
class payee_account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payee_name = models.CharField(max_length=30)
    account_no = models.PositiveIntegerField(db_index=True)
    
    class Meta:
        unique_together = (('user', 'payee_name', 'account_no'),)
        
    def __str__(self):
        return str(self.account_no)