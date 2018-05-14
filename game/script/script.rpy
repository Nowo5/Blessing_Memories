
define t = Character('[Taku]', color="E92900")
define c = Character('Chinatsu', color="#320C90")
define ks = Character('Kepala Sekolah', color="#8CEE03")
define e = Character('Eri', color="#03E9EE")
define cf = Character('Bu Chifuyu', color="#5603EE")
define m = Character('Bu Misaki', color="#A003EE")
define k = Character('Kuroyuuki', color="#EE03AD")
define tk = Character('[t] dan Kuroyuuki', color='#EE0311')
define sm = Character ('Seluruh Murid', color='#900C3F')

label splashscreen:
    scene black
    with Pause(1)

    show text "Khusus Pecinta Rider..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label start:
    play music "reverie.mp3"
    scene bg pexels-photo-176851
    $ Taku = renpy.input("Namaku adalah.....")
    $ Taku = Taku.strip()
    "Anda mau ke mana?"
    menu:
        "CHAPTER 1":
            jump chapter_1
        "CHAPTER 2.":
            jump chapter_2

label chapter_1:
    "Aku ingin memiliki keluarga perhatian, penyayang serta perduli kepada anaknya"
    "namun semua itu hanya impian semata"
    "Aku berharap mempunyai sahabat yang dapat berbagi keluh dan kesah"
    "itu pun hanya ilusi di dalam kehidupanku"
    "Dan di saat aku menemukan sesuatu yang berharga"
    "berakhir dengan di manfaatkan dan di lecehkan oleh orang sekitarku"
    "Apakah aku tak berhak untuk memiliki kebahagiaan, ataukah kesedihan dan
    keterpurukan menjadi akhir perjalanan hidupku?"
    "Ini sungguh tak adil mereka di luar sana yg bersikap egois, individualis,
    dan materialistis dapat memiliki segalanya"
    "sedangkan aku yang mencurahkan segala yg ku punya demi kebahagian orang
    lain malah berakhir dengan menyedihkan. "
    "Apakah berbuat baik saja tidak cukup untuk dunia ini ataukah pengorbanan
    diperlukan untuk meraihnya."
    "Ku benci segalanya, ku benci dunia ini, mengapa ini semua terjadi kepadaku
    Tuhan."
    "Aku lebih memilih untuk tidak di lahirkan di dunia ini jika berakhir
    demikian"
    "menjadi tak berarti dan tak bernilai hingga membuatku muak untuk menjalaninya. "
    $ Taku = renpy.input("Namaku adalah.....")
    $ Taku = Taku.strip()

    play music "Serenity.mp3"
    scene bg kamar_pagi
    "Jam tepat pukul 06.05 di balik selimut aku tertidur lelap dan tiba-tiba ada
    seseorang yang berada di atasku"
    show chinatsu senang_zoom
    c "[t] ayo bangun, sudah jam berapa ini"
    "(melirik jam weker)"
    t "Sebentar 5 menit lagi masih ngantuk nih !"
    show chinatsu senang_zoom2
    c "Ayolah cepat bangun, kau tak ingin melewatkan upacara sambutan kan?"
    t "Baik aku akan bangun tapi, kau turun dulu dari atasku berat tau"
    show chinatsu sedih_zoom
    c "Tega sekali kau berkata begitu padaku"
    "(turun dari kasur sambil nangis)"
    t "Maaf aku kan bercanda gak maksut kasar kok"
    "(beranjak dari tempat tidur)"
    show chinatsu senang_zoom
    c "Kena deh ku kerjain habisnya gak bangun-bangun sih"
    t "Ok, sekarang tolong keluar sebentar dari kamarku, mau mandi sama ganti
    baju dulu nih"
    show chinatsu senang_zoom2
    c "Baik ku tunggu di luar,  jangan lama-lama ya"
    "(tersenyum sambil menutup pintu)"
    "Chinatsu adalah teman masa kecilku, Ia tinggal bersebelahan dengan rumahku,"
    "entah kenapa dia selalu mengikuti kemana aku pergi. "
    "SD hingga SMA bahkan dia selalu bergabung dengan klub yang sama denganku."

    scene bg jalan_menuju_sekolah
    play music "Mountain Breeze.mp3"
    with fade
    show chinatsu sedih
    c "Selalu saja begini kesiangan, gak pernah deh tepat waktu"
    t "Maaf kemarin aku begadang nonton anime"
    show chinatsu bertanya2
    c "Oh begitu pantas saja,"
    c "tapi [t] kenapa saat tidur tadi kau menangis ?"
    t "Masa sih, kayaknya enggak deh"
    show chinatsu bertanya
    c "Beneran aku gak bohong dari matamu aja menetes air mata"
    t "Iya aku percaya kok, tadi itu cuman mimpi buruk aja"
    "(perasaan aneh ini terus menghantuiku)"
    show chinatsu senang
    c "Baiklah jika begitu"
    show chinatsu bertanya
    c "Nee [t] apakah kau tetap menjadi ketua klub Otaku ?"
    t "Tidak mungkin, aku akan menyerahkan jabatan ketua klub pada junior,
    sudah kupikirkan siapa yang akan menjadi ketua."
    show chinatsu sedih
    c "Kalau begitu kita sudah tidak memiliki tempat bermain lagi ?"
    t "Tidak juga, murid kelas 3 tetap menjadi anggota klub meski tidak wajib
    mengikuti kegiatan klub."
    show chinatsu senang
    c "Baguslah kalau begitu."
    t "Lagipula bukannya Chi chan sudah saatnya belajar untuk masuk Universitas
    Tokyo."
    show chinatsu ragu-ragu
    c "Soal itu, ettooo, anu.. [t] akan membantuku belajar kan ?"
    t "Tentu saja Chi chan."

    scene bg aula_sekolah
    play music "bensound-sweet.mp3"
    with fade
    "Sesampainya di sekolah kami bergegas menuju aula, pidato sambutan di buka
    oleh ketua OSIS."
    show eri tersenyum
    e "Sekian sambutan dari saya, kurang lebihnya mohon maaf."
    "Ketua OSIS turun dari podium, dilanjutkan dengan sambutan Kepala Sekolah."
    hide eri tersenyum
    show chifuyu senyum
    cf "Selamat datang di SMA Aoba, kalian berhak bangga menjadi murid salah
    satu sekolah terbaik di Kyoto, . . "
    "(Melanjutkan pidatonya)"
    cf  "Mulai tahun ajaran 2018/2019 SMA Aoba akan menerapkan peraturan baru,"
    cf  "dimana semua murid kelas tiga yang belum pernah mengikuti kegiatan klub
    harus bergabung dengan klub baru yang akan saya dirikan,"
    cf  "untuk informasi selengkapnya akan diumumkan dikelas masing-masing saat
    jam pembinaan wali kelas."

    scene bg ruang_kelas
    play music "bensound-clearday.mp3"
    with fade
    show misaki senang
    m   "Selamat pagi anak-anak waktunya jam bimbingan wali kelas. "
    m   "Sebenarnya wali kelas 3-A adalah Bu Chifuyu tetapi karena beliau sibuk
    maka saya akan menggantikannya,"
    m   "kalian dapat memanggil saya Bu Misaki, saya guru baru di SMA Aoba tahun
    ini jadi mohon kerjasamanya."
    show misaki senyum
    m   "Apakah pengurus kelas untuk tahun ini sudah dibentuk?"
    sm  "Belum Bu"
    m   "Kalau begitu kita akan menentukan pengurus kelas sebelum memulai
    pelajaran."
    m   "Karena SMA Aoba adalah sekolah dengan sistem ranking"
    m   "maka yang akan menjadi ketua kelas adalah murid ranking 1 saat ujian
    kenaikan kelas dan wakilnya yang mendapat ranking 2,"
    m   "didalam stopmap yang Ibu bawa tertulis ranking satu adalah Kuroyuki dan
        wakilnya adalah [t]."
    m   "Untuk murid yang namanya disebutkan silahkan maju kedepan kelas"
    "Aku dan Kuroyuki maju kedepan kelas"
    tk  "Baik Bu."
    m   "Selamat untuk kalian berdua karena menjadi ketua dan wakil ketua tahun
    ini,"
    m   "mungkin ada kata-kata motivasi untuk teman-teman disini."
    show kuroyuki senang at right
    k   "Saya merasa terhormat menjadi ketua kelas meski baru terwujud saat
    kelas tiga,"
    k    "semoga kita semua dapat terus semangat belajar dan masuk universitas
    yang diinginkan."
    show kuroyuki mendengarkan
    t   "Kalau saya ingin menyampaikan kepada ketua yang baru bahwa tanggung
    jawab ketua kelas itu berat,"
    t   "jika wakil hanya mengurus internal kelas maka ketua kelas berarti
    menjadi perwakilan kelas,"
    t   "bahkan untuk kelas 3-A menjadi ketua kelas berarti menjadi perwakilan
    sekolah, untuk teman-teman kurasa tidak ada yang perlu saya sampaikan."

    show misaki senyum
    m   "Kita berikan tepuk tangan untuk pengurus kelas yang baru."
    "Seluruh murid kelas A tepuk tangan"
    m   "Sekarang kalian berdua boleh duduk."
    hide kuroyuki mendengarkan
    "Kami berdua kembali ke tempat duduk masing-masing, pelajaran pun dimulai."
    "Pelajaran berakhir pukul 13.00 dan dilanjutkan dengan bimbingan wali kelas,"
    "wali kelas 3-A adalah Bu Chifuyu, aku penasaran dengan klub baru yang
    beliau sampaikan tadi"
    "walaupun itu bukan urusanku karena aku pernah mengikuti klub otaku selama
    dua tahun."

    hide misaki senyum
    show chifuyu senyum
    cf  "Selamat pagi semuanya"
    cf  "Langsung saja ibu jelaskan tentang klub yang akan saya bentuk, klub baru
    tersebut adalah klub relawan,"
    cf  "tugas klub relawan adalah membantu masalah yang dialami seluruh warga
    sekolah ini. "
    cf  "Jadi bagi kalian diperbolehkan untuk datang dan berkonsultasi ke klub
    relawan,"
    cf  "Tempatnya di gedung klub, sebelah ruang klub otaku. "
    cf  "Selanjutnya Ibu akan umumkan murid yang akan bergabung dengan klub
    relawan,"
    cf  "dari kelas 3-A ada Kuroyuki dan Taku, setelah ini segera temui saya
    di ruang kepala sekolah,"
    cf  "saya akan menjawab semua pertanyaan kalian. Sekian."
    "Saat selesai berbicara Bu Chifuyu melirikku, seakan tahu bahwa ada yang
    ingin kutanyakan."
    "Untuk sekarang aku akan ke ruang kepala sekolah."
    hide chifuyu senyum
    show kuroyuki senang
    k "Kau akan ke ruang kepala sekolah juga kan? Ayo pergi bersama."
    "menghampiri [t]"
    t "Ah, ba-baik"
    "(kaget)"

    scene bg lorong_sekolah
    play music "Mountain Breeze.mp3"
    show kuroyuki senang
    "Aku dan Kuroyuki pergi menuju ruang kepala sekolah"
    t "Kamu ternyata belum pernah mengikuti klub ya?"
    k "Iya, aku terlalu sibuk belajar jadi tidak ada waktu untuk
    megikuti klub, [t] sendiri apakah tidak mengikuti klub? Padahal aku kira
    kau mengikuti klub."
    t "Ah tidak, aku mengikuti klub otaku sejak kelas satu dan menjadi ketua
    klub saat kelas dua."
    show kuroyuki mendengarkan
    k "Kalau begitu kenapa kepala sekolah memanggilmu juga?"
    t "Aku tidak tahu, kenapa kau berpikir aku mengikuti klub?"
    show kuroyuki senang
    k "Aku sering melihatmu berjalan dengan siswi dari kelas 3-C menuju ruang
    klub, apakah dia pacarmu?"
    t "Ah, ti-tidak kok, Chinatsu hanya teman masa kecilku saja."
    show kuroyuki bertanya
    k "Begitu ya, kau tahu rumor tentang Chinatsu?"
    t "Eh? Rumor tentang apa?"
    show kuroyuki serius
    k "Kata adikku yang di kelas C ada senior kelas 3 yang bisa dikatakan
    ‘antara ada dan tiada'"
    t "Apa-apaan itu? Aku tidak mengerti."
    k "Benar juga ya, tapi kata anak-anak kelas C murid yang mendapat julukan
    itu adalah Chinatsu, entah karena apa dia mendapat julukan itu."
    "Lalu tiba-tiba Chinatsu datang."
    show chinatsu bertanya2 at right
    t "Ada apa, kenapa terburu-buru begitu Chinatsu?"
    c "Taku disuruh bergabung dengan klub relawan kan? Aku juga dipanggil ke
    ruang kepala sekolah."
    t "Eh, Chinatsu juga dipanggil?"
    show chinatsu senang
    c "Hehe, kita satu klub lagi Taku, ini aku membelikanmu roti melon dan
    yang satu untuk....?"
    show kuroyuki senang2
    k "Kuroyuki, aku teman sekelas Taku, senang bertemu denganmu Chinatsu."
    show chinatsu senang2 at right
    c "Ah iya, senang bertemu denganmu Kuroyuki. Ini roti melon untukmu."
    k "Terima kasih"
    c "Sama-sama."
    t "Baiklah kita sudah sampai di ruang kepala sekolah, ayo masuk kedalam."

    scene bg ruang_kepala_sekolah
    play music "bensound-sweet.mp3"
    t "Permisi Bu, kami sudah tiba."
    show chifuyu jengkel
    show eri merajuk at left
    e "Kenapa aku harus ikut klub relawan? Tugasku sebagai ketua OSIS saja sudah
    banyak, mengapa Mamah tambah lagi ?"
    cf "Tidak ada yang harus kujelaskan lagi padamu Eri, keputusan Ibu sudah
    final."
    "Kami disuguhi pemandangan, pertengkaran sengit antara ibu dan anak."
    hide eri marah
    show chifuyu senyum
    cf  "Oh, kalian sudah datang ternyata, kalau begitu sudah lengkap anggota
    klub ini ada Eri, Taku, Kuroyuki dan,.."
    c   "Chinatsu Bu."
    cf  "Ah iya Chinatsu. Dari penjelasan saya sebelumnya, apakah ada pertanyaan?"
    cf  "Apakah masih ada yang kurang jelas terkait klub relawan"
    t   "Maaf Bu Chifuyu, saya ingin bertanya"
    cf "Apa itu?."
    t   "Saya ingin bertanya Bu, mengapa saya dan Chinatsu masuk klub relawan?
    padahal kami anggota klub otaku selama dua tahun."
    show chifuyu marah
    cf "Taku, kau memang megikuti klub otaku dan juga menjadi ranking satu
    selama dua tahun tapi di klub itu kau tak menghasilkan prestasi apapun"
    cf "oleh sebab itu kau ku masukkan ke klub relawan yang tanggung jawab dan
    jangkauannya setara OSIS."
    cf "Bedanya hanya di administrasi bagian OSIS dan klub relawan bagian teknis
    atau lapangan sedangkan untuk Chinatsu itu rahasia. "
    cf "Bukan kah itu lebih bermanfaat dari pada membuang waktumu di klub otaku
    dengan hal yang tidak berguna !!!!"
    t   "Saya rasa klub itu berdasarkan minat dan bakat, bukan tanggung jawab."
    cf "Ya memang hal yang kau katakan itu betul tapi bukankah kau mengikuti
    klub otaku hanya berdasarkan minat bukan bakat"
    cf "pantaskah kau mengatakannya kepadaku?"
    cf "Tahun ini kau kuberi dua pilihan pertama menjadi ketua klub relawan atau
    keluar menjadi wakilnya"
    cf "karena kurasa Kuroyuki sudah pantas menjadi ketua klub relawan,
    jadi mana yang kau pilih?"
    menu:
        "Sepertinya tak ada pilihan lain, saya pilih menjadi ketua":
            jump rute_1a
        "Pilihan yang tak menguntungkan, lebih baik aku tak memilih apapun.":
            jump rute_1b
    label rute_1a:
        show chifuyu senyum
        cf "Keputusan bijak, kau memang harus memilih karena tak ada kata
        tidak dalam perintahku"
        jump Selanjutnya
    label rute_1b:
        show chifuyu marah
        cf "Dasar manusia tak berakal, berani sekali kau menentang perintahku,
        memangnya kau siapa berhak menolak perintahku yang mutlak"
        t "Ekspresi itu, kenapa mebuat hatiku bergejolak tak karuan"
        jump Selanjutnya

    label Selanjutnya:
    show chifuyu jengkel
    show eri marah merajuk at left
    e "Tunggu dulu, aku tidak diberitahu tentang hal ini!"
    e "Kenapa aku harus menjadi anggota klub dari Sampah seperti dia?"
    cf "Kalau tidak ada pertanyaan kita akhiri pertemuan hari ini dan kegiatan
    klub dimulai besok sepulang sekolah."
    show eri sedih at left
    "Bu Chifuyu tidak bergeming sedikitpun."
    "Aku memandangi Bu Chifuyu, Chinatsu, Kuroyuuki dan Eri sejenak."
    "Kulihat Eri meneteskan air mata seperti ingin menangis, apakah dia
    sebegitu benci kepadaku?"

    show eri marah_merah at left
    e "Apa kau lihat-lihat, dasar bodoh!"
    t "Ah, bukan apa-apa, mohon kerjasamanya untuk satu tahun ini. Bu Chifuyu
    kami mohon pamit."

    scene bg jalan_pulang
    play music "Introspection.mp3"
    with fade
    show chinatsu senang2
    "Di perjalanan pulang aku dan Chinatsu mengobrol membahas kejadian yang
    terjadi hari ini"
    t "Mengapa kau terus tersenyum Chi chan?"
    show chinatsu senang
    c "Akhirnya kita satu klub lagi tahun ini, ya kan [t]."
    c "Kita satu klub lagi tahun ini. He he"
    t "Ya, walaupun sedikit aneh menyuruh murid kelas tiga menjadi ketua klub."
    show chinatsu bertanya2
    c "[t] tidak senang dengan klub relawan?"
    t "Bukan begitu, justru sebaliknya aku merasa tertantang menjadi ketua klub
    relawan"
    t "aku tadi hanya merasa penasaran dengan kepala sekolah."
    "Chinatsu tiba-tiba berhenti dan melirik ke samping"
    show chinatsu bertanya_red
    c "Nee Taku, kau masih ingat tempat ini."
    menu:
        "Tentu saja aku ingat":
            jump ingat
        "Aku tidak ingat tempat apa ini.":
            jump tidak_ingat

    label ingat:
        show chinatsu senang2
        c "Benar juga ya, disini kan tempat pertama kali Taku menyelamatkanku."
        play music "music/coba2.mp3" fadeout 1
        scene event chinatsu1 with fade
        "Kejadian itu terjadi saat aku masih kelas 6 SD"
        "karena badai salju sekolah diliburkan, padahal aku terlanjur
        sampai sekolah"
        "Saat perjalanan pulang ditengah badai, aku mendengar suara tangisan
         dari taman sakura"
        "aku mencari asal suara tersebut dan menemukan Chinatsu menangis
        dibawah perosotan, akupun bertanya."
        t "mengapa kau menangis?"
        c "Hari ini ulang tahunku tapi kedua orang tuaku tidak ada dirumah."
        t "Kebetulan hari ulang tahunku besok lusa, bagaimana kalau kita
        mengadakannya bersama dirumahku"
        t "jadi jangan menangis lagi"
        "Setelah itu kami berdua pulang kerumahku dan mengadakan pesta
        kecil-kecilan,"
        "walaupun sederhana tetapi Chi chan tampak sangat bahagia, sejak
        saat itu dia selalu mengikutiku."
        jump Selanjutnya_2

    label tidak_ingat:
        show chinatsu sedih
        c "Oh begitu, maaf deh kalau perkataanku tadi aneh"
        t "Aneh, memangnya apa?"
        show chinatsu senang21
        c "Sudah lupakan saja jika kau tak ingat tak apa"
        show chinatsu sedih
        t "Baiklah jika itu keinginanmu"
        jump Selanjutnya_2

    label Selanjutnya_2:
        scene bg kamar_sore with fade
        play music "Serenity.mp3"
        "Aku dan Chinatsu sudah sampai di rumah masing-masing, sesampainya aku
        segera ganti baju, makan, belajar kemudian istirahat."
        "Hari yang cukup melelahkan mungkin besok akan lebih baik."
        jump chapter_2
