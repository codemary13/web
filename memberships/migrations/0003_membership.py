# Generated by Django 3.0.7 on 2020-07-24 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0002_member_stripe_customer_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(null=True)),
                ('stripe_subscription_id', models.CharField(max_length=255)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memberships.Member')),
            ],
        ),
    ]