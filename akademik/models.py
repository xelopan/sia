from django.db import models

JENIS_KELAMIN = (
    (0, 'Pria'),
    (1, 'Wanita'),
)
AGAMA = (
    (0, 'Islam'),
    (1, 'Kristen'),
    (2, 'Katolik'),
    (3, 'Hindu'),
    (4, 'Budha'),
)
HARI = (
    (0, 'Senin'),
    (1, 'Selasa'),
    (2, 'Rabu'),
    (3, 'Kamis'),
    (4, 'Jumat'),
    (5, 'Sabtu'),
    (6, 'Minggu'),
)


class Biodata(models.Model):
    nama = models.CharField(max_length=80)
    aktif = models.BooleanField(verbose_name='aktif?', default=True)
    jenis_kelamin = models.SmallIntegerField(choices=JENIS_KELAMIN)
    agama = models.SmallIntegerField(choices=AGAMA)
    tanggal_lahir = models.DateField()
    alamat = models.TextField()
    email = models.EmailField(max_length=255, default='', blank=True, null=True)
    nomor_telepon = models.CharField(max_length=25, default='', blank=True, null=True)
    keterangan = models.TextField(default='', blank=True, null=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.nama


class Jurusan(models.Model):
    nama = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'jurusan'

    def __unicode__(self):
        return self.nama


class Guru(Biodata):
    nik = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'guru'


class Kelas(models.Model):
    jurusan = models.ForeignKey(Jurusan)
    wali = models.ForeignKey(Guru)
    nama = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'kelas'

    def __unicode__(self):
        return self.nama


class Siswa(Biodata):
    kelas = models.ForeignKey(Kelas)
    nis = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'siswa'


class MataPelajaran(models.Model):
    jurusan = models.ManyToManyField(Jurusan, verbose_name='diajarkan pada')
    nama = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'mata pelajaran'

    def __unicode__(self):
        return self.nama


class Pengajaran(models.Model):
    mata_pelajaran = models.ForeignKey(MataPelajaran)
    kelas = models.ForeignKey(Kelas)
    pengajar = models.ForeignKey(Guru)

    class Meta:
        verbose_name_plural = 'pengajaran'

    def __unicode__(self):
        return '%s' % (self.mata_pelajaran,)


class Jadwal(models.Model):
    pengajaran = models.ForeignKey(Pengajaran)
    hari = models.SmallIntegerField(choices=HARI)
    mulai = models.TimeField()
    selesai = models.TimeField()

    class Meta:
        verbose_name_plural = 'jadwal'

    def __unicode__(self):
        return '%s' % (self.hari,)


class JenisAgenda(models.Model):
    nama = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'jenis agenda'

    def __unicode__(self):
        return self.nama


class KalenderAkademik(models.Model):
    jenis_agenda = models.ForeignKey(JenisAgenda)
    nama = models.CharField(max_length=255)
    keterangan = models.TextField()
    mulai = models.DateTimeField()
    akhir = models.DateTimeField()

    class Meta:
        ordering = ['-mulai', '-akhir']
        verbose_name_plural = 'kalender akademik'

    def __unicode__(self):
        return self.nama
