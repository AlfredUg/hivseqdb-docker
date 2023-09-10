# Generated by Django 3.2.16 on 2023-08-09 10:23

from django.db import migrations, models
import uploads.models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0003_auto_20230606_0841'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsensusSequence',
            fields=[
                ('projectID', models.AutoField(primary_key=True, serialize=False)),
                ('project_Name', models.CharField(max_length=50)),
                ('Region_Sequenced', models.CharField(max_length=50)),
                ('Sequencing_Technology', models.CharField(max_length=50)),
                ('Sequencing_Platform', models.CharField(max_length=50)),
                ('fasta_File', models.FileField(upload_to=uploads.models.project_upload_path)),
                ('sample_CSV_File', models.FileField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='sample',
            name='HLAtype',
        ),
    ]