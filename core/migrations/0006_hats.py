# Generated by Django 2.2.14 on 2021-04-26 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210425_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('category', models.CharField(choices=[('S', 'Shirt'), ('H', 'Hats'), ('HD', 'Hoodies')], max_length=2)),
                ('label', models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], max_length=1)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
