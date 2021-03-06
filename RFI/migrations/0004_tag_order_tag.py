# Generated by Django 4.0.2 on 2022-02-13 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RFI', '0003_order_customer_order_product_alter_customer_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='tag',
            field=models.ManyToManyField(to='RFI.Tag'),
        ),
    ]
