# Generated by Django 5.0.3 on 2024-04-20 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "update_time",
                    models.DateTimeField(auto_now=True, verbose_name="更新时间"),
                ),
                (
                    "project_name",
                    models.CharField(max_length=50, unique=True, verbose_name="项目名称"),
                ),
                (
                    "responsible_name",
                    models.CharField(max_length=20, verbose_name="负责人"),
                ),
                ("test_user", models.CharField(max_length=100, verbose_name="测试人员")),
                ("dev_user", models.CharField(max_length=100, verbose_name="开发人员")),
                ("publish_app", models.CharField(max_length=100, verbose_name="发布应用")),
                (
                    "simple_desc",
                    models.CharField(max_length=100, null=True, verbose_name="简要描述"),
                ),
                (
                    "other_desc",
                    models.CharField(max_length=100, null=True, verbose_name="其他信息"),
                ),
            ],
            options={
                "verbose_name": "项目信息",
                "db_table": "ProjectInfo",
            },
        ),
    ]
