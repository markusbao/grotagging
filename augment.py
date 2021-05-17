#!/usr/bin/python

import random
import copy
import re

superdict = {

	"moi": ["ik","'k"],
	"zijn" : ["bin", "bist", "is", "binnen", "was", "wast", "wazzen","waren"],
	"gaan" : ["goa","gaaist","gaait","goan","ging", "gingst", "gongst","gingen","gongen"],
	"laten" : ["loat", "loa'k", "letst", "let","loaten","lo've", "lait","luit","laitst","luitst","laiten","luiten"],
	"zien" : ["zigst","zugst","zigt","zugt","zain","zag","zagst","zagen"],
	"hebben": ["heb","hest","het","hetten",'had', "hebb'n", "hadd'n","hadden"],
	"kommen" : ['kom','kwam', "kwammen","kwamen", "kommen","komen","komt"],
	"telwoorden" :["twij","twei","tweie","drij","drei","dreie","vaaier","vare","vief","vuuf","zes","zesse","zeuven","aachte","negen","elven","twolven","dartien","vartien","vieftien","zestien","zeuventien","aachttien","negentien"],
	"tientallen" :["tien","tiene","twinteg","darteg","varteg","vieftig","zesteg","zeuventeg","taahteg","negenteg","honderd","doezend"],
	"kleuren" : ["rood","geel","blauw","gruin","oraanje","paars","sangen","ros","gries","swaart","broen","wit"],
	"weekdagen": ["moandag","dingsdag","wonsdag","dunderdag","vraaidag","zoaterdag","zundag"],
	"maanden": ["jannewoari","febrewoari","meert","pril","maai","juni","juli","augustes","septimber","oktober","novìmber","dezimber"],
	"seizoenen" : ["zummer","haafst","winter","linte"],
	"overdag" : ["middeg", "mirreg", "noamiddag", "nommerdag", "oavend", "veumiddag", "veumirreg", "veurmirreg", "vummerdag", "naacht", "nacht","nachte","nommiddag"],
	"sdags" : ["middegs", "mirregs", "noamiddags", "nommerdags", "oavends", "veumiddags", "veumirregs", "veurmirregs", "vummerdags", "naachts", "nachts","nommiddags"],
	"gender" : ['wichtje', 'wicht', 'kerel', 'kereltje',"boaswicht","manskerel", "elfrib", "mensk", "poerie" ,"vraauw" ,"wief","man","meneer" ],
	"kleuren" : ['blauuw', 'greun', 'gruin', 'gaal', 'gale', 'broen','bruun', 'oraanje']

}

