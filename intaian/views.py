from django.shortcuts import render
from django.http import HttpResponse
import http.client
import json
from . import forms
from . models import * 
import pandas as pd

auth_conn = http.client.HTTPSConnection("apimws.bkn.go.id")
authorization_conn = http.client.HTTPSConnection("sso-siasn.bkn.go.id")
datautama = http.client.HTTPSConnection("apimws.bkn.go.id", 8243)

def ViewAuth(request):
    payload = 'grant_type=client_credentials'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic ZmZ1NXRzR0NsVV84Tm5TWE15NTFHWnVkSnlvYTpQZ09tUDl1RVgxWTZ6VUU5MktwX0ZFbDdIXzBh',
        'Cookie': 'pdns=1091068938.58148.0000'}
    auth_conn.request("POST", "/oauth2/token", payload, headers)
    res = auth_conn.getresponse()
    data = res.read()

    jsonauthtoken = json.loads(data.decode("utf-8"))
    tokenpertama = jsonauthtoken['access_token']
    #print(tokenpertama)
    return tokenpertama


def ViewAuthorization(request):
    payload = 'client_id=provjambiws&grant_type=password&username=198501292011011007&password=Sayangku85'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'SERVERID=keycloak-02|ZMCM2|ZMCMY'
    }
    authorization_conn.request("POST", "/auth/realms/public-siasn/protocol/openid-connect/token", payload, headers)
    res = authorization_conn.getresponse()
    data = res.read()

    jsonauthorizationstoken = json.loads(data.decode("utf-8"))
    tokenkedua = jsonauthorizationstoken["access_token"]
    #print(tokenkedua)
    return tokenkedua


