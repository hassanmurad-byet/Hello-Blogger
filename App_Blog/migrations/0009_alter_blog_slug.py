# Generated by Django 5.0.3 on 2024-03-25 19:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("App_Blog", "0008_alter_blog_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="slug",
            field=models.SlugField(max_length=264, unique=True),
        ),
    ]
