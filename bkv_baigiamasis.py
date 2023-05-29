from tkinter import *

parametrai = {
    1: "WBC LEUKOCITAI (*10^9/l)",
    2: "NEUT Neutrofilai (%)",
    3: "NEUT Neutrofilai (#)",
    4: "LYM Limfocitai (%)",
    5: "LYM# Limfocitai (#)",
    6: "MONO Monocitai (%)",
    7: "MONO Monocitai (#)",
    8: "EOS Eozinofilai (%)",
    9: "EOS Eozinofilai (%)",
    10: "BASO Bazofilai (#)",
    11: "BASO Bazofilai (%)",
    12: "RBC ERITROCITAI (*10^12/l)",
    13: "HGB HEMOGLOBINAS (g/l)",
    14: "HCT Hematokritas (%)",
    15: "MCV Vidutinis eritrocitų tūris (fl)",
    16: "MCH Vidutinis hemoglobino kiekis eritrocite (pg)",
    17: "MCHC Vidutinė eritrocitų hemoglobino koncentracija (g/l)",
    18: "RDW-CV Eritrocitų pasiskirstymo plotis (%)",
    19: "PLT Trombocitai (*10^9/l)",
    20: "PDW Trombocitų pasiskirstymo plotis (fl)",
    21: "MPV Trombocitų vidutinis tūris (fl)",
    22: "P-LCR Didelių trombocitų santykis (%)",
    23: "PCT Trombokritas (%)"
}


