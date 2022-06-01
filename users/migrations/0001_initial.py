# Generated by Django 4.0 on 2022-01-01 13:48

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_driver', models.BooleanField(default=False, verbose_name='Driver')),
                ('is_passenger', models.BooleanField(default=False, verbose_name='Passenger')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin')),
                ('is_superadmin', models.BooleanField(default=False, verbose_name='Super Admin')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('other_name', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('creator', models.CharField(max_length=100)),
                ('createDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='EdQual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('creator', models.CharField(max_length=100)),
                ('createDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('creator', models.CharField(max_length=100)),
                ('createDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('creator', models.CharField(max_length=100)),
                ('createDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('creator', models.CharField(max_length=100)),
                ('createDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False, verbose_name='Active')),
                ('bio', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.user')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.role'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('otherName', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('matricNo', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('state', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('lga', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('phoneNumber', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('address', models.TextField()),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.gender')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('state', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('lga', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('otherName', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('nok', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('serialNumber', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('plateNumber', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('phoneNumber', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('address', models.TextField()),
                ('is_active', models.BooleanField(default=False, verbose_name='Active')),
                ('is_car_owner', models.BooleanField(default=False, verbose_name='Car Owner')),
                ('carType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.cartype')),
                ('edQlf', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.edqual')),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.gender')),
                ('maritalStatus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.maritalstatus')),
            ],
        ),
    ]