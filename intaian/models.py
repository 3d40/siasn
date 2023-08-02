import uuid
from django.db import models

class Datautama(models.Model):
   id = models.UUIDField(default=uuid.uuid4, editable=False)
   idpns = models.TextField(primary_key=True,db_column='idpns')
   nipbaru = models.TextField(db_column='nipBaru', blank=True, null=True)  # Field name made lowercase.
   niplama = models.TextField(db_column='nipLama', blank=True, null=True)  # Field name made lowercase.
   nama = models.TextField(blank=True, null=True)
   gelardepan = models.TextField(db_column='gelarDepan', blank=True, null=True)  # Field name made lowercase.
   gelarbelakang = models.TextField(db_column='gelarBelakang', blank=True, null=True)  # Field name made lowercase.
   tempatlahir = models.TextField(db_column='tempatLahir', blank=True, null=True)  # Field name made lowercase.
   tempatlahirid = models.TextField(db_column='tempatLahirId', blank=True, null=True)  # Field name made lowercase.
   tgllahir = models.TextField(db_column='tglLahir', blank=True, null=True)  # Field name made lowercase.
   agama = models.TextField(blank=True, null=True)
   agamaid = models.IntegerField(db_column='agamaId', blank=True, null=True)  # Field name made lowercase.
   email = models.TextField(blank=True, null=True)
   emailgov = models.TextField(db_column='emailGov', blank=True, null=True)  # Field name made lowercase.
   nik = models.TextField(blank=True, null=True)
   alamat = models.TextField(blank=True, null=True)
   nohp = models.TextField(db_column='noHp', blank=True, null=True)  # Field name made lowercase.
   notelp = models.TextField(db_column='noTelp', blank=True, null=True)  # Field name made lowercase.
   jenispegawaiid = models.IntegerField(db_column='jenisPegawaiId', blank=True, null=True)  # Field name made lowercase.
   mktahun = models.IntegerField(db_column='mkTahun', blank=True, null=True)  # Field name made lowercase.
   mkbulan = models.IntegerField(db_column='mkBulan', blank=True, null=True)  # Field name made lowercase.
   jenispegawainama = models.TextField(db_column='jenisPegawaiNama', blank=True,
                                       null=True)  # Field name made lowercase.
   kedudukanpnsid = models.IntegerField(db_column='kedudukanPnsId', blank=True, null=True)  # Field name made lowercase.
   kedudukanpnsnama = models.TextField(db_column='kedudukanPnsNama', blank=True,
                                       null=True)  # Field name made lowercase.
   statuspegawai = models.TextField(db_column='statusPegawai', blank=True, null=True)  # Field name made lowercase.
   jeniskelamin = models.TextField(db_column='jenisKelamin', blank=True, null=True)  # Field name made lowercase.
   jenisiddokumenid = models.IntegerField(db_column='jenisIdDokumenId', blank=True,
                                          null=True)  # Field name made lowercase.
   jenisiddokumennama = models.TextField(db_column='jenisIdDokumenNama', blank=True,
                                         null=True)  # Field name made lowercase.
   nomoriddocument = models.TextField(db_column='nomorIdDocument', blank=True, null=True)  # Field name made lowercase.
   noserikarpeg = models.TextField(db_column='noSeriKarpeg', blank=True, null=True)  # Field name made lowercase.
   tkpendidikanterakhirid = models.IntegerField(db_column='tkPendidikanTerakhirId', blank=True,
                                                null=True)  # Field name made lowercase.
   tkpendidikanterakhir = models.TextField(db_column='tkPendidikanTerakhir', blank=True,
                                           null=True)  # Field name made lowercase.
   pendidikanterakhirid = models.TextField(db_column='pendidikanTerakhirId', blank=True,
                                           null=True)  # Field name made lowercase.
   pendidikanterakhirnama = models.TextField(db_column='pendidikanTerakhirNama', blank=True,
                                             null=True)  # Field name made lowercase.
   tahunlulus = models.TextField(db_column='tahunLulus', blank=True, null=True)  # Field name made lowercase.
   tmtpns = models.TextField(db_column='tmtPns', blank=True, null=True)  # Field name made lowercase.
   tmtpensiun = models.TextField(db_column='tmtPensiun', blank=True, null=True)  # Field name made lowercase.
   buppensiun = models.IntegerField(db_column='bupPensiun', blank=True, null=True)  # Field name made lowercase.
   tglskpns = models.TextField(db_column='tglSkPns', blank=True, null=True)  # Field name made lowercase.
   tmtcpns = models.TextField(db_column='tmtCpns', blank=True, null=True)  # Field name made lowercase.
   tglskcpns = models.TextField(db_column='tglSkCpns', blank=True, null=True)  # Field name made lowercase.
   instansiindukid = models.TextField(db_column='instansiIndukId', blank=True, null=True)  # Field name made lowercase.
   instansiinduknama = models.TextField(db_column='instansiIndukNama', blank=True,
                                        null=True)  # Field name made lowercase.
   satuankerjaindukid = models.TextField(db_column='satuanKerjaIndukId', blank=True,
                                         null=True)  # Field name made lowercase.
   satuankerjainduknama = models.TextField(db_column='satuanKerjaIndukNama', blank=True,
                                           null=True)  # Field name made lowercase.
   kanregid = models.IntegerField(db_column='kanregId', blank=True, null=True)  # Field name made lowercase.
   kanregnama = models.TextField(db_column='kanregNama', blank=True, null=True)  # Field name made lowercase.
   instansikerjaid = models.TextField(db_column='instansiKerjaId', blank=True, null=True)  # Field name made lowercase.
   instansikerjanama = models.TextField(db_column='instansiKerjaNama', blank=True,
                                        null=True)  # Field name made lowercase.
   instansikerjakodecepat = models.IntegerField(db_column='instansiKerjaKodeCepat', blank=True,
                                                null=True)  # Field name made lowercase.
   satuankerjakerjaid = models.TextField(db_column='satuanKerjaKerjaId', blank=True,
                                         null=True)  # Field name made lowercase.
   satuankerjakerjanama = models.TextField(db_column='satuanKerjaKerjaNama', blank=True,
                                           null=True)  # Field name made lowercase.
   unorid = models.TextField(db_column='unorId', blank=True, null=True)  # Field name made lowercase.
   unornama = models.TextField(db_column='unorNama', blank=True, null=True)  # Field name made lowercase.
   unorindukid = models.TextField(db_column='unorIndukId', blank=True, null=True)  # Field name made lowercase.
   unorinduknama = models.TextField(db_column='unorIndukNama', blank=True, null=True)  # Field name made lowercase.
   jenisjabatanid = models.IntegerField(db_column='jenisJabatanId', blank=True, null=True)  # Field name made lowercase.
   jenisjabatan = models.TextField(db_column='jenisJabatan', blank=True, null=True)  # Field name made lowercase.
   jabatannama = models.TextField(db_column='jabatanNama', blank=True, null=True)  # Field name made lowercase.
   jabatanstrukturalid = models.TextField(db_column='jabatanStrukturalId', blank=True,
                                          null=True)  # Field name made lowercase.
   jabatanstrukturalnama = models.TextField(db_column='jabatanStrukturalNama', blank=True,
                                            null=True)  # Field name made lowercase.
   jabatanfungsionalid = models.TextField(db_column='jabatanFungsionalId', blank=True,
                                          null=True)  # Field name made lowercase.
   jabatanfungsionalnama = models.TextField(db_column='jabatanFungsionalNama', blank=True,
                                            null=True)  # Field name made lowercase.
   jabatanfungsionalumumid = models.TextField(db_column='jabatanFungsionalUmumId', blank=True,
                                              null=True)  # Field name made lowercase.
   jabatanfungsionalumumnama = models.TextField(db_column='jabatanFungsionalUmumNama', blank=True,
                                                null=True)  # Field name made lowercase.
   tmtjabatan = models.TextField(db_column='tmtJabatan', blank=True, null=True)  # Field name made lowercase.
   lokasikerjaid = models.TextField(db_column='lokasiKerjaId', blank=True, null=True)  # Field name made lowercase.
   lokasikerja = models.TextField(db_column='lokasiKerja', blank=True, null=True)  # Field name made lowercase.
   golruangawalid = models.IntegerField(db_column='golRuangAwalId', blank=True, null=True)  # Field name made lowercase.
   golruangawal = models.TextField(db_column='golRuangAwal', blank=True, null=True)  # Field name made lowercase.
   golruangakhirid = models.IntegerField(db_column='golRuangAkhirId', blank=True,
                                         null=True)  # Field name made lowercase.
   golruangakhir = models.TextField(db_column='golRuangAkhir', blank=True, null=True)  # Field name made lowercase.
   tmtgolakhir = models.TextField(db_column='tmtGolAkhir', blank=True, null=True)  # Field name made lowercase.
   masakerja = models.TextField(db_column='masaKerja', blank=True, null=True)  # Field name made lowercase.
   eselon = models.TextField(blank=True, null=True)
   eselonid = models.TextField(db_column='eselonId', blank=True, null=True)  # Field name made lowercase.
   eselonlevel = models.TextField(db_column='eselonLevel', blank=True, null=True)  # Field name made lowercase.
   tmteselon = models.TextField(db_column='tmtEselon', blank=True, null=True)  # Field name made lowercase.
   gajipokok = models.TextField(db_column='gajiPokok', blank=True, null=True)  # Field name made lowercase.
   kpknid = models.TextField(db_column='kpknId', blank=True, null=True)  # Field name made lowercase.
   kpknnama = models.TextField(db_column='kpknNama', blank=True, null=True)  # Field name made lowercase.
   ktuaid = models.TextField(db_column='ktuaId', blank=True, null=True)  # Field name made lowercase.
   ktuanama = models.TextField(db_column='ktuaNama', blank=True, null=True)  # Field name made lowercase.
   taspenid = models.TextField(db_column='taspenId', blank=True, null=True)  # Field name made lowercase.
   taspennama = models.TextField(db_column='taspenNama', blank=True, null=True)  # Field name made lowercase.
   jeniskawinid = models.IntegerField(db_column='jenisKawinId', blank=True, null=True)  # Field name made lowercase.
   statusperkawinan = models.TextField(db_column='statusPerkawinan', blank=True,
                                       null=True)  # Field name made lowercase.
   statushidup = models.IntegerField(db_column='statusHidup', blank=True, null=True)  # Field name made lowercase.
   tglsuratketerangandokter = models.TextField(db_column='tglSuratKeteranganDokter', blank=True,
                                               null=True)  # Field name made lowercase.
   nosuratketerangandokter = models.TextField(db_column='noSuratKeteranganDokter', blank=True,
                                              null=True)  # Field name made lowercase.
   jumlahistrisuami = models.TextField(db_column='jumlahIstriSuami', blank=True,
                                       null=True)  # Field name made lowercase.
   jumlahanak = models.TextField(db_column='jumlahAnak', blank=True, null=True)  # Field name made lowercase.
   nosuratketeranganbebasnarkoba = models.TextField(db_column='noSuratKeteranganBebasNarkoba', blank=True,
                                                    null=True)  # Field name made lowercase.
   tglsuratketeranganbebasnarkoba = models.TextField(db_column='tglSuratKeteranganBebasNarkoba', blank=True,
                                                     null=True)  # Field name made lowercase.
   skck = models.TextField(blank=True, null=True)
   tglskck = models.TextField(db_column='tglSkck', blank=True, null=True)  # Field name made lowercase.
   aktekelahiran = models.TextField(db_column='akteKelahiran', blank=True, null=True)  # Field name made lowercase.
   aktemeninggal = models.TextField(db_column='akteMeninggal', blank=True, null=True)  # Field name made lowercase.
   tglmeninggal = models.TextField(db_column='tglMeninggal', blank=True, null=True)  # Field name made lowercase.
   nonpwp = models.TextField(db_column='noNpwp', blank=True, null=True)  # Field name made lowercase.
   tglnpwp = models.TextField(db_column='tglNpwp', blank=True, null=True)  # Field name made lowercase.
   noaskes = models.TextField(db_column='noAskes', blank=True, null=True)  # Field name made lowercase.
   bpjs = models.TextField(blank=True, null=True)
   kodepos = models.TextField(db_column='kodePos', blank=True, null=True)  # Field name made lowercase.
   nospmt = models.TextField(db_column='noSpmt', blank=True, null=True)  # Field name made lowercase.
   notaspen = models.TextField(db_column='noTaspen', blank=True, null=True)  # Field name made lowercase.
   bahasa = models.TextField(blank=True, null=True)
   kppnid = models.TextField(db_column='kppnId', blank=True, null=True)  # Field name made lowercase.
   kppnnama = models.TextField(db_column='kppnNama', blank=True, null=True)  # Field name made lowercase.
   pangkatakhir = models.TextField(db_column='pangkatAkhir', blank=True, null=True)  # Field name made lowercase.
   tglsttpl = models.TextField(db_column='tglSttpl', blank=True, null=True)  # Field name made lowercase.
   nomorsttpl = models.TextField(db_column='nomorSttpl', blank=True, null=True)  # Field name made lowercase.
   nomorskcpns = models.TextField(db_column='nomorSkCpns', blank=True, null=True)  # Field name made lowercase.
   nomorskpns = models.TextField(db_column='nomorSkPns', blank=True, null=True)  # Field name made lowercase.
   jenjang = models.TextField(blank=True, null=True)
   jabatanasn = models.TextField(db_column='jabatanAsn', blank=True, null=True)  # Field name made lowercase.
   kartuasn = models.TextField(db_column='kartuAsn', blank=True, null=True)  # Field name made lowercase.
   
   def __str__(self):
       return self.nipbaru +' - '+ self.nama

   class Meta:
      managed = False
      db_table = 'DataUtama'
      