def get_data(request):
    form = forms.FormNIp()
    nip = request.POST.get('nip')
    print(nip)
    if request.method == "POST":
        payload = ''
        headers = {
            'accept': 'application/json',
            'Auth': 'bearer ' + ViewAuthorization(request),
            'Authorization': 'Bearer ' + ViewAuth(request),
            'Cookie': 'ff8d625df24f2272ecde05bd53b814bc=adf347710c85a1a12688d6aad5ce27da; pdns=1091068938.58148.0000'
        }
        datautama.request("GET", "/apisiasn/1.0/pns/data-utama/" + nip, payload, headers)
        res = datautama.getresponse()
        data = res.read()

        xyz = json.loads(data.decode("utf-8"))
        x = xyz
        # create a form instance and populate it with data from the request:
        form = form
        sumber = x.get('data')
        if not Datautama.objects.filter(idpns=sumber.get('id')).exists():
            datautamainput = Datautama.objects.update_or_create(
                idpns =sumber.get( 'id' ),
                nipbaru =sumber.get( 'nipBaru' ),
                niplama=sumber.get( 'nipLama'),
                nama=sumber.get( 'nama'),
                gelardepan=sumber.get( 'gelarDepan'),
                gelarbelakang =sumber.get( 'gelarBelakang' ),
                tempatlahir=sumber.get( 'tempatLahir'),
                tempatlahirid=sumber.get( 'tempatLahirId'),
                tgllahir=sumber.get( 'tglLahir'),
                agama=sumber.get( 'agama'),
                agamaid=sumber.get( 'agamaId'),
                email=sumber.get( 'email'),
                emailgov=sumber.get( 'emailGov'),
                nik=sumber.get( 'nik'),
                alamat=sumber.get( 'alamat'),
                nohp=sumber.get( 'noHp'),
                notelp=sumber.get( 'noTelp'),
                jenispegawaiid=sumber.get( 'jenisPegawaiId'),
                mktahun=sumber.get( 'mkTahun'),
                mkbulan=sumber.get( 'mkBulan'),
                jenispegawainama=sumber.get( 'jenisPegawaiNama'),
                kedudukanpnsid=sumber.get( 'kedudukanPnsId'),
                kedudukanpnsnama =sumber.get( 'kedudukanPnsNama' ),
                statuspegawai =sumber.get( 'statusPegawai' ),
                jeniskelamin =sumber.get( 'jenisKelamin' ),
                jenisiddokumenid =sumber.get( 'jenisidDokumenId' ),
                jenisiddokumennama =sumber.get( 'jenisIdDokumennama' ),
                nomoriddocument =sumber.get( 'nomorIdDocument' ),
                noserikarpeg =sumber.get( 'noSeriKarpeg' ),
                tkpendidikanterakhirid =sumber.get( 'tkPendidikanTerakhirId' ),
                tkpendidikanterakhir =sumber.get( 'tkPendidikanTerakhir' ),
                pendidikanterakhirid =sumber.get( 'pendidikanTerakhirId' ),
                pendidikanterakhirnama =sumber.get( 'pendidikanTerakhirNama' ),
                tahunlulus =sumber.get( 'tahunLulus' ),
                tmtpns =sumber.get( 'tmtPns' ),
                tmtpensiun =sumber.get( 'tmtPensiun' ),
                buppensiun =sumber.get( 'bupPensiun' ),
                tglskpns =sumber.get( 'tglSkPns' ),
                tmtcpns =sumber.get( 'tmtCpns' ),
                tglskcpns =sumber.get( 'tglSkCpns' ),
                instansiindukid =sumber.get( 'instansiIndukId' ),
                instansiinduknama =sumber.get( 'instansiIndukNama' ),
                satuankerjaindukid =sumber.get( 'satuanKerjaIndukId' ),
                satuankerjainduknama =sumber.get( 'satuanKerjaIndukNama' ),
                kanregid = sumber.get('kanregId'), 
                kanregnama =sumber.get( 'kanregNama' ),
                instansikerjaid =sumber.get( 'instansiKerjaId' ),
                instansikerjanama =sumber.get( 'instansiKerjaNama' ),
                instansikerjakodecepat =sumber.get( 'instansiKerjaKodeCepat' ),
                satuankerjakerjaid =sumber.get( 'satuanKerjaKerjaId' ),
                satuankerjakerjanama =sumber.get( 'satuanKerjaKerjaNama' ),
                unorid =sumber.get( 'unorId' ),
                unornama =sumber.get( 'unorNama' ),
                unorindukid =sumber.get( 'unorIndukId' ),
                unorinduknama =sumber.get( 'unorIndukNama' ),
                jenisjabatanid =sumber.get( 'jenisJabatanId' ),
                jenisjabatan =sumber.get( 'jenisJabatan' ),
                jabatannama =sumber.get( 'jabatanNama' ),
                jabatanstrukturalid =sumber.get( 'jabatanStrukturalId' ),
                jabatanstrukturalnama =sumber.get( 'jabatanStrukturalNama' ),
                jabatanfungsionalid =sumber.get( 'jabatanFungsionalId' ),
                jabatanfungsionalnama =sumber.get( 'jabatanFungsionalNama' ),
                jabatanfungsionalumumid =sumber.get( 'jabatanFungsionalUmumId' ),
                jabatanfungsionalumumnama =sumber.get( 'jabatanFungsionalUmumNama' ),
                tmtjabatan =sumber.get( 'tmtJabatan' ),
                lokasikerjaid =sumber.get( 'lokasiKerjaId' ),
                lokasikerja =sumber.get( 'lokasiKerja' ),
                golruangawalid =sumber.get( 'golRuangAwalId' ),
                golruangawal =sumber.get( 'golRuangAwal' ),
                golruangakhirid =sumber.get( 'golRuangAkhirId' ),
                golruangakhir =sumber.get( 'golRuangAkhir' ),
                tmtgolakhir =sumber.get( 'tmtGolAkhir' ),
                masakerja =sumber.get( 'masaKerja' ),
                eselon =sumber.get( 'eselon' ),
                eselonid =sumber.get( 'eselonId' ),
                eselonlevel =sumber.get( 'eselonLevel' ),
                tmteselon =sumber.get( 'tmtEselon' ),
                gajipokok =sumber.get( 'gajiPokok' ),
                kpknid =sumber.get( 'kpknId' ),
                kpknnama =sumber.get( 'kpknNama' ),
                ktuaid =sumber.get( 'ktuaId' ),
                ktuanama =sumber.get( 'ktuaNama' ),
                taspenid =sumber.get( 'taspenId' ),
                taspennama =sumber.get( 'taspenNama' ),
                jeniskawinid =sumber.get( 'jeniskawinid' ),
                statusperkawinan =sumber.get( 'statusPerkawinan' ),
                statushidup =sumber.get( 'statusHidup' ),
                tglsuratketerangandokter =sumber.get( 'tglSuratKeteranganDokter' ),
                nosuratketerangandokter =sumber.get( 'noSuratKeteranganDokter' ),
                jumlahistrisuami =sumber.get( 'jumlahIstriSuami' ),
                jumlahanak =sumber.get( 'jumlahAnak' ),
                nosuratketeranganbebasnarkoba =sumber.get( 'noSuratKeteranganBebasNarkoba' ),
                tglsuratketeranganbebasnarkoba =sumber.get( 'tglSuratKeteranganBebasNarkoba' ),
                skck =sumber.get( 'skck' ),
                tglskck =sumber.get( 'tglSkck' ),
                aktekelahiran =sumber.get( 'akteKelahiran' ),
                aktemeninggal =sumber.get( 'akteMeninggal' ),
                tglmeninggal =sumber.get( 'tglMeninggal' ),
                nonpwp =sumber.get( 'noNpwp' ),
                tglnpwp =sumber.get( 'tglNpwp' ),
                noaskes =sumber.get( 'noAskes' ),
                bpjs =sumber.get( 'bpjs' ),
                kodepos =sumber.get( 'kodePos' ),
                nospmt =sumber.get( 'noSpmt' ),
                notaspen =sumber.get( 'noTaspen' ),
                bahasa =sumber.get( 'bahasa' ),
                kppnid =sumber.get( 'kppnId' ),
                kppnnama =sumber.get( 'kppnNama' ),
                pangkatakhir =sumber.get( 'pangkatAkhir' ),
                tglsttpl =sumber.get( 'tglSttpl' ),
                nomorsttpl =sumber.get( 'nomorSttpl' ),
                nomorskcpns =sumber.get( 'nomorSkCpns' ),
                nomorskpns =sumber.get( 'nomorSkPns' ),
                jenjang =sumber.get( 'jenjang' ),
                jabatanasn =sumber.get( 'jabatanAsn' ),
                kartuasn=sumber.get( 'kartuAsn'),
            )
        # check whether it's valid:
        return render(request, 'intaian/index.html', {'form': form, 'x': x, 'sumber':sumber})
    else:
        form : forms.FormNIp()
    return render(request, "intaian/index.html", {'form':form})