def tikrinti_analyte(pasirinkimas, lytis, rezultatas):
    if pasirinkimas == 1:
        if 7.0 < rezultatas <= 10.2 and (lytis == "vyr" or lytis == "mot"):
            return """Stebimas suaktyvintas imuninis atsakas. 
Atkreipkite dėmesį į galimus uždegiminius ar lėtinius procesus organizme."""
        elif rezultatas > 10.20 and (lytis == "vyr" or lytis == "mot"):
            return """Leukocitų rezultatas virš norminės  ribos. 
Leukocitų skaičiaus padidėjimas dažniausiai būna bakterinių ar virusinių infekcijų padarinys. 
Retesniais atvejais leukocitų skaičiaus padidėjimą taip pat įtakoja, alergijos, skydliaukės patologija, 
jungiamojo audinio patologija, audinių traumos. Ilgai užsitęsęs WBC koncentracijos padidėjimas 
gali sukelti įtarimą dėl leukemijos ar piktybinio naviko."""
        elif rezultatas < 3.9 and (lytis == "vyr" or lytis == "mot"):
            return """Leukocitų rezultatas žemiau norminės ribos.
Stebimas užslopintas imuninis atsakas. Galima sunki virusinė infekcija.
Leukocitų skaičius gali sumažėti dėl virusinio viršutinių kvėpavimo takų uždegimo,
esant skydliaukės funkcijos padidėjimui (tirotoksikozei), sergant geležies stokos mažakraujyste, 
lėtinio uždegimo, kepenų pažeidimo, blužnies padidėjimo septinio proceso metu,
sergant megaloblastine anemija (sumažėjusi vitamino B12, folio rūgšties koncentracija),
leukemija, agranuliocitoze, hemolize, viklige, įgimta leukopenija ar esant cheminių medžiagų 
bei jonizuojančios radiacijos poveikiui."""
        else:
            return """Leukocitų rezultatas normos ribose.
Leukocitai dalyvauja įvairiose imuninėse organizmo reakcijose.
Yra penkios leukocitų klasės: neutrofilai, limfocitai, eozinofilai, monocitai ir bazofilai."""

    if pasirinkimas == 2:
        if rezultatas > 77.0 and (lytis == "vyr" or lytis == "mot"):
            return """Neutrofilų rezultatas virš norminės  ribos.
Galima bakterinė infekcija.
Neutrofilų parametro padidėjimą taip pat  įtakoja pirmuonys, ūmios ir lėtinės leukemijos,  
audinių traumos, nekrozės, chirurginės traumos, miokardo ar plaučių infarktas, 
stambiųjų kraujagyslių trombozės,  jungiamojo audinio ligos (reumatoidinis artritas, 
vaskulitas, kolagenozės), piktybiniai navikai, mielofibrozė, hemolizinė anemija, 
lėtinė idiopatinė neutrofilija,  skydliaukės patologija, metabolinės ir endokrininės ligos(hipertirozė,
uremija, podagra,pieno rūgšties acidozė), medikamentai(steroidai,adrenalinas,litis,augimo hormonas), 
fiziologinė neutrofilija(skausmas,stresas,fizinis krūvis,hipoksuja, rūkymas), pašalinus blužnį."""
        elif rezultatas < 42.0 and (lytis == "vyr" or lytis == "mot"):
            return """Neutrofilų rezultatas žemiau norminės ribos.
Galima virusinė infekcija (gripas, hepatitas, raudoniukė, ŽIV ,CMV...). 
Neutrofilų parametro sumažėjimą taip pat  įtakoja gydimas citostatikais ir spindulinė terapija,  
medikamentai (kai kurie vaistai nuo skausmo ir temperatūros, nuo epilepsijos, diabeto, psichotropiniai, 
skydliaukės funkciją slopinantys), ūmi leukemija, agranuliocitozė imuninės kilmės(sisteminė vilkligė, 
reumatoidinis artritas ir kitos), aplazija, kaulų čiulpų metastazės, 
komplemento aktyvacija (visos būklės, kai kraujas kontaktuoja su sintetinėmis medžiagomis ir 
pusiau pralaidžiomomis membranomis), grybelinės infekcijos,geležies deficitas, 
megaloblastinė anemija,padidėjusi blužnis, įgimta neutropenija, kai 
kurios sunkios bakterinės infekcijos(bruceliozė,tuliaremija, tifoidinė infekcija)."""
        else:
            return """Rezultatas normos ribose.
Neutrofilai atlieka antimikrobinę funkciją, gali fagocituoti, dalyvauja uždegiminėje reakcijoje."""

    if pasirinkimas == 3:
        if rezultatas > 7.7 and (lytis == "vyr" or lytis == "mot"):
            return """Neutrofilų rezultatas virš norminės  ribos.
Galima bakterinė infekcija.
Neutrofilų parametro padidėjimą taip pat  įtakoja pirmuonys, ūmios ir lėtinės leukemijos,  
audinių traumos, nekrozės, chirurginės traumos, miokardo ar plaučių infarktas, 
stambiųjų kraujagyslių trombozės,  jungiamojo audinio ligos (reumatoidinis artritas, 
vaskulitas, kolagenozės), piktybiniai navikai, mielofibrozė, hemolizinė anemija, 
lėtinė idiopatinė neutrofilija,  skydliaukės patologija, metabolinės ir endokrininės ligos(hipertirozė,
uremija, podagra,pieno rūgšties acidozė), medikamentai(steroidai,adrenalinas,litis,augimo hormonas), 
fiziologinė neutrofilija(skausmas,stresas,fizinis krūvis,hipoksuja, rūkymas), pašalinus blužnį."""
        elif rezultatas < 1.5 and (lytis == "vyr" or lytis == "mot"):
            return """Neutrofilų rezultatas žemiau norminės ribos. 
Galima virusinė infekcija (gripas, hepatitas, raudoniukė, ŽIV ,CMV...). 
Neutrofilų parametro sumažėjimą taip pat  įtakoja gydimas citostatikais ir spindulinė terapija,  
medikamentai (kai kurie vaistai nuo skausmo ir temperatūros, nuo epilepsijos, diabeto, psichotropiniai, 
skydliaukės funkciją slopinantys), ūmi leukemija, agranuliocitozė imuninės kilmės(sisteminė vilkligė, 
reumatoidinis artritas ir kitos), aplazija, kaulų čiulpų metastazės, 
komplemento aktyvacija (visos būklės, kai kraujas kontaktuoja su sintetinėmis medžiagomis ir 
pusiau pralaidžiomomis membranomis), grybelinės infekcijos,geležies deficitas, 
megaloblastinė anemija,padidėjusi blužnis, įgimta neutropenija, kai 
kurios sunkios bakterinės infekcijos(bruceliozė,tuliaremija, tifoidinė infekcija)."""
        else:
            return """Neutrofilų rezultatas normos ribose.
    Neutrofilai atlieka antimikrobinę funkciją, gali fagocituoti, dalyvauja uždegiminėje reakcijoje."""
    if pasirinkimas == 4:
        if rezultatas > 44.0 and (lytis == "vyr" or lytis == "mot"):
            return """Limfocitų rezultatas virš norminės  ribos.
Galima virusinė infekcija.Limfocitų parametro padidėjimą taip pat  įtakoja  infekcinė mononukleozė, 
lėtinė limfoleukėmija,ūmi leukėmija, kokliušas, infekcinis hepatitas, citomegaloviruso infekcija, 
toksoplazmozė,raudoniukė, tuberkuliozė, sifilis, maliarija,vidurių šiltinė,bruceliozė,difterija, 
antinkščių nepakankamumas."""
        elif rezultatas < 20.0 and (lytis == "vyr" or lytis == "mot"):
            return """Limfocitų rezultatas žemiau norminės  ribos.
Galima sunki virusinė infekcija, gripo virusas, ŽIV, infekcinis hepatitas.Limfocitų parametro sumažėjimą 
taip pat  įtakoja  aplastinė anemija, hemoterapija, spindulinis gydymas,antilimfocitiniai preparatai, 
kortikosteroidai, mitybos trūkumai, Vilkligė, sarkoidozė, enteropatijos,idiopatinė limfocitopenija, 
navikai, ascitas, inkstų nepakankamumas."""
        else:
            return """Limfocitų rezultatas normos ribose. 
Limfocitai dalyvauja įgytame imunitete, sintetina antikūnus, naikina ne tik svetimas, 
bet ir savas patologines ląsteles (onkologines)."""
    if pasirinkimas == 5:
        if rezultatas > 4.5 and (lytis == "vyr" or lytis == "mot"):
            return """Limfocitų rezultatas virš norminės  ribos.
Galima virusinė infekcija.Limfocitų parametro padidėjimą taip pat  įtakoja  infekcinė mononukleozė, 
lėtinė limfoleukėmija,ūmi leukėmija, kokliušas, infekcinis hepatitas, citomegaloviruso infekcija, 
toksoplazmozė,raudoniukė, tuberkuliozė, sifilis, maliarija,vidurių šiltinė,bruceliozė,difterija, 
antinkščių nepakankamumas."""
        elif rezultatas < 1.0 and (lytis == "vyr" or lytis == "mot"):
            return """Limfocitų rezultatas žemiau norminės  ribos.
Galima sunki virusinė infekcija, gripo virusas, ŽIV, infekcinis hepatitas.Limfocitų parametro sumažėjimą 
taip pat  įtakoja  aplastinė anemija, hemoterapija, spindulinis gydymas,antilimfocitiniai preparatai, 
kortikosteroidai, mitybos trūkumai, Vilkligė, sarkoidozė, enteropatijos,idiopatinė limfocitopenija, 
navikai, ascitas, inkstų nepakankamumas."""
        else:
            return """Limfocitų rezultatas normos ribose. 
Limfocitai dalyvauja įgytame imunitete, sintetina antikūnus, naikina ne tik svetimas, 
bet ir savas patologines ląsteles (onkologines)."""
    if pasirinkimas == 6:
        if rezultatas > 9.5 and (lytis == "vyr" or lytis == "mot"):
            return """Monocitų rezultatas virš norminės  ribos. 
Galima inkstų lėtinė liga ar yra  sveikimo procesas po persirgtos ūmios infekcijos. 
Monocitų parametro padidėjimą taip pat  įtakoja bakterinė infekcija(tuberkuliozė, sifilis, bruceliozė, 
vidurių šiltinė), alkoholine kepenų liga, grybelinės ir parazitinės infekcijos, pirmuonys(leišmaniozė,
maliarija), sisteminės autoimuninės ligos(vilkligė, reumatoidinis artritas, poliarteritas, polimiozitas), 
leukemija, navikai, sarkoidozė."""
        elif rezultatas < 2.0 and (lytis == "vyr" or lytis == "mot"):
            return """Monocitų rezultatas žemiau norminės  ribos. 
Monocitų kiekio sumažėjimas kraujo tyrime galimas esant pūlingiems-uždegiminiams procesams, 
aplastinei anemijai, pooperaciniu ar pogimdyminiu laikotarpiu, vartojant steroidus."""
        else:
            return """Monocitų rezultatas normos ribose. 
Monocitai gali fagocituoti (absorbuoti) virusus, bakterijas, navikus ir parazitines ląsteles. 
Dalyvauja susidarant antikūnams, citokinams bei  kraujo krešėjimo procese."""
    if pasirinkimas == 7:
        if rezultatas > 0.9 and (lytis == "vyr" or lytis == "mot"):
            return """Monocitų rezultatas virš norminės  ribos. 
Galima inkstų lėtinė liga ar yra  sveikimo procesas po persirgtos ūmios infekcijos. 
Monocitų parametro padidėjimą taip pat  įtakoja bakterinė infekcija(tuberkuliozė, sifilis, bruceliozė, 
vidurių šiltinė), alkoholine kepenų liga, grybelinės ir parazitinės infekcijos, pirmuonys(leišmaniozė,
maliarija), sisteminės autoimuninės ligos(vilkligė, reumatoidinis artritas, poliarteritas, polimiozitas), 
leukemija, navikai, sarkoidozė."""
        elif rezultatas < 0.1 and (lytis == "vyr" or lytis == "mot"):
            return """Monocitų rezultatas žemiau norminės  ribos. 
Monocitų kiekio sumažėjimas kraujo tyrime galimas esant pūlingiems-uždegiminiams procesams, 
aplastinei anemijai, pooperaciniu ar pogimdyminiu laikotarpiu, vartojant steroidus."""
        else:
            return """Monocitų rezultatas normos ribose. 
Monocitai gali fagocituoti (absorbuoti) virusus, bakterijas, navikus ir parazitines ląsteles. 
Dalyvauja susidarant antikūnams, citokinams bei  kraujo krešėjimo procese."""
    if pasirinkimas == 8:
        if rezultatas > 5.5 and (lytis == "vyr" or lytis == "mot"):
            return """Eozinofilų rezultatas virš norminės ribos. 
Eozinofilų kiekio padidėjimas gali atsirasti esant medikamentinei alergijai,alerginėms ligoms, 
helmintinei infekcijai. Eozinofilų  parametro padidėjimą taip pat  įtakoja  kai kurios 
odos ligos,  jungiamojo audinio ligos, infekcinės ligos(skarlatina,tuberkuliozė,
alerginė bronchopneumoninė aspergiliozė), leukemijos, piktybiniai navikai (limfomos), 
plaučių infiltratai su eozinofilija, žarnyno patologija, antinkčių nepakankamumas, 
ateroembolinės patologijos, eozinofilinės mialgijos sindromas."""
        elif rezultatas < 0.5 and (lytis == "vyr" or lytis == "mot"):
            return """Eozinofilų rezultatas žemiau norminės ribos.
Eozinofilų kiekio sumažėjimas gali atsirasti po didelio streso ar po ūmaus uždegimo gydymo, 
vartojus kortikostreroidinių medikamentų. Eozinofilų parametro sumažėjimą taip pat įtakoja sepsis, 
ūmios infekcijos,antinkščių žievės hormonų hiperfunkcija, vartojami steroidiniai preaparatai."""
        else:
            return """Eozinofilų rezultatas normos ribose.
Eozinofilai yra kraujo ląstelės, kurios fagocituoja organizme esančius antigenų- antikūnių 
imunoglobulino E kompleksus. Tai ląstelės, kurios yra aktyvuojamos vėlyvosiose uždegimo stadijose. 
Eozinofilai dalyvauja alerginėse reakcijose.Eozinofilai yra  vienintelė kraujo ląstelė, 
pasižyminti paros ritmu – didžiausi eozinofilų kiekiai yra aptinkami naktį."""
    if pasirinkimas == 9:
        if rezultatas > 0.5 and (lytis == "vyr" or lytis == "mot"):
            return """Eozinofilų rezultatas virš norminės ribos. 
Eozinofilų kiekio padidėjimas gali atsirasti esant medikamentinei alergijai,alerginėms ligoms, 
helmintinei infekcijai. Eozinofilų  parametro padidėjimą taip pat  įtakoja  kai kurios 
odos ligos,  jungiamojo audinio ligos, infekcinės ligos(skarlatina,tuberkuliozė,
alerginė bronchopneumoninė aspergiliozė), leukemijos, piktybiniai navikai (limfomos), 
plaučių infiltratai su eozinofilija(PIE), žarnyno patologija, antinkčių nepakankamumas, 
ateroembolinės patologijos, eozinofilinės mialgijos sindromas."""
        elif rezultatas < 0.02 and (lytis == "vyr" or lytis == "mot"):
            return """Eozinofilų rezultatas žemiau norminės ribos.
Eozinofilų kiekio sumažėjimas gali atsirasti po didelio streso ar po ūmaus uždegimo gydymo, 
vartojus kortikostreroidinių medikamentų. Eozinofilų parametro sumažėjimą taip pat įtakoja sepsis, 
ūmios infekcijos,antinkščių žievės hormonų hiperfunkcija, vartojami steroidiniai preaparatai."""
        else:
            return """Eozinofilų rezultatas normos ribose. 
Eozinofilai yra kraujo ląstelės, kurios fagocituoja organizme esančius antigenų- antikūnių 
imunoglobulino E kompleksus. Tai ląstelės, kurios yra aktyvuojamos vėlyvosiose uždegimo stadijose. 
Eozinofilai dalyvauja alerginėse reakcijose.Eozinofilai yra  vienintelė kraujo ląstelė, 
pasižyminti paros ritmu – didžiausi eozinofilų kiekiai yra aptinkami naktį."""
    if pasirinkimas == 10:
        if rezultatas > 1.0 and (lytis == "vyr" or lytis == "mot"):
            return """Bazofilų rezultatas virš norminės ribos.
Ryškiau bazofilų kiekis padidėja esant medikamentinei, maisto ar buitinei  greito tipo alerginei reakcijai.
Bazofilų padidėjimas taip pat gali būti stebimas esant žaizdų gijimui bei tam  tikroms ligoms  
(reumatoidiniui artritui, virškinamojo trakto opoms ir uždegimams,  eritrodermijai,  eritremijai, 
lėtinei mieloleukemijai, geležies stokos anemijai, uždegimai, sepsis, piktybinės ligos 
esant audinių destrukcijai, gydimas estrogenais diabetas,hipotirozė, limfogranulomatozė). 
Vidutinio laipsnio absoliuti bazofilija gali būti ankstyvas lėtinės mieloleukemijos požymis. 
Jeigu lėtinės mieloleukemijos fone ryškiai didėja bazofilų skaičius, tai dažnai būna susiję su leukemijos
blastine transformacija, akceleracijos faze."""
        elif rezultatas == 0.00 and (lytis == "vyr" or lytis == "mot"):
            return """Bazofilų rezultatas žemiau norminės ribos.
Bazofilų kiekio sumažėjimą gali įtakoti ūmios infekcijos, hipertirozė, stresas."""
        else:
            return """Bazofilų rezultatas normos ribose. 
Bazofilai - dalyvauja greito tipo alerginėse reakcijose"""
    if pasirinkimas == 11:
        if rezultatas > 0.25 and (lytis == "vyr" or lytis == "mot"):
            return """Bazofilų rezultatas virš norminės ribos.
Ryškiau bazofilų kiekis padidėja esant medikamentinei, maisto ar buitinei  greito tipo alerginei reakcijai.
Bazofilų padidėjimas taip pat gali būti stebimas esant žaizdų gijimui bei tam  tikroms ligoms  
(reumatoidiniui artritui, virškinamojo trakto opoms ir uždegimams,  eritrodermijai,  eritremijai, 
lėtinei mieloleukemijai, geležies stokos anemijai, uždegimai, sepsis, piktybinės ligos 
esant audinių destrukcijai, gydimas estrogenais diabetas,hipotirozė, limfogranulomatozė). 
Vidutinio laipsnio absoliuti bazofilija gali būti ankstyvas lėtinės mieloleukemijos požymis. 
Jeigu lėtinės mieloleukemijos fone ryškiai didėja bazofilų skaičius, tai dažnai būna susiję su leukemijos
blastine transformacija, akceleracijos faze."""
        elif rezultatas < 0.01 and (lytis == "vyr" or lytis == "mot"):
            return """Bazofilų rezultatas žemiau norminės ribos.
Bazofilų kiekio sumažėjimą gali įtakoti ūmios infekcijos, hipertirozė, stresas."""
        else:
            return """Bazofilų rezultatas normos ribose. 
    Bazofilai - dalyvauja greito tipo alerginėse reakcijose"""
    if pasirinkimas == 12:
        if lytis == "vyr" and rezultatas < 4.3:
            return """RBC rezultatas žemiau norminės ribos.
Kai eritrocitų kiekis sumažėja, diagnozuojama anemija(mažakraujystė).Anemija išsivysto tada, 
jei dėl ligos arba nusilpusio organizmo susilpnėja kraujo ląsteles gaminančių organų veikla 
arba suintensyvėja eritrocitų irimas."""
        elif lytis == "mot" and rezultatas < 3.9:
            return """RBC rezultatas žemiau norminės ribos.
Kai eritrocitų kiekis sumažėja, diagnozuojama anemija(mažakraujystė).Anemija išsivysto tada, 
jei dėl ligos arba nusilpusio organizmo susilpnėja kraujo ląsteles gaminančių organų veikla 
arba suintensyvėja eritrocitų irimas."""
        elif lytis == "vyr" and rezultatas > 5.75:
            return """RBC rezultatas virš norminės ribos. 
Eritrocitų skaičius gali padidėti sergant lėtinėmis širdies ir plaučių ligomis. 
Esant deguonies trūkumui audiniuose, dehidratacijos metu, sergant inkstų policistoze, 
kai yra taikomas gydymas steroidais, sergant piktybiniu inkstų naviku, feochromocitoma, 
Kušingo sindromu."""
        elif lytis == "mot" and rezultatas > 5.2:
            return """RBC rezultatas virš norminės ribos. 
Eritrocitų skaičius gali padidėti sergant lėtinėmis širdies ir plaučių ligomis. 
Esant deguonies trūkumui audiniuose, dehidratacijos metu, sergant inkstų policistoze, 
kai yra taikomas gydymas steroidais, sergant piktybiniu inkstų naviku, feochromocitoma, 
Kušingo sindromu."""
        else:
            return """RBC rezultatas normos ribose.
Eritrocitai yra raudonieji kraujo kūneliai, kurie atlieka deguonies pernešimo funkciją iš plaučių 
į viso organizmo ląsteles. Taip pat iš ląstelių jie prisijungia anglies dvideginį ir nuneša jį 
į plaučius, kad šis būtų pašalintas."""
    if pasirinkimas == 13:
        if lytis == "vyr" and rezultatas < 135:
            return """HGB rezultatas žemiau norminės ribos.
Stebima mažakraujystė- anemijos.Hemoglobino kiekis gali sumažėti dėl: nevisavertės mitybos, 
geležies stokos ar sutrikusio jos įsisavinimo,dėl dažno ar gausaus kraujavimo, 
uždegiminių procesų organizme."""
        elif lytis == "mot" and rezultatas < 120:
            return """HGB rezultatas žemiau norminės ribos.
Stebima mažakraujystė- anemijos.Hemoglobino kiekis gali sumažėti dėl: nevisavertės mitybos, 
geležies stokos ar sutrikusio jos įsisavinimo,dėl dažno ar gausaus kraujavimo, 
uždegiminių procesų organizme."""
        elif lytis == "vyr" and rezultatas > 172:
            return """HGB rezultatas virš norminės ribos.
HGB padidėja dėl organizmo prisitaikymo prie gaunamo sumažėjusio deguonies kiekio."""
        elif lytis == "mot" and rezultatas > 156:
            return """HGB rezultatas virš norminės ribos.
HGB padidėja dėl organizmo prisitaikymo prie gaunamo sumažėjusio deguonies kiekio."""
        else:
            return """HGB rezultatas normos ribose.
Hemoglobinas ‒ tai baltymas, esantis eritrocituose. Būtent hemoglobinas geba  prisijungti deguonies  
ir anglies dioksido molekules."""
    if pasirinkimas == 14:
        if lytis == "vyr" and rezultatas < 39.5:
            return """HCT rezultatas žemiau norminės ribos.
Kraujyje sumažėjęs eritrocitų kiekis,o tai dažniausiai reiškia mažakraujystę, geležies stokos anemiją."""
        elif lytis == "mot" and rezultatas < 35.5:
            return """"HCT rezultatas žemiau norminės ribos.
Kraujyje sumažėjęs eritrocitų kiekis,o tai dažniausiai reiškia mažakraujystę, geležies stokos anemiją."""
        elif lytis == "vyr" and rezultatas > 50.5:
            return """HCT rezultatas virš norminės ribos.
Stebimas kraujo klampumo padidėjimas (daugiau eritrocitų, mažiau skystosios kraujo dalies plazmos). 
Dėl šios priežasties  apsunkinamas širdies darbas. Gali įtakoti per mažas skysčių vartojimas."""
        elif lytis == "mot" and rezultatas > 45:
            return """HCT rezultatas virš norminės ribos.
Stebimas kraujo klampumo padidėjimas (daugiau eritrocitų, mažiau skystosios kraujo dalies plazmos). 
Dėl šios priežasties  apsunkinamas širdies darbas. Gali įtakoti per mažas skysčių vartojimas."""
        else:
            return """HCT rezultatas normos ribose.
Tai yra kraujo eritrocitų suminis tūris. Parodo kiek yra plazmos ir kiek suminės eritrocitų masės"""
    if pasirinkimas == 15:
        if rezultatas > 98.0 and (lytis == "vyr" or lytis == "mot"):
            return """ MCV rezultatas virš norminės ribos. 
Galima makrocitine anemija (dažnai dėl folio rūgšties ar vitamino B12 trūkumo atsiradusi mažakraujystė).  
Rodiklio padidėjimą gali įtakoti  megaloblastinė anemija ( padidėja  eritrocitai arba Hb kiekis), 
toksinis kepenų pažeidimas, lėtinis alkoholizmas, kontraceptikų vartojimas, skrandžio gleivinės pažeidimai,
skrandžio vėžys, žarnyno malabsorbcija, parazitai žarnyne (askaridės, strongiloidai, plokščiosios kirmėlės
 ir t.t.), divertikuliozė, Krono (Crohn) liga, taikomas gydymas citostatikais,  vegetarinis maistas, 
 mielodisplazinis sindromas (MDS). Retai – transkobalamino trūkumas (genetinis defektas) kraujyje.  """
        elif rezultatas < 82.0 and (lytis == "vyr" or lytis == "mot"):
            return """MCV rezultatas žemiau norminės ribos.
Galima lėtinė anemija, ilgalaikis geležies trūkumas, apsinuodijimas švynu.  
Rodiklio sumažėjimui gali įtakoti  „Lėtinės ligos“ , kurias lydi anemija,  lėtiniai kraujavimai 
(sukeliantys geležies deficitą), neštumas, eritremija, sideroblastinės anemijos 
(jų atveju ne tik padidėja geležies rodiklis, bet ir feritino koncentracija), 
hematoporfirijos ( kartu padidėja ir feritino rodiklis ), talasemijos (kartu padidėja ir feritino rodiklis),
tuberkuliozė"""
        else:
            return """MCV Rezultatas normos ribose. 
    Tai svarbus rodiklis anemijos klasifikacijai ir gydymo sekimui."""
    if pasirinkimas == 16:
        if rezultatas > 33.5 and (lytis == "vyr" or lytis == "mot"):
            return """ MCH rezultatas virš norminės ribos. 
Galima makrocitine anemija (dažnai dėl folio rūgšties ar vitamino B12 trūkumo atsiradusi mažakraujystė).
Rodiklio padidėjimą gali įtakoti  megaloblastinė anemija ( padidėja  eritrocitai arba Hb kiekis), 
toksinis kepenų pažeidimas, lėtinis alkoholizmas, kontraceptikų vartojimas, skrandžio gleivinės pažeidimai,
skrandžio vėžys, žarnyno malabsorbcija, parazitai žarnyne (askaridės, strongiloidai, plokščiosios kirmėlės
ir t.t.), divertikuliozė, Krono (Crohn) liga, taikomas gydymas citostatikais,  vegetarinis maistas, 
mielodisplazinis sindromas (MDS). Retai – transkobalamino trūkumas (genetinis defektas) kraujyje. """
        elif rezultatas < 27.0 and (lytis == "vyr" or lytis == "mot"):
            return """MCH rezultatas žemiau norminės ribos.
Galima lėtinė anemija, ilgalaikis geležies trūkumas, apsinuodijimas švynu.  
Rodiklio sumažėjimui gali įtakoti  „Lėtinės ligos“ , kurias lydi anemija,  lėtiniai kraujavimai 
(sukeliantys geležies deficitą), neštumas, eritremija, sideroblastinės anemijos 
(jų atveju ne tik padidėja geležies rodiklis, bet ir feritino koncentracija), 
hematoporfirijos ( kartu padidėja ir feritino rodiklis ), talasemijos (kartu padidėja ir feritino rodiklis),
    tuberkuliozė"""
        else:
            return """MCH rezultatas normos ribose. 
Tai yra santykis tarp hemoglobino koncentracijos (HGB) ir eritrocitų (RBC) skaičiaus. 
Šis rodiklis parodo, kiek vidutiniškai viename eritrocite yra hemoglobino."""
    if pasirinkimas == 17:
        if rezultatas > 360 and (lytis == "vyr" or lytis == "mot"):
            return """ MCHC rezultatas virš norminės ribos. 
Preanalizės /matavimo klaida. Retais atvejais labai intensyvi hemolizė ar neįmanomas hemoglobino išmatavimas"""
        elif rezultatas < 315 and (lytis == "vyr" or lytis == "mot"):
            return """MCHC rezultatas žemiau norminės ribos.
MCHC mažėja, kai sutrinka hemoglobino sintezė"""
        else:
            return """MCHC rezultatas normos ribose. 
    Šis rodiklis susietas su hemoglobino koncentracija."""
    if pasirinkimas == 18:
        if rezultatas > 14.5 and (lytis == "vyr" or lytis == "mot"):
            return """ RDW-CV rezultatas virš norminės ribos.
RDW  padidėja kai yra stebimi šie susirgimai ar būklės: piktnaudžiavimas alkoholiu, 
folinės rūgšties deficito sukelta anemija (kartu stebimas ir MCV rodiklio padidėjimas bei HGB rodiklio sumažėjimas),
geležies deficito sukelta anemija (kartu stebimas ir MCV rodiklio norma ar pamažėjimas bei HGB rodiklio sumažėjimas),  
hemolizinė anemija, piktybinė anemija, pjautuvinių ląstelių anemija.
Padidėjęs RDW kartu su padidėjusiu MCH būdingesnis megaloblastinėms anemijoms."""
        elif rezultatas < 11.5 and (lytis == "vyr" or lytis == "mot"):
            return """RDW-CV rezultatas žemiau norminės ribos."""
        else:
            return """RDW-CV rezultatas normos ribose. 
Šis rodiklis svarbus veiksnys vertinant anemiją. RDV rodiklis turi būti vertinamas kartu su MCV rodikliu.
Nepadidėjęs RDW ir kartu padidėjęs MCV kartais būna ikileukeminių būklių bei aplastinės anemijos metu."""
    if pasirinkimas == 19:
        if rezultatas > 370 and (lytis == "vyr" or lytis == "mot"):
            return """ PLT rezultatas virš norminės ribos.
Didėjant PLT  rodikliui, didėja kraujo krešulių susidarymo tikimybė. 
Trombocitų skaičius gali padidėti: po operacijų, nukraujavus, po intensyvaus fizinio krūvio, streso, 
retais atvejais  sergant lėtinėmis uždegiminėmis ligomis, anemija, mielofibroze."""
        elif rezultatas < 150 and (lytis == "vyr" or lytis == "mot"):
            return """PLT  rezultatas žemiau norminės ribos.
Sumažėja kraujo krešėjimo galimybės. 
Trombocitų skaičiaus sumažėjimą gali lemti: kaulų čiulpų veiklą slopinančios ligos, leukemija, 
autoimuniniai sindromai, esantys kaulų čiulpų pažeidimai dėl piktybinių navikų metastazių, 
gausiai vartojamas alkoholis, nėštumas."""
        else:
            return """PLT rezultatas normos ribose. 
Trombocitai dalyvauja kraujo krešėjime."""
    else:
        return None


