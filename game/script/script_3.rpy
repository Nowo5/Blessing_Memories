label chapter_3:
    "Aku perlahan membuka mataku, hal biasa yang aku lakukakan saat bangun tidur"
    "namun entah mengapa pemandangan yang kulihat saat ini bukanlah kamarku melainkan ruang 
    klub relawan."
    "Apakah aku tertidur? Tapi bagaimana? Aku bahkan tidak ingat kalau hari ini aku 
    pergi kesekolah."

    scene bg ruang_kelas
    c   "Ada apa [t]? Kau kelihatan bingung."
    k   "Apa kau tidak enak badan? Bagaimana kalau kuantar ke UKS?"
    e   "Coba lihat! Bisa-bisanya ketua tertidur saat evaluasi kegiatan 
    klub dan persiapan festival sekolah!"
    t   "Eri? Kau mengikuti kegiatan klub?"
    e   "Hah! Apa maksudmu?! Aku tidak mengerti."
    k   "Sudah-sudah, jangan bertengkar lagi. Taku, kau tampak sangat 
    berkeringat, apa kau baik-baik saja?"
    e   "Hmph, padahal baru saja dia memimpin rapat, tapi sekarang seperti orang linglung."

    "Bruk"

    "Tiba-tiba Chinatsu jatuh dari bangku dan tidak sadarkan diri."
    tk  "Chinatsu!"
    "Kuroyuki dengan sigap mendekap Chinatsu."
    k   "Bagaimana ini [t]?"
    menu:
        "Tolong kau antar Chinatsu ke UKS.":
            jump rute_4a
        "Biar aku antar Chinatsu ke UKS.":
            jump rute_4b
    
    label rute_4a:
        k   "Kau yakin? Aku bisa mengantar kalian berdua ke UKS."
        t   "Aku baik-baik saja, hanya sedikit pusing, yang penting Chinatsu. 
        Aku akan menyusul ke UKS setelah urusan klub selesai."
        k   "Baiklah kalau begitu."
        "Setelah itu Kuroyuki mengantar Chinatsu ke UKS"
        "sekarang hanya kami berdua di ruang klub, 
        karena bingung aku tidak berkata apapun pada Eri."
        e   "begini Taku, untuk kejadian hari selasa aku minta maaf."
        e   "Sebenarnya aku sudah minta maaf hari rabu tapi karena kau 
        terlihat tidak sehat jadi aku mengulanginya lagi."
        t   "Begitu ya, maaf kalau aku kurang sopan, tapi 
        bagaimana kau memutuskan untuk mengikuti kegiatan klub?"
        e   "Jadi kau benar-benar lupa? Selasa malam, Kuroyuki datang ke rumahku"
        e   "ia keras kepala sekali berkata tidak akan pulang sebelum aku mengalah 
        untuk mengikuti kegiatan klub."
        t   "Apa yang Kuroyuki katakan?"
        e   "Soal itu? Pokoknya aku memutuskan untuk ikut kegiatan klub."
        t   "Kalau begitu pertanyaan terakhir, apa yang sedang kita lakukan saat ini?"
        t   "Kau tadi berkata tentang evaluasi minggu pertama, berarti sekarang hari Sabtu?"
        e   "Pertanyaan aneh"
        e   "Iya sekarang hari Sabtu. Sejak hari rabu kita sudah rutin mengadakan kegiatan klub, 
        laporannya ada di depanmu."
        t   "Baiklah, terimakasih Eri, laporannya sudah selesai, sekarang aku 
        mau ke UKS, kau mau ikut?"
        e   "Tidak perlu, aku mau langsung pulang."

        "Tinggal aku sendiri di ruang klub, merapikan dokumen klub, aku mengkhawatirkan 
        keadaan Chinatsu yang tiba-tiba pingsan, sebenarnya apa yang sedang terjadi."

        "*suara pesan masuk*"

        t   "Siapa yang mengirim sms padaku?"
        "Dari Kuroyuki, coba kulihat isinya"
        "Chinatsu aku antar pulang, cepatlah kemari. Ada sesuatu yang ingin kusampaikan padamu"
        "Apa yang terjadi pada Chinatsu, aku harus cepat.b"
