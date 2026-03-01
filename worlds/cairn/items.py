from enum import Enum, auto
from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import CairnWorld


class ItemValue(Enum):
    """
    Items 1-314 correspond exactly with InventoryItemStringId values in the game
    """

    # WATER = 1 # Liquids become weird items in bag
    # MILK = 2
    Piton = 3
    # VIGORADE = 4
    # LIGHT_STICK = 5 #Light stick seems to always be available
    # BRUTOFLEX = 6
    # ALPINE_COLA = 7
    LargeFlask = 8
    MediumBottle = 9
    LargeBottle = 10
    # HALLU_CHICKEN = 11 #Not normally obtainable, not consumable and not compostable
    # HALLU_PIZZA = 12 #Not normally obtainable, not consumable and not compostable
    # WATER_SWEET = 13
    # MILK_SWEET = 14
    # TEA = 15
    # COFFEE = 16
    # BROTH = 17
    # SOUP = 18
    # SOUP_INTENSE = 19
    # MILK_HERBAL = 20
    # MILK_BROTH = 21
    # SOUP_MILK = 22
    Flask = 23
    # VIGORADE_SWEET = 24
    # ALPINE_COLA_SWEET = 25
    # INFUSION_JUNIPER = 26
    # INFUSION_NETTLE = 27
    # INFUSION_GENTIAN = 28
    # SP_FRUIT_MILK = 29
    # ALC_EGG_NOG = 30
    # ALC_SANGRIA = 31
    # ALC_BLOODY_MARY = 32
    NettleStew = 33
    BoiledPlants = 34
    CreamyWildGarlic = 35
    # EGG_MILK = 36
    CreamyDandelion = 37
    CreamyThistle = 38
    # BRUTOFLEX_EXTRA = 39
    TroglodytePiton = 40
    SuperHoneyRecipe = 41
    # HALLU_ICE_CREAM = 42 #Not normally obtainable, not consumable and not compostable
    Nuts = 43
    CreamyPlantain = 44
    SmallBottle = 45
    PlasticWrap = 46
    CreamyMushrooms = 47
    # EMPTY_BOX = 48
    FlambeedMushrooms = 49
    HuntersMushrooms = 50
    FlambeedTrout = 51
    CaveStyleTrout = 52
    CookedTomatoes = 53
    SweetTomatoes = 54
    # MUCK = 55
    CoffeePacket = 56
    TeaBag = 57
    PowderedMilk = 58
    ExtraLargeBottle = 59
    # BROTH_DEHYDRATED = 60 #Not implemented in game
    DehydratedSoup = 61
    # HYDRATION_PACK = 62 #Not normally obtainable, but seems to work
    Thermos = 63
    SolarThermos = 64
    # PAPER_BAG = 65
    # GLASS_BOTTLE = 66
    # FOOD_CAN = 67
    # Pika = 68 # TODO: implement this location on the client
    # FROG = 69
    # SALAMANDER = 70
    Raspberries = 71
    # MOSS = 72 # Not normally obtainable, seems like slop, maybe it has cool recipes?
    Juniper = 73
    Nettle = 74
    Gentian = 75
    WildGarlic = 76
    Dandelion = 77
    Thistle = 78
    Plantain = 79
    Mushrooms = 80
    Troup = 81
    HoneyDipper = 82
    Eggs = 83
    MapleSyrup = 84
    Sugar = 85
    InstantNoodles = 86
    UncookedRice = 87
    InstantMashedPotatoes = 88
    FreezeDriedVeggies = 89
    LentilsAndHam = 90
    # QUINOA = 91
    Oatmeal = 92
    Pretzel = 93
    Compote = 94
    Chocolate = 95
    Crackers = 96
    # JERKY = 97 # Not normally obtainable, seems to work
    DriedFish = 98
    PeanutButter = 99
    # CHOCOLATE_DRINK = 100
    EnergyGummies = 101
    SportGel = 102
    FruitJellies = 103
    ProteinBar = 104
    Caramel = 105
    CookedWildGarlic = 106
    CookedDandelion = 107
    CookedThistle = 108
    CookedPlantain = 109
    CookedMushrooms = 110
    CreamyTomatoes = 111
    CookedTrout = 112
    SweetTrout = 113
    HerbalTomatoes = 114
    CookedNoodles = 115
    SweetNoodles = 116
    PastureTomatoes = 117
    CookedRice = 118
    SweetRice = 119
    CreamyEggs = 120
    CookedMashedPotatoes = 121
    SweetMashedPotatoes = 122
    MapleFudge = 123
    StewedVeggies = 124
    SweetVeggies = 125
    CoffeeDippedSugarCube = 126
    CookedLentilsAndHam = 127
    SweetLentilsAndHam = 128
    FlambeedNoodles = 129
    # QUINOA_COOKED = 130
    # QUINOA_SWEET = 131
    TouristTrapNoodles = 132
    CookedOatmeal = 133
    SweetOatmeal = 134
    PocketChange = 135
    SickeningSlop = 136
    Penkira700 = 137
    Kurinol = 138
    Atataxium4ch = 139
    Vomyametin = 140
    KuriStrip = 141
    # PLASTER = 142
    # COMPRESS = 143
    Spabast05mg = 144
    # ANTIDIARRHEALS = 145
    BananaminB12 = 146
    # SILDENAFIL = 147
    Corutiko = 148
    # HEATER = 149
    ClimbingTape = 150
    Chalk = 151
    Raisins = 152
    FlambeedRice = 153
    MountainRice = 154
    # CAPUCCINO = 155
    FlambeedMashedPotatoes = 156
    KickstartPotatoes = 157
    FlambeedVeggies = 158
    # BAROMETER = 159
    BrokenBottle = 160
    TinCan = 161
    AbandonedBottle = 162
    PlasticBag = 163
    # AA_DEBUG_ALL = 164
    # AA_DEBUG_ALL_COOKED = 165
    # CLIMBOT = 166 # Would be nice to implement starting without climbot to prevent using pitons
    # INTERACTION_TEST = 167
    BeekeeperMap = 168
    # RASPBERRIES_JUICE = 169
    MotherNatureVeggies = 170
    FlambeedLentilsAndHam = 171
    # COFFEE_HERBAL = 172
    # BROTH_HERBAL = 173
    # BROTH_SWEET = 174
    # SOUP_HERBAL = 175
    # SOUP_SWEET = 176
    SweetWildGarlic = 177
    SweetDandelion = 178
    SweetThistle = 179
    SweetPlantain = 180
    SweetMushrooms = 181
    HerbalMushrooms = 182
    HerbalEggs = 183
    SweetEggs = 184
    ChocolateEggs = 185
    HerbalTrout = 186
    HerbalRice = 187
    HerbalMashedPotatoes = 188
    HerbalLentilsAndHam = 189
    # QUINOA_HERBAL = 190
    HerbalNoodles = 191
    HerbalVeggies = 192
    HerbalOatmeal = 193
    CavePartyDrawing = 194
    # DANGLING_PITONS = 195 # receiving doesn't do anything
    BrokenCamera = 196
    RobertoLetter1 = 197  # Letter
    SmallWindmill = 198
    GlowingGloves = 199
    SurvivalBlanket = 200
    SuperGentianHoney = 201
    Fireworks = 202
    Tomato = 203
    CrystalShard = 204
    RobertoLetter2 = 205
    RobertoLetter3 = 206
    RobertoLetter4 = 207
    RobertoLetter5 = 208
    RobertoLetter6 = 209
    RodannaLetter = 210  # progression
    TroglodytesMap = 211
    FriendsMap = 212
    # MAP_ARCHITECT = 213
    # MAP_HALLUCINATION = 214
    WeatherDoll1 = 215
    WeatherDoll2 = 216
    WeatherDoll3 = 217
    # WEATHER_DOLL = 218 # This works fine but send the parts separately
    # SELF_DRINK_FROM_SOURCE = 219 #Unsure if this is useful
    UndergroundOak = 220
    Edelweiss = 221
    ClimbingPractice2 = 222
    # READABLES_BOOK = 223 # This is the notes book
    # PUFF_STORAGE = 224
    LargeChalkBag = 225
    MountainStew = 226
    FlambeedOatmeal = 227
    # INFUSION_SWEET = 228
    # INFUSION_INTENSE = 229
    # INFUSION_ULTIMATE = 230
    # CHOCOLATE_DRINK_SWEET = 231
    # CHOCOLATE_DRINK_MILK = 232
    # CHOCOLATE_DRINK_HERBAL = 233
    # CHOCOLATE_DRINK_INTENSE = 234
    # TEA_MILK = 235
    # TEA_HERBAL = 236
    # TEA_SWEET = 237
    # TEA_INTENSE = 238
    # COFFEE_SWEET = 239
    # COFFEE_MILK = 240
    # COFFEE_INTENSE = 241
    # MILK_INTENSE = 242
    # EGG_MILK_SWEET = 243
    # RASPBERRIES_JUICE_SWEET = 244
    # ALC_MOONSHINE = 245
    # ALC_GROG = 246
    # ALC_IRISH_COFFEE = 247
    # ALC_HOT_TODDY = 248
    # ALC_WHITE_RUSSIAN = 249
    # ALC_MONTAGNARDE = 250
    # ALC_HALF_EMPTY = 251
    # ALC_CHOCOLATE_MARTINI = 252
    # ALC_TI_PUNCH = 253
    CreamyTrout = 254
    BoiledEggs = 255
    CreamyNoodles = 256
    CreamyRice = 257
    CreamyMashedPotatoes = 258
    CreamyStewedVegetables = 259
    CreamyLentilsAndHam = 260
    CreamyOatmeal = 261
    Porridge = 262
    Caffuel = 263
    ChocolateFondue = 264
    MedicinalExtract = 265
    OrigamiLynx = 266
    # CAN_TEST = 267
    # MAGIC_FROG_LICK = 268
    # MAGIC_FROG_SECOND_LICK = 269
    # QUINOA_MILK = 270
    PastureTomatoesRecipe = 271
    MapleFudgeRecipe = 272
    CaveStyleTroutRecipe = 273
    MountainStewRecipe = 274
    HuntersMushroomsRecipe = 275
    TouristTrapNoodlesRecipe = 276
    PorridgeRecipe = 277
    MountainRiceRecipe = 278
    # CAN_MILK = 279 # these cans are sent without their liquid
    # CAN_ALPINE_COLA = 280
    # CAN_VIGORADE = 281
    # CAN_RASPBERRY_JUICE = 282
    # CAN_WATER = 283
    # STATUETTE = 284
    # GAME_JOURNAL = 285
    HygrocybeRubescens = 286
    ClimbingPractice4 = 287
    ClimbingPractice3 = 288
    ClimbingPractice = 289
    # CHARM_TEST_A = 290
    # CHARM_TEST_B = 291
    # CHARM_TEST_C = 292
    # CHARM_NONE = 293
    # CHARM_COMET = 294
    # CHARM_CAT = 295
    # CHARM_STATUETTE = 296
    # CHARM_PENNANT = 297
    # CHARM_COLA = 298
    # CHARM_TROGLODYTE_TOKEN = 299
    # CHARM_BELL = 300
    # CHARM_WEATHER_DOLL = 301
    # CHARM_TENZEN = 302
    # CHARM_FROG = 303
    # CHARM_TROUT = 304
    # CHARM_CRYSTAL = 305
    # CHARM_CLIMBOT = 306
    # CHARM_PIKA_DOLL = 307
    # CHARM_TENT = 308
    # CHARM_KAMI = 309
    # CHARM_LOUVE_DOLL = 310
    # CAN_MOONSHINE = 311
    HandwrittenLetter = 312
    # CHARM_THE_VOICE = 313
    # CHARM_CAIRN = 314

    IceEquipment = 10000
    SmallChalkBag = auto()


