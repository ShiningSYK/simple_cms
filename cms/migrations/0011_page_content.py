# Generated by Django 2.2 on 2019-07-04 08:38

from django.db import migrations
import ueditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_auto_20190704_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='content',
            field=ueditor.fields.RichTextField(null=True, verbose_name='内容'),
        ),
    ]
