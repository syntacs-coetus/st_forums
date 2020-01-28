from django.db import models
from users.models import Users

# Create your models here.
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_title = models.TextField(null=False)
    cat_description = models.TextField(null=False)
    cat_parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True)
    cat_creator = models.ForeignKey(Users, on_delete=models.PROTECT)
    cat_collapsed = models.BooleanField(default=True)
    cat_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'post_categories'

class Posts(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    post_title = models.TextField()
    post_description = models.TextField()
    post_parent = models.ForeignKey(Category, on_delete=models.PROTECT)
    post_creator = models.ForeignKey(Users, on_delete=models.PROTECT)
    post_likes = models.IntegerField(default=0)
    post_dislikes = models.IntegerField(default=0)
    post_created = models.DateTimeField(auto_now_add=True)
    post_edited = models.DateTimeField(null=True)
    class Meta:
        db_table = 'posts'

class PostsInteractions(models.Model):
    post_id = models.ForeignKey(Posts, on_delete=models.PROTECT)
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT)
    post_liked = models.BooleanField(default=False, null=True)
    post_disliked = models.BooleanField(default=False, null=True)
    post_interactdate = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table = 'post_interactions'

class Comments(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    post_id = models.ForeignKey(Posts, on_delete=models.PROTECT)
    comment_message = models.TextField(null=False)
    commentor_id = models.ForeignKey(Users, on_delete=models.PROTECT)
    comment_likes = models.BigIntegerField(default=0, null=True)
    comment_dislikes = models.BigIntegerField(default=0, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_editdate = models.DateTimeField(null=True)
    class Meta:
        db_table = 'post_comments'

class CommentInteractions(models.Model):
    comment_id = models.ForeignKey(Comments, on_delete=models.PROTECT)
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT)
    comment_liked = models.BooleanField(default=False, null=True)
    comment_disliked = models.BooleanField(default=False, null=True)
    comment_interactdate = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table = 'comment_interactions'