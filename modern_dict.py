def m_dict(kata):
    meme_dict = {  "CRINGE": "Sesuatu yang sangat memalukan",
                    "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
                    "AFK": "Sedang jauh dari keyboard",
                    "GG": "Pemainan bagus",
                    "BRB": "Tunggu sebentar",
                    "CREEPY": "Menakutkan",
                    "marah": "\U0001F620",
                    "terbahak": "\U0001F923",
                    "keren": "\U0001F60E",
                    "sedih": "\U0001F62D",
                    "senyum": "\U0001F642",
                    "ok": "\U0001F44C"
                } 	
    kamus = ""
    if kata in meme_dict:
        kamus += meme_dict[kata]
    else:
        kamus += "kata tidak ditemukan"
    return kamus    