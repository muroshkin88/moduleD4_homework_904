# Generated by Django 4.2.5 on 2023-10-04 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0005_alter_post_authorarticle_alter_post_categorytype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
    ]