# TODO: Seperate cooked food and ingredients, seperate by tier
FOOD = [
    ItemValue.NettleStew,
    ItemValue.BoiledPlants,
    ItemValue.CreamyWildGarlic,
    ItemValue.CreamyDandelion,
    ItemValue.CreamyThistle,
    ItemValue.Nuts,
    ItemValue.CreamyPlantain,
    ItemValue.CreamyMushrooms,
    ItemValue.FlambeedMushrooms,
    ItemValue.HuntersMushrooms,
    ItemValue.FlambeedTrout,
    ItemValue.CaveStyleTrout,
    ItemValue.CookedTomatoes,
    ItemValue.SweetTomatoes,
    ItemValue.CoffeePacket,
    ItemValue.TeaBag,
    ItemValue.PowderedMilk,
    ItemValue.DehydratedSoup,
    ItemValue.Raspberries,
    ItemValue.Juniper,
    ItemValue.Nettle,
    ItemValue.Gentian,
    ItemValue.WildGarlic,
    ItemValue.Dandelion,
    ItemValue.Thistle,
    ItemValue.Plantain,
    ItemValue.Mushrooms,
    ItemValue.Troup,
    ItemValue.HoneyDipper,
    ItemValue.Eggs,
    ItemValue.MapleSyrup,
    ItemValue.Sugar,
    ItemValue.InstantNoodles,
    ItemValue.UncookedRice,
    ItemValue.InstantMashedPotatoes,
    ItemValue.FreezeDriedVeggies,
    ItemValue.LentilsAndHam,
    ItemValue.Oatmeal,
    ItemValue.Pretzel,
    ItemValue.Compote,
    ItemValue.Chocolate,
    ItemValue.Crackers,
    ItemValue.DriedFish,
    ItemValue.PeanutButter,
    ItemValue.EnergyGummies,
    ItemValue.SportGel,
    ItemValue.FruitJellies,
    ItemValue.ProteinBar,
    ItemValue.Caramel,
    ItemValue.CookedWildGarlic,
    ItemValue.CookedDandelion,
    ItemValue.CookedThistle,
    ItemValue.CookedPlantain,
    ItemValue.CookedMushrooms,
    ItemValue.CreamyTomatoes,
    ItemValue.CookedTrout,
    ItemValue.SweetTrout,
    ItemValue.HerbalTomatoes,
    ItemValue.CookedNoodles,
    ItemValue.SweetNoodles,
    ItemValue.PastureTomatoes,
    ItemValue.CookedRice,
    ItemValue.SweetRice,
    ItemValue.CreamyEggs,
    ItemValue.CookedMashedPotatoes,
    ItemValue.SweetMashedPotatoes,
    ItemValue.MapleFudge,
    ItemValue.StewedVeggies,
    ItemValue.SweetVeggies,
    ItemValue.CoffeeDippedSugarCube,
    ItemValue.CookedLentilsAndHam,
    ItemValue.SweetLentilsAndHam,
    ItemValue.FlambeedNoodles,
    ItemValue.TouristTrapNoodles,
    ItemValue.CookedOatmeal,
    ItemValue.SweetOatmeal,
    ItemValue.SickeningSlop,
    ItemValue.Raisins,
    ItemValue.FlambeedRice,
    ItemValue.MountainRice,
    ItemValue.FlambeedMashedPotatoes,
    ItemValue.KickstartPotatoes,
    ItemValue.FlambeedVeggies,
    ItemValue.MotherNatureVeggies,
    ItemValue.FlambeedLentilsAndHam,
    ItemValue.SweetWildGarlic,
    ItemValue.SweetDandelion,
    ItemValue.SweetThistle,
    ItemValue.SweetPlantain,
    ItemValue.SweetMushrooms,
    ItemValue.HerbalMushrooms,
    ItemValue.HerbalEggs,
    ItemValue.SweetEggs,
    ItemValue.ChocolateEggs,
    ItemValue.HerbalTrout,
    ItemValue.HerbalRice,
    ItemValue.HerbalMashedPotatoes,
    ItemValue.HerbalLentilsAndHam,
    ItemValue.HerbalNoodles,
    ItemValue.HerbalVeggies,
    ItemValue.HerbalOatmeal,
    ItemValue.SuperGentianHoney,
    ItemValue.Tomato,
    ItemValue.UndergroundOak,
    ItemValue.MountainStew,
    ItemValue.FlambeedOatmeal,
    ItemValue.CreamyTrout,
    ItemValue.BoiledEggs,
    ItemValue.CreamyNoodles,
    ItemValue.CreamyRice,
    ItemValue.CreamyMashedPotatoes,
    ItemValue.CreamyStewedVegetables,
    ItemValue.CreamyLentilsAndHam,
    ItemValue.CreamyOatmeal,
    ItemValue.Porridge,
    ItemValue.ChocolateFondue,
    ItemValue.HygrocybeRubescens,
]

