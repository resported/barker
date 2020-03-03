# Generated by Django 3.0.3 on 2020-03-02 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200302_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='HumanGender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='gender',
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
    ]