startdict={
	"ik":"moi","'k":"moi",
	"bin":"zijn","bist":"zijn","is":"zijn","binnen":"zijn","was":"zijn","wast":"zijn","wazzen":"zijn","waren":"zijn",
	"goa":"gaan","gaaist":"gaan","gaait":"gaan","goan":"gaan","ging":"gaan","gingst":"gaan","gongst":"gaan","gingen":"gaan","gongen":"gaan",
	"loat":"laten","loa'k":"laten","letst":"laten","let":"laten","loaten":"laten","lo've":"laten","lait":"laten","luit":"laten","laitst":"laten","luitst":"laten","laiten":"laten","luiten":"laten",
	"zai":"zien","zigst":"zien","zugst":"zien","zigt":"zien","zugt":"zien","zain":"zien","zag":"zien","zagst":"zien","zagen":"zien",
	"heb":"hebben","hest":"hebben","het":"hebben","hetten":"hebben","had":"hebben","hebb'n":"hebben","hadd'n":"hebben","hadden":"hebben",
	"kom":"kommen","kwam":"kommen","kwammen":"kommen","kwamen":"kommen","kommen":"kommen","komen":"kommen","komt":"kommen",
	"twij":"telwoorden","twei":"telwoorden","tweie":"telwoorden","drij":"telwoorden","drei":"telwoorden","dreie":"telwoorden","vaaier":"telwoorden","vare":"telwoorden","vief":"telwoorden","vuuf":"telwoorden","zes":"telwoorden","zesse":"telwoorden","zeuven":"telwoorden","aachte":"telwoorden","negen":"telwoorden","elven":"telwoorden","twolven":"telwoorden","dartien":"telwoorden","vartien":"telwoorden","vieftien":"telwoorden","zestien":"telwoorden","zeuventien":"telwoorden","aachttien":"telwoorden","negentien":"telwoorden",
	"tien":"tientallen","tiene":"tientallen","twinteg":"tientallen","darteg":"tientallen","varteg":"tientallen","vieftig":"tientallen","zesteg":"tientallen","zeuventeg":"tientallen","taahteg":"tientallen","negenteg":"tientallen","honderd":"tientallen","doezend":"tientallen",
	"blauuw":"kleuren","greun":"kleuren","gruin":"kleuren","gaal":"kleuren","gale":"kleuren","broen":"kleuren","bruun":"kleuren","oraanje":"kleuren",
	"moandag":"weekdagen","dingsdag":"weekdagen","wonsdag":"weekdagen","dunderdag":"weekdagen","vraaidag":"weekdagen","zoaterdag":"weekdagen","zundag":"weekdagen",
	"jannewoari":"maanden","febrewoari":"maanden","meert":"maanden","pril":"maanden","maai":"maanden","juni":"maanden","juli":"maanden","augustes":"maanden","septimber":"maanden","oktober":"maanden","novìmber":"maanden","dezimber":"maanden",
	"zummer":"seizoenen","haafst":"seizoenen","winter":"seizoenen","linte":"seizoenen",
	"middeg":"overdag","mirreg":"overdag","noamiddag":"overdag","nommerdag":"overdag","oavend":"overdag","veumiddag":"overdag","veumirreg":"overdag","veurmirreg":"overdag","vummerdag":"overdag","naacht":"overdag","nacht":"overdag","nachte":"overdag","nommiddag":"sdags",
	"middegs":"sdags","mirregs":"sdags","noamiddags":"sdags","nommerdags":"sdags","oavends":"sdags","veumiddags":"sdags","veumirregs":"sdags","veurmirregs":"sdags","vummerdags":"sdags","naachts":"sdags","nachts":"sdags", "nommiddags":"sdags",
	"wichtje":"gender","wicht":"gender","kerel":"gender","kereltje":"gender","boaswicht":"gender","manskerel":"gender","elfrib":"gender","mensk":"gender","poerie":"gender","vraauw":"gender","wief":"gender","man":"gender","meneer":"gender"
}



superlocdic={
	"steden" : ['Oadörp','Auwerd','Bavvelt','Beem','Beerte','Bennewolle','Baaierm','Blijham','Boertang','Bronsveen','Delfziel','Naandel','Doezum','Ainrom','Aikamp','Aimentil','Eppenhoezen','Euvelgun','Aizing','Faarmsom','Fiwwerd','Finnerwol','Foxhol',	'Gaarmwol','Garwerd','Garsthoezen','Glimmen','Glìnse','Gruupskerk','Hoaren','Haarstee','Helm','Holwier','Hogezaand','Hoogkerk','Hörnhoezen','Houwerziel','Kannes','Kloosterboeren','Kommerziel','Kraiwerd','Wolle','Leek','Lains','Leerms','Loppersom','Lösdörp','Lutjegast','Lutjesoaksem',
				'Houk','Moarum','Maiden','Middelsom','Midwolle','Muntendam','Muzzelknoal','Nijbert','Nijhoof','Nijziel','Noordbrouk','Noordhörn','Noordloaren','Noordwiek','Nuus','Obergum','Olhoof','Onderndaam','Onnen','Onstwedde','Oosterhogebrug','Nijlaand','Oostwol','Paiterboeren','Pieterziel',
				'Raskerd','Röppen','Roeskerbrug','Soaksum','Soaksumhoezen','Saauwerd','Sapmeer','Schaarmer','Scheemde','Schewòl','Seballeburen','Zèlng','Sibboeren','Slochter','Spiek','Knoal','Steem','Stivverd','Troapel','Troapelknoal','Termunten','Taisn','Tinaalngn','Tjuggem','Oethoezen','Meij','Ollerom','Oskerd',	'Veendam','Vlagtwedde','Vraiskelo','Woagenbörgen','Waarvum','Wedde','Wij','Westeremmen','Westerlij','Nijlaand','Wetsen','Winschoot','Winzum','Wirdum','Woldendörp','Baarge','Woltersom','Zanneweer','Zeuvenhuzen','Zieldiek','Zoltkamp','Zuudhorn','Zuudwòl'],
	"lidwoorden" :["'t", "'n",'de','Den','Ten','Nij'],
	"windrichtingen" : ['Noord','Oost','Zuud','West','Zuid','Noordwest','Zuudwest','Noordoost','Zuudoost'],
	"bijvoegelijke_plaatsen" : ['Grode', 'Grote',"Nieuwe", 'Nij', 'Olte','Ol'],
	"na_lidwoord" : ['Hoag','Noorden','Zuiden','Westen','Oosten','Post','Pekel','Daam','Hammerk','Ham','Boer','Zaand','Penne','Wilp'],
	"stedenenlanden" : ['Nederland', 'Groningen','Assen','Leeuwarden','Amsterdam','Rotterdam','Emmen','Duitsland','Japan','Afrika','Europa','Amerikoa','Azie','China','Rusland','Oceanie'],
	"daip":['Raidaip','Damsterdaip','Schutendaip','Raitdaip','Winschoterdaip','Zuuderdaip'],
	"grunnen":['Grunnen','Friesland','Drenthe','Zwolle','Assen','Utrecht','Emmen','Berlijn','Moskou']
}

