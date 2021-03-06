# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-26 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(blank=True, null=True, verbose_name='消费日期')),
                ('order_id', models.IntegerField(verbose_name='订单id')),
                ('number', models.IntegerField(verbose_name='交易号')),
                ('type', models.CharField(choices=[('A', '充值汇款'), ('B', '投放消费'), ('C', '退款')], max_length=1, verbose_name='操作类型')),
                ('amount', models.IntegerField(verbose_name='金额')),
                ('Balance', models.IntegerField(verbose_name='余额')),
            ],
            options={
                'verbose_name': '消费记录',
                'verbose_name_plural': '消费记录',
                'db_table': 't_expenses',
            },
        ),
        migrations.CreateModel(
            name='Financial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='财务报表')),
                ('time', models.DateTimeField(blank=True, null=True, verbose_name='日期')),
                ('type', models.CharField(choices=[('A', '基本户'), ('B', '临时户'), ('C', '一般户'), ('D', '专用户')], default='A', max_length=1, verbose_name='账户类型')),
                ('lmonth_balance', models.CharField(blank=True, max_length=100, null=True, verbose_name='上月结余')),
                ('tmonth_recharge', models.CharField(blank=True, max_length=100, null=True, verbose_name='本月充值')),
                ('tmonth_consumption', models.CharField(blank=True, max_length=100, null=True, verbose_name='本月消耗')),
                ('tmonth_balance', models.CharField(blank=True, max_length=100, null=True, verbose_name='本月结余')),
            ],
            options={
                'verbose_name': '财务报表',
                'verbose_name_plural': '财务报表',
                'db_table': 't_financial',
            },
        ),
        migrations.CreateModel(
            name='Funds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=100, verbose_name='账号')),
                ('name', models.CharField(max_length=100, verbose_name='账号名称')),
                ('bank', models.CharField(max_length=100, verbose_name='开户银行')),
            ],
            options={
                'verbose_name': '汇款账号管理',
                'verbose_name_plural': '汇款账号管理',
                'db_table': 't_funds',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(blank=True, null=True, verbose_name='日期')),
                ('name', models.CharField(max_length=255, verbose_name='发票抬头')),
                ('address', models.CharField(max_length=255, verbose_name='配送地址')),
                ('amount', models.IntegerField(verbose_name='发票金额')),
                ('application_time', models.DateTimeField(blank=True, null=True, verbose_name='申请时间')),
                ('tracking_number', models.CharField(max_length=255, verbose_name='快递单号')),
                ('status', models.CharField(choices=[('A', '未审核'), ('B', '待审核'), ('C', '待付款'), ('D', '已付款')], max_length=1, verbose_name='发票状态')),
                ('type', models.CharField(choices=[('A', '普通发票'), ('B', '增值税发票')], max_length=1, verbose_name='发票类型')),
                ('content', models.CharField(max_length=255, verbose_name='发票内容')),
            ],
            options={
                'verbose_name': '发票信息',
                'verbose_name_plural': '发票信息',
                'db_table': 't_invoice',
            },
        ),
        migrations.CreateModel(
            name='Recharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(blank=True, null=True, verbose_name='充值时间')),
                ('name', models.CharField(max_length=100, verbose_name='开户名称')),
                ('from_account', models.CharField(max_length=100, verbose_name='汇款账号')),
                ('to_account', models.CharField(max_length=100, verbose_name='支付账号')),
                ('amount', models.IntegerField(verbose_name='充值金额')),
                ('type', models.CharField(choices=[('A', '汇款转账'), ('B', '支付宝')], max_length=1, verbose_name='充值方式')),
                ('bank_info', models.CharField(max_length=100, verbose_name='银行信息')),
                ('branch_info', models.CharField(max_length=100, verbose_name='支行信息')),
            ],
            options={
                'verbose_name': '充值汇款',
                'verbose_name_plural': '充值汇款',
                'db_table': 't_recharge',
            },
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='退款金额')),
                ('type', models.CharField(choices=[('A', '汇款转账'), ('B', '支付宝')], max_length=1, verbose_name='退款方式')),
                ('name', models.CharField(max_length=100, verbose_name='开户名称')),
                ('account', models.CharField(max_length=100, verbose_name='银行账号')),
                ('bank_info', models.CharField(max_length=100, verbose_name='银行信息')),
                ('branch_info', models.CharField(max_length=100, verbose_name='支行信息')),
                ('info', models.CharField(max_length=100, verbose_name='退款说明')),
                ('time', models.DateTimeField(blank=True, null=True, verbose_name='退款时间')),
            ],
            options={
                'verbose_name': '退款记录',
                'verbose_name_plural': '退款记录',
                'db_table': 't_refund',
            },
        ),
    ]
