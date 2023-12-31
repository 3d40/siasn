# Generated by Django 3.2.20 on 2023-08-01 04:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('intaian', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelRwgolongan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.TextField(blank=True, null=True)),
                ('data_idsiasn', models.TextField(blank=True, null=True)),
                ('data_idpns', models.TextField(blank=True, db_column='data_idPns', null=True)),
                ('data_nipbaru', models.TextField(blank=True, db_column='data_nipBaru', null=True)),
                ('data_niplama', models.TextField(blank=True, db_column='data_nipLama', null=True)),
                ('data_golonganid', models.IntegerField(blank=True, db_column='data_golonganId', null=True)),
                ('data_golongan', models.TextField(blank=True, null=True)),
                ('data_sknomor', models.TextField(blank=True, db_column='data_skNomor', null=True)),
                ('data_sktanggal', models.TextField(blank=True, db_column='data_skTanggal', null=True)),
                ('data_tmtgolongan', models.TextField(blank=True, db_column='data_tmtGolongan', null=True)),
                ('data_nopertekbkn', models.TextField(blank=True, db_column='data_noPertekBkn', null=True)),
                ('data_tglpertekbkn', models.TextField(blank=True, db_column='data_tglPertekBkn', null=True)),
                ('data_jumlahkreditutama', models.IntegerField(blank=True, db_column='data_jumlahKreditUtama', null=True)),
                ('data_jumlahkredittambahan', models.IntegerField(blank=True, db_column='data_jumlahKreditTambahan', null=True)),
                ('data_jeniskpid', models.TextField(blank=True, db_column='data_jenisKPId', null=True)),
                ('data_jeniskpnama', models.TextField(blank=True, db_column='data_jenisKPNama', null=True)),
                ('data_masakerjagolongantahun', models.TextField(blank=True, db_column='data_masaKerjaGolonganTahun', null=True)),
                ('data_masakerjagolonganbulan', models.TextField(blank=True, db_column='data_masaKerjaGolonganBulan', null=True)),
                ('data_path_858_dok_id', models.TextField(blank=True, default='None', null=True)),
                ('data_path_858_dok_nama', models.TextField(blank=True, default='None', null=True)),
                ('data_path_858_dok_uri', models.TextField(blank=True, default='None', null=True)),
                ('data_path_858_object', models.TextField(blank=True, default='None', null=True)),
                ('data_path_858_slug', models.TextField(blank=True, default='None', null=True)),
                ('data_path', models.TextField(blank=True, default='None', null=True)),
            ],
            options={
                'db_table': 'RwGolongan',
                'managed': False,
            },
        ),
    ]
