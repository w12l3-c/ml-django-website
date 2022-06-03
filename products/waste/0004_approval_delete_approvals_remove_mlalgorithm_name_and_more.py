# Generated by Django 4.0.2 on 2022-05-02 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_mlalgorithm_mlendpoint_mlrequest_mlalgorithmstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=15)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=15)),
                ('married', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15)),
                ('monthly_income', models.FloatField(default=0)),
                ('monthly_debt', models.FloatField(default=0)),
                ('revolving_utilization', models.FloatField(default=0)),
                ('thirty_to_fifty_nine_days_late', models.FloatField(default=0)),
                ('sixty_to_eighty_nine_days_late', models.FloatField(default=0)),
                ('ninety_days_late', models.FloatField(default=0)),
                ('dependents', models.IntegerField(default=0)),
                ('real_estate_loans', models.FloatField(default=0)),
                ('open_credit_lines_and_loans', models.FloatField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Approvals',
        ),
        migrations.RemoveField(
            model_name='mlalgorithm',
            name='name',
        ),
        migrations.AddField(
            model_name='mlalgorithm',
            name='firstname',
            field=models.CharField(default='Firstname', max_length=15),
        ),
        migrations.AddField(
            model_name='mlalgorithm',
            name='lastname',
            field=models.CharField(default='Lastname', max_length=15),
        ),
        migrations.AlterField(
            model_name='mlalgorithm',
            name='education',
            field=models.CharField(choices=[('Graduated', 'graduated'), ('Not_Graduate', 'not_graduated')], max_length=15),
        ),
        migrations.AlterField(
            model_name='mlalgorithm',
            name='married',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15),
        ),
        migrations.AlterField(
            model_name='mlalgorithm',
            name='property_area',
            field=models.CharField(choices=[('Urban', 'Urban'), ('Rural', 'Rural')], max_length=15),
        ),
        migrations.AlterField(
            model_name='mlalgorithm',
            name='self_employed',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15),
        ),
    ]