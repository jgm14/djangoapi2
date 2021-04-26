# Generated by Django 3.1.7 on 2021-04-13 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('first_name', models.CharField(db_column='FIRST_NAME', max_length=40)),
                ('last_name', models.CharField(db_column='LAST_NAME', max_length=40)),
                ('customer_id', models.AutoField(db_column='CUSTOMER_ID', primary_key=True, serialize=False)),
                ('phone_num', models.CharField(db_column='PHONE_NUM', max_length=11)),
                ('email_add', models.CharField(db_column='EMAIL_ADD', max_length=40)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('guest_id', models.AutoField(db_column='GUEST_ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'guest',
            },
        ),
        migrations.CreateModel(
            name='AllQueues',
            fields=[
                ('queue_id', models.AutoField(db_column='QUEUE_ID', primary_key=True, serialize=False)),
                ('queue_name', models.CharField(blank=True, db_column='QUEUE_NAME', max_length=100, null=True)),
                ('queue_desc', models.CharField(blank=True, db_column='QUEUE_DESC', max_length=100, null=True)),
                ('estimated_wait', models.IntegerField(blank=True, db_column='ESTIMATED_WAIT', null=True)),
                ('customer_id', models.ForeignKey(db_column='CUSTOMER_ID', default=None, on_delete=django.db.models.deletion.CASCADE, to='queueapi.customer')),
            ],
            options={
                'db_table': 'all_queues',
            },
        ),
        migrations.CreateModel(
            name='QueuingIn',
            fields=[
                ('queue_id', models.ForeignKey(db_column='QUEUE_ID', default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='queueapi.allqueues')),
                ('timestamp', models.DateTimeField(blank=True, db_column='TIMESTAMP', null=True)),
                ('guest_id', models.ForeignKey(db_column='GUEST_ID', default=None, on_delete=django.db.models.deletion.CASCADE, to='queueapi.guest')),
            ],
            options={
                'db_table': 'queuing_in',
            },
        ),
    ]