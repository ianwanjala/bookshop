# Generated by Django 4.1.5 on 2023-01-14 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20230114_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='town',
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.CharField(help_text='Enter your Town', max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.customer'),
        ),
        migrations.AddField(
            model_name='address',
            name='street_address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='zip_code',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='books',
            name='ISBN',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='books',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(help_text='Enter your first name', max_length=50, null=True),
        ),
    ]