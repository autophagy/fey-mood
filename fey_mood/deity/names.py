import random

names = [
    "Aban",
    "Adil",
    "Alåth",
    "Amost",
    "Asmel",
    "Asob",
    "Ast",
    "Astesh",
    "Asën",
    "Athel",
    "Atír",
    "Atîs",
    "Avuz",
    "Ber",
    "Besmar",
    "Bim",
    "Bomrek",
    "Bëmbul",
    "Catten",
    "Cerol",
    "Cilob",
    "Cog",
    "Dakost",
    "Dastot",
    "Datan",
    "Deduk",
    "Degël",
    "Deler",
    "Dodók",
    "Domas",
    "Doren",
    "Ducim",
    "Dumat",
    "Dumed",
    "Dîshmab",
    "Dôbar",
    "Edzul",
    "Edëm",
    "Endok",
    "Eral",
    "Erib",
    "Erush",
    "Eshtân",
    "Etur",
    "Fath",
    "Feb",
    "Fikod",
    "Geshud",
    "Goden",
    "Id",
    "Iden",
    "Ilral",
    "Imush",
    "Ineth",
    "Ingish",
    "Inod",
    "Kadol",
    "Kadôl",
    "Kel",
    "Kib",
    "Kikrost",
    "Kivish",
    "Kogan",
    "Kogsak",
    "Kol",
    "Kosoth",
    "Kulet",
    "Kumil",
    "Kûbuk",
    "Led",
    "Libash",
    "Likot",
    "Limul",
    "Litast",
    "Logem",
    "Lokum",
    "Lolor",
    "Lorbam",
    "Lòr",
    "Mafol",
    "Mebzuth",
    "Medtob",
    "Melbil",
    "Meng",
    "Mestthos",
    "Minkot",
    "Mistêm",
    "Moldath",
    "Momuz",
    "Monom",
    "Mosus",
    "Mörul",
    "Mûthkat",
    "Nil",
    "Nish",
    "Nomal",
    "Obok",
    "Oddom",
    "Olin",
    "Olon",
    "Onget",
    "Onol",
    "Rakust",
    "Ral",
    "Reg",
    "Rigòth",
    "Rimtar",
    "Rith",
    "Rovod",
    "Rîsen",
    "Sarvesh",
    "Sazir",
    "Shem",
    "Shorast",
    "Sibrek",
    "Sigun",
    "Sodel",
    "Solon",
    "Stinthäd",
    "Stodir",
    "Stukos",
    "Stâkud",
    "Såkzul",
    "Tekkud",
    "Thob",
    "Tholtig",
    "Thîkut",
    "Tirist",
    "Tobul",
    "Tosid",
    "Tulon",
    "Tun",
    "Ubbul",
    "Udib",
    "Udil",
    "Unib",
    "Urdim",
    "Urist",
    "Urvad",
    "Ushat",
    "Ustuth",
    "Uvash",
    "Uzol",
    "Vabôk",
    "Vucar",
    "Vutok",
    "Zan",
    "Zaneg",
    "Zas",
    "Zasit",
    "Zefon",
    "Zon",
    "Zuglar",
    "Zulban",
    "Zuntîr",
    "Zutthan",
    "Äs",
    "Åblel",
    "Èrith",
    "Èzum",
    "Îton",
    "Ïngiz",
    "Ïteb",
    "Ònul",
    "Ùshrir",
]


def create_random_name():
    name_parts = []
    for _ in range(random.randint(1, 2)):
        name_parts.append(random.choice(names))
    return "-".join(name_parts)