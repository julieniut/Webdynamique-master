# Generated by Django 4.0.4 on 2022-05-14 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0003_alter_livre_imaurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livre',
            name='imaurl',
            field=models.URLField(default=200000, max_length=300),
            preserve_default=False,
        ),
    ]
