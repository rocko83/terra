# Generated by Django 2.0.4 on 2018-04-12 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20171229_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
