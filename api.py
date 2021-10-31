import requests
import json

import lk_dict

at_dict = {
    1:'OBJECTID',
    2:'EWZ',
    3:'last_update',
    4:'death_rate',
    5:'cases',
    6:'deaths',
    7:'cases_per_100k',
    8:'county',
    9:'cases7_lk',
    10:'death7_lk',
    11:'cases7_per_100k_txt',
}

while True:
    try:
        print('Name des Landkreises:')
        searched_name = input('>>> ')
        if searched_name == 'q': break

        for num, name in lk_dict.my_dict.items():
            if name.upper() == searched_name.upper():
                lk_id = num

    except:
        print('Etwas ist schiefgelaufen.')
        continue


    try:
        url = f'https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=OBJECTID%3D{lk_id}&outFields=OBJECTID%2CEWZ%2Clast_update%2Cdeath_rate%2Ccases%2Cdeaths%2Ccases_per_100k%2Ccounty%2Ccases7_lk%2Cdeath7_lk%2Ccases7_per_100k_txt&returnGeometry=false&f=json'

        r = requests.get(url)


        content = r.content
        data = json.loads(content)

        attributes = data['features'][0]['attributes']

    except:
        print('Etwas ist schiefgelaufen.')
        continue


    try:
        print('Was möchten Sie wissen?\n-1 Objekt ID\n-2 Einwohnerzahl\n-3 Letzte Aktualisierung\n-4 Sterberate\n-5 Anzahl Fälle\n-6 Anzahl Todesfälle\n-7 Fälle Pro 100.000 EW\n-8 Landkreis\n-9 Anzahl Fälle der letzten 7 Tage\n-10 Anzahl Todesfälle der letzten 7 Tage\n-11 Fälle der letzten 7 Tage Pro 100.000 EW')
        at = input('>>> ')
        if at == 'q': break

        print(attributes[at_dict[int(at)]])

    except:
        print('Etwas ist schiefgelaufen.')
        continue

