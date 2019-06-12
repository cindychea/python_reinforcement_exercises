import requests
import json

ottawa_wards_response = requests.get(
    "https://represent.opennorth.ca/boundaries/?sets=ottawa-wards"
)

ottawa_wards_response.json()
{
    "meta": {
        "previous": None,
        "next": "/boundaries/?sets=ottawa-wards&offset=20&limit=20",
        "offset": 0,
        "limit": 20,
        "related": {
            "centroids_url": "/boundaries/centroid?sets=ottawa-wards",
            "simple_shapes_url": "/boundaries/simple_shape?sets=ottawa-wards",
            "shapes_url": "/boundaries/shape?sets=ottawa-wards",
        },
        "total_count": 23,
    },
    "objects": [
        {
            "name": "Barrhaven",
            "external_id": "3",
            "url": "/boundaries/ottawa-wards/barrhaven/",
            "boundary_set_name": "Ottawa ward",
            "related": {"boundary_set_url": "/boundary-sets/ottawa-wards/"},
        },
        {
            "name": "West Carleton-March",
            "external_id": "5",
            "url": "/boundaries/ottawa-wards/west-carleton-march/",
            "boundary_set_name": "Ottawa ward",
            "related": {"boundary_set_url": "/boundary-sets/ottawa-wards/"},
        },
        {
            "name": "Somerset",
            "external_id": "14",
            "url": "/boundaries/ottawa-wards/somerset/",
            "boundary_set_name": "Ottawa ward",
            "related": {"boundary_set_url": "/boundary-sets/ottawa-wards/"},
        },
        {
            "name": "Rideau-Goulbourn",
            "external_id": "21",
            "url": "/boundaries/ottawa-wards/rideau-goulbourn/",
            "boundary_set_name": "Ottawa ward",
            "related": {"boundary_set_url": "/boundary-sets/ottawa-wards/"},
        },
        {
            "name": "Cumberland",
            "external_id": "19",
            "url": "/boundaries/ottawa-wards/cumberland/",
            "boundary_set_name": "Ottawa ward",
            "related": {"boundary_set_url": "/boundary-sets/ottawa-wards/"},
        },
        {
            "name": "Orléans",
            "external_id": "1",
            "url": "/boundaries/ottawa-wards/orleans/",
            "boundary_set_name": "Ottawa ward",
            "related": {"boundary_set_url": "/boundary-sets/ottawa-wards/"},
        },
        {
            "name": "Innes",
            "external_id": "2",
            "url": "/boundaries/ottawa-wards/innes/",
            "boundary_set_name": "Ottawa ward",
            "related": {"boundary_set_url": "/boundary-sets/ottawa-wards/"},
        },
        {
            "name": "Rideau-Rockcliffe",
            "external_id": "13",
            "url": "/boundaries/ottawa-wards/rideau-rockcliffe/",
            "boundary_set_name": "Ottawa ward",
            "related": {"boundary_set_url": "/boundary-sets/ottawa-wards/"},
        },
        {
            "name": "Rideau-Vanier",
            "external_id": "12",
            "url": "/boundaries/ottawa-wards/rideau-vanier/",
            "boundary_set_name": "Ottawa ward",
            "related": {"boundary_set_url": "/boundary-sets/ottawa-wards/"},
        },
        {
            "name": "Stittsville",
            "external_id": "6",
            "url": "/boundaries/ottawa-wards/stittsville/",
            "boundary_set_name": "Ottawa ward",
            "related": {"boundary_set_url": "/boundary-sets/ottawa-wards/"},
        },
        {
            "name": "Alta Vista",
            "external_id": "18",
            "url": "/boundaries/ottawa-wards/alta-vista/",
            "boundary_set_name": "Ottawa ward",
            "related": {"boundary_set_url": "/boundary-sets/ottawa-wards/"},
        },
        {
            "name": "Gloucester-Southgate",
            "external_id": "10",
            "url": "/boundaries/ottawa-wards/gloucester-southgate/",
            "boundary_set_name": "Ottawa ward",
            "related": {"boundary_set_url": "/boundary-sets/ottawa-wards/"},
        },
        {
            "name": "Kitchissippi",
            "external_id": "15",
            "url": "/boundaries/ottawa-wards/kitchissippi/",
            "boundary_set_name": "Ottawa ward",
            "related": {"boundary_set_url": "/boundary-sets/ottawa-wards/"},
        },
        {
            "name": "Capital",
            "external_id": "17",
            "url": "/boundaries/ottawa-wards/capital/",
            "boundary_set_name": "Ottawa ward",
            "related": {"boundary_set_url": "/boundary-sets/ottawa-wards/"},
        },
        {
            "name": "River",
            "external_id": "16",
            "url": "/boundaries/ottawa-wards/river/",
            "boundary_set_name": "Ottawa ward",
            "related": {"boundary_set_url": "/boundary-sets/ottawa-wards/"},
        },
        {
            "name": "Knoxdale-Merivale",
            "external_id": "9",
            "url": "/boundaries/ottawa-wards/knoxdale-merivale/",
            "boundary_set_name": "Ottawa ward",
            "related": {"boundary_set_url": "/boundary-sets/ottawa-wards/"},
        },
        {
            "name": "Kanata North",
            "external_id": "4",
            "url": "/boundaries/ottawa-wards/kanata-north/",
            "boundary_set_name": "Ottawa ward",
            "related": {"boundary_set_url": "/boundary-sets/ottawa-wards/"},
        },
        {
            "name": "Gloucester-South Nepean",
            "external_id": "22",
            "url": "/boundaries/ottawa-wards/gloucester-south-nepean/",
            "boundary_set_name": "Ottawa ward",
            "related": {"boundary_set_url": "/boundary-sets/ottawa-wards/"},
        },
        {
            "name": "College",
            "external_id": "8",
            "url": "/boundaries/ottawa-wards/college/",
            "boundary_set_name": "Ottawa ward",
            "related": {"boundary_set_url": "/boundary-sets/ottawa-wards/"},
        },
        {
            "name": "Beacon Hill-Cyrville",
            "external_id": "11",
            "url": "/boundaries/ottawa-wards/beacon-hill-cyrville/",
            "boundary_set_name": "Ottawa ward",
            "related": {"boundary_set_url": "/boundary-sets/ottawa-wards/"},
        },
    ],
}

