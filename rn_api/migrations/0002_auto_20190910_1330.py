# Generated by Django 2.1.7 on 2019-09-10 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rn_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='breakfast',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='main',
            name='dinner',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='main',
            name='lunch',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='yangjin',
            name='breakfast',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='yangjin',
            name='dinner',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='yangjin',
            name='lunch',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='yangsung',
            name='breakfast',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='yangsung',
            name='dinner',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='yangsung',
            name='lunch',
            field=models.TextField(),
        ),
    ]
