# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Jurusan'
        db.create_table(u'akademik_jurusan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'akademik', ['Jurusan'])

        # Adding model 'Guru'
        db.create_table(u'akademik_guru', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('aktif', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('jenis_kelamin', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('agama', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('tanggal_lahir', self.gf('django.db.models.fields.DateField')()),
            ('alamat', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(default='', max_length=255, null=True, blank=True)),
            ('nomor_telepon', self.gf('django.db.models.fields.CharField')(default='', max_length=25, null=True, blank=True)),
            ('keterangan', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('nik', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'akademik', ['Guru'])

        # Adding model 'Kelas'
        db.create_table(u'akademik_kelas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('jurusan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['akademik.Jurusan'])),
            ('wali', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['akademik.Guru'])),
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'akademik', ['Kelas'])

        # Adding model 'Siswa'
        db.create_table(u'akademik_siswa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('aktif', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('jenis_kelamin', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('agama', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('tanggal_lahir', self.gf('django.db.models.fields.DateField')()),
            ('alamat', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(default='', max_length=255, null=True, blank=True)),
            ('nomor_telepon', self.gf('django.db.models.fields.CharField')(default='', max_length=25, null=True, blank=True)),
            ('keterangan', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('kelas', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['akademik.Kelas'])),
            ('nis', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'akademik', ['Siswa'])

        # Adding model 'MataPelajaran'
        db.create_table(u'akademik_matapelajaran', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nama', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'akademik', ['MataPelajaran'])

        # Adding M2M table for field jurusan on 'MataPelajaran'
        m2m_table_name = db.shorten_name(u'akademik_matapelajaran_jurusan')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('matapelajaran', models.ForeignKey(orm[u'akademik.matapelajaran'], null=False)),
            ('jurusan', models.ForeignKey(orm[u'akademik.jurusan'], null=False))
        ))
        db.create_unique(m2m_table_name, ['matapelajaran_id', 'jurusan_id'])

        # Adding model 'JenisAgenda'
        db.create_table(u'akademik_jenisagenda', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nama', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'akademik', ['JenisAgenda'])

        # Adding model 'KalenderAkademik'
        db.create_table(u'akademik_kalenderakademik', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('jenis_agenda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['akademik.JenisAgenda'])),
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('keterangan', self.gf('django.db.models.fields.TextField')()),
            ('mulai', self.gf('django.db.models.fields.DateTimeField')()),
            ('akhir', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'akademik', ['KalenderAkademik'])


    def backwards(self, orm):
        # Deleting model 'Jurusan'
        db.delete_table(u'akademik_jurusan')

        # Deleting model 'Guru'
        db.delete_table(u'akademik_guru')

        # Deleting model 'Kelas'
        db.delete_table(u'akademik_kelas')

        # Deleting model 'Siswa'
        db.delete_table(u'akademik_siswa')

        # Deleting model 'MataPelajaran'
        db.delete_table(u'akademik_matapelajaran')

        # Removing M2M table for field jurusan on 'MataPelajaran'
        db.delete_table(db.shorten_name(u'akademik_matapelajaran_jurusan'))

        # Deleting model 'JenisAgenda'
        db.delete_table(u'akademik_jenisagenda')

        # Deleting model 'KalenderAkademik'
        db.delete_table(u'akademik_kalenderakademik')


    models = {
        u'akademik.guru': {
            'Meta': {'object_name': 'Guru'},
            'agama': ('django.db.models.fields.SmallIntegerField', [], {}),
            'aktif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'alamat': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jenis_kelamin': ('django.db.models.fields.SmallIntegerField', [], {}),
            'keterangan': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'nik': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'nomor_telepon': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'tanggal_lahir': ('django.db.models.fields.DateField', [], {})
        },
        u'akademik.jenisagenda': {
            'Meta': {'object_name': 'JenisAgenda'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'akademik.jurusan': {
            'Meta': {'object_name': 'Jurusan'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'akademik.kalenderakademik': {
            'Meta': {'object_name': 'KalenderAkademik'},
            'akhir': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jenis_agenda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['akademik.JenisAgenda']"}),
            'keterangan': ('django.db.models.fields.TextField', [], {}),
            'mulai': ('django.db.models.fields.DateTimeField', [], {}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'akademik.kelas': {
            'Meta': {'object_name': 'Kelas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jurusan': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['akademik.Jurusan']"}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'wali': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['akademik.Guru']"})
        },
        u'akademik.matapelajaran': {
            'Meta': {'object_name': 'MataPelajaran'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jurusan': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['akademik.Jurusan']", 'symmetrical': 'False'}),
            'nama': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'akademik.siswa': {
            'Meta': {'object_name': 'Siswa'},
            'agama': ('django.db.models.fields.SmallIntegerField', [], {}),
            'aktif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'alamat': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jenis_kelamin': ('django.db.models.fields.SmallIntegerField', [], {}),
            'kelas': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['akademik.Kelas']"}),
            'keterangan': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'nis': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'nomor_telepon': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'tanggal_lahir': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['akademik']