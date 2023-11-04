import random, sys, os, time
print(".:: Chatbot ciwi ::.")
SapaanIn = ['halo cuyy','asslamualaikum','hallo','selamat pagi','hai','hey ngabs']
NamaIn = ['siapa kamu','namamu siapa','kamu siapa','kenalan yuk']
TanyaIn = ['kamu lagi ngapain','ngapain luwh','lagi ngapain','ngapain sieee']
HobbyIn = ['hobby mu apa','kamu suka apa','hobby ?','hobby']
PenciptaIn = ['bapak kamu siapa', 'kamu ciptaan siapa','bapakmu siapa','siapa bapakmu']
SapaanOut = ['hey cuy','Selamat Datang di Chatbot ciwi','halo ngab','halo cuys']
NamaOut = ['ciwi cantik','Hamba Allah','ciwi gemes','ciwi Lucu']
TanyaOut = ['Kepo deh','Memikirkan bagaimana membenarkan semua masalah ini','Mikirin kamu']
PenciptaOut = ['yang tercantiek','anak baik']
HobbyOut = ['Nonton Drakor','Dengerin Musik','Jalan-jalan','gangguin orang']
ToxicOut = ['apa luwh','HAHH','makan yuk']
while (True) :
    inputan = input("=>")
    inp = inputan.lower()
    if inputan == "" :
        sys.exit
        break
    elif inp in SapaanIn :\
        print("=>",random.choice(SapaanOut))
    elif inp in NamaIn :\
        print("=>",random.choice(NamaOut))
    elif inp in TanyaIn:\
        print("=>",random.choice(TanyaOut))
    elif inp in PenciptaIn :\
        print("=>",random.choice(PenciptaOut))
    elif inp in HobbyIn :\
        print("=>",random.choice(HobbyOut))
    else:
        print("=>Maaf Versi bot masih belum bisa merespon")