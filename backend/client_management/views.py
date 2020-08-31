from django.shortcuts import render
from django.http import HttpResponse
from client_management.models import discount_policy
from client_management.models import Member
from django.core import serializers
import datetime


def discount(request):
    data = discount_policy.objects.all()                           # discount_policy是存储优惠信息的数据表
    length = data.count()                                          # 获取表数据总长度
    result = discount_policy.objects.filter(policy_id=length - 1)  # 取出最后一行（即最新）数据
    result_start = result.values('start_date')[0]['start_date']    # 取出这行数据的开始日期
    result_end = result.values('end_date')[0]['end_date']          # 取出这行数据的截止日期
    today = datetime.date.today()
    if result_start < today and result_end > today:                # 若今日日期在这行数据有效期内，返回该优惠策略的内容
        return HttpResponse(result.values('policy_content')[0]['policy_content'])
    else:
        return HttpResponse(None)


def add_credit(request):  # 会员消费增加积分
    consumption = 100     # 此数值目前仅用于测试，日后需要修改，应为计算出的用户应付的价格
    phone = 12345678900   # 此数值目前仅用于测试，日后需要修改，应为计算出的用户应付的价格
    target = Member.objects.filter(phone=phone)
    original_credit = target.values('credit')[0]['credit']
    Member.objects.filter(phone=phone).update(credit = original_credit + consumption)  # 消费120
    return HttpResponse('消费增加积分成功！')