locdic={
	"oadörp":"steden","auwerd":"steden","bavvelt":"steden","beem":"steden","beerte":"steden","bennewolle":"steden","baaierm":"steden","blijham":"steden","boertang":"steden","bronsveen":"steden","delfziel":"steden","naandel":"steden","doezum":"steden","ainrom":"steden","aikamp":"steden","aimentil":"steden","eppenhoezen":"steden","euvelgun":"steden","aizing":"steden",
	"faarmsom":"steden","fiwwerd":"steden","finnerwol":"steden","foxhol":"steden","gaarmwol":"steden","garwerd":"steden","garsthoezen":"steden","glimmen":"steden","glìnse":"steden","gruupskerk":"steden",
	"hoaren":"steden","haarstee":"steden","helm":"steden","holwier":"steden","hogezaand":"steden","hoogkerk":"steden","hörnhoezen":"steden","houwerziel":"steden","kannes":"steden","kloosterboeren":"steden","kommerziel":"steden","kraiwerd":"steden","wolle":"steden",
	"leek":"steden","lains":"steden","leerms":"steden","loppersom":"steden","lösdörp":"steden","lutjegast":"steden","lutjesoaksem":"steden","houk":"steden","moarum":"steden","maiden":"steden","middelsom":"steden","midwolle":"steden","muntendam":"steden","muzzelknoal":"steden",
	"nijbert":"steden","nijhoof":"steden","nijziel":"steden","noordbrouk":"steden","noordhörn":"steden","noordloaren":"steden","noordwiek":"steden","nuus":"steden","obergum":"steden","olhoof":"steden","onderndaam":"steden","onnen":"steden","onstwedde":"steden","oosterhogebrug":"steden",
	"nijlaand":"steden","oostwol":"steden","paiterboeren":"steden","pieterziel":"steden","raskerd":"steden","röppen":"steden","roeskerbrug":"steden","soaksum":"steden","soaksumhoezen":"steden","saauwerd":"steden","sapmeer":"steden","schaarmer":"steden","scheemde":"steden","schewòl":"steden","seballeburen":"steden","zèlng":"steden",
	"sibboeren":"steden","slochter":"steden","spiek":"steden","knoal":"steden","steem":"steden","stivverd":"steden","troapel":"steden","troapelknoal":"steden","termunten":"steden","taisn":"steden","tinaalngn":"steden","tjuggem":"steden","oethoezen":"steden","meij":"steden","ollerom":"steden","oskerd":"steden","veendam":"steden","vlagtwedde":"steden","vraiskelo":"steden",
	"woagenbörgen":"steden","waarvum":"steden","wedde":"steden","wij":"steden","westeremmen":"steden","westerlij":"steden","nijlaand":"steden","wetsen":"steden","winschoot":"steden","winzum":"steden","wirdum":"steden","woldendörp":"steden","baarge":"steden","woltersom":"steden","zanneweer":"steden","zeuvenhuzen":"steden","zieldiek":"steden","zoltkamp":"steden",
	"zuudhorn":"steden","zuudwòl":"steden","'t":"lidwoorden","'n":"lidwoorden","de":"lidwoorden","den":"lidwoorden","ten":"lidwoorden","nij":"lidwoorden","noord":"windrichtingen","oost":"windrichtingen","zuud":"windrichtingen","west":"windrichtingen","zuid":"windrichtingen","noordwest":"windrichtingen","zuudwest":"windrichtingen","noordoost":"windrichtingen",
	"zuudoost":"windrichtingen","grode":"bijvoegelijke_plaatsen","grote":"bijvoegelijke_plaatsen","nieuwe":"bijvoegelijke_plaatsen","nij":"bijvoegelijke_plaatsen","olte":"bijvoegelijke_plaatsen","ol":"bijvoegelijke_plaatsen",
	"hoag":"na_lidwoord","noorden":"na_lidwoord","zuiden":"na_lidwoord","westen":"na_lidwoord","oosten":"na_lidwoord","post":"na_lidwoord","pekel":"na_lidwoord","daam":"na_lidwoord","hammerk":"na_lidwoord","ham":"na_lidwoord","boer":"na_lidwoord","zaand":"na_lidwoord","penne":"na_lidwoord","wilp":"na_lidwoord"
}

