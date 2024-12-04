# Generated by Django 5.1.3 on 2024-12-02 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='شماره تلفن')),
                ('sub', models.CharField(blank=True, max_length=100, null=True, verbose_name='عنوان')),
                ('text', models.CharField(blank=True, max_length=1000, null=True, verbose_name='متن دیدگاه')),
            ],
            options={
                'verbose_name': 'ارتباط با ما',
                'verbose_name_plural': 'ارتباط با ما',
            },
        ),
    ]
