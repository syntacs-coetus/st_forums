from django.db import models
from users.models import Users
    
class Groups(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=65)
    group_description = models.TextField()
    group_editusers = models.BooleanField(default=False)
    group_deleteusers = models.BooleanField(default=False)
    group_addusers = models.BooleanField(default=False)
    group_addgroups = models.BooleanField(default=False)
    group_addusergroup = models.BooleanField(default=False)
    group_removeusergroup = models.BooleanField(default=False)
    group_editgroups = models.BooleanField(default=False)
    group_removegroups = models.BooleanField(default=False)
    group_editposts = models.BooleanField(default=False)
    group_removeposts = models.BooleanField(default=False)
    group_banuser = models.BooleanField(default=False)
    group_timebanuser = models.BooleanField(default=False)
    group_unbanuser = models.BooleanField(default=False)
    group_created = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table = 'authorized_groups'

class UserGroups(models.Model):
    group_id = models.ManyToManyField(Groups)
    user_id = models.ManyToManyField(Users)
    user_joined = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table = 'user_groups'