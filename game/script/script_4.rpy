label sequance_20:
    play music "music/bensound-clearday.mp3"
    scene bg kamar_pagi
    show shiroyuki 1
    t   "Apa yang barusan dia katakan? Darling? Apa maksudnya? Lagipula sebenarnya siapa gadis ini?"
    t   "Maaf dengan siapa ya?"
    show shiroyuki 2
    "???" "Jangan bercanda Taku, jangan bilang kau lupa denganku."
    show kuroyuki bingung at left
    k   "Sedang apa kau disini?"
    t   "Kuroyuki, kau kenal dengan dia?"
    show shiroyuki 3
    s   "Kakak sendiri tidak biasanya keluar hari minggu."
    t   "Hheehhh, kau adiknya Kuroyuki?"
    s   "Bukan ‘Kau’ tapi Shiroyuki. Mulai sekarang kau harus mengingatnya Darling!" 
    show shiroyuki 1
    s   "Tapi kalau Darling ingin memanggilku Honey tidak apa-apa."
    show eri marah at right
    e   "Tunggu sebentar! ‘Darling’’Honey’ sebenarnya apa hubungan kalian berdua!"
    menu:
        "Aku tidak mengenalnya.":
            jump rute_4a
        "Aku tidak ada hubungan apa-apa dengannya":
            jump rute_4a
    
    label rute_4a:
        play music "music/bensound-love.mp3"
        show shiroyuki 3
        s   "Dingin sekali sikap Darling padaku, apa kau lupa dengan janjimu?"
        t   "Maaf aku benar-benar tidak mengenalmu."
        show shiroyuki 4
        k   "Shiroyuki kemari sebentar!"
        "Kemudian Shiroyuki masuk rumahku, menghampiri kakaknya, Kuroyuki. 
        Kuroyuki tampak membisikkan sesuatu pada adiknya."
        show shiroyuki 5
        s   "Tidak apa-apa kakak, aku tidak akan melakukan hal yang berbahaya. Aku hanya ingin 
        bermain sebentar karena tidak pernah tampil di chapter-chapter sebelumnya."
        show eri biasa
        e   "Jadi ada yang bisa jelaskan padaku apa yang terjadi disini?! Apa hubungan Taku dengan 
        Shiroyuki dan mengapa dia mengenal Taku? Kuroyuki, kau sebagai kakaknya mengetahui sesuatu kan?"
        show kuroyuki senang
        k   "Seperti yang dikatakan Taku, bahwa tidak ada hubungan khusus antara Taku dengan adikku, 
        dia hanya bermain-main saja."
        show shiroyuki 6
        s   "Hehhh, memangnya kenapa kalau aku ada hubungan dengan Darling? Kenapa 
        Eri-cchi langsung panik?"
        show eri kaget
        t   "Eri-cchi?"
        show eri marah_merah
        show shiroyuki 5
        e   "Jangan menggodaku kau murid gagal, bisa-bisanya ranking 2 SMP Aoba sekarang berada di kelas 
        C dan juga jangan sok akrab denganku, kau bukan murid elite lagi."
        show shiroyuki 6
        s   "Jadi begitu ya, kau mengalihkan pembicaraan. Baiklah kalau begitu aku akan diam saja ‘Murid elite Eri’."
        show eri marah
        e   "Orang ini!"
        show kuroyuki bertanya
        show eri biasa
        t   "Sudah-sudah jangan emosi, lagipula kita disini untuk pergi menjenguk Chinatsu kan? 
        Ayo kita kesana."
        show kuroyuki senang
        k   "Shiroyuki, apakah kau juga ikut?"
        show shiroyuki 5
        s   "Darling masih bermain dengan bone- ahh"
        show shiroyuki 1
        s   "maaf maksudku dengan Chinatsu ya. Aku tidak ikut, masih ada hal penting yang harus kukerjakan. Kalau begitu aku langsung pamit, 
        bye Kakak, bye-bye Darling."
        hide shiroyuki 1
        show eri marah
        e   "Orang itu, bahkan tidak menyapaku"
        t   "Kalau begitu Eri, Kuroyuki ayo kita pergi sekarang."
        hide eri
        hide kuroyuki

