from django.db import models

class DataSiswa(models.Model):
    Nama = models.CharField(max_length = 20, null=True)
    NIS = models.CharField(max_length=10, null=True)
    Status_Aktif = models.BooleanField()
    JENIS_KELAMIN = (
        ('P', 'Pria'),
        ('W', 'Wanita'),
        )
    AGAMA = (
        ('IM', 'Islam'),
        ('KR', 'Kristen'),
        ('KT','Katolik'),
        ('HD', 'Hindu'),
        ('BD', 'Budha'),
        )
    Jenis_Kelamin = models.CharField(max_length=20, choices=JENIS_KELAMIN)
    Agama = models.CharField(max_length=20, choices=AGAMA)
    TTL = models.DateField()
    Alamat = models.TextField()
    Email = models.EmailField(max_length = 50)
    No_Tlp = models.BigIntegerField()
    Keterangan = models.TextField()

    def __unicode__(self):
        return self.Nama

class Prodi(models.Model):
    Nama_Prodi = models.CharField(max_length=50)
    Jurusan = models.CharField(max_length=50)

    def __unicode__(self):
        return self.Nama_Prodi

class MataPelajaran(models.Model):
    MataPelajaran = models.ForeignKey(Prodi)
    Nama_matPelajaran = models.CharField(max_length=100)
  # SKS = models.BigIntegerField()

    def __unicode__(self):
        return self.Nama_matPelajaran