def rodyti_komentara():
    pasirinkimas = entry_pas.curselection()
    if pasirinkimas:
        pasirinkimas = int(pasirinkimas[0]) + 1
        rezultatas = entry_rez.get().replace(",", ".")
        try:
            rezultatas = float(rezultatas)
            if rezultatas < 0:
                rezultatas_text.set("Skaičius turi būti teigiamas.")
            else:
                lytis = lyties_var.get()
                if lytis == "Vyras":
                    lytis = "vyr"
                elif lytis == "Moteris":
                    lytis = "mot"
                komentaras = tikrinti_analyte(pasirinkimas, lytis, rezultatas)
                if komentaras is not None:
                    rezultatas_text.set(komentaras)
                else:
                    rezultatas_text.set("Nėra komentarų šiam rezultatui.")
        except ValueError:
            rezultatas_text.set("Įvestas ne skaičius. Pakartotinai pasirinkite analitę ir įveskite rezultatą.")


def prideti_parametrus():
    for indeksas, parametras in parametrai.items():
        entry_pas.insert(indeksas, parametras)


def rezultato_komentavimas():
    rodyti_komentara()


pagrindinis = Tk()
pagrindinis.title("BKV")

uzrasas = Label(pagrindinis, width=40, height=5, fg='red', font=('Helvetica bold', 12),
                text="Bendro kraujo vaizdo komentavimas (suaugusiems)")