DRUGS = [
    ItemValue.Penkira700,
    ItemValue.Kurinol,
    ItemValue.Atataxium4ch,
    ItemValue.Vomyametin,
    ItemValue.KuriStrip,
    ItemValue.Spabast05mg,
    ItemValue.BananaminB12,
    ItemValue.Corutiko,
    ItemValue.Caffuel,
    ItemValue.MedicinalExtract,
]

GEAR = [
    ItemValue.Piton,
    ItemValue.MediumBottle,
    ItemValue.LargeBottle,
    ItemValue.ClimbingTape,
    ItemValue.Chalk,  # FIXME: should probably be more common, this only sends 1/10
]

MAPS = [
    ItemValue.BeekeeperMap,
    ItemValue.TroglodytesMap,
    ItemValue.FriendsMap,
]

READING_MATERIAL = [
    ItemValue.CavePartyDrawing,
    ItemValue.RobertoLetter1,
    ItemValue.RobertoLetter2,
    ItemValue.RobertoLetter3,
    ItemValue.RobertoLetter4,
    ItemValue.RobertoLetter5,
    ItemValue.RobertoLetter6,
    ItemValue.ClimbingPractice2,
    ItemValue.PastureTomatoesRecipe,
    ItemValue.MapleFudgeRecipe,
    ItemValue.CaveStyleTroutRecipe,
    ItemValue.MountainStewRecipe,
    ItemValue.HuntersMushroomsRecipe,
    ItemValue.TouristTrapNoodlesRecipe,
    ItemValue.PorridgeRecipe,
    ItemValue.MountainRiceRecipe,
    ItemValue.ClimbingPractice4,
    ItemValue.ClimbingPractice3,
    ItemValue.ClimbingPractice,
    ItemValue.HandwrittenLetter,
]

