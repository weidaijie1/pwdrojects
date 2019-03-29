#!/usr/bin/env python
# coding:utf-8
# import  redis
# conn = redis.Redis(host='106.13.104.194',port=6379,password='123123')
# conn.set('k4','alex')
# val = conn.get('k4')
# print(val)
import psycopg2
conn = psycopg2.connect(database="wei", user="postgres", password="123123", host="106.13.104.194", port="5432")
print  ("Opened database successfully")
