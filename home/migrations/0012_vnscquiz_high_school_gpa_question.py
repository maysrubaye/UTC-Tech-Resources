# Generated by Django 2.2.9 on 2020-11-21 19:00

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20201009_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='vnscquiz',
            name='high_school_gpa_question',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
