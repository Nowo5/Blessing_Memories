label chapter_3:
    ##SEQUANCE_1
    play music "music/Rain On Lake Erie.mp3"
    scene bg ruang_kepala_sekolah
    "Aku perlahan membuka mataku, hal biasa yang aku lakukakan saat bangun tidur"
    "namun entah mengapa pemandangan yang kulihat saat ini bukanlah kamarku melainkan ruang 
    klub relawan."
    "Apakah aku tertidur? Tapi bagaimana? Aku bahkan tidak ingat kalau hari ini aku 
    pergi kesekolah."
    
    show chinatsu bertanya2
    c   "Ada apa [t]? Kau kelihatan bingung."
    k   "Apa kau tidak enak badan? Bagaimana kalau kuantar ke UKS?"
    show eri biasa at right
    e   "Coba lihat! Bisa-bisanya ketua tertidur saat evaluasi kegiatan 
   	klub dan persiapan festival sekolah!"
    show chinatsu sedih
    t   "Eri? Kau mengikuti kegiatan klub?"
    show eri marah at right
    e   "Hah! Apa maksudmu?! Aku tidak mengerti."
    show kuroyuki bertanya at left
    k   "Sudah-sudah, jangan bertengkar lagi. Taku, kau tampak sangat 
    berkeringat, apa kau baik-baik saja?"
    show eri biasa at right
    e   "Hmph, padahal baru saja dia memimpin rapat, tapi sekarang seperti orang linglung."
    
    hide chinatsu
    play sound "sound_effect/jatuh.mp3"
    "Bruk"

    "Tiba-tiba Chinatsu jatuh dari bangku dan tidak sadarkan diri."
    play music "music/The Chase.mp3"
    show eri merajuk at right
    show kuroyuki bertanya at left
    tk  "Chinatsu!"
    "Kuroyuki dengan sigap mendekap Chinatsu."
    show kuroyuki serius
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
        show kuroyuki bertanya
        k   "Baiklah kalau begitu."
        hide kuroyuki
        show eri biasa
        "Setelah itu Kuroyuki mengantar Chinatsu ke UKS"
        "sekarang hanya kami berdua di ruang klub, 
        karena bingung aku tidak berkata apapun pada Eri."
        show eri sedih 
        e   "begini Taku, untuk kejadian hari selasa aku minta maaf."
        show eri marah_merah
        e   "Sebenarnya aku sudah minta maaf hari rabu tapi karena kau 
        terlihat tidak sehat jadi aku mengulanginya lagi."
        t   "Begitu ya, maaf kalau aku kurang sopan, tapi 
        bagaimana kau memutuskan untuk mengikuti kegiatan klub?"
        show eri marah
        e   "Jadi kau benar-benar lupa? Selasa malam, Kuroyuki datang ke rumahku"
        show eri biasa
        e   "ia keras kepala sekali berkata tidak akan pulang sebelum aku mengalah 
        untuk mengikuti kegiatan klub."
        t   "Apa yang Kuroyuki katakan?"
        show eri marah_merah
        e   "Soal itu? Pokoknya aku memutuskan untuk ikut kegiatan klub."
        t   "Kalau begitu pertanyaan terakhir, apa yang sedang kita lakukan saat ini?"
        t   "Kau tadi berkata tentang evaluasi minggu pertama, berarti sekarang hari Sabtu?"
        show eri biasa
        e   "Pertanyaan aneh"
        e   "Iya sekarang hari Sabtu. Sejak hari rabu kita sudah rutin mengadakan kegiatan klub, 
        laporannya ada di depanmu."
        t   "Baiklah, terimakasih Eri, laporannya sudah selesai, sekarang aku 
        mau ke UKS, kau mau ikut?"
        e   "Tidak perlu, aku mau langsung pulang."
        hide eri

        "Tinggal aku sendiri di ruang klub, merapikan dokumen klub, aku mengkhawatirkan 
        keadaan Chinatsu yang tiba-tiba pingsan, sebenarnya apa yang sedang terjadi."

        "*suara pesan masuk*"
        play sound "sound_effect/suara_HP.mp3"

        t   "Siapa yang mengirim sms padaku?"
        "Dari Kuroyuki, coba kulihat isinya"
        "Chinatsu aku antar pulang, cepatlah kemari. Ada sesuatu yang ingin kusampaikan padamu"
        "Apa yang terjadi pada Chinatsu, aku harus cepat."

        play music "music/Daybreak.mp3"
        scene bg rumah chinatsu – sore hari
        "Aku segera menuju rumah Chinatsu, sesampainya disana kulihat Kuroyuki menunggu 
        di luar kamar Chinatsu."
        t   "Bagaimana keadaan Chinatsu?"
        show kuroyuki bertanya
        k   "Dia masih tidak sadarkan diri, tapi nafasnya sudah normal"
        t   "daripada saat di ruang klub, sekarang dia sedang beristirahat."
        t   "Syukurlah, aku kira Chinatsu kenapa-napa setelah membaca pesanmu tadi."
        show kuroyuki serius
        k   "Mengenai itu Taku~"

        "Kuroyuki nampak gugup"

        t   "Ada apa?"
        show kuroyuki bertanya
        k   "Sikapmu minggu ini aneh sekali, hari kamis kau seperti mengerjai Eri."
        t   "Mengerjai bagaimana?."
        show kuroyuki serius
        k   "Laporan klub kau serahkan semuanya pada Eri, padahal kau tau sendiri 
        kalau Eri sibuk urusan OSIS."
        show kuroyuki bertanya
        k   "Dia sampai menangis dan meminta bantuanku."
        t   "Aku? Berbuat seperti itu pada Eri?"
        t   "Maaf aku tidak mengingatnya"
        t   "hal terakhir yang kuingat adalah aku pulang sekolah bersama Chinatsu pada hari selasa."
        jump Selanjutnya_3a

    play music "music/The Chase.mp3"
    label rute_4b:
        show kuroyuki bertanya
        k   "Kau yakin? Aku bisa mengantar kalian berdua."
        t   "Aku saja tidak apa-apa, Kuroyuki selesaikan saja urusan klub."

        scene bg ruangUKS
        "Dengan perlahan aku menuntun Chinatsu menuju UKS, disana kami 
        bertemu dengan Bu Misaki."
        
        m   "Are? Taku? Kau baik-baik saja?"
        t   "Tolong Chinatsu Bu, dia tiba-tiba pingsan di ruang klub."
        m   "Chinatsu? Siapa dia?"

        "Tunggu sebentar, apa yang barusan Bu Misaki katakan? Bukankah terlihat jelas 
        kalau aku bersama Chinatsu saat ini?!"
        t   "Apa yang Ibu kat~"

        "Ahh, kepalaku terasa berat, pandanganku berputar"
        "cahaya lampu mendadak menyilaukan pandanganku dan dalam sekejap semua menjadi gelap."

        t   "Huh, dimana aku? Dimana Chinatsu?"
        e   "Tidak apa-apa Taku, perlahan saja kau pasti mengingatnya."

        "Ada apa ini, mengapa aku tertidur disini. Aku ada di pangkuan Eri?"
        "Apakah aku sedang bermimpi? Tubuhku tidak dapat kugerakkan"
        "Akhirnya aku pasrah dan tertidur lagi."

    ##SEQUANCE_2
        play music "music/Shadowlands.mp3"
        scene bg ruangUKS_malam
        "Akhirnya aku sadar sekitar pukul 21.00 malam di ruang UKS, dan di sebelahku 
        terlihat Eri sedang tertidur."

        t   "Eri?"
        e   "Kau sudah bangun, . ."
        e   "Asal kau tau saja ya aku tidak bermaksud menunggumu bangun atau apa"
        e   "uma saja ini sekolah ibuku dan aku tidak enak ada siswa pingsan 
        di UKS sampai larut malam."

        t   "Terimakasih Eri"

        "Aku tidak akan bercerita padanya tentang mimpiku yang berada dipangkuannya tadi."
        "Setelah itu aku bangkit dari tempat tidur."

        e   "Apa kau baik-baik saja? Kau bisa pingsan lagi lho."
        t   "Tidak apa-apa, ngomong-ngomong dimana Chinatsu."
        e   "Lagi-lagi kau lupa, bukankah kau tadi sore kirim sms padaku dan Kuroyuki 
        bahwa Chinatsu sudah diantar kerumah oleh pihak sekolah."
        t   "Tapi tadi seingatku tadi aku bertemu bu Misaki dan . ."
        e   "Bu Misaki hari ini tidak masuk, beliau sedang training guru 
        baru untuk persiapan festival sekolah."
        t   "Oh bagitu ya, kalau begitu aku mau pulang sekarang, besok pagi
        aku akan menjenguk Chinatsu."
        e   "Sebelum kau pergi ada hal yang ingin kutanyakan padamu Taku."
        t   "Apa itu?"
        e   "Apa hal terakhir yang kau ingat sebelum rapat klub?"
        t   "Aku kurang begitu mengingatnya,"
        t   "tapi kurasa aku sedang pulang dari sekolah bersama Chinatsu."
        e   "Baiklah kalau begitu."
        t   "Apa ada hal yang ingin kau sampaikan?"
        e   "Tidak ada."
        t   "Kalau begitu aku pulang sekarang."
        jump Selanjutnya_3a
    
    play music "music/Serenity.mp3"
    scene bg bg kamar_pagi
    label Selanjutnya_3a:
        scene bg kamar_pagi
        "Hari ini hari minggu, setelah kejadian aneh kemarin aku sudah tidak 
        begitu memikirkannya,"
        "yang aku pikirkan sekarang adalah keadaan Chinatsu, semoga dia sudah baikan."

        play sound "sound_effect/suara_bel.mp3"
        "*suara bell*"

        "Siapa yang datang hari minggu seperti ini?"

        t   "Iya sebentar."
        ek  "Permisi."
        t   "Eri dan Kuroyuki, ada apa tiba-tiba datang berkunjung? Mengapa tidak kirim sms dahulu?"
        k   "Maaf tiba-tiba, tapi kami juga ingin menjenguk Chinatsu"
        k   "jadi kami putuskan untuk mampir. Iya kan Eri?"
        e   "Tidak juga, aku hanya tidak senang jika Chinatsu terus begini"
        e   "dia akan menjadi beban saat festival sekolah."
        t   "Boleh juga sih, tapi kenapa harus mampir rumahku dulu?"
        t   "Rumah Chinatsu kan berada disebelah rumahku, kalian tinggal kesana sendiri."
        k   "Ada apa dengan ‘hawa’ mengusir ini, Taku?"
        t   "Ah, tidak. Bukan maksudku mengusir, tapi rumahku kan berantakan."
        k   "Sebenarnya kami mampir dulu karena Eri ingin memberikan ini."
        t   "Apa ini?"
        k   "Itu laporan rapat evaluasi dan persiapan festival sekolah kemarin."
        k   "Mungkin saja kau lupa jadi kami bawa ke rumahmu."
        t   "Bukannya ini dapat kau berikan saat di sekolah? Tidak perlu repot-repot datang ke rumahku."
        t   "Lagipula kau tidak apa-apa hari minggu kesini, kau memiliki adik kan Kuroyuki?"
        k   "Tidak apa-apa, pagi tadi adikku sudah pergi entah kemana. Jarang sekali dia begitu."
        e   "Adikmu itu yang di kelas 2-C kan Kuroyuki?"
        k   "Iya, sama sepertimu Eri, dia SMP di Aoba tapi waktu kelas 1 SMA sekolah di luar negeri, 
        dan sekarang dia kembali ke Aoba."
        e   "Tahun lalu aku sekolah di Rusia, sedangkan Adikmu di Inggris"
        e   "SMP Aoba memang memberikan hadiah sekolah di luar negeri selama setahun bagi siswa berprestasi 
        tapi kenapa sekarang adikmu ada di kelas C?"
        k   "Ah, aku juga tidak tahu apa yang ada dipikirannya, bicara padanya pun aku susah."
        k   "Kalau begitu bagaimana kalau kita segera menuju rumah Chinatsu?"

        play sound "sound_effect/suara_bel.mp3"
        "*suara bell*"
        k   "Taku, kau sepertinya kedatangan tamu."
        t   "Siapa lagi sekarang, iya sebentar."

        "Aku membukakan pintu"
        "Dihadapanku berdiri perempuan dengan rambut putih dikepang dua, tersenyum manis padaku. 
        Apa mungkin dia salah alamat?"

        s   "D a r l i n g ! "