uzrasas.pack()

icon_kelias = r"C:\Users\juozu\OneDrive\Desktop\bkv.ico"
pagrindinis.iconbitmap(icon_kelias)

label_pas = Label(pagrindinis, fg='blue', font=('Helvetica bold', 12), text="Pasirinkite analitės pavadinimą")
label_pas.pack()

entry_pas = Listbox(pagrindinis, font=('Helvetica bold', 10), height=10, width=50, selectmode=SINGLE)
entry_pas.pack()

label_rez = Label(pagrindinis, fg='blue', font=('Helvetica bold', 12), text="Įveskite rezultato skaičių")
label_rez.pack()

entry_rez = Entry(pagrindinis, font=('Helvetica bold', 12), width=10)
entry_rez.pack()

label_lytis = Label(pagrindinis, fg='blue', font=('Helvetica bold', 12), text="Pasirinkite lytį")
label_lytis.pack()

lyties_var = StringVar()
lyties_var.set("Vyras")

radio_vyras = Radiobutton(pagrindinis, text="Vyras", font=('Helvetica bold', 10), variable=lyties_var, value="Vyras")
radio_vyras.pack()

radio_mot = Radiobutton(pagrindinis, text="Moteris", font=('Helvetica bold', 10), variable=lyties_var, value="Moteris")
radio_mot.pack()

mygtukas = Button(pagrindinis, text="Rodyti komentarą", font=('Helvetica bold', 12), command=rodyti_komentara)
mygtukas.pack()

rezultatas_text = StringVar()
rezultatas_text.set("")

label_komentaras = Label(pagrindinis, textvariable=rezultatas_text, fg='green', font=('Helvetica bold', 12))
label_komentaras.pack()

prideti_parametrus()

pagrindinis.mainloop()