def get_rwgolongan(request):
    form = forms.FormNIp()
    nip = request.POST.get('nip')
    if request.method == "POST":
        payload = ''
        headers = {
            'accept': 'application/json',
            'Auth': 'bearer ' + ViewAuthorization(request),
            'Authorization': 'Bearer ' + ViewAuth(request),
            'Cookie': 'ff8d625df24f2272ecde05bd53b814bc=adf347710c85a1a12688d6aad5ce27da; pdns=1091068938.58148.0000'
        }
        datautama.request("GET", "/apisiasn/1.0/pns/rw-golongan/" + nip, payload, headers)
        res = datautama.getresponse()
        data = res.read()

        xyz = json.loads(data.decode("utf-8"))
        sumber = xyz.get('data')
        # print(xyz['data'])
        # print(xyz['data'][0]['path']['858']['slug'])
        
        # create a form instance and populate it with data from the request:
        form = form
        rwgolonganinput = ModelRwgolongan.objects.all()
        for hasil in sumber:
            if not ModelRwgolongan.objects.filter(data_idsiasn=hasil['id']).exists():
                rwgolonganinput.update_or_create(data_idsiasn = hasil['id'], data_idpns = hasil['idPns'], data_nipbaru = hasil['nipBaru'], 
                                                 data_niplama = hasil['nipLama'], data_golonganid = hasil['golonganId'], data_golongan = hasil['golongan'], 
                                                 data_sknomor = hasil['skNomor'], data_sktanggal = hasil['skTanggal'], data_tmtgolongan = hasil['tmtGolongan'], 
                                                 data_nopertekbkn = hasil['noPertekBkn'], data_tglpertekbkn = hasil['tglPertekBkn'], data_jumlahkreditutama = hasil['jumlahKreditUtama'], 
                                                 data_jumlahkredittambahan = hasil['jumlahKreditTambahan'], data_jeniskpid = hasil['jenisKPId'], data_jeniskpnama = hasil['jenisKPNama'], 
                                                 data_masakerjagolongantahun = hasil['masaKerjaGolonganTahun'], data_masakerjagolonganbulan = hasil['masaKerjaGolonganBulan'])
            pk = rwgolonganinput.get(data_idsiasn=hasil['id'])
            try :
                pk.data_path_858_dok_id = hasil['path']['858']['dok_id'], 
                pk.data_path_858_dok_nama = hasil['path']['858']['dok_nama'], 
                pk.data_path_858_dok_uri = hasil['path']['858']['dok_uri'], 
                pk.data_path_858_object = hasil['path']['858']['object'], 
                pk.data_path_858_slug = hasil['path']['858']['slug'],  
                pk.data_path = hasil['path'] 
                pk.save()
            except TypeError as e:
                print (e)
                
            
            
        return render(request, 'intaian/index.html', {'form': form, 'x': xyz, 'sumber': sumber})
    else:
        form : forms.FormNIp()
    return render(request, "intaian/index.html", {'form': form})


