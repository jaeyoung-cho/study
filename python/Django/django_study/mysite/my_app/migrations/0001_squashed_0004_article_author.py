# Generated by Django 2.1 on 2018-10-18 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('my_app', '0001_initial'), ('my_app', '0002_article'), ('my_app', '0003_author'), ('my_app', '0004_article_author')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeStampedModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flavor',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='my_app.TimeStampedModel')),
                ('title', models.CharField(max_length=200)),
            ],
            bases=('my_app.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.Author'),
            preserve_default=False,
        ),
    ]