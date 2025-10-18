def dfa(metin):
    # Başlangıç durumu
    durum = "q0"
    
    # Girdideki her bir karakteri işle
    for karakter in metin:
        match durum:
            case "q0":
                if karakter == "a":
                    durum = "q3"
                elif karakter == "b":
                    durum = "q1"
                else:
                    return "Reddedildi"
            case "q1":
                if karakter == "a":
                    durum = "q4"
                elif karakter == "b":
                    durum = "q2"
                else:
                    return "Reddedildi"
            case "q2":
                if karakter == "a":
                    durum = "q5"
                elif karakter == "b":
                    durum = "q2"
                else:
                    return "Reddedildi"
            case "q3":
                if karakter == "a":
                    durum = "q6"
                elif karakter == "b":
                    durum = "q4"
                else:
                    return "Reddedildi"
            case "q4":
                if karakter == "a":
                    durum = "q7"
                elif karakter == "b":
                    durum = "q5"
                else:
                    return "Reddedildi"
            case "q5":
                if karakter == "a":
                    durum = "q8"
                elif karakter == "b":
                    durum = "q5"
                else:
                    return "Reddedildi"
            case "q6":
                if karakter == "a":
                    durum = "q6"
                elif karakter == "b":
                    durum = "q7"
                else:
                    return "Reddedildi"
            case "q7":
                if karakter == "a":
                    durum = "q6"
                elif karakter == "b":
                    durum = "q8"
                else:
                    return "Reddedildi"
            case "q8":
                if karakter == "a" or karakter == "b":
                    durum = "q8"
                else:
                    return "Reddedildi"
            case _:
                return "Reddedildi"
    
    # Kabul edici durumlar: q6, q7, q8
    if durum in { "q8"}:
        return "Kabul Edildi"
    else:
        return "Reddedildi"


# Kullanıcıdan sürekli girdi almak için ana fonksiyon
if __name__ == "__main__":
    print("DFA Metin Denetleyici")
    print("Kontrol etmek istediğiniz metni girin. Çıkmak için 'çıkış' yazın.\n")
    
    while True:
        kullanici_girdisi = input("Bir metin girin: ").strip()  # Kullanıcıdan girdi al
        if kullanici_girdisi.lower() == "çıkış":  # Çıkış koşulu
            print("DFA Denetleyici kapatılıyor. Hoşça kalın!")
            break
        sonuc = dfa(kullanici_girdisi)  # Metni DFA'da işle
        print(f"Girdi: {kullanici_girdisi} -> Sonuç: {sonuc}\n")
