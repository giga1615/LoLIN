# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MemberForRecommend(models.Model):
    no = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    time_predict = models.FloatField(blank=True, null=True)
    game_style = models.CharField(max_length=100, blank=True, null=True)
    liked_position = models.CharField(max_length=100, blank=True, null=True)
    liked = models.IntegerField(blank=True, null=True)
    tier = models.CharField(max_length=100, blank=True, null=True)
    user_level = models.IntegerField(blank=True, null=True)
    win_rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_for_recommend'


