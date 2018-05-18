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
        "Apa yang terjadi pada Chinatsu, aku harus cepat."

        scene bg kamar_sore
        "Aku segera menuju rumah Chinatsu, sesampainya disana kulihat Kuroyuki menunggu 
        di luar kamar Chinatsu."
        t   "Bagaimana keadaan Chinatsu?"
		k	"Dia masih tidak sadarkan diri, tapi nafasnya sudah normal"
		t	"daripada saat di ruang klub, sekarang dia sedang beristirahat."
		t	"Syukurlah, aku kira Chinatsu kenapa-napa setelah membaca pesanmu tadi."
		k	"Mengenai itu Taku~"

		"Kuroyuki nampak gugup"

		t	"Ada apa?"
		k	"Sikapmu minggu ini aneh sekali, hari kamis kau seperti mengerjai Eri."
		t	"Mengerjai bagaimana?."
		k	"Laporan klub kau serahkan semuanya pada Eri, padahal kau tau sendiri 
		kalau Eri sibuk urusan OSIS."
		k	"Dia sampai menangis dan meminta bantuanku."
		t	"Aku? Berbuat seperti itu pada Eri?"
		t	"Maaf aku tidak mengingatnya"
		t	"hal terakhir yang kuingat adalah aku pulang sekolah bersama Chinatsu pada hari selasa."

	label rute_4b:
		k	"Kau yakin? Aku bisa mengantar kalian berdua."
		t	"Aku saja tidak apa-apa, Kuroyuki selesaikan saja urusan klub."

		scene ruang_kelas
		"Dengan perlahan aku menuntun Chinatsu menuju UKS, disana kami 
		bertemu dengan Bu Misaki."
		m	"Are? Taku? Kau baik-baik saja?"
		t	"Tolong Chinatsu Bu, dia tiba-tiba pingsan di ruang klub."
		m	"Chinatsu? Siapa dia?"

		"Tunggu sebentar, apa yang barusan Bu Misaki katakan? Bukankah terlihat jelas 
		kalau aku bersama Chinatsu saat ini?!"
		t	"Apa yang Ibu kat~"

		"Ahh, kepalaku terasa berat, pandanganku berputar"
		"cahaya lampu mendadak menyilaukan pandanganku dan dalam sekejap semua menjadi gelap."

		t	"Huh, dimana aku? Dimana Chinatsu?"
		e	"Tidak apa-apa Taku, perlahan saja kau pasti mengingatnya."

		"Ada apa ini, mengapa aku tertidur disini. Aku ada di pangkuan Eri?"
		"Apakah aku sedang bermimpi? Tubuhku tidak dapat kugerakkan"
		"Akhirnya aku pasrah dan tertidur lagi."
			jump Selanjutnya_3a

		scene ruang_kelas
		"Ahirnya aku sadar sekitar pukul 21.00 malam di ruang UKS, dan di sebelahku 
		terlihat Eri sedang tertidur."

		t	"Eri?"
		e	"Kau sudah bangun, . ."
		e	"Asal kau tau saja ya aku tidak bermaksud menunggumu bangun atau apa"
		e	"uma saja ini sekolah ibuku dan aku tidak enak ada siswa pingsan 
		di UKS sampai larut malam."

		t	"Terimakasih Eri"

		"Aku tidak akan bercerita padanya tentang mimpiku yang berada dipangkuannya tadi."
		"Setelah itu aku bangkit dari tempat tidur."

		e	"Apa kau baik-baik saja? Kau bisa pingsan lagi lho."
		t	"Tidak apa-apa, ngomong-ngomong dimana Chinatsu."
		e	"Lagi-lagi kau lupa, bukankah kau tadi sore kirim sms padaku dan Kuroyuki 
		bahwa Chinatsu sudah diantar kerumah oleh pihak sekolah."
		t	"Tapi tadi seingatku tadi aku bertemu bu Misaki dan . ."
		e	"Bu Misaki hari ini tidak masuk, beliau sedang training guru 
		baru untuk persiapan festival sekolah."
		t	"Oh bagitu ya, kalau begitu aku mau pulang sekarang, besok pagi
		aku akan menjenguk Chinatsu."
		e	"Sebelum kau pergi ada hal yang ingin kutanyakan padamu Taku."
		t	"Apa itu?"
		e	"Apa hal terakhir yang kau ingat sebelum rapat klub?"
		t	"Aku kurang begitu mengingatnya,"
		t	"tapi kurasa aku sedang pulang dari sekolah bersama Chinatsu."
		e	"Baiklah kalau begitu."
		t	"Apa ada hal yang ingin kau sampaikan?"
		e	"Tidak ada."
		t	"Kalau begitu aku pulang sekarang."
			jump Selanjutnya_3a

	scene bg kamar_pagi
		"Hari ini hari minggu, setelah kejadian aneh kemarin aku sudah tidak 
		begitu memikirkannya,"
		"yang aku pikirkan sekarang adalah keadaan Chinatsu, semoga dia sudah baikan."

		"*suara bell*"

		"Siapa yang datang hari minggu seperti ini?"
		