class ModelRwgolongan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.TextField(blank=True, null=True)
    data_idsiasn = models.TextField(blank=True, null=True)
    data_idpns = models.TextField(db_column='data_idPns', blank=True, null=True)  # Field name made lowercase.
    data_nipbaru = models.TextField(db_column='data_nipBaru', blank=True, null=True)  # Field name made lowercase.
    data_niplama = models.TextField(db_column='data_nipLama', blank=True, null=True)  # Field name made lowercase.
    data_golonganid = models.IntegerField(db_column='data_golonganId', blank=True, null=True)  # Field name made lowercase.
    data_golongan = models.TextField(blank=True, null=True)
    data_sknomor = models.TextField(db_column='data_skNomor', blank=True, null=True)  # Field name made lowercase.
    data_sktanggal = models.TextField(db_column='data_skTanggal', blank=True, null=True)  # Field name made lowercase.
    data_tmtgolongan = models.TextField(db_column='data_tmtGolongan', blank=True, null=True)  # Field name made lowercase.
    data_nopertekbkn = models.TextField(db_column='data_noPertekBkn', blank=True, null=True)  # Field name made lowercase.
    data_tglpertekbkn = models.TextField(db_column='data_tglPertekBkn', blank=True, null=True)  # Field name made lowercase.
    data_jumlahkreditutama = models.IntegerField(db_column='data_jumlahKreditUtama', blank=True, null=True)  # Field name made lowercase.
    data_jumlahkredittambahan = models.IntegerField(db_column='data_jumlahKreditTambahan', blank=True, null=True)  # Field name made lowercase.
    data_jeniskpid = models.TextField(db_column='data_jenisKPId', blank=True, null=True)  # Field name made lowercase.
    data_jeniskpnama = models.TextField(db_column='data_jenisKPNama', blank=True, null=True)  # Field name made lowercase.
    data_masakerjagolongantahun = models.TextField(db_column='data_masaKerjaGolonganTahun', blank=True, null=True)  # Field name made lowercase.
    data_masakerjagolonganbulan = models.TextField(db_column='data_masaKerjaGolonganBulan', blank=True, null=True)  # Field name made lowercase.
    data_path_858_dok_id = models.TextField(blank=True, null=True)
    data_path_858_dok_nama = models.TextField(blank=True, null=True)
    data_path_858_dok_uri = models.TextField(blank=True, null=True)
    data_path_858_object = models.TextField(blank=True, null=True)
    data_path_858_slug = models.TextField(blank=True, null=True)
    data_path = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RwGolongan'

