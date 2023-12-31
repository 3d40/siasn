from rest_framework import routers, serializers, viewsets
from intaian.models import *


# Serializers define the API representation.
class DataUtamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datautama
        fields = ('id', 'idpns', 'nipbaru', 'niplama', 'nama', 'gelardepan', 'gelarbelakang', 'tempatlahir', 'tempatlahirid', 'tgllahir', 
                  'agama', 'agamaid', 'email', 'emailgov', 'nik', 'alamat', 'nohp', 'notelp', 'jenispegawaiid', 'mktahun', 'mkbulan', 
                  'jenispegawainama', 'kedudukanpnsid', 'kedudukanpnsnama', 'statuspegawai', 'jeniskelamin', 'jenisiddokumenid', 
                  'jenisiddokumennama', 'nomoriddocument', 'noserikarpeg', 'tkpendidikanterakhirid', 'tkpendidikanterakhir', 'pendidikanterakhirid', 
                  'pendidikanterakhirnama', 'tahunlulus', 'tmtpns', 'tmtpensiun', 'buppensiun', 'tglskpns', 'tmtcpns', 'tglskcpns', 'instansiindukid', 
                  'instansiinduknama', 'satuankerjaindukid', 'satuankerjainduknama', 
                  'kanregid', 'kanregnama', 'instansikerjaid', 'instansikerjanama', 'instansikerjakodecepat', 'satuankerjakerjaid', 
                  'satuankerjakerjanama', 'unorid', 'unornama', 'unorindukid', 'unorinduknama', 'jenisjabatanid', 'jenisjabatan', 
                  'jabatannama', 'jabatanstrukturalid', 'jabatanstrukturalnama', 'jabatanfungsionalid', 'jabatanfungsionalnama', 
                  'jabatanfungsionalumumid', 'jabatanfungsionalumumnama', 'tmtjabatan', 'lokasikerjaid', 'lokasikerja', 'golruangawalid', 
                  'golruangawal', 'golruangakhirid', 'golruangakhir', 'tmtgolakhir', 'masakerja', 'eselon', 'eselonid', 'eselonlevel', 
                  'tmteselon', 'gajipokok', 'kpknid', 'kpknnama', 'ktuaid', 'ktuanama', 'taspenid', 'taspennama', 'jeniskawinid', 
                  'statusperkawinan', 'statushidup', 'tglsuratketerangandokter', 'nosuratketerangandokter', 'jumlahistrisuami', 'jumlahanak', 
                  'nosuratketeranganbebasnarkoba', 'tglsuratketeranganbebasnarkoba', 'skck', 'tglskck', 'aktekelahiran', 'aktemeninggal', 'tglmeninggal', 
                  'nonpwp', 'tglnpwp', 'noaskes', 'bpjs', 'kodepos', 'nospmt', 'notaspen', 'bahasa', 'kppnid', 'kppnnama', 'pangkatakhir', 'tglsttpl', 'nomorsttpl', 
                  'nomorskcpns', 'nomorskpns', 'jenjang', 'jabatanasn', 'kartuasn'
                  )


class pasanganSerializer(serializers.ModelSerializer):
    class Meta :
        model = ModelPasangan
        fields = ['id', 'idsiasn', 'ayahid', 'ibuid', 'nama', 'namaktp', 'gelardepan', 'gelarblk', 'tempatlahir', 'tgllahir', 'aktameninggal', 'tglmeninggal', 
                  'jeniskelamin', 'jenisanak', 'statushidup', 'jeniskawinid', 'statusnikah', 'datapernikahan_id', 'datapernikahan_orangid', 
                  'datapernikahan_pnsorangid', 'datapernikahan_tgglmenikah', 'datapernikahan_aktamenikah', 'datapernikahan_tgglcerai', 'datapernikahan_aktacerai', 
                  'datapernikahan_posisi', 'datapernikahan_status', 'datapernikahan_ispns', 'datapernikahan_noskpensiun'
        ]


class rwPangkatSerializer(serializers.ModelSerializer):
    class Meta :
        model = ModelRwgolongan
        fields = ['id', 'code', 'data_idsiasn', 'data_idpns', 'data_nipbaru', 'data_niplama', 'data_golonganid', 'data_golongan', 'data_sknomor', 'data_sktanggal', 
                  'data_tmtgolongan', 'data_nopertekbkn', 'data_tglpertekbkn', 'data_jumlahkreditutama', 'data_jumlahkredittambahan', 'data_jeniskpid', 
                  'data_jeniskpnama', 'data_masakerjagolongantahun', 'data_masakerjagolonganbulan', 'data_path_858_dok_id', 'data_path_858_dok_nama', 
                  'data_path_858_dok_uri', 'data_path_858_object', 'data_path_858_slug', 'data_path']
        
