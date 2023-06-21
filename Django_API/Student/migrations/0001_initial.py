# Generated by Django 4.2.2 on 2023-06-21 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('StudentID', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('DateOfBirth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('SubjectID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Coefficient', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.students')),
                ('Subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.subjects')),
            ],
        ),
    ]
