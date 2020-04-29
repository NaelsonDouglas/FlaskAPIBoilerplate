import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Flask API boilerplate</h1>"

@app.route('/api/v1/resources/data/all', methods=['GET'])
def api_all():
    return jsonify(data)


@app.route('/api/v1/resources/data', methods=['GET'])
def api_id():    
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    
    results = []
    
    for dt in data:
        if dt['_id'] == id:
            results.append(dt)
    
    return jsonify(results)


data = [
  {
    "_id": 2,
    "index": 0,
    "guid": "040a493d-0cc5-47c9-84a0-069d5e4d656c",
    "isActive": False,
    "balance": "$3,527.24",
    "picture": "http://placehold.it/32x32",
    "age": 35,
    "eyeColor": "blue",
    "name": {
      "first": "Peggy",
      "last": "Deleon"
    },
    "company": "VOIPA",
    "email": "peggy.deleon@voipa.info",
    "phone": "+1 (826) 560-3608",
    "address": "543 Schenck Street, Corriganville, Puerto Rico, 7216",
    "about": "Consectetur duis irure ullamco eu non aliqua ut aliqua magna Lorem ad culpa pariatur. Ut veniam anim excepteur eu proident aliquip veniam commodo anim ipsum proident. Est aliqua fugiat proident ipsum officia aliqua ut exercitation ea et est in officia tempor. Nisi sit proident minim cillum. Est ea sint eiusmod nulla eu Lorem officia irure. Adipisicing enim laborum reprehenderit ea nulla esse ut pariatur esse reprehenderit nulla consequat fugiat. Non duis quis excepteur proident aute nostrud laboris mollit irure sint amet eu.",
    "registered": "Saturday, April 6, 2019 7:29 PM",
    "latitude": "72.80808",
    "longitude": "59.070813",
    "tags": [
      "elit",
      "quis",
      "irure",
      "pariatur",
      "elit"
    ],
    "range": [
      0,
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9
    ],
    "friends": [
      {
        "id": 0,
        "name": "Morin Douglas"
      },
      {
        "id": 1,
        "name": "Gibbs Whitehead"
      },
      {
        "id": 2,
        "name": "Angela Mckay"
      }
    ],
    "greeting": "Hello, Peggy! You have 6 unread messages.",
    "favoriteFruit": "apple"
  },
  {
    "_id": 8,
    "index": 1,
    "guid": "b7b3cb4e-85fe-43c8-9b2c-dccb51f9ecc8",
    "isActive": False,
    "balance": "$3,700.03",
    "picture": "http://placehold.it/32x32",
    "age": 30,
    "eyeColor": "green",
    "name": {
      "first": "Olivia",
      "last": "Gomez"
    },
    "company": "EXOSWITCH",
    "email": "olivia.gomez@exoswitch.tv",
    "phone": "+1 (820) 582-3557",
    "address": "197 Oriental Court, Soudan, Maryland, 5311",
    "about": "Quis ullamco sit cillum est officia minim non culpa veniam ullamco. Voluptate est id fugiat velit laborum amet quis nisi sunt deserunt labore adipisicing magna. Nulla labore ipsum adipisicing officia ea eiusmod ullamco occaecat. Culpa est commodo elit magna. Ipsum elit consequat tempor amet do cupidatat commodo est enim consequat magna Lorem fugiat. Do irure consequat magna dolor adipisicing.",
    "registered": "Friday, May 31, 2019 5:50 AM",
    "latitude": "63.33588",
    "longitude": "-90.106291",
    "tags": [
      "consequat",
      "cillum",
      "eiusmod",
      "proident",
      "non"
    ],
    "range": [
      0,
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9
    ],
    "friends": [
      {
        "id": 0,
        "name": "Knowles Donaldson"
      },
      {
        "id": 1,
        "name": "Yvonne Cantu"
      },
      {
        "id": 2,
        "name": "Christie Gross"
      }
    ],
    "greeting": "Hello, Olivia! You have 7 unread messages.",
    "favoriteFruit": "strawberry"
  },
  {
    "_id": 10,
    "index": 2,
    "guid": "592ce5c2-8c20-4a18-8a75-e87b6f3d6207",
    "isActive": False,
    "balance": "$3,220.71",
    "picture": "http://placehold.it/32x32",
    "age": 23,
    "eyeColor": "green",
    "name": {
      "first": "Chase",
      "last": "Thompson"
    },
    "company": "INSURESYS",
    "email": "chase.thompson@insuresys.com",
    "phone": "+1 (852) 597-3922",
    "address": "109 Lake Street, Fontanelle, Kansas, 4083",
    "about": "Qui proident non officia et eu enim occaecat dolore aute velit excepteur id laborum exercitation. Consectetur sint laborum nulla nostrud nostrud fugiat ullamco ullamco ut eu occaecat non. Ad enim amet qui exercitation amet ex laborum reprehenderit est minim sint sint nisi.",
    "registered": "Thursday, July 26, 2018 10:46 AM",
    "latitude": "3.999808",
    "longitude": "-103.326521",
    "tags": [
      "cupidatat",
      "aliquip",
      "elit",
      "quis",
      "officia"
    ],
    "range": [
      0,
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9
    ],
    "friends": [
      {
        "id": 0,
        "name": "Hebert Luna"
      },
      {
        "id": 1,
        "name": "Tammy Maddox"
      },
      {
        "id": 2,
        "name": "Newton Woodward"
      }
    ],
    "greeting": "Hello, Chase! You have 6 unread messages.",
    "favoriteFruit": "strawberry"
  },
  {
    "_id": 1,
    "index": 3,
    "guid": "9dc4653b-2e61-4588-b067-736292395e61",
    "isActive": True,
    "balance": "$1,384.20",
    "picture": "http://placehold.it/32x32",
    "age": 26,
    "eyeColor": "brown",
    "name": {
      "first": "Shelley",
      "last": "Ryan"
    },
    "company": "PORTICO",
    "email": "shelley.ryan@portico.net",
    "phone": "+1 (804) 457-3661",
    "address": "327 Bartlett Place, Walland, South Carolina, 3658",
    "about": "Mollit deserunt voluptate et est duis laboris incididunt quis. Sit minim eu dolore labore ipsum cupidatat amet est in. Culpa fugiat anim in consectetur est veniam aute sint est mollit occaecat velit reprehenderit.",
    "registered": "Sunday, October 5, 2014 2:22 PM",
    "latitude": "-80.454187",
    "longitude": "-0.502344",
    "tags": [
      "laboris",
      "mollit",
      "officia",
      "reprehenderit",
      "deserunt"
    ],
    "range": [
      0,
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9
    ],
    "friends": [
      {
        "id": 0,
        "name": "Hill Wade"
      },
      {
        "id": 1,
        "name": "Carter Oneill"
      },
      {
        "id": 2,
        "name": "Santiago Ramsey"
      }
    ],
    "greeting": "Hello, Shelley! You have 8 unread messages.",
    "favoriteFruit": "apple"
  },
  {
    "_id": 7,
    "index": 4,
    "guid": "77480f1a-41c1-494b-95b4-023919424c35",
    "isActive": True,
    "balance": "$2,484.35",
    "picture": "http://placehold.it/32x32",
    "age": 35,
    "eyeColor": "blue",
    "name": {
      "first": "Keith",
      "last": "Norman"
    },
    "company": "ONTAGENE",
    "email": "keith.norman@ontagene.name",
    "phone": "+1 (885) 471-3841",
    "address": "914 Schaefer Street, Barrelville, Alaska, 2006",
    "about": "Dolor nulla minim sint consectetur dolore ipsum magna officia. Cillum nulla officia esse commodo sit sit commodo consequat velit voluptate. Velit fugiat anim ipsum nisi dolore esse amet commodo aliquip sit eiusmod ullamco. Adipisicing esse dolor et aute enim irure culpa amet est labore Lorem elit.",
    "registered": "Wednesday, December 13, 2017 2:46 PM",
    "latitude": "25.441672",
    "longitude": "4.266063",
    "tags": [
      "incididunt",
      "aute",
      "irure",
      "excepteur",
      "enim"
    ],
    "range": [
      0,
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9
    ],
    "friends": [
      {
        "id": 0,
        "name": "Meadows Santos"
      },
      {
        "id": 1,
        "name": "Goodwin Patton"
      },
      {
        "id": 2,
        "name": "Manning Garrison"
      }
    ],
    "greeting": "Hello, Keith! You have 10 unread messages.",
    "favoriteFruit": "strawberry"
  },
  {
    "_id": 5,
    "index": 5,
    "guid": "34b08841-ad93-4106-8aff-df251cda8a7a",
    "isActive": False,
    "balance": "$1,083.48",
    "picture": "http://placehold.it/32x32",
    "age": 22,
    "eyeColor": "blue",
    "name": {
      "first": "Alisha",
      "last": "Dillon"
    },
    "company": "VIOCULAR",
    "email": "alisha.dillon@viocular.biz",
    "phone": "+1 (807) 445-3095",
    "address": "959 Imlay Street, Mooresburg, Indiana, 4790",
    "about": "Duis irure aute velit sit voluptate ex veniam laborum et laborum elit. Non quis dolore eiusmod incididunt duis. Aliquip consectetur non ut nostrud aute laboris consequat cillum. Quis aliquip reprehenderit exercitation fugiat dolor sint in ea. Pariatur ipsum anim excepteur ipsum. Ea cupidatat do amet ad occaecat ex. Ut laborum ullamco mollit velit.",
    "registered": "Friday, January 24, 2020 10:24 PM",
    "latitude": "-27.258962",
    "longitude": "65.596418",
    "tags": [
      "aute",
      "exercitation",
      "adipisicing",
      "quis",
      "cupidatat"
    ],
    "range": [
      0,
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9
    ],
    "friends": [
      {
        "id": 0,
        "name": "Mueller Harrington"
      },
      {
        "id": 1,
        "name": "Norman Copeland"
      },
      {
        "id": 2,
        "name": "Salas Davidson"
      }
    ],
    "greeting": "Hello, Alisha! You have 5 unread messages.",
    "favoriteFruit": "banana"
  },
  {
    "_id": 2,
    "index": 6,
    "guid": "28036e48-93d7-49d7-8ecb-e2e31789e783",
    "isActive": False,
    "balance": "$1,763.50",
    "picture": "http://placehold.it/32x32",
    "age": 23,
    "eyeColor": "blue",
    "name": {
      "first": "Ivy",
      "last": "Combs"
    },
    "company": "ZOXY",
    "email": "ivy.combs@zoxy.co.uk",
    "phone": "+1 (840) 513-2351",
    "address": "538 Opal Court, Grayhawk, Northern Mariana Islands, 7737",
    "about": "Exercitation fugiat excepteur cillum et culpa ut voluptate. Consequat ut nisi mollit nisi nisi eiusmod mollit cupidatat nulla qui magna. Nulla id culpa laboris eiusmod laboris laboris ut ex anim dolor exercitation quis deserunt laborum. Est sint sunt aliquip fugiat fugiat consequat eu. Eu velit laboris elit exercitation ad incididunt fugiat velit ad veniam.",
    "registered": "Monday, June 10, 2019 6:07 AM",
    "latitude": "-67.865055",
    "longitude": "71.832843",
    "tags": [
      "laborum",
      "exercitation",
      "enim",
      "officia",
      "aliqua"
    ],
    "range": [
      0,
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9
    ],
    "friends": [
      {
        "id": 0,
        "name": "Perez Parks"
      },
      {
        "id": 1,
        "name": "Bernadette Wood"
      },
      {
        "id": 2,
        "name": "Terra Morton"
      }
    ],
    "greeting": "Hello, Ivy! You have 10 unread messages.",
    "favoriteFruit": "banana"
  },
  {
    "_id": 10,
    "index": 7,
    "guid": "a91021d3-3aa7-4e15-9c3c-01f99138b555",
    "isActive": False,
    "balance": "$3,948.31",
    "picture": "http://placehold.it/32x32",
    "age": 32,
    "eyeColor": "blue",
    "name": {
      "first": "Jerry",
      "last": "Duke"
    },
    "company": "ECOLIGHT",
    "email": "jerry.duke@ecolight.biz",
    "phone": "+1 (904) 495-3664",
    "address": "280 Chestnut Avenue, Cleary, New York, 3676",
    "about": "Exercitation officia eiusmod ea ullamco aute fugiat qui do reprehenderit pariatur qui incididunt ex. In sunt duis et ad occaecat consequat cupidatat excepteur commodo. Exercitation amet ullamco anim do labore pariatur. Incididunt nulla esse nisi voluptate.",
    "registered": "Sunday, August 10, 2014 11:28 AM",
    "latitude": "13.165065",
    "longitude": "-176.558119",
    "tags": [
      "eu",
      "mollit",
      "excepteur",
      "in",
      "cupidatat"
    ],
    "range": [
      0,
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9
    ],
    "friends": [
      {
        "id": 0,
        "name": "Warren Casey"
      },
      {
        "id": 1,
        "name": "Catherine Phillips"
      },
      {
        "id": 2,
        "name": "Blanchard Huffman"
      }
    ],
    "greeting": "Hello, Jerry! You have 6 unread messages.",
    "favoriteFruit": "apple"
  },
  {
    "_id": 3,
    "index": 8,
    "guid": "ea51edac-d76b-4af3-98d2-820a35c0c3a9",
    "isActive": False,
    "balance": "$1,298.88",
    "picture": "http://placehold.it/32x32",
    "age": 22,
    "eyeColor": "blue",
    "name": {
      "first": "Doyle",
      "last": "Castro"
    },
    "company": "FILODYNE",
    "email": "doyle.castro@filodyne.ca",
    "phone": "+1 (903) 537-2690",
    "address": "250 Cyrus Avenue, Kenmar, Iowa, 4287",
    "about": "Fugiat esse et consectetur qui ad. Laborum reprehenderit sunt ex non laborum labore. Exercitation mollit elit ipsum aute veniam ea sint.",
    "registered": "Wednesday, May 6, 2015 3:56 PM",
    "latitude": "-48.536985",
    "longitude": "4.045135",
    "tags": [
      "culpa",
      "ut",
      "Lorem",
      "laboris",
      "fugiat"
    ],
    "range": [
      0,
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9
    ],
    "friends": [
      {
        "id": 0,
        "name": "Angelina Valenzuela"
      },
      {
        "id": 1,
        "name": "Gonzalez Everett"
      },
      {
        "id": 2,
        "name": "Gail Jarvis"
      }
    ],
    "greeting": "Hello, Doyle! You have 9 unread messages.",
    "favoriteFruit": "strawberry"
  },
  {
    "_id": 10,
    "index": 9,
    "guid": "e865b110-4eaa-4cd6-a15a-b9f3343ae25d",
    "isActive": True,
    "balance": "$2,289.10",
    "picture": "http://placehold.it/32x32",
    "age": 22,
    "eyeColor": "green",
    "name": {
      "first": "Lawanda",
      "last": "Austin"
    },
    "company": "PLASMOX",
    "email": "lawanda.austin@plasmox.me",
    "phone": "+1 (801) 529-3146",
    "address": "989 Morton Street, Tolu, Washington, 4719",
    "about": "Reprehenderit ipsum deserunt mollit elit proident. Eiusmod occaecat deserunt excepteur laboris cupidatat ea dolore officia aute incididunt minim. Amet pariatur aliquip enim aliquip sit duis Lorem. Consectetur ad exercitation tempor dolor magna et nulla ex esse dolor. Sunt exercitation nostrud id quis. Consequat proident reprehenderit culpa sint aute nulla mollit eu. Exercitation deserunt magna fugiat pariatur labore veniam nostrud qui esse culpa anim proident.",
    "registered": "Saturday, February 20, 2016 7:13 AM",
    "latitude": "-43.876119",
    "longitude": "46.899935",
    "tags": [
      "eiusmod",
      "et",
      "non",
      "veniam",
      "nisi"
    ],
    "range": [
      0,
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9
    ],
    "friends": [
      {
        "id": 0,
        "name": "Pam Pennington"
      },
      {
        "id": 1,
        "name": "Rogers Farrell"
      },
      {
        "id": 2,
        "name": "Hinton Bowman"
      }
    ],
    "greeting": "Hello, Lawanda! You have 8 unread messages.",
    "favoriteFruit": "banana"
  }
]
app.run(host='0.0.0.0', port=80)
