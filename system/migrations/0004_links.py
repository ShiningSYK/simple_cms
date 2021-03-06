# Generated by Django 2.2 on 2019-07-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_navbar_sort'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='名称')),
                ('url', models.URLField(max_length=256, verbose_name='链接')),
                ('sort', models.IntegerField(default=0, help_text='值越小排越前', verbose_name='排序')),
                ('type', models.IntegerField(choices=[(0, 'QQ'), (1, '微信'), (2, '邮箱'), (3, '手机'), (4, '其他')], default=0, verbose_name='类型')),
            ],
            options={
                'verbose_name': '友链',
                'verbose_name_plural': '友链管理',
            },
        ),
    ]