TRASH = [
    ItemValue.BrokenBottle,
    ItemValue.TinCan,
    ItemValue.AbandonedBottle,
    ItemValue.PlasticBag,
]

ITEM_NAME_TO_ID = {item.name: item.value for item in ItemValue}
ITEM_CLASSIFICATION_OVERRIDES = {
    ItemValue.IceEquipment: ItemClassification.progression | ItemClassification.useful,
    ItemValue.RodannaLetter: ItemClassification.progression,
    ItemValue.CrystalShard: ItemClassification.progression,
}


class CairnItem(Item):
    game: str = "Cairn"


# def create_item_with_correct_classification(world: "CairnWorld", item: ItemValue) -> CairnItem:
#     return CairnItem(item.name, ItemClassification.filler, item.value, world.player)


def create_all_items(world: "CairnWorld") -> None:
    # Add unique items
    itempool = [
        CairnItem(
            item.name, ITEM_CLASSIFICATION_OVERRIDES.get(item, ItemClassification.useful), item.value, world.player
        )
        for item in [
            ItemValue.SmallChalkBag,
            ItemValue.LargeChalkBag,
            ItemValue.Flask,
            ItemValue.LargeFlask,
            ItemValue.GlowingGloves,
            ItemValue.SmallWindmill,
            ItemValue.SurvivalBlanket,
            ItemValue.IceEquipment,
            ItemValue.Thermos,
            ItemValue.SolarThermos,
            ItemValue.RodannaLetter,
            ItemValue.OrigamiLynx,
            ItemValue.TroglodytePiton,
            ItemValue.TroglodytePiton,
            ItemValue.TroglodytePiton,
            # TODO: Double check the number of required shards
            ItemValue.CrystalShard,
            ItemValue.CrystalShard,
            ItemValue.CrystalShard,
            ItemValue.CrystalShard,
            ItemValue.CrystalShard,
            ItemValue.WeatherDoll1,
            ItemValue.WeatherDoll2,
            ItemValue.WeatherDoll3,
            ItemValue.Edelweiss,
        ]
    ]

    itempool += [
        CairnItem(
            item.name, ITEM_CLASSIFICATION_OVERRIDES.get(item, ItemClassification.useful), item.value, world.player
        )
        for item in MAPS
    ]
    itempool += [
        CairnItem(
            item.name, ITEM_CLASSIFICATION_OVERRIDES.get(item, ItemClassification.filler), item.value, world.player
        )
        for item in READING_MATERIAL
    ]

    # Now fill out the rest of the items with repeatable items
    # TODO: Balance these categories. For now: 25% of each
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    num_gear = num_drugs = num_food = needed_number_of_filler_items // 4
    num_trash = num_gear + needed_number_of_filler_items % 4

    itempool += [
        CairnItem(
            item.name,
            ITEM_CLASSIFICATION_OVERRIDES.get(item, ItemClassification.progression_deprioritized_skip_balancing),
            item.value,
            world.player,
        )
        for item in world.random.choices(FOOD, k=num_food)
    ]
    itempool += [
        CairnItem(
            item.name,
            ITEM_CLASSIFICATION_OVERRIDES.get(item, ItemClassification.progression_deprioritized_skip_balancing),
            item.value,
            world.player,
        )
        for item in world.random.choices(DRUGS, k=num_drugs)
    ]
    itempool += [
        CairnItem(
            item.name,
            ITEM_CLASSIFICATION_OVERRIDES.get(item, ItemClassification.progression_deprioritized_skip_balancing),
            item.value,
            world.player,
        )
        for item in world.random.choices(GEAR, k=num_gear)
    ]
    itempool += [
        CairnItem(
            item.name, ITEM_CLASSIFICATION_OVERRIDES.get(item, ItemClassification.filler), item.value, world.player
        )
        for item in world.random.choices(TRASH, k=num_trash)
    ]

    world.multiworld.itempool += itempool