namesdict={
	"voornamen": ["Aafje","Aafke","Aaltien","Aaltje","Aafie","Aalie","Aalkje","Alkien","Amke","Anja","Anje","Annechien","Antje","Aukje","Berendina","Bertha","Betje","Bettina","Bientje","Bontina","Bougien","Bouke","Boukelien","Bouwien","Diddie","Dientje","Dina","Dini",
	"Eempien","Efina","Eisien","Eisje","Elsien","Emke","Enna","Erda","Erika","Erna","Eika","Emmie","Fennie","Fiene","Fieneke","Finne","Fokkelien","Frouke","Froukje","Geertruida","Geesje","Geessie","Gepke","Geppie","Gerrie","Gezina","Giena","Gre","Greta","Gretje","Hanna","Harkolien","Harmanna","Harmien","Harmina","Henderika","Henderkien","Hendrikje","Hennie","Hilda","Hillechie","Hillie","Hiltje","Hinnie",
	"Ietje","Janke","Jantina","Jantje","Jeltina","Juurtje","Kee","Kina","Knelske","Koba","Kornelia","Kunera","Lammechien","Lammie","Lies","Maike","Manna","Mannie","Marchien","Margina","Martje","Meika","Meike","Meintje","Mennie","Miene","Mila","Neissien","Nies","Niesje","Okje","Okkina","Paulina","Pia","Piek","Piekie","Pieterdina","Pike","Popkolina",
	"Reika","Reina","Renske","Richtje","Roelfien","Roelfje","Roelie","Sapke","Sela","Siebrig","Siena","Sietske","Sina","Stientje","Stineke","Swannie","Tamma","Tammo","Tet","Tetske","Teuntje","Tina","Tini","Tipi","Tjaakje","Tjitske","Trientje","Trijnie","Trijntje","Trineke","Trui","Truida","Wiepke","Wiegedina","Zwaantina","Zwaantje",
	"Aaldrik","Aalf","Ale","Aalje","Aalko","Alle","Amel","Andries","Anje","Anjo","Anko","Appie","Arend","Auko","Bartje","Be","Berend","Bobbe","Bodde","Bontko","Bouke","Bouko","Bruin","Derk","Derwinus","Dienko","Dietert","Dirk","Dries","Drikus","Eelje","Eelko","Eildert","Eise","Eiso","Eltje","Eltjo","Elzo","Emke","Enno","Epi","Eppe","Eppo","Evert",
	"Fedde","Feike","Fekke","Fokke","Fokko","Freek","Frerk","Garmt","Ge","Geert","Gepko","Geppie","Gerko","Gerrie","Gert","Geurt","Gezinus","Gienus","Haimo","Harjo","Harko","Harm","Harmannus","Harte","Heerke","Heertje","Hemmo","Henderkien","Hendrik","Hennie","Hiele","Hielke","Hielko","Hilko","Hilleginus","Hinne",
	"Jelte","Jelting","Jelto","Job","Jochem","Jochie","Jop","Jurrie","Kobus","Koop","Kris","Kunje","Kuno","Lammert","Laurens","Leendert","Loekie","Lubbe","Luit","Luitsen","Lukkien","Luppo","Luut","Manne","Mannie","Mans","Meine","Melle","Menno","Nanko","Okke","Omke","Ommo","Otto",
	"Pike","Popke","Popko","Reinder","Reindert","Remko","Remmelt","Repko","Rieks","Riks","Rikus","Roelf","Sebe","Sicco","Siebe","Siepko","Sietze","Sipko","Sjabe","Sjakie","Sjako","Sjoerd","Sjonnie","Steffen","Steven",
	"Talo","Tamme","Tammo","Tebbe","Teun","Teunes","Teunis","Theo","Ties","Tijs","Tinus","Tjaard","Tjabbo","Tjabe","Tjakko","Tjapke","Tjapko","Toal","Toams","Tobàis","Tole","Tonko","Tonnie","Tonnies","Trienko","Tunnies","Uulderik","Wiendelt","Wiep","Wietze","Wilderik","Willy","Winus","Wobbe","Wobbie","Wolter","Wopke","Wubbe"],
	"achternamen":["Albronda","Alberda","Alers","Ahlers","Allersma","Alting","Anema","Atzema","Balkema","Beens","Beins","Beks","Boerma","Bontjer","Bosker","Bouland","Brands","Broekema","Bulthuis","Bults","Busker","Deuling","Dieters","Dijkema","Dubben","Edens","Eltingh","Engelage","Engwerda",
	"Ferwerda","Garrelds","Geertsema","Glaasker","Haaksema","Harms","Hartsema","Hindriks","Heidema","Hensens","Hensema","Hoeksema","Hoiting","Hoitzing","Idema","Ipema","Iwema","Jans","Jansma","Jensema","Kuper","Luttjeboer","Lutjeboer","Luursema","Luurtsema","Medema","Meins","Meinders","Moesker","Molema","Nienhuis",
	"Oldenhuis","Oolders","Oosterhuis","Peters","Prummel","Rauwerda","Reiffers","Rendering","Renkema","Rensema","Rensuma","Ritzema","Ripperda","Ronda","Roorda","Roukema","Schepers","Scholtens","Schripsema","Schuitema","Siemens","Siemons","Simons","Siepel","Sikkema","Sikkens","Slopsema","Snitjer","Steenhuis",
	"Tieben","Tjabbes","Vries","Wams","Wiegers","Wichers","Wiechers","Wierda","Wiersma of Wiersema","Wigbold","Wigboldus","van Winsum","Woldendorp","Wolgen","Wubs"]
}




