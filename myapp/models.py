# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Activity(models.Model):
    name = models.CharField(max_length=16)
    holder = models.ForeignKey('Users', models.DO_NOTHING, db_column='holder')
    apply_time = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    place = models.CharField(max_length=32)
    max_num = models.IntegerField()
    introduction = models.CharField(max_length=200)
    act_status = models.IntegerField()
    label1 = models.CharField(max_length=10)
    label2 = models.CharField(max_length=10)
    label3 = models.CharField(max_length=10)
    label4 = models.CharField(max_length=10)
    label5 = models.CharField(max_length=10)
    img1 = models.CharField(max_length=256)
    img2 = models.CharField(max_length=256)
    img3 = models.CharField(max_length=256)
    reject = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'activity'


class Discuss(models.Model):
    disc_id = models.AutoField(primary_key=True)
    publisher = models.CharField(max_length=32)
    act_id = models.IntegerField()
    post_time = models.DateTimeField()
    content = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'discuss'


class Favorite(models.Model):
    fav_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='fav_user', primary_key=True)
    fav_act = models.ForeignKey(Activity, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'favorite'
        unique_together = (('fav_user', 'fav_act'),)


class Participate(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='user', primary_key=True)
    act = models.ForeignKey(Activity, models.DO_NOTHING)
    join_time = models.DateTimeField()
    score = models.IntegerField()
    comment = models.CharField(max_length=100)
    comment_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'participate'
        unique_together = (('user', 'act'),)


class Users(models.Model):
    email = models.CharField(primary_key=True, max_length=32)
    password = models.CharField(max_length=32)
    nickname = models.CharField(max_length=16)
    status = models.IntegerField()
    gender = models.IntegerField()
    create_time = models.DateTimeField()
    last_login = models.DateTimeField(blank=True, null=True)
    label_vec = models.CharField(max_length=512)
    img = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'users'


class Admin(models.Model):
    name = models.CharField('用户名', primary_key=True, max_length=32)
    password = models.CharField('密码', max_length=100)

    class Meta:
        managed = False
        db_table = 'admin'


class Feedback(models.Model):
    fbid = models.AutoField(primary_key=True)
    provider = models.CharField(max_length=32)
    opinion = models.CharField(max_length=256)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'feedback'
