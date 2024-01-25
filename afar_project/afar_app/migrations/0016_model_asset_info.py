# Generated by Django 4.2.6 on 2023-12-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afar_app', '0015_remove_input_field_depriciation_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='model_asset_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('economic_code', models.IntegerField()),
                ('expected_life_pre', models.IntegerField()),
                ('expected_life_post', models.IntegerField()),
                ('depreciation_method', models.CharField(max_length=100)),
            ],
        ),
    ]
