replace_dic={'@CAPS1': 'broadtail',
	'@CAPS2': 'dysthymia',
	'@CAPS3': 'picador',
	'@CAPS4': 'malleolus',
	'@CAPS5': 'anhydride',
	'@CAPS6': 'bazar',
	'@CAPS7': 'squeezebox',
	'@CAPS8': 'lightship',
	'@CAPS9': 'enuresis',
	'@CAPS10': 'myasthenia',
	'@CAPS11': 'anthropoid',
	'@CAPS12': 'destructor',
	'@CAPS14': 'scotoma',
	'@CAPS13': 'tremolite',
        '@CAPS15': 'jackscrew',
        '@CAPS16': 'enucleation',
	'@CAPS17': 'torr',
	'@CAPS18': 'relator',
	'@CAPS19': 'esophagitis',
	'@CAPS20': 'hydrogel',
	'@CAPS21': 'benne',
	'@CAPS22': 'mandamus',
	'@CAPS23': 'pyrolysis',
	'@CAPS24': 'hemiplegia',
	'@CAPS25': 'hypomania',
	'@CAPS26': 'stromatolite',
	'@CAPS27': 'kirtle',
	'@CAPS28': 'silversides',
	'@CAPS29': 'princedom',
	'@CAPS30': 'hypercapnia',
        '@CAPS31': 'contador',
	'@CAPS32': 'onchocerciasis',
	'@CAPS33': 'perianth',
	'@CAPS34': 'pastorale',
	'@CAPS35': 'splenectomy',
	'@CAPS36': 'kopje',
	'@CAPS37': 'internode',
	'@CAPS38': 'telescreen',
	'@CAPS39': 'paracetamol',
	'@CAPS40': 'millenarian',
	'@CAPS41': 'wingspread',
	'@CAPS42': 'krait',
	'@CAPS43': 'tunica',
	'@CAPS44': 'heterojunction',
             '@NUM1': 'One',
             '@NUM2': 'Two',
             '@NUM3': 'Three',
             '@NUM4': 'Four',
             '@NUM5': 'Five',
             '@NUM6': 'Six',
             '@NUM7': 'Seven',
             '@NUM8': 'Eight',
             '@NUM9': 'Nine',
             '@NUM10': 'Ten',
             '@NUM11': 'Eleven',
             '@NUM12': 'Twelve',
             '@NUM13': 'Thirteen',
             '@NUM14': 'Fourteen',
             '@PERSON1': 'Obama',
             '@PERSON2': 'Clinton',
             '@PERSON3': 'Jack',
             '@PERSON4': 'Richard',
             '@PERSON5': 'Alan',
             '@PERSON6': 'James',
             '@PERSON7': 'Andrew',
             '@MONTH1' : 'January',
             '@MONTH2': 'February',
             '@ORGANIZATION1' : 'Facebook',
             '@ORGANIZATION2' : 'Youtube',
             '@ORGANIZATION3' : 'Google',
             '@ORGANIZATION4' : 'Microsoft',
             '@ORGANIZATION5' : 'Yahoo',
             '@ORGANIZATION6' : 'Intel',
             '@LOCATION1' : 'America',
             '@LOCATION2' : 'Paris',
             '@LOCATION3' : 'London',
             '@LOCATION4' : 'Washington',
             '@LOCATION5' : 'Japan',
             '@LOCATION6' : 'Korea',
             '@DATE1' : '1 January 2000',
             '@DATE2' : '2 February 2001',
             '@DATE3' : '3 March 2002',
             '@DATE4' : '4 June 2003',
             '@DATE5' : '5 November 2008',
             '@DATE6' : '17 July 1998',
             '@PERCENT1' : '44%',
             '@PERCENT2' : '85%',
             '@PERCENT3' : '98%',
             '@PERCENT4' : '76%',
             '@PERCENT5' : '97%',
             '@PERCENT6' : '58%',
             
             }

file_name = "data/python3_data.tsv"

datafile = open(file_name, "rb")

data = datafile.read()

for key in replace_dic:
      data = data.replace(key, replace_dic[key])

out_file = open('data/python3_data_names.tsv', 'wb')
out_file.write(data)
