with open('programnyelv_1feladat.txt', 'r', encoding='utf-8') as f: #1. feladat
    f.readline()
    f.readline()
    with open('evszamok.txt', 'w', encoding='utf-8') as c:
        evek = [sor.strip().split(';')[0] for sor in f]
        for ev in sorted(evek):
            print(ev, file=c)

with open('programnyelv_1feladat.txt', 'r', encoding='utf-8') as f: #2. feladat
    f.readline()
    f.readline()
    with open('programozo.txt', 'w', encoding='utf-8') as d:
        nevek = [sor.strip().split(';')[2] for sor in f]
        for nev in sorted(nevek):
            print(nev, file=d)

with open('evszamok.txt', 'r', encoding='utf-8') as f: #3. feladat
    f.readline()
    f.readline()
    evek = [sor.strip().split(';')[0] for sor in f]
    with open('ismetles.txt', 'w', encoding='utf-8') as e:
        evek_szotar = {}
        for ev in evek:
            if ev not in evek_szotar:
                evek_szotar[ev] = 1
            else:
                evek_szotar[ev] += 1
        tobbszor_elofordulo_evek = [ev for ev, db in evek_szotar.items() if db > 1]
        for ev in sorted(tobbszor_elofordulo_evek):
            print(ev, file=e)