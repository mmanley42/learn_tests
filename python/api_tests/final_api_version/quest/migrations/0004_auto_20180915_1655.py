# Generated by Django 2.1.1 on 2018-09-15 14:55

from django.db import migrations, models
import quest.models


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0003_auto_20180915_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, validators=[quest.models.check_if_quest]),
        ),
    ]