for object in ottawa_wards_response.json()["objects"]:
    print(object["name"])
        Barrhaven
        West Carleton-March
        Somerset
        Rideau-Goulbourn
        Cumberland
        Orléans
        Innes
        Rideau-Rockcliffe
        Rideau-Vanier
        Stittsville
        Alta Vista
        Gloucester-Southgate
        Kitchissippi
        Capital
        River
        Knoxdale-Merivale
        Kanata North
        Gloucester-South Nepean
        College
        Beacon Hill-Cyrville

hoc_reps_response = requests.get(
    "https://represent.opennorth.ca/representatives/house-of-commons/"
)

hoc_reps_response.json()
{
    "meta": {
        "limit": 20,
        "previous": None,
        "total_count": 336,
        "next": "/representatives/house-of-commons/?limit=20&offset=20",
        "offset": 0,
    },
    "objects": [
        {
            "gender": "",
            "party_name": "Liberal",
            "first_name": "Mike",
            "offices": [
                {
                    "fax": "1 613 996-8652",
                    "postal": "House of Commons\nOttawa ON  K1A 0A6",
                    "tel": "1 613 992-5321",
                    "type": "legislature",
                },
                {
                    "fax": "1 613 354-0913",
                    "postal": "20-B Richmond Blvd (Main Office)\n\nNapanee ON  K7R 4A4",
                    "tel": "1 866 471-3800",
                    "type": "constituency",
                },
            ],
            "representative_set_name": "House of Commons",
            "extra": {},
            "related": {
                "representative_set_url": "/representative-sets/house-of-commons/",
                "boundary_url": "/boundaries/federal-electoral-districts/35039/",
            },
            "source_url": "http://www.parl.gc.ca/Parliamentarians/en/members?view=ListAll",
            "photo_url": "http://www.ourcommons.ca/Parliamentarians/Images/OfficialMPPhotos/42/BossioMike_Lib.jpg",
            "url": "http://www.parl.gc.ca/Parliamentarians/en/members/Mike-Bossio(88786)",
            "personal_url": "http://www.mikebossiomp.ca",
            "elected_office": "MP",
            "district_name": "Hastings—Lennox and Addington",
            "name": "Mike Bossio",
            "last_name": "Bossio",
            "email": "Mike.Bossio@parl.gc.ca",
        },
        {
            "gender": "",
            "party_name": "Liberal",
            "first_name": "Anita",
            "offices": [
                {
                    "fax": "1 613 996-9880",
                    "postal": "House of Commons\nOttawa ON  K1A 0A6",
                    "tel": "1 613 996-0984",
                    "type": "legislature",
                },
                {
                    "fax": "1 613 993-6501",
                    "postal": "1315 Richmond road (Main Office)\n\nOttawa ON  K2B 7Y4",
                    "tel": "1 613 990-7720",
                    "type": "constituency",
                },
            ],
            "representative_set_name": "House of Commons",
            "extra": {},
            "related": {
                "representative_set_url": "/representative-sets/house-of-commons/",
                "boundary_url": "/boundaries/federal-electoral-districts/35079/",
            },
            "source_url": "http://www.parl.gc.ca/Parliamentarians/en/members?view=ListAll",
            "photo_url": "http://www.ourcommons.ca/Parliamentarians/Images/OfficialMPPhotos/42/VandenbeldAnita_Lib.jpg",
            "url": "http://www.parl.gc.ca/Parliamentarians/en/members/Anita-Vandenbeld(71738)",
            "personal_url": "http://www.anitamp.ca",
            "elected_office": "MP",
            "district_name": "Ottawa West—Nepean",
            "name": "Anita Vandenbeld",
            "last_name": "Vandenbeld",
            "email": "Anita.Vandenbeld@parl.gc.ca",
        },
        {
            "gender": "",
            "party_name": "Liberal",
            "first_name": "Robert",
            "offices": [
                {
                    "fax": "1 613 996-1759",
                    "postal": "House of Commons\nOttawa ON  K1A 0A6",
                    "tel": "1 613 996-1161",
                    "type": "legislature",
                },
                {
                    "fax": "1 807 468-4896",
                    "postal": "301 First Avenue S (Main Office)\nSuite 202\nKenora ON  P9N 1W2",
                    "tel": "1 807 468-2170",
                    "type": "constituency",
                },
                {
                    "fax": "1 807 737-1812",
                    "postal": "53 Front Street\nSuite 1-A\nSioux Lookout ON  P8T 1A0",
                    "tel": "1 807 737-4934",
                    "type": "constituency",
                },
                {
                    "postal": "66 Keith Avenue\nSuite 2\nDryden ON  P8N 3K8",
                    "tel": "1 807 407-4758",
                    "type": "constituency",
                },
            ],
            "representative_set_name": "House of Commons",
            "extra": {},
            "related": {
                "representative_set_url": "/representative-sets/house-of-commons/",
                "boundary_url": "/boundaries/federal-electoral-districts/35042/",
            },
            "source_url": "http://www.parl.gc.ca/Parliamentarians/en/members?view=ListAll",
            "photo_url": "http://www.ourcommons.ca/Parliamentarians/Images/OfficialMPPhotos/42/NaultRobert_Lib.jpg",
            "url": "http://www.parl.gc.ca/Parliamentarians/en/members/Robert-D-Nault(709)",
            "personal_url": "http://bnault.liberal.ca",
            "elected_office": "MP",
            "district_name": "Kenora",
            "name": "Robert Nault",
            "last_name": "Nault",
            "email": "Bob.Nault@parl.gc.ca",
        },
        {
            "gender": "",
            "party_name": "Liberal",
            "first_name": "Peter",
            "offices": [
                {
                    "fax": "1 613 952-0874",
                    "postal": "House of Commons\nOttawa ON  K1A 0A6",
                    "tel": "1 613 957-3744",
                    "type": "legislature",
                },
                {
                    "fax": "1 450 510-2383",
                    "postal": "223 St. Charles Avenue (Main Office)\n\nVaudreuil-Dorion QC  J7V 2L6",
                    "tel": "1 450 510-2305",
                    "type": "constituency",
                },
            ],
            "representative_set_name": "House of Commons",
            "extra": {},
            "related": {
                "representative_set_url": "/representative-sets/house-of-commons/",
                "boundary_url": "/boundaries/federal-electoral-districts/24074/",
            },
            "source_url": "http://www.parl.gc.ca/Parliamentarians/en/members?view=ListAll",
            "photo_url": "http://www.ourcommons.ca/Parliamentarians/Images/OfficialMPPhotos/42/SchiefkePeter_Lib.jpg",
            "url": "http://www.parl.gc.ca/Parliamentarians/en/members/Peter-Schiefke(88649)",
            "personal_url": "http://pschiefke.liberal.ca/en",
            "elected_office": "MP",
            "district_name": "Vaudreuil—Soulanges",
            "name": "Peter Schiefke",
            "last_name": "Schiefke",
            "email": "Peter.Schiefke@parl.gc.ca",
        },
        {
            "gender": "",
            "party_name": "Liberal",
            "first_name": "Gagan",
            "offices": [
                {
                    "fax": "1 613 943-1768",
                    "postal": "House of Commons\nOttawa ON  K1A 0A6",
                    "tel": "1 613 943-1762",
                    "type": "legislature",
                },
                {
                    "fax": "1 905 812-8464",
                    "postal": "6990 Financial Drive (Main Office)\nUnit 8G\nMississauga ON  L5N 8J4",
                    "tel": "1 905 812-1811",
                    "type": "constituency",
                },
            ],
            "representative_set_name": "House of Commons",
            "extra": {},
            "related": {
                "representative_set_url": "/representative-sets/house-of-commons/",
                "boundary_url": "/boundaries/federal-electoral-districts/35063/",
            },
            "source_url": "http://www.parl.gc.ca/Parliamentarians/en/members?view=ListAll",
            "photo_url": "http://www.ourcommons.ca/Parliamentarians/Images/OfficialMPPhotos/42/SikandGagan_Lib.jpg",
            "url": "http://www.parl.gc.ca/Parliamentarians/en/members/Gagan-Sikand(88858)",
            "personal_url": "http://gsikand.liberal.ca",
            "elected_office": "MP",
            "district_name": "Mississauga—Streetsville",
            "name": "Gagan Sikand",
            "last_name": "Sikand",
            "email": "Gagan.Sikand@parl.gc.ca",
        },
        {
            "gender": "",
            "party_name": "Conservative",
            "first_name": "Larry",
            "offices": [
                {
                    "fax": "1 613 952-0979",
                    "postal": "House of Commons\nOttawa ON  K1A 0A6",
                    "tel": "1 613 996-5191",
                    "type": "legislature",
                },
                {
                    "fax": "1 519 371-1752",
                    "postal": "1131 - 2nd Avenue East (Main Office)\nSuite 208\nOwen Sound ON  N4K 2J1",
                    "tel": "1 519 371-1059",
                    "type": "constituency",
                },
            ],
            "representative_set_name": "House of Commons",
            "extra": {},
            "related": {
                "representative_set_url": "/representative-sets/house-of-commons/",
                "boundary_url": "/boundaries/federal-electoral-districts/35014/",
            },
            "source_url": "http://www.parl.gc.ca/Parliamentarians/en/members?view=ListAll",
            "photo_url": "http://www.ourcommons.ca/Parliamentarians/Images/OfficialMPPhotos/42/MillerLarry_CPC.jpg",
            "url": "http://www.parl.gc.ca/Parliamentarians/en/members/Larry-Miller(25522)",
            "personal_url": "http://www.larrymiller.ca",
            "elected_office": "MP",
            "district_name": "Bruce—Grey—Owen Sound",
            "name": "Larry Miller",
            "last_name": "Miller",
            "email": "larry.miller@parl.gc.ca",
        },
        {
            "gender": "",
            "party_name": "People's Party",
            "first_name": "Maxime",
            "offices": [
                {
                    "fax": "1 613 995-0687",
                    "postal": "House of Commons\nOttawa ON  K1A 0A6",
                    "tel": "1 613 992-8053",
                    "type": "legislature",
                },
                {
                    "fax": "1 418 227-3093",
                    "postal": "11535 1st Avenue (Main Office)\nSuite 430\nSaint-Georges QC  G5Y 7H5",
                    "tel": "1 418 227-2171",
                    "type": "constituency",
                },
                {
                    "fax": "1 418 387-8124",
                    "postal": "1068 Vachon Blvd North\nSuite 225\nSainte-Marie QC  G6E 1M6",
                    "tel": "1 418 387-4224",
                    "type": "constituency",
                },
            ],
            "representative_set_name": "House of Commons",
            "extra": {},
            "related": {
                "representative_set_url": "/representative-sets/house-of-commons/",
                "boundary_url": "/boundaries/federal-electoral-districts/24007/",
            },
            "source_url": "http://www.parl.gc.ca/Parliamentarians/en/members?view=ListAll",
            "photo_url": "http://www.ourcommons.ca/Parliamentarians/Images/OfficialMPPhotos/42/BernierMaxime_CPC.jpg",
            "url": "http://www.parl.gc.ca/Parliamentarians/en/members/Maxime-Bernier(35309)",
            "personal_url": "http://maximebernier.ca",
            "elected_office": "MP",
            "district_name": "Beauce",
            "name": "Maxime Bernier",
            "last_name": "Bernier",
            "email": "maxime.bernier@parl.gc.ca",
        },
        {
            "gender": "",
            "party_name": "Liberal",
            "first_name": "Rémi",
            "offices": [
                {
                    "fax": "1 613 995-5184",
                    "postal": "House of Commons\nOttawa ON  K1A 0A6",
                    "tel": "1 613 995-1013",
                    "type": "legislature",
                },
                {
                    "fax": "1 418 562-7655",
                    "postal": "290 Saint-Jérôme Avenue (Main Office)\n\nMatane QC  G4W 3A9",
                    "tel": "1 418 562-0343",
                    "type": "constituency",
                },
                {
                    "postal": "598 C Perron Blvd\n\nCarleton-sur-Mer QC  G0C 1J0",
                    "tel": "1 418 364-6254",
                    "type": "constituency",
                },
            ],
            "representative_set_name": "House of Commons",
            "extra": {},
            "related": {
                "representative_set_url": "/representative-sets/house-of-commons/",
                "boundary_url": "/boundaries/federal-electoral-districts/24006/",
            },
            "source_url": "http://www.parl.gc.ca/Parliamentarians/en/members?view=ListAll",
            "photo_url": "http://www.ourcommons.ca/Parliamentarians/Images/OfficialMPPhotos/42/MasséRémi_Lib.jpg",
            "url": "http://www.parl.gc.ca/Parliamentarians/en/members/Remi-Masse(88397)",
            "personal_url": "",
            "elected_office": "MP",
            "district_name": "Avignon—La Mitis—Matane—Matapédia",
            "name": "Rémi Massé",
            "last_name": "Massé",
            "email": "Remi.Masse@parl.gc.ca",
        },
        {
            "gender": "",
            "party_name": "NDP",
            "first_name": "Brian",
            "offices": [
                {
                    "fax": "1 613 992-5397",
                    "postal": "House of Commons\nOttawa ON  K1A 0A6",
                    "tel": "1 613 996-1541",
                    "type": "legislature",
                },
                {
                    "fax": "1 519 255-7913",
                    "postal": "1398 Ouellette Avenue (Main Office)\nSuite 2\nWindsor ON  N8X 1J8",
                    "tel": "1 519 255-1631",
                    "type": "constituency",
                },
            ],
            "representative_set_name": "House of Commons",
            "extra": {},
            "related": {
                "representative_set_url": "/representative-sets/house-of-commons/",
                "boundary_url": "/boundaries/federal-electoral-districts/35117/",
            },
            "source_url": "http://www.parl.gc.ca/Parliamentarians/en/members?view=ListAll",
            "photo_url": "http://www.ourcommons.ca/Parliamentarians/Images/OfficialMPPhotos/42/MasseBrian_NDP.jpg",
            "url": "http://www.parl.gc.ca/Parliamentarians/en/members/Brian-Masse(9137)",
            "personal_url": "http://brianmasse.ca",
            "elected_office": "MP",
            "district_name": "Windsor West",
            "name": "Brian Masse",
            "last_name": "Masse",
            "email": "brian.masse@parl.gc.ca",
        },
        {
            "gender": "",
            "party_name": "Liberal",
            "first_name": "Steven",
            "offices": [
                {
                    "fax": "1 613 992-1037",
                    "postal": "House of Commons\nOttawa ON  K1A 0A6",
                    "tel": "1 613 992-4351",
                    "type": "legislature",
                },
                {
                    "fax": "1 819 561-0005",
                    "postal": "160 de l'Hôpital Blvd (Main Office)\nSuite 204\nGatineau QC  J8T 8J1",
                    "tel": "1 819 561-5555",
                    "type": "constituency",
                },
            ],
            "representative_set_name": "House of Commons",
            "extra": {},
            "related": {
                "representative_set_url": "/representative-sets/house-of-commons/",
                "boundary_url": "/boundaries/federal-electoral-districts/24027/",
            },
            "source_url": "http://www.parl.gc.ca/Parliamentarians/en/members?view=ListAll",
            "photo_url": "http://www.ourcommons.ca/Parliamentarians/Images/OfficialMPPhotos/42/MacKinnonSteven_Lib.jpg",
            "url": "http://www.parl.gc.ca/Parliamentarians/en/members/Steven-MacKinnon(88468)",
            "personal_url": "http://smackinnon.liberal.ca/en",
            "elected_office": "MP",
            "district_name": "Gatineau",
            "name": "Steven MacKinnon",
            "last_name": "MacKinnon",
            "email": "Steven.MacKinnon@parl.gc.ca",
        },
        {
            "gender": "",
            "party_name": "Conservative",
            "first_name": "Bob",
            "offices": [
                {
                    "fax": "1 613 947-4527",
                    "postal": "House of Commons\nOttawa ON  K1A 0A6",
                    "tel": "1 613 947-4524",
                    "type": "legislature",
                },
                {
                    "fax": "1 250 787-1195",
                    "postal": "9916 - 100th Avenue (Main Office)\n\nFort St. John BC  V1J 1Y5",
                    "tel": "1 250 787-1192",
                    "type": "constituency",
                },
                {
                    "fax": "1 250 561-7983",
                    "postal": "1520 - 3rd Avenue\n\nPrince George BC  V2L 3G4",
                    "tel": "1 855 767-4567",
                    "type": "constituency",
                },
                {
                    "fax": "1 250 719-6838",
                    "postal": "10421 - 10th Street\n\nDawson Creek BC  V1G 3T4",
                    "tel": "1 250 719-6848",
                    "type": "constituency",
                },
            ],
            "representative_set_name": "House of Commons",
            "extra": {},
            "related": {
                "representative_set_url": "/representative-sets/house-of-commons/",
                "boundary_url": "/boundaries/federal-electoral-districts/59024/",
            },
            "source_url": "http://www.parl.gc.ca/Parliamentarians/en/members?view=ListAll",
            "photo_url": "http://www.ourcommons.ca/Parliamentarians/Images/OfficialMPPhotos/42/ZimmerBob_CPC.jpg",
            "url": "http://www.parl.gc.ca/Parliamentarians/en/members/Bob-Zimmer(72035)",
            "personal_url": "http://www.bobzimmer.ca",
            "elected_office": "MP",
            "district_name": "Prince George—Peace River—Northern Rockies",
            "name": "Bob Zimmer",
            "last_name": "Zimmer",
            "email": "Bob.Zimmer@parl.gc.ca",
        },
        {
            "gender": "",
            "party_name": "NDP",
            "first_name": "Linda",
            "offices": [
                {
                    "fax": "1 613 995-5342",
                    "postal": "House of Commons\nOttawa ON  K1A 0A6",
                    "tel": "1 613 995-7325",
                    "type": "legislature",
                },
                {
                    "fax": "1 780 495-8403",
                    "postal": "10049 - 81st Avenue (Main Office)\n\nEdmonton AB  T6E 1W7",
                    "tel": "1 780 495-8404",
                    "type": "constituency",
                },
            ],
            "representative_set_name": "House of Commons",
            "extra": {},
            "related": {
                "representative_set_url": "/representative-sets/house-of-commons/",
                "boundary_url": "/boundaries/federal-electoral-districts/48019/",
            },
            "source_url": "http://www.parl.gc.ca/Parliamentarians/en/members?view=ListAll",
            "photo_url": "http://www.ourcommons.ca/Parliamentarians/Images/OfficialMPPhotos/42/DuncanLinda_NDP.jpg",
            "url": "http://www.parl.gc.ca/Parliamentarians/en/members/Linda-Duncan(35873)",
            "personal_url": "http://lindaduncanmp.ca",
            "elected_office": "MP",
            "district_name": "Edmonton Strathcona",
            "name": "Linda Duncan",
            "last_name": "Duncan",
            "email": "linda.duncan@parl.gc.ca",
        },
        {
            "gender": "",
            "party_name": "Bloc Québécois",
            "first_name": "Gabriel",
            "offices": [
                {
                    "fax": "1 613 995-2818",
                    "postal": "House of Commons\nOttawa ON  K1A 0A6",
                    "tel": "1 613 996-6910",
                    "type": "legislature",
                },
                {
                    "fax": "1 450 752-1719",
                    "postal": "436 St-Viateur (Main Office)\n\nJoliette QC  J6E 3B2",
                    "tel": "1 450 752-1940",
                    "type": "constituency",
                },
            ],
            "representative_set_name": "House of Commons",
            "extra": {},
            "related": {
                "representative_set_url": "/representative-sets/house-of-commons/",
                "boundary_url": "/boundaries/federal-electoral-districts/24031/",
            },
            "source_url": "http://www.parl.gc.ca/Parliamentarians/en/members?view=ListAll",
            "photo_url": "http://www.ourcommons.ca/Parliamentarians/Images/OfficialMPPhotos/42/SteMarieGabriel_BQ.jpg",
            "url": "http://www.parl.gc.ca/Parliamentarians/en/members/Gabriel-Ste-Marie(88485)",
            "personal_url": "http://gabrielstemarie.quebec",
            "elected_office": "MP",
            "district_name": "Joliette",
            "name": "Gabriel Ste-Marie",
            "last_name": "Ste-Marie",
            "email": "Gabriel.Ste-Marie@parl.gc.ca",
        },
        {
            "gender": "",
            "party_name": "Liberal",
            "first_name": "Adam",
            "offices": [
                {
                    "fax": "1 613 992-6301",
                    "postal": "House of Commons\nOttawa ON  K1A 0A6",
                    "tel": "1 613 992-2352",
                    "type": "legislature",
                },
                {
                    "fax": "1 416 533-2236",
                    "postal": "280 Spadina Avenue (Main Office)\nSuite 307\nToronto ON  M5T 2C7",
                    "tel": "1 416 533-2710",
                    "type": "constituency",
                },
            ],
            "representative_set_name": "House of Commons",
            "extra": {},
            "related": {
                "representative_set_url": "/representative-sets/house-of-commons/",
                "boundary_url": "/boundaries/federal-electoral-districts/35101/",
            },
            "source_url": "http://www.parl.gc.ca/Parliamentarians/en/members?view=ListAll",
            "photo_url": "http://www.ourcommons.ca/Parliamentarians/Images/OfficialMPPhotos/42/VaughanAdam_Lib.jpg",
            "url": "http://www.parl.gc.ca/Parliamentarians/en/members/Adam-Vaughan(54434)",
            "personal_url": "http://www.adamvaughanmp.ca",
            "elected_office": "MP",
            "district_name": "Spadina—Fort York",
            "name": "Adam Vaughan",
            "last_name": "Vaughan",
            "email": "Adam.Vaughan@parl.gc.ca",
        },
        {
            "gender": "",
            "party_name": "Liberal",
            "first_name": "Bernadette",
            "offices": [
                {
                    "fax": "1 613 996-0878",
                    "postal": "House of Commons\nOttawa ON  K1A 0A6",
                    "tel": "1 613 996-0877",
                    "type": "legislature",
                },
                {
                    "fax": "1 902 527-5656",
                    "postal": "129 Aberdeen Road (Main Office)\nSuite 106\nBridgewater NS  B4V 2S7",
                    "tel": "1 902 527-5655",
                    "type": "constituency",
                },
            ],
            "representative_set_name": "House of Commons",
            "extra": {},
            "related": {
                "representative_set_url": "/representative-sets/house-of-commons/",
                "boundary_url": "/boundaries/federal-electoral-districts/12009/",
            },
            "source_url": "http://www.parl.gc.ca/Parliamentarians/en/members?view=ListAll",
            "photo_url": "http://www.ourcommons.ca/Parliamentarians/Images/OfficialMPPhotos/42/JordanBernadette_Lib.jpg",
            "url": "http://www.parl.gc.ca/Parliamentarians/en/members/Bernadette-Jordan(88340)",
            "personal_url": "http://bernadettejordan.ca",
            "elected_office": "MP",
            "district_name": "South Shore—St. Margarets",
            "name": "Bernadette Jordan",
            "last_name": "Jordan",
            "email": "Bernadette.Jordan@parl.gc.ca",
        },
        {
            "gender": "",
            "party_name": "Liberal",
            "first_name": "Jim",
            "offices": [
                {
                    "fax": "1 613 992-9586",
                    "postal": "House of Commons\nOttawa ON  K1A 0A6",
                    "tel": "1 613 992-9475",
                    "type": "legislature",
                },
                {
                    "fax": "1 204 984-3979",
                    "postal": "611 Corydon Avenue (Main Office)\nSuite 102\nWinnipeg MB  R3L 0P3",
                    "tel": "1 204 983-1355",
                    "type": "constituency",
                },
            ],
            "representative_set_name": "House of Commons",
            "extra": {},
            "related": {
                "representative_set_url": "/representative-sets/house-of-commons/",
                "boundary_url": "/boundaries/federal-electoral-districts/46014/",
            },
            "source_url": "http://www.parl.gc.ca/Parliamentarians/en/members?view=ListAll",
            "photo_url": "http://www.ourcommons.ca/Parliamentarians/Images/OfficialMPPhotos/42/CarrJim_Lib.jpg",
            "url": "http://www.parl.gc.ca/Parliamentarians/en/members/Jim-Carr(89059)",
            "personal_url": "http://www.jimcarrmp.ca",
            "elected_office": "MP",
            "district_name": "Winnipeg South Centre",
            "name": "Jim Carr",
            "last_name": "Carr",
            "email": "Jim.Carr@parl.gc.ca",
        },
        {
            "gender": "",
            "party_name": "Liberal",
            "first_name": "Angelo",
            "offices": [
                {
                    "fax": "1 613 992-8556",
                    "postal": "House of Commons\nOttawa ON  K1A 0A6",
                    "tel": "1 613 992-0611",
                    "type": "legislature",
                },
                {
                    "fax": "1 450 661-5623",
                    "postal": "3131 de la Concorde East (Main Office)\nSuite 300\nLaval QC  H7E 4W4",
                    "tel": "1 450 661-4117",
                    "type": "constituency",
                },
            ],
            "representative_set_name": "House of Commons",
            "extra": {},
            "related": {
                "representative_set_url": "/representative-sets/house-of-commons/",
                "boundary_url": "/boundaries/federal-electoral-districts/24004/",
            },
            "source_url": "http://www.parl.gc.ca/Parliamentarians/en/members?view=ListAll",
            "photo_url": "http://www.ourcommons.ca/Parliamentarians/Images/OfficialMPPhotos/42/IaconoAngelo_Lib.jpg",
            "url": "http://www.parl.gc.ca/Parliamentarians/en/members/Angelo-Iacono(71337)",
            "personal_url": "http://aiacono.liberal.ca/en",
            "elected_office": "MP",
            "district_name": "Alfred-Pellan",
            "name": "Angelo Iacono",
            "last_name": "Iacono",
            "email": "",
        },
        {
            "gender": "",
            "party_name": "Conservative",
            "first_name": "Diane",
            "offices": [
                {
                    "fax": "1 613 996-9749",
                    "postal": "House of Commons\nOttawa ON  K1A 0A6",
                    "tel": "1 613 996-4974",
                    "type": "legislature",
                },
                {
                    "fax": "1 519 426-0003",
                    "postal": "76 Kent Street South (Main Office)\n\nSimcoe ON  N3Y 2Y1",
                    "tel": "1 866 496-3400",
                    "type": "constituency",
                },
                {
                    "postal": "231 Chestnut Street\n\nDunnville ON  N1A 2H2",
                    "tel": "1 866 496-3400",
                    "type": "constituency",
                },
            ],
            "representative_set_name": "House of Commons",
            "extra": {},
            "related": {
                "representative_set_url": "/representative-sets/house-of-commons/",
                "boundary_url": "/boundaries/federal-electoral-districts/35033/",
            },
            "source_url": "http://www.parl.gc.ca/Parliamentarians/en/members?view=ListAll",
            "photo_url": "http://www.ourcommons.ca/Parliamentarians/Images/OfficialMPPhotos/42/FinleyDiane_CPC.jpg",
            "url": "http://www.parl.gc.ca/Parliamentarians/en/members/Diane-Finley(25501)",
            "personal_url": "http://dianefinley.ca",
            "elected_office": "MP",
            "district_name": "Haldimand—Norfolk",
            "name": "Diane Finley",
            "last_name": "Finley",
            "email": "diane.finley@parl.gc.ca",
        },
        {
            "gender": "",
            "party_name": "Liberal",
            "first_name": "MaryAnn",
            "offices": [
                {
                    "fax": "1 613 996-9125",
                    "postal": "House of Commons\nOttawa ON  K1A 0A6",
                    "tel": "1 613 992-7148",
                    "type": "legislature",
                },
                {
                    "fax": "1 204 984-6415",
                    "postal": "1575 Main Street (Main Office)\n\nWinnipeg MB  R2W 3W5",
                    "tel": "1 204 984-6322",
                    "type": "constituency",
                },
                {
                    "postal": "1215 Henderson Hwy\n\nWinnipeg MB  R2G 1L8",
                    "tel": "1 204 984-0382",
                    "type": "constituency",
                },
            ],
            "representative_set_name": "House of Commons",
            "extra": {},
            "related": {
                "representative_set_url": "/representative-sets/house-of-commons/",
                "boundary_url": "/boundaries/federal-electoral-districts/46006/",
            },
            "source_url": "http://www.parl.gc.ca/Parliamentarians/en/members?view=ListAll",
            "photo_url": "http://www.ourcommons.ca/Parliamentarians/Images/OfficialMPPhotos/42/MihychukMaryAnn_Lib.jpg",
            "url": "http://www.parl.gc.ca/Parliamentarians/en/members/MaryAnn-Mihychuk(89037)",
            "personal_url": "http://mmihychuk.liberal.ca",
            "elected_office": "MP",
            "district_name": "Kildonan—St. Paul",
            "name": "MaryAnn Mihychuk",
            "last_name": "Mihychuk",
            "email": "MaryAnn.Mihychuk@parl.gc.ca",
        },
        {
            "gender": "",
            "party_name": "Conservative",
            "first_name": "Lisa",
            "offices": [
                {
                    "fax": "1 613 992-0851",
                    "postal": "House of Commons\nOttawa ON  K1A 0A6",
                    "tel": "1 613 996-7046",
                    "type": "legislature",
                },
                {
                    "fax": "1 905 693-0704",
                    "postal": "86 Main Street East (Main Office)\n\nMilton ON  L9T 1N3",
                    "tel": "1 905 693-0166",
                    "type": "constituency",
                },
            ],
            "representative_set_name": "House of Commons",
            "extra": {},
            "related": {
                "representative_set_url": "/representative-sets/house-of-commons/",
                "boundary_url": "/boundaries/federal-electoral-districts/35057/",
            },
            "source_url": "http://www.parl.gc.ca/Parliamentarians/en/members?view=ListAll",
            "photo_url": "http://www.ourcommons.ca/Parliamentarians/Images/OfficialMPPhotos/42/RaittLisa_CPC.jpg",
            "url": "http://www.parl.gc.ca/Parliamentarians/en/members/Lisa-Raitt(54325)",
            "personal_url": "http://lisaraittmp.ca",
            "elected_office": "MP",
            "district_name": "Milton",
            "name": "Lisa Raitt",
            "last_name": "Raitt",
            "email": "lisa.raitt@parl.gc.ca",
        },
    ],
}

hoc_reps_response.json().keys()
dict_keys(["meta", "objects"])

for object in hoc_reps_response.json()["objects"]:
    print(object["name"])
        Mike Bossio
        Anita Vandenbeld
        Robert Nault
        Peter Schiefke
        Gagan Sikand
        Larry Miller
        Maxime Bernier
        Rémi Massé
        Brian Masse
        Steven MacKinnon
        Bob Zimmer
        Linda Duncan
        Gabriel Ste-Marie
        Adam Vaughan
        Bernadette Jordan
        Jim Carr
        Angelo Iacono
        Diane Finley
        MaryAnn Mihychuk
        Lisa Raitt
