# Generated by Django 4.2.5 on 2023-10-03 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "base_blog_app",
            "0002_alter_article_published_alter_author_birthday_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="article",
            field=models.ForeignKey(
                default=4,
                on_delete=django.db.models.deletion.CASCADE,
                to="base_blog_app.article",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="author",
            field=models.ForeignKey(
                default=4,
                on_delete=django.db.models.deletion.CASCADE,
                to="base_blog_app.author",
            ),
        ),
    ]