label sequance_21:
    play music "music/Rain On Lake Erie.mp3"
    scene bg kamar_chinatsu_pagi
    "Setelah pertemuan tak terduga dengan Shiroyuki, Adik perempuan Kuroyuki, kami 
    mengunjungi Chinatsu di rumahnya yang hanya berada di sebelah rumahku. Aku membawa 
    buah-buahan sedangkan Kuroyuki dan Eri membawa cokelat"
    t   "apa yang mereka pikirkan?"
    t   "Assalamu’alaikum, Chinatsu. Aku datang bersama teman-teman."
    c   "Masuk saja Taku, pintunya tidak dikunci."
    t   "Permisi."
    "Lalu aku, Kuroyuki dan Eri masuk ke dalam kamar Chinatsu."
    show kuroyuki bertanya at left
    k   "Bagaimana keadaanmu Chinatsu? Apakah sudah baikan?"
    show chinatsu senang
    c   "Ah, aku baik-baik saja kok. Terimakasih sudah menjengukku teman-teman, 
    maaf membuat kalian khawatir."
    show eri tersenyum at right
    e   "Jadi, sebenarnya kau kenapa? Tiba-tiba pingsan seperti itu."
    show kuroyuki serius
    show chinatsu sedih
    k   "Eri, jangan langsung begitu!"
    show chinatsu senang
    c   "Ahaha, kenapa ya. Aku sendiri kurang tahu, tiba-tiba saja 
    kepalaku berat kemarin saat rapat."
    t   "Yang penting kau sekarang beristirahat saja Chinatsu, ini aku bawa banyak buah-buahan,
    mau kukupaskan apel?"
    show chinatsu senang21
    c   "Ah, terimakasih. Tapi aku baru saja sarapan. Taku taruh saja di meja sebelah."
    t   "Oke."
    show kuroyuki senang2
    k   "Kami juga membawa Cokelat untukmu Chinatsu, mau kubuatkan cokelat panas? 
    Tidak langsung diminum tidak apa-apa."
    show chinatsu senang2
    c   "Terimakasih Kuroyuki, maaf merepotkan."
    show kuroyuki senang
    k   "Kalau begitu aku pinjam dapurnya."
    c   "Oke, dapurnya ada diujung lorong ini."
    hide kuroyuki
    hide chinatsu
    "Kemudian Kuroyuki pergi ke dapur untuk membuatkan cokelat panas."
    t   "Eri, boleh aku bertanya?"
    show eri kaget
    e   "Apa?"
    t   "Kenapa kau dan Kuroyuki membawa cokelat?"
    show eri merajuk
    e   "Tidak ada alasan khusus."
    t   "Kalau begitu untuk apa?"
    show eri marah
    e   "Kenapa kau penasaran?"
    show eri biasa
    t   "Ah tidak, hanya saja setauku cokelat bermanfaat untuk otak, membantu 
    memperkuat daya ingat dan mencegah stress. Biasanya cokelat diberikan saat natal, 
    valentine atau white day agar membuat seseorang bahagia"
    t   "lalu kenapa kau dan Kuroyuki menjenguk Chinatsu dengan membawa cokelat?"
    show eri marah
    e   "Sudah kubilang tidak ada alasan khusus, aku hanya kebetulan membawa cokelat 
    dan Kuroyuki kau tanya sendiri saja."
    hide eri
    "Setelah itu suasana disini menjadi dingin, tidak ada yang berbicara lagi. Sampai 
    Kuroyuki kembali membawa empat cangkir cokelat panas."
    show kuroyuki senang2 at left
    k   "Aku kembali, ini Chinatsu Cokelat panasnya, yang ini untuk Eri dan Taku."
    show chinatsu senang21
    c   "Terimakasih Kuroyuki."
    show kuroyuki bingung
    k   "Ada apa dengan kalian Eri, Taku. Kok rasanya dingin sekali berada diantara kalian."
    show eri sedih at right

    play music "music/bensound-slowmotion.mp3"
    e   "Bukan apa-apa, hanya saja Taku kepo dengan alasan kita membawa cokelat hari ini."
    show kuroyuki mendengarkan
    k   "Jadi begitu, Taku sebagai MC yang baik kau harus mencari tahu sendiri, 
    jangan apa-apa langsung bertanya."
    t   "MC? Apa yang kau bicarakan?"
    show kuroyuki bingung
    k   "…"
    show kuroyuki senang2
    k   "Ngomong-ngomong Chinatsu, apa kau besok sudah bisa pergi sekolah?"
    show chinatsu senang22
    c   "Semoga, kau nanti sore aku sudah tidak pusing lagi besok aku akan ke sekolah."
    show eri tersenyum
    e   "Kami tidak memaksamu, kalau masih sakit kau berbaring saja disini."
    show chinatsu senang21
    c   "Aku tidak apa-apa Eri, aku juga tidak enak dengan kalian. Karena mulai 
    besok kita harus mempersiapkan festival sekolah bukan."
    show kuroyuki senang
    k   "Kami baik-baik saja kok Chinatsu jika besok kau belum masuk sekolah, 
    lihat saja siapa saja disini ada Eri ketua OSIS"
    k   "Aku ketua kelas dan Taku mantan ketua kelas, kami baik-baik saja mengurus festival sekolah."
    show eri sedih
    e   "Langsung saja, kami baik-baik saja mengurus semuanya dengan atau tanpamu Chinatsu"
    show chinatsu sedih
    show kuroyuki bingung
    t   "Eri, jaga bahasamu."
    show chinatsu bertanya
    c   "Ahaha, tapi kalian tahu saja kalau Taku mungkin hanya menjadi beban kalian berdua. 
    Taku belum pernah berbuat banyak di dua festival sekolah sebelumnya, walau dia ketua 
    klub otaku."
    show kuroyuki senang
    k   "Jadi begitu ya, tapi tahun ini berbeda karena kami berdua yang akan menjadi 
    staff-nya Taku. Maka tidak mungkin festival sekolah tahun ini gagal, iya kan Eri."
    show eri marah
    show kuroyuki bingung
    e   "Asal kau tahu saja, aku akan menggunakan caraku sendiri dalam festival 
    sekolah tahun ini, aku tidak mau diperintah oleh orang ini."
    show kuroyuki bertanya
    k   "Ayolah Eri jangan mulai lagi. Taku sendiri akan berjuang dalam festival 
    sekolah tahun ini kan?"
    t   "Akan kuusahakan."
    show kuroyuki senang
    k   "Berarti semua baik-baik saja. Eri dan Taku tidak meminum cokelatnya?"
    t   "Ah maaf, tadi masih panas, akan kuminum sekarang."
    show kuroyuki senang2
    k   "Kalau sudah akan kubawa cangkirnya kembali ke dapur."
    t   "Terimakasih, cokelat panasnya enak sekali Kuroyuki."
    k   "Sama-sama."
    hide eri
    hide kuroyuki
    hide chinatsu
    play music "music/Determination.mp3"
    "Setelah itu kami membereskan barang-barang dan berpamitan untuk pulang ke rumah masing-masing."

label sequance_22:
    scene bg kamar_sore
    "Tidak terasa sudah jam 6 sore, ternyata lama juga kami menjenguk Chinatsu."
    "Dirumah aku membuka catatan evaluasi dari Eri, tapi setelah kubuka terdapat kertas usang yang tampak lusuh."

    t   "Kertas apa ini?"
    menu:
        "Membuka lipatan kertas lusuh tersebut":
            jump rute_5b
        "Menyingkirkannya di laci meja":
            jump rute_5b
            
    label rute_5b:
        "chapter 4 selesai"