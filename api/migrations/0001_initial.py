# Generated by Django 4.1.2 on 2022-10-20 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(blank=True, max_length=240, null=True)),
                ('question_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('question_type', models.CharField(choices=[('MCQWithRadio', 'Radio'), ('MCQWithCheckBox', 'Checkbox'), ('Matrix', 'Matrix')], max_length=300)),
                ('question_order', models.IntegerField()),
                ('question_marks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='QuestionSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('slug', models.CharField(blank=True, max_length=120, null=True)),
                ('enable_neg_marking', models.BooleanField(default=False)),
                ('negative_marking_percentage', models.IntegerField()),
                ('ideal_time_to_complete', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GroupQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.question')),
            ],
            bases=('api.question',),
        ),
        migrations.CreateModel(
            name='QuestionOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_text', models.CharField(blank=True, max_length=240, null=True)),
                ('option_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('option_order', models.IntegerField(default=1)),
                ('correct_answer', models.BooleanField(default=False)),
                ('marks', models.IntegerField(blank=True, null=True)),
                ('id_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='id_questionset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.questionset'),
        ),
        migrations.CreateModel(
            name='groupInlineQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_order', models.IntegerField()),
                ('question_marks', models.IntegerField()),
                ('Id_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='api.question')),
                ('Id_group_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groupquestion', to='api.groupquestion')),
            ],
        ),
    ]
