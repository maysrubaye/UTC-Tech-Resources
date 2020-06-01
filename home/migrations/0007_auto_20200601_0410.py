# Generated by Django 2.2.9 on 2020-06-01 04:10

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200601_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='country_q_options',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='first_q_options',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='gpa_q_options',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='result',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='ten_year_q_options',
        ),
        migrations.AddField(
            model_name='quiz',
            name='esl_result',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='math_egl_result',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='no_test_result',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