readfile=open('spec_sentences.txt', 'r')
outfile=open('augmented_full.txt', 'a+')


for line in readfile:
	skip=0
#	print(line)
	line = eval(line)
	#print(line)
	sentence=[]

	for word in line:
		x = word.split('\t')
		sentence.append(x)



	#print(sentence)
	a1 = copy.deepcopy(sentence)
	b2 = copy.deepcopy(sentence)
	c3 = copy.deepcopy(sentence)
	d4 = copy.deepcopy(sentence)
	e5 = copy.deepcopy(sentence)



#	print(line)
	#print(line)
	#s1,s2,s3,s4,s5  = sentence,sentence,sentence,sentence,sentence
	#print(s2)
	#print(s3)
	#print(s4)
	#print(s5)
	c=-1
	for word in sentence:
		#print(word)
		#rint(word[0])
		#print(word)
		c+=1
		if word[1] == 'B-PER':
			try:
				if sentence[c+1][1] == 'I-PER':
					replacewords = namesdict['voornamen']
					rp=random.sample(replacewords,5)
					a1[c][0]=rp[0]
					b2[c][0]=rp[1]
					c3[c][0]=rp[2]
					d4[c][0]=rp[3]
					e5[c][0]=rp[4]
					replacewords=[]
					rp=[]
				else:
					try:
						if startdict[sentence[c-1][0]] == 'meneer':
							replacewords = namesdict['achternamen']
							rp=random.sample(replacewords,5)
							a1[c][0]=rp[0]
							b2[c][0]=rp[1]
							c3[c][0]=rp[2]
							d4[c][0]=rp[3]
							e5[c][0]=rp[4]
							replacewords=[]
							rp=[]
						else:
							replacewords = namesdict['voornamen']
							rp=random.sample(replacewords,5)
							a1[c][0]=rp[0]
							b2[c][0]=rp[1]
							c3[c][0]=rp[2]
							d4[c][0]=rp[3]
							e5[c][0]=rp[4]
							replacewords=[]
							rp=[]
					except:
						replacewords = namesdict['voornamen']
						rp=random.sample(replacewords,5)
						a1[c][0]=rp[0]
						b2[c][0]=rp[1]
						c3[c][0]=rp[2]
						d4[c][0]=rp[3]
						e5[c][0]=rp[4]
						replacewords=[]
						rp=[]


			except:
				#Als het woord voor B-PER woord in meneer of mevrouw dict zit, dan wordt het een achternaam, anders een voornaam
				try:
					if startdict[sentence[c-1][0]] == 'meneer':
						replacewords = namesdict['achternamen']
						rp=random.sample(replacewords,5)
						a1[c][0]=rp[0]
						b2[c][0]=rp[1]
						c3[c][0]=rp[2]
						d4[c][0]=rp[3]
						e5[c][0]=rp[4]
						replacewords=[]
						rp=[]
					else:
						replacewords = namesdict['voornamen']
						rp=random.sample(replacewords,5)
						a1[c][0]=rp[0]
						b2[c][0]=rp[1]
						c3[c][0]=rp[2]
						d4[c][0]=rp[3]
						e5[c][0]=rp[4]
						replacewords=[]
						rp=[]
				except:
					replacewords = namesdict['voornamen']
					rp=random.sample(replacewords,5)
					a1[c][0]=rp[0]
					b2[c][0]=rp[1]
					c3[c][0]=rp[2]
					d4[c][0]=rp[3]
					e5[c][0]=rp[4]
					replacewords=[]
					rp=[]

		elif word[1] == 'I-PER':
			try:
				#Als er nog een I-PER achterzit wordt het een voornaam, anders achternaam
				if sentence[c+1][1] == 'I-PER':
					replacewords = namesdict['voornamen']
					rp=random.sample(replacewords,5)
					a1[c][0]=rp[0]
					b2[c][0]=rp[1]
					c3[c][0]=rp[2]
					d4[c][0]=rp[3]
					e5[c][0]=rp[4]
					replacewords=[]
					rp=[]
				else:
					replacewords = namesdict['achternamen']
					rp=random.sample(replacewords,5)
					a1[c][0]=rp[0]
					b2[c][0]=rp[1]
					c3[c][0]=rp[2]
					d4[c][0]=rp[3]
					e5[c][0]=rp[4]
					replacewords=[]
					rp=[]		
			except:
				replacewords = namesdict['achternamen']
				rp=random.sample(replacewords,5)
				a1[c][0]=rp[0]
				b2[c][0]=rp[1]
				c3[c][0]=rp[2]
				d4[c][0]=rp[3]
				e5[c][0]=rp[4]
				replacewords=[]
				rp=[]


		elif word[1] == 'B-LOC':			
			try:
				#komt er na B-LOC ook I-LOC? Zo, ja, komt er na I-LOC ook I-LOC
				if sentence[c+1][1] == 'I-LOC':
					try:
						if word[0].lower() in locdic:
							if sentence[c+2][1] == 'I-LOC':
								pass
							elif word[0].lower() in locdic:
								replacewords = superlocdic[locdic[word[0].lower()]]
								rp=random.sample(replacewords,5)
								a1[c][0]=rp[0]
								b2[c][0]=rp[1]
								c3[c][0]=rp[2]
								d4[c][0]=rp[3]
								e5[c][0]=rp[4]
								rp = []
								replacewords=[]	
							else:
								replacewords = superlocdic['bijvoegelijke_plaatsen']
								rp=random.sample(replacewords,5)
								a1[c][0]=rp[0]
								b2[c][0]=rp[1]
								c3[c][0]=rp[2]
								d4[c][0]=rp[3]
								e5[c][0]=rp[4]
								rp = []
								replacewords=[]
					except:									
						replacewords = superlocdic['lidwoorden']
						rp=random.sample(replacewords,5)
						a1[c][0]=rp[0]
						b2[c][0]=rp[1]
						c3[c][0]=rp[2]
						d4[c][0]=rp[3]
						e5[c][0]=rp[4]
						replacewords=[]
						rp=[]
				else:
					tw = word[0].lower()
					if re.match("straat",tw) or re.match("stroat",tw) or re.match("laan",tw) or re.match("loan",tw) or re.match("loane",tw) or re.match("weg",tw) or re.match("kade",tw) or re.match("heerd",tw) or re.match("singel",tw) or re.match("steeg",tw):
						replacewords = superlocdic['straat']
						rp=random.sample(replacewords,5)
						a1[c][0]=rp[0]
						b2[c][0]=rp[1]
						c3[c][0]=rp[2]
						d4[c][0]=rp[3]
						e5[c][0]=rp[4]
						rp = []
						replacewords=[]
					elif re.match("daip",tw) or re.match("gracht",tw):
						replacewords = superlocdic['daip']
						rp=random.sample(replacewords,5)
						a1[c][0]=rp[0]
						b2[c][0]=rp[1]
						c3[c][0]=rp[2]
						d4[c][0]=rp[3]
						e5[c][0]=rp[4]
						rp =[]
						replacewords=[]
					elif tw =='grunnen':
						replacewords = superlocdic['grunnen']
						rp=random.sample(replacewords,5)
						a1[c][0]=rp[0]
						b2[c][0]=rp[1]
						c3[c][0]=rp[2]
						d4[c][0]=rp[3]
						e5[c][0]=rp[4]
						rp=[]
						replacewords=[]
					elif word[0].lower() in locdic:
						replacewords = superlocdic[locdic[word[0].lower()]]
						rp=random.sample(replacewords,5)
						a1[c][0]=rp[0]
						b2[c][0]=rp[1]
						c3[c][0]=rp[2]
						d4[c][0]=rp[3]
						e5[c][0]=rp[4]
						rp = []
						replacewords=[]					
					else:
						replacewords = superlocdic['steden']
						rp=random.sample(replacewords,5)
						a1[c][0]=rp[0]
						b2[c][0]=rp[1]
						c3[c][0]=rp[2]
						d4[c][0]=rp[3]
						e5[c][0]=rp[4]
						rp=[]
						replacewords=[]																											
			#Alleen B-LOC
			except:
				tw = word[0].lower()
				if re.match("straat",tw) or re.match("stroat",tw) or re.match("laan",tw) or re.match("loan",tw) or re.match("loane",tw) or re.match("weg",tw) or re.match("kade",tw) or re.match("heerd",tw) or re.match("singel",tw) or re.match("steeg",tw):
					replacewords = superlocdic['straat']
					rp=random.sample(replacewords,5)
					a1[c][0]=rp[0]
					b2[c][0]=rp[1]
					c3[c][0]=rp[2]
					d4[c][0]=rp[3]
					e5[c][0]=rp[4]
					rp = []
					replacewords=[]
				elif re.match("daip",tw) or re.match("gracht",tw):
					replacewords = superlocdic['daip']
					rp=random.sample(replacewords,5)
					a1[c][0]=rp[0]
					b2[c][0]=rp[1]
					c3[c][0]=rp[2]
					d4[c][0]=rp[3]
					e5[c][0]=rp[4]
					rp =[]
					replacewords=[]
				elif tw =='grunnen':
					replacewords = superlocdic['grunnen']
					rp=random.sample(replacewords,5)
					a1[c][0]=rp[0]
					b2[c][0]=rp[1]
					c3[c][0]=rp[2]
					d4[c][0]=rp[3]
					e5[c][0]=rp[4]
					rp=[]
					replacewords=[]				
				else:
					replacewords = superlocdic['steden']
					rp=random.sample(replacewords,5)
					a1[c][0]=rp[0]
					b2[c][0]=rp[1]
					c3[c][0]=rp[2]
					d4[c][0]=rp[3]
					e5[c][0]=rp[4]
					rp=[]
					replacewords=[]							

		elif word[1] == 'I-LOC':
			tw = word[0].lower()
			if word[0] == 'en' or sentence[c-1][0] =='en':
				pass
				#Als straat naam is, verander in straatnaam
			elif word[0].lower() in locdic:
				replacewords = superlocdic[locdic[word[0].lower()]]
				rp=random.sample(replacewords,5)
				a1[c][0]=rp[0]
				b2[c][0]=rp[1]
				c3[c][0]=rp[2]
				d4[c][0]=rp[3]
				e5[c][0]=rp[4]
				rp = []
				replacewords=[]					
			elif re.match("straat",tw) or re.match("stroat",tw) or re.match("laan",tw) or re.match("loan",tw) or re.match("loane",tw) or re.match("weg",tw) or re.match("kade",tw) or re.match("heerd",tw) or re.match("singel",tw) or re.match("steeg",tw):
				replacewords = superlocdic['straat']
				rp=random.sample(replacewords,5)
				a1[c][0]=rp[0]
				b2[c][0]=rp[1]
				c3[c][0]=rp[2]
				d4[c][0]=rp[3]
				e5[c][0]=rp[4]
				rp = []
			elif re.match("daip",tw) or re.match("gracht",tw):
				replacewords = superlocdic['daip']
				rp= random.sample(replacewords,5)
				a1[c][0]=rp[0]
				b2[c][0]=rp[1]
				c3[c][0]=rp[2]
				d4[c][0]=rp[3]
				e5[c][0]=rp[4]
				rp =[]
				replacewords=[]			
			else:
				try:
					sentence[c+1][1] == 'I-LOC'
					replacewords = superlocdic[locdic[word[0].lower()]]
					rp=random.sample(replacewords,5)
					a1[c][0]=rp[0]
					b2[c][0]=rp[1]
					c3[c][0]=rp[2]
					d4[c][0]=rp[3]
					e5[c][0]=rp[4]
					rp = []
					replacewords=[]
				except:
					try:
						if sentence[c-1][0] in superlocdic['lidwoorden']:
							replacewords = superlocdic['na_lidwoord']
							rp=random.sample(replacewords,5)
							a1[c][0]=rp[0]
							b2[c][0]=rp[1]
							c3[c][0]=rp[2]
							d4[c][0]=rp[3]
							e5[c][0]=rp[4]
							rp=[]
							replacewords=[]
						else:
							replacewords = superlocdic['stedenenlanden']
							rp=random.sample(replacewords,5)
							a1[c][0]=rp[0]
							b2[c][0]=rp[1]
							c3[c][0]=rp[2]
							d4[c][0]=rp[3]
							e5[c][0]=rp[4]
							rp=[]
							replacewords=[]								

					except:
						replacewords = superlocdic['stedenenlanden']
						rp=random.sample(replacewords,5)
						a1[c][0]=rp[0]
						b2[c][0]=rp[1]
						c3[c][0]=rp[2]
						d4[c][0]=rp[3]
						e5[c][0]=rp[4]
						rp=[]
						replacewords=[]								






		elif word[0] in startdict:
			#print(s1)
			print(word[0])
			replacewords = superdict[startdict[word[0].lower()]]
			print(replacewords)
			if len(replacewords) >= 5:
				rp = random.sample(replacewords,5)
				a1[c][0]=rp[0]
				b2[c][0]=rp[1]
				c3[c][0]=rp[2]
				d4[c][0]=rp[3]
				e5[c][0]=rp[4]

				replacewords=[]
				rp=[]				
			else:
				#print(s1)
				print('tttttttttttttttttttttttttttttttttttttt')

				rp=replacewords
				print(rp)
				randomlist = replacewords
				while len(rp) < 5:
					rp.append(random.choice(randomlist))
				rp=random.sample(rp, len(rp))
				print(rp)
				print('a1 -----------------------------------------------------')
				a1[c][0]=rp[0]
				print(a1[c][0])
				print(a1)
				b2[c][0]=rp[1]
				c3[c][0]=rp[2]
				print('d4 -----------------------------------------------------')
				d4[c][0]=rp[3]
				print(d4[c][0])
				print(d4)
				print(a1)
				print('e5 -----------------------------------------------------')
				e5[c][0]=rp[4]
				print(e5[c][0])
				print(e5)
				print(a1)
				replacewords=[]
				randomlist=[]
				rp=[]


	print('end')
	
	outfile.write('----------------' + '\n')
	outfile.write(str(line)+ '\n')
	outfile.write('----------------'+ '\n')
	outfile.write(str(a1)+ '\n')
	outfile.write(str(b2)+ '\n')
	outfile.write(str(c3)+ '\n')
	outfile.write(str(d4)+ '\n')
	outfile.write(str(e5)+ '\n')

outfile.close()
readfile.close()


