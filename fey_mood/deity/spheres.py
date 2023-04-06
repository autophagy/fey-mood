import random

spheres = {
    "AGRICULTURE": {
        "children": [],
        "friends": ["FOOD", "FERTILITY", "RAIN"],
        "precluded": [],
        "parents": [],
    },
    "ANIMALS": {
        "children": ["FISH"],
        "friends": ["PLANTS"],
        "precluded": [],
        "parents": ["NATURE"],
    },
    "ART": {
        "children": ["DANCE", "MUSIC", "PAINTING", "POETRY", "SONG"],
        "friends": ["INSPIRATION", "BEAUTY"],
        "precluded": [],
        "parents": [],
    },
    "BALANCE": {"children": [], "friends": [], "precluded": [], "parents": []},
    "BEAUTY": {
        "children": [],
        "friends": ["ART"],
        "precluded": ["BLIGHT", "DEFORMITY", "DISEASE", "MUCK"],
        "parents": [],
    },
    "BIRTH": {
        "children": [],
        "friends": [
            "CHILDREN",
            "CREATION",
            "FAMILY",
            "MARRIAGE",
            "PREGNANCY",
            "REBIRTH",
            "YOUTH",
        ],
        "precluded": [],
        "parents": [],
    },
    "BLIGHT": {
        "children": [],
        "friends": ["DISEASE", "DEATH"],
        "precluded": ["BEAUTY", "FOOD", "FERTILITY", "HEALING"],
        "parents": [],
    },
    "BOUNDARIES": {
        "children": ["COASTS"],
        "friends": [],
        "precluded": [],
        "parents": [],
    },
    "CAVERNS": {
        "children": [],
        "friends": ["MOUNTAINS", "EARTH"],
        "precluded": [],
        "parents": [],
    },
    "CHAOS": {
        "children": [],
        "friends": ["WAR"],
        "precluded": ["DISCIPLINE", "ORDER", "LAWS"],
        "parents": [],
    },
    "CHARITY": {
        "children": [],
        "friends": ["GENEROSITY", "SACRIFICE"],
        "precluded": ["JEALOUSY"],
        "parents": [],
    },
    "CHILDREN": {
        "children": [],
        "friends": ["BIRTH", "FAMILY", "YOUTH", "PREGNANCY"],
        "precluded": [],
        "parents": [],
    },
    "COASTS": {
        "children": [],
        "friends": ["LAKES", "OCEANS"],
        "precluded": [],
        "parents": ["BOUNDARIES"],
    },
    "CONSOLATION": {
        "children": [],
        "friends": [],
        "precluded": ["MISERY"],
        "parents": [],
    },
    "COURAGE": {
        "children": ["VALOR"],
        "friends": [],
        "precluded": [],
        "parents": [],
    },
    "CRAFTS": {
        "children": [],
        "friends": ["CREATION", "LABOR", "METALS"],
        "precluded": [],
        "parents": [],
    },
    "CREATION": {
        "children": [],
        "friends": ["CRAFTS", "BIRTH", "PREGNANCY", "REBIRTH"],
        "precluded": [],
        "parents": [],
    },
    "DANCE": {
        "children": [],
        "friends": ["FESTIVALS", "MUSIC", "REVELRY"],
        "precluded": [],
        "parents": ["ART"],
    },
    "DARKNESS": {
        "children": [],
        "friends": ["NIGHT"],
        "precluded": ["DAWN", "DAY", "LIGHT", "TWILIGHT", "SUN"],
        "parents": [],
    },
    "DAWN": {
        "children": [],
        "friends": ["SUN", "TWILIGHT"],
        "precluded": ["NIGHT", "DAY", "DARKNESS"],
        "parents": [],
    },
    "DAY": {
        "children": [],
        "friends": ["LIGHT", "SUN"],
        "precluded": [
            "DARKNESS",
            "NIGHT",
            "DAWN",
            "DUSK DREAMS",
            "NIGHTMARES",
            "TWILIGHT",
        ],
        "parents": [],
    },
    "DEATH": {
        "children": [],
        "friends": ["BLIGHT", "DISEASE", "MURDER", "REBIRTH", "SUICIDE", "WAR"],
        "precluded": ["HEALING", "LONGEVITY", "YOUTH"],
        "parents": [],
    },
    "DEFORMITY": {
        "children": [],
        "friends": ["DISEASE"],
        "precluded": ["BEAUTY"],
        "parents": [],
    },
    "DEPRAVITY": {
        "children": [],
        "friends": ["LUST"],
        "precluded": ["LAWS"],
        "parents": [],
    },
    "DISCIPLINE": {
        "children": [],
        "friends": ["LAWS", "ORDER"],
        "precluded": ["CHAOS"],
        "parents": [],
    },
    "DISEASE": {
        "children": [],
        "friends": ["BLIGHT", "DEATH", "DEFORMITY"],
        "precluded": ["BEAUTY", "HEALING"],
        "parents": [],
    },
    "DREAMS": {
        "children": [],
        "friends": ["NIGHT", "NIGHTMARES"],
        "precluded": ["DAY"],
        "parents": [],
    },
    "DUSK": {
        "children": [],
        "friends": ["TWILIGHT"],
        "precluded": ["NIGHT", "DAY"],
        "parents": [],
    },
    "DUTY": {
        "children": [],
        "friends": ["ORDER"],
        "precluded": [],
        "parents": [],
    },
    "EARTH": {
        "children": ["METALS", "MINERALS", "SALT"],
        "friends": ["CAVERNS", "MOUNTAINS", "VOLCANOS"],
        "precluded": [],
        "parents": [],
    },
    "FAMILY": {
        "children": [],
        "friends": ["BIRTH", "CHILDREN", "MARRIAGE", "PREGNANCY"],
        "precluded": [],
        "parents": [],
    },
    "FAME": {
        "children": [],
        "friends": ["RUMORS"],
        "precluded": ["SILENCE"],
        "parents": [],
    },
    "FATE": {"children": [], "friends": [], "precluded": ["LUCK"], "parents": []},
    "FERTILITY": {
        "children": [],
        "friends": ["AGRICULTURE", "FOOD", "RAIN"],
        "precluded": ["BLIGHT"],
        "parents": [],
    },
    "FESTIVALS": {
        "children": [],
        "friends": ["DANCE", "MUSIC", "REVELRY", "SONG"],
        "precluded": ["MISERY"],
        "parents": [],
    },
    "FIRE": {
        "children": [],
        "friends": ["METALS", "SUN", "VOLCANOS"],
        "precluded": ["WATER", "OCEANS", "LAKES", "RIVERS"],
        "parents": [],
    },
    "FISH": {
        "children": [],
        "friends": ["OCEANS", "LAKES", "RIVERS", "WATER", "FISHING"],
        "precluded": [],
        "parents": ["ANIMALS"],
    },
    "FISHING": {
        "children": [],
        "friends": ["FISH", "HUNTING"],
        "precluded": [],
        "parents": [],
    },
    "FOOD": {
        "children": [],
        "friends": ["AGRICULTURE", "FERTILITY"],
        "precluded": ["BLIGHT"],
        "parents": [],
    },
    "FORGIVENESS": {
        "children": [],
        "friends": ["MERCY"],
        "precluded": ["REVENGE"],
        "parents": [],
    },
    "FORTRESSES": {
        "children": [],
        "friends": ["WAR"],
        "precluded": [],
        "parents": [],
    },
    "FREEDOM": {
        "children": [],
        "friends": [],
        "precluded": ["ORDER"],
        "parents": [],
    },
    "GAMBLING": {
        "children": [],
        "friends": ["GAMES", "LUCK"],
        "precluded": [],
        "parents": [],
    },
    "GAMES": {
        "children": [],
        "friends": ["GAMBLING", "LUCK"],
        "precluded": [],
        "parents": [],
    },
    "GENEROSITY": {
        "children": [],
        "friends": ["CHARITY", "SACRIFICE"],
        "precluded": [],
        "parents": [],
    },
    "HAPPINESS": {
        "children": [],
        "friends": ["REVELRY"],
        "precluded": ["MISERY"],
        "parents": [],
    },
    "HEALING": {
        "children": [],
        "friends": [],
        "precluded": ["DISEASE", "BLIGHT", "DEATH"],
        "parents": [],
    },
    "HOSPITALITY": {
        "children": [],
        "friends": [],
        "precluded": [],
        "parents": [],
    },
    "HUNTING": {
        "children": [],
        "friends": ["FISHING"],
        "precluded": [],
        "parents": [],
    },
    "INSPIRATION": {
        "children": [],
        "friends": ["ART", "PAINTING", "POETRY"],
        "precluded": [],
        "parents": [],
    },
    "JEALOUSY": {
        "children": [],
        "friends": [],
        "precluded": ["CHARITY"],
        "parents": [],
    },
    "JEWELS": {
        "children": [],
        "friends": ["MINERALS", "WEALTH"],
        "precluded": [],
        "parents": [],
    },
    "JUSTICE": {
        "children": [],
        "friends": ["LAWS"],
        "precluded": [],
        "parents": [],
    },
    "LABOR": {
        "children": [],
        "friends": ["CRAFTS"],
        "precluded": [],
        "parents": [],
    },
    "LAKES": {
        "children": [],
        "friends": ["COASTS", "FISH", "OCEANS", "RIVERS"],
        "precluded": ["FIRE"],
        "parents": ["WATER"],
    },
    "LAWS": {
        "children": [],
        "friends": ["DISCIPLINE", "JUSTICE", "OATHS", "ORDER"],
        "precluded": ["CHAOS", "DEPRAVITY", "MURDER", "THEFT"],
        "parents": [],
    },
    "LIES": {
        "children": [],
        "friends": ["TREACHERY", "TRICKERY"],
        "precluded": ["TRUTH"],
        "parents": [],
    },
    "LIGHT": {
        "children": [],
        "friends": ["DAY", "RAINBOWS", "SUN"],
        "precluded": ["DARKNESS", "TWILIGHT"],
        "parents": [],
    },
    "LIGHTNING": {
        "children": [],
        "friends": ["RAIN", "STORMS", "THUNDER"],
        "precluded": [],
        "parents": ["WEATHER"],
    },
    "LONGEVITY": {
        "children": [],
        "friends": ["YOUTH"],
        "precluded": ["DEATH"],
        "parents": [],
    },
    "LOVE": {"children": [], "friends": [], "precluded": [], "parents": []},
    "LOYALTY": {
        "children": [],
        "friends": ["OATHS"],
        "precluded": ["TREACHERY"],
        "parents": [],
    },
    "LUCK": {
        "children": [],
        "friends": ["GAMBLING", "GAMES"],
        "precluded": ["FATE"],
        "parents": [],
    },
    "LUST": {
        "children": [],
        "friends": ["DEPRAVITY"],
        "precluded": [],
        "parents": [],
    },
    "MARRIAGE": {
        "children": [],
        "friends": ["BIRTH", "FAMILY", "OATHS", "PREGNANCY"],
        "precluded": [],
        "parents": [],
    },
    "MERCY": {
        "children": [],
        "friends": ["FORGIVENESS"],
        "precluded": ["REVENGE"],
        "parents": [],
    },
    "METALS": {
        "children": [],
        "friends": ["CRAFTS", "FIRE", "MINERALS"],
        "precluded": [],
        "parents": ["EARTH"],
    },
    "MINERALS": {
        "children": [],
        "friends": ["JEWELS", "METALS"],
        "precluded": [],
        "parents": ["EARTH"],
    },
    "MISERY": {
        "children": [],
        "friends": ["TORTURE"],
        "precluded": ["CONSOLATION", "FESTIVALS", "REVELRY", "HAPPINESS"],
        "parents": [],
    },
    "MIST": {"children": [], "friends": [], "precluded": [], "parents": []},
    "MOON": {
        "children": [],
        "friends": ["NIGHT", "SKY"],
        "precluded": [],
        "parents": [],
    },
    "MOUNTAINS": {
        "children": [],
        "friends": ["CAVERNS", "EARTH", "VOLCANOS"],
        "precluded": [],
        "parents": [],
    },
    "MUCK": {
        "children": [],
        "friends": [],
        "precluded": ["BEAUTY"],
        "parents": [],
    },
    "MURDER": {
        "children": [],
        "friends": ["DEATH"],
        "precluded": ["LAWS"],
        "parents": [],
    },
    "MUSIC": {
        "children": [],
        "friends": ["DANCE", "FESTIVALS", "REVELRY", "SONG"],
        "precluded": ["SILENCE"],
        "parents": ["ART"],
    },
    "NATURE": {
        "children": ["ANIMALS", "PLANTS"],
        "friends": ["RAIN", "SUN", "WATER", "WEATHER"],
        "precluded": [],
        "parents": [],
    },
    "NIGHT": {
        "children": [],
        "friends": ["DARKNESS", "DREAMS", "MOON", "NIGHTMARES", "STARS"],
        "precluded": ["DAY", "DAWN", "DUSK", "TWILIGHT"],
        "parents": [],
    },
    "NIGHTMARES": {
        "children": [],
        "friends": ["DREAMS", "NIGHT"],
        "precluded": ["DAY"],
        "parents": [],
    },
    "OATHS": {
        "children": [],
        "friends": ["LAWS", "LOYALTY", "MARRIAGE"],
        "precluded": ["TREACHERY"],
        "parents": [],
    },
    "OCEANS": {
        "children": [],
        "friends": ["COASTS", "FISH", "LAKES", "RIVERS", "SALT"],
        "precluded": ["FIRE"],
        "parents": ["WATER"],
    },
    "ORDER": {
        "children": [],
        "friends": ["DISCIPLINE", "DUTY", "LAWS"],
        "precluded": ["CHAOS", "FREEDOM"],
        "parents": [],
    },
    "PAINTING": {
        "children": [],
        "friends": ["INSPIRATION"],
        "precluded": [],
        "parents": ["ART"],
    },
    "PEACE": {"children": [], "friends": [], "precluded": [], "parents": []},
    "PERSUASION": {
        "children": [],
        "friends": ["POETRY", "SPEECH"],
        "precluded": [],
        "parents": [],
    },
    "PLANTS": {
        "children": ["TREES"],
        "friends": ["ANIMALS", "RAIN"],
        "precluded": [],
        "parents": ["NATURE"],
    },
    "POETRY": {
        "children": [],
        "friends": ["INSPIRATION", "PERSUASION", "SONG", "WRITING"],
        "precluded": [],
        "parents": ["ART"],
    },
    "PREGNANCY": {
        "children": [],
        "friends": ["BIRTH", "CHILDREN", "CREATION", "FAMILY", "MARRIAGE"],
        "precluded": [],
        "parents": [],
    },
    "RAIN": {
        "children": [],
        "friends": [
            "AGRICULTURE",
            "FERTILITY",
            "LIGHTNING",
            "NATURE",
            "PLANTS",
            "RAINBOWS",
            "STORMS",
            "THUNDER",
            "TREES",
        ],
        "precluded": [],
        "parents": ["WATER", "WEATHER"],
    },
    "RAINBOWS": {
        "children": [],
        "friends": ["LIGHT", "RAIN", "SKY"],
        "precluded": [],
        "parents": ["WEATHER"],
    },
    "REBIRTH": {
        "children": [],
        "friends": ["BIRTH", "CREATION", "DEATH"],
        "precluded": [],
        "parents": [],
    },
    "REVELRY": {
        "children": [],
        "friends": ["DANCE", "FESTIVALS", "HAPPINESS", "MUSIC", "SONG"],
        "precluded": ["MISERY"],
        "parents": [],
    },
    "REVENGE": {
        "children": [],
        "friends": [],
        "precluded": ["FORGIVENESS", "MERCY"],
        "parents": [],
    },
    "RIVERS": {
        "children": [],
        "friends": ["FISH", "LAKES", "OCEANS"],
        "precluded": ["FIRE"],
        "parents": ["WATER"],
    },
    "RULERSHIP": {
        "children": [],
        "friends": [],
        "precluded": [],
        "parents": [],
    },
    "RUMORS": {
        "children": [],
        "friends": ["FAME"],
        "precluded": [],
        "parents": [],
    },
    "SACRIFICE": {
        "children": [],
        "friends": ["CHARITY", "GENEROSITY"],
        "precluded": ["WEALTH"],
        "parents": [],
    },
    "SALT": {
        "children": [],
        "friends": ["OCEANS"],
        "precluded": [],
        "parents": ["EARTH"],
    },
    "SCHOLARSHIP": {
        "children": [],
        "friends": ["WISDOM", "WRITING"],
        "precluded": [],
        "parents": [],
    },
    "SEASONS": {"children": [], "friends": [], "precluded": [], "parents": []},
    "SILENCE": {
        "children": [],
        "friends": [],
        "precluded": ["FAME", "MUSIC"],
        "parents": [],
    },
    "SKY": {
        "children": [],
        "friends": ["MOON", "RAINBOWS", "SUN", "STARS", "WEATHER", "WIND"],
        "precluded": [],
        "parents": [],
    },
    "SONG": {
        "children": [],
        "friends": ["FESTIVALS", "MUSIC", "POETRY", "REVELRY"],
        "precluded": [],
        "parents": ["ART"],
    },
    "SPEECH": {
        "children": [],
        "friends": ["PERSUASION"],
        "precluded": [],
        "parents": [],
    },
    "STARS": {
        "children": [],
        "friends": ["NIGHT", "SKY"],
        "precluded": [],
        "parents": [],
    },
    "STORMS": {
        "children": [],
        "friends": ["LIGHTNING", "RAIN", "THUNDER"],
        "precluded": [],
        "parents": ["WEATHER"],
    },
    "STRENGTH": {"children": [], "friends": [], "precluded": [], "parents": []},
    "SUICIDE": {
        "children": [],
        "friends": ["DEATH"],
        "precluded": [],
        "parents": [],
    },
    "SUN": {
        "children": [],
        "friends": ["DAWN", "DAY", "FIRE", "LIGHT", "NATURE", "SKY"],
        "precluded": ["DARKNESS"],
        "parents": [],
    },
    "THEFT": {
        "children": [],
        "friends": [],
        "precluded": ["LAWS", "TRADE"],
        "parents": [],
    },
    "THRALLDOM": {
        "children": [],
        "friends": [],
        "precluded": [],
        "parents": [],
    },
    "THUNDER": {
        "children": [],
        "friends": ["LIGHTNING", "RAIN", "STORMS"],
        "precluded": [],
        "parents": ["WEATHER"],
    },
    "TORTURE": {
        "children": [],
        "friends": ["MISERY"],
        "precluded": [],
        "parents": [],
    },
    "TRADE": {
        "children": [],
        "friends": ["WEALTH"],
        "precluded": ["THEFT"],
        "parents": [],
    },
    "TRAVELERS": {
        "children": [],
        "friends": [],
        "precluded": [],
        "parents": [],
    },
    "TREACHERY": {
        "children": [],
        "friends": ["LIES", "TRICKERY"],
        "precluded": ["LOYALTY", "OATHS"],
        "parents": [],
    },
    "TREES": {
        "children": [],
        "friends": ["RAIN"],
        "precluded": [],
        "parents": ["PLANTS"],
    },
    "TRICKERY": {
        "children": [],
        "friends": ["LIES", "TREACHERY"],
        "precluded": ["TRUTH"],
        "parents": [],
    },
    "TRUTH": {
        "children": [],
        "friends": [],
        "precluded": ["LIES", "TRICKERY"],
        "parents": [],
    },
    "TWILIGHT": {
        "children": [],
        "friends": ["DAWN", "DUSK"],
        "precluded": ["LIGHT", "DARKNESS", "DAY", "NIGHT"],
        "parents": [],
    },
    "VALOR": {
        "children": [],
        "friends": ["WAR"],
        "precluded": [],
        "parents": ["COURAGE"],
    },
    "VICTORY": {
        "children": [],
        "friends": ["WAR"],
        "precluded": [],
        "parents": [],
    },
    "VOLCANOS": {
        "children": [],
        "friends": ["EARTH", "FIRE", "MOUNTAINS"],
        "precluded": [],
        "parents": [],
    },
    "WAR": {
        "children": [],
        "friends": ["CHAOS", "DEATH", "FORTRESSES", "VALOR", "VICTORY"],
        "precluded": [],
        "parents": [],
    },
    "WATER": {
        "children": ["LAKES", "OCEANS", "RIVERS", "RAIN"],
        "friends": ["FISH", "NATURE"],
        "precluded": ["FIRE"],
        "parents": [],
    },
    "WEALTH": {
        "children": [],
        "friends": ["JEWELS", "TRADE"],
        "precluded": ["SACRIFICE"],
        "parents": [],
    },
    "WEATHER": {
        "children": ["LIGHTNING", "RAIN", "RAINBOWS", "STORMS", "THUNDER", "WIND"],
        "friends": ["NATURE", "SKY"],
        "precluded": [],
        "parents": [],
    },
    "WIND": {
        "children": [],
        "friends": ["SKY"],
        "precluded": [],
        "parents": ["WEATHER"],
    },
    "WISDOM": {
        "children": [],
        "friends": ["SCHOLARSHIP"],
        "precluded": [],
        "parents": [],
    },
    "WRITING": {
        "children": [],
        "friends": ["POETRY", "SCHOLARSHIP"],
        "precluded": [],
        "parents": [],
    },
    "YOUTH": {
        "children": [],
        "friends": ["BIRTH", "CHILDREN", "LONGEVITY"],
        "precluded": ["DEATH"],
        "parents": [],
    },
}


def bases(num_bases=2):
    items = list(spheres.items())
    bases = []

    for _ in range(num_bases):
        base = random.choice(items)
        precluded = [b[1]["precluded"] for b in bases]
        if base[0] not in precluded:
            bases.append(base)
    return {key: value for key, value in bases}


def friends(bases, num_friends=1):
    forbidden = []
    for base, a in bases.items():
        f = a["children"] + a["parents"] + a["precluded"] + [base]
        forbidden.extend(f)

    chosen_friends = []
    for _ in range(num_friends):
        # Filter out forbidden candidates
        candidates = [k for k, v in spheres.items() if k not in forbidden]

        # Choose a random friend from the remaining candidates
        friend = random.choice(candidates)
        chosen_friends.append(friend)

        # Update the forbidden list with the newly chosen friend and its precluded items
        forbidden.append(friend)
        forbidden.extend(spheres[friend]["precluded"])

    return chosen_friends
