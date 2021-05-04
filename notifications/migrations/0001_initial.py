# Generated by Django 3.2 on 2021-05-04 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0003_auto_20210504_1652'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=255)),
                ('redirect_to', models.URLField(max_length=255, null=True)),
                ('notification_type', models.CharField(choices=[('N', 'Notify'), ('NE', 'Notify With Email')], default='N', max_length=100)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='groups.group')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]