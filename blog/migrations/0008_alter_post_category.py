# Generated by Django 5.0 on 2025-04-22 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Economics', 'Economics'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('Maths', 'Maths')], default='Economics', max_length=9),
        ),
    ]