class ModelPasangan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idsiasn = models.ForeignKey('Datautama', on_delete=models.CASCADE, editable=False)
    ayahid = models.TextField(db_column='ayahId', blank=True, null=True)  # Field name made lowercase.
    ibuid = models.TextField(db_column='ibuId', blank=True, null=True)  # Field name made lowercase.
    nama = models.TextField(blank=True, null=True)
    namaktp = models.TextField(db_column='namaKtp', blank=True, null=True)  # Field name made lowercase.
    gelardepan = models.TextField(db_column='gelarDepan', blank=True, null=True)  # Field name made lowercase.
    gelarblk = models.TextField(db_column='gelarBlk', blank=True, null=True)  # Field name made lowercase.
    tempatlahir = models.TextField(db_column='tempatLahir', blank=True, null=True)  # Field name made lowercase.
    tgllahir = models.TextField(db_column='tglLahir', blank=True, null=True)  # Field name made lowercase.
    aktameninggal = models.TextField(db_column='aktaMeninggal', blank=True, null=True)  # Field name made lowercase.
    tglmeninggal = models.TextField(db_column='tglMeninggal', blank=True, null=True)  # Field name made lowercase.
    jeniskelamin = models.TextField(db_column='jenisKelamin', blank=True, null=True)  # Field name made lowercase.
    jenisanak = models.TextField(db_column='jenisAnak', blank=True, null=True)  # Field name made lowercase.
    statushidup = models.TextField(db_column='StatusHidup', blank=True, null=True)  # Field name made lowercase.
    jeniskawinid = models.IntegerField(db_column='JenisKawinId', blank=True, null=True)  # Field name made lowercase.
    statusnikah = models.TextField(db_column='statusNikah', blank=True, null=True)  # Field name made lowercase.
    datapernikahan_id = models.TextField(db_column='dataPernikahan_id', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    datapernikahan_orangid = models.TextField(db_column='dataPernikahan_orangId', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    datapernikahan_pnsorangid = models.TextField(db_column='datapernikahan_pnsorangid', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    datapernikahan_tgglmenikah = models.TextField(db_column='dataPernikahan_tgglMenikah', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    datapernikahan_aktamenikah = models.TextField(db_column='dataPernikahan_aktaMenikah', blank=True, null=True)  # Field name made lowercase.
    datapernikahan_tgglcerai = models.TextField(db_column='dataPernikahan_tgglCerai', blank=True, null=True)  # Field name made lowercase.
    datapernikahan_aktacerai = models.TextField(db_column='dataPernikahan_aktaCerai', blank=True, null=True)  # Field name made lowercase.
    datapernikahan_posisi = models.IntegerField(db_column='dataPernikahan_posisi', blank=True, null=True)  # Field name made lowercase.
    datapernikahan_status = models.IntegerField(db_column='dataPernikahan_status', blank=True, null=True)  # Field name made lowercase.
    datapernikahan_ispns = models.TextField(db_column='dataPernikahan_isPns', blank=True, null=True)  # Field name made lowercase.
    datapernikahan_noskpensiun = models.TextField(db_column='dataPernikahan_noSkPensiun', blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        return self.idsiasn

    class Meta:
        managed = False
        db_table = 'Pasangan'