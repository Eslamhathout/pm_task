# Generated by Django 2.1.15 on 2021-08-28 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0002_auto_20210828_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('delivery_method', models.CharField(blank=True, choices=[('home', 'Home'), ('office', 'Office'), ('pick-up-station', 'Pick-up-station')], default='home', help_text='How order should be delivered!', max_length=30)),
                ('payment_method', models.CharField(blank=True, choices=[('cod', 'Cash on delivery'), ('credit-card', 'Credit-Card'), ('wallet', 'Wallet')], default='cod', help_text='How order should be paid!', max_length=3)),
                ('dog', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalog.Dog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
