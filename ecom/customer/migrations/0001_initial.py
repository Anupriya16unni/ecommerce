# Generated by Django 4.0.2 on 2022-04-27 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0003_reseller'),
        ('reseller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.reseller')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reseller.product')),
            ],
        ),
    ]