def get_pasangan(request):
    form = forms.FormNIp()
    nip = request.POST.get('nip')
    if request.method == "POST":
        payload = ''
        headers = {
            'accept': 'application/json',
            'Auth': 'bearer ' + ViewAuthorization(request),
            'Authorization': 'Bearer ' + ViewAuth(request),
            'Cookie': 'ff8d625df24f2272ecde05bd53b814bc=adf347710c85a1a12688d6aad5ce27da; pdns=1091068938.58148.0000'
        }
        datautama.request("GET", "/apisiasn/1.0/pns/data-pasangan/" + nip, payload, headers)
        res = datautama.getresponse()
        data = res.read()

        xyz = json.loads(data.decode("utf-8"))
        sumber = xyz.get('data')
        form = form
        pasanganall = ModelPasangan.objects.all()
        if not pasanganall.filter(idsiasn=sumber.get('idPns')).exists():
            pns = Datautama.objects.get(idpns = sumber.get('idPns') )
            print(pns.id)
            try :
                pasanganall.update_or_create(
                    idsiasn_id = sumber['idPns'],
                    ayahid = sumber['listPasangan'][0]['orang']['ayahId'],
                    ibuid =sumber['listPasangan'][0]['orang']['ibuId'],
                    nama = sumber['listPasangan'][0]['orang']['nama'],
                    namaktp = sumber['listPasangan'][0]['orang']['namaKtp'],  # Field name made lowercase.
                    gelardepan = sumber['listPasangan'][0]['orang']['gelarDepan'],  # Field name made lowercase.
                    gelarblk = sumber['listPasangan'][0]['orang']['gelarBlk'],  # Field name made lowercase.
                    tempatlahir = sumber['listPasangan'][0]['orang']['tempatLahir'],   # Field name made lowercase.
                    tgllahir = sumber['listPasangan'][0]['orang']['tglLahir'],   # Field name made lowercase.
                    aktameninggal = sumber['listPasangan'][0]['orang']['aktaMeninggal'],
                    tglmeninggal = sumber['listPasangan'][0]['orang']['tglMeninggal'],
                    jeniskelamin = sumber['listPasangan'][0]['orang']['jenisKelamin'],
                    jenisanak = sumber['listPasangan'][0]['orang']['jenisAnak'],
                    statushidup = sumber['listPasangan'][0]['orang']['StatusHidup'],
                    jeniskawinid = sumber['listPasangan'][0]['orang']['JenisKawinId'],
                    statusnikah = sumber['listPasangan'][0]['statusNikah'],
                    datapernikahan_id =sumber['listPasangan'][0]['dataPernikahan']['id'],
                    datapernikahan_orangid = sumber['listPasangan'][0]['dataPernikahan']['orangId'],
                    datapernikahan_pnsorangid = sumber['listPasangan'][0]['dataPernikahan']['pnsOrangId'],
                    datapernikahan_tgglmenikah = sumber['listPasangan'][0]['dataPernikahan']['tgglMenikah'],
                    datapernikahan_aktamenikah = sumber['listPasangan'][0]['dataPernikahan']['aktaMenikah'],
                    datapernikahan_tgglcerai = sumber['listPasangan'][0]['dataPernikahan']['tgglCerai'],
                    datapernikahan_aktacerai = sumber['listPasangan'][0]['dataPernikahan']['aktaCerai'],
                    datapernikahan_posisi = sumber['listPasangan'][0]['dataPernikahan']['posisi'],
                    datapernikahan_status =sumber['listPasangan'][0]['dataPernikahan']['status'],
                    datapernikahan_ispns = sumber['listPasangan'][0]['dataPernikahan']['isPns'],
                    datapernikahan_noskpensiun = sumber['listPasangan'][0]['dataPernikahan']['noSkPensiun'],
                )
            except TypeError as e:
                pass
        return render(request, 'intaian/index2.html', {'form': form, 'x': xyz, 'sumber': sumber})
    else:
        form : forms.FormNIp()
    return render(request, "intaian/index2.html", {'form': form})
