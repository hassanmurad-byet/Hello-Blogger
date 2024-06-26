# Generated by Django 5.0.3 on 2024-03-20 19:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("App_Blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={"ordering": ("-publish_date",)},
        ),
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ("-comment_date",)},
        ),
        migrations.AlterField(
            model_name="blog",
            name="blog_image",
            field=models.ImageField(blank=True, null=True, upload_to="blog_images/"),
        ),
    ]
