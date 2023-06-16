def convert(value: float, input_unit: str, output_unit: str, multiplier: float):
    match input_unit:
        case "th":
            multiplier = multiplier / 1000
        case "bc":
            multiplier = multiplier / 3
        case "in":
            multiplier = multiplier
        case "h":
            multiplier = multiplier * 4
        case "ft":
            multiplier = multiplier * 12
        case "yd":
            multiplier = multiplier * 36
        case "ftm":
            multiplier = multiplier * 72.9132
        case "ch":
            multiplier = multiplier * 792
        case "fur":
            multiplier = multiplier * 7920
        case "mi":
            multiplier = multiplier * 63360
        case "nmi":
            multiplier = multiplier * 72913.2
        case "lea":
            multiplier = multiplier * 190080
        case "mm":
            multiplier = multiplier
        case "cm":
            multiplier = multiplier * 10
        case "dm":
            multiplier = multiplier * 100
        case "m":
            multiplier = multiplier * 1000
        case "dam":
            multiplier = multiplier * 10000
        case "hm":
            multiplier = multiplier * 100000
        case "km":
            multiplier = multiplier * 1000000
        case "gr":
            multiplier = multiplier / 7000
        case "dr":
            multiplier = multiplier / 256
        case "oz":
            multiplier = multiplier / 16
        case "lb":
            multiplier = multiplier
        case "st":
            multiplier = multiplier * 14
        case "qtr":
            multiplier = multiplier * 28
        case "cwt-l":
            multiplier = multiplier * 112
        case "cwt-s":
            multiplier = multiplier * 100
        case "t-l":
            multiplier = multiplier * 2240
        case "t-s":
            multiplier = multiplier * 2000
        case "mg":
            multiplier = multiplier
        case "cg":
            multiplier = multiplier * 10
        case "dg":
            multiplier = multiplier * 100
        case "g":
            multiplier = multiplier * 1000
        case "dag":
            multiplier = multiplier * 10000
        case "hg":
            multiplier = multiplier * 100000
        case "kg":
            multiplier = multiplier * 1000000
        case "fl oz":
            multiplier = multiplier
        case "gi":
            multiplier = multiplier * 5
        case "pt":
            multiplier = multiplier * 20
        case "qt":
            multiplier = multiplier * 40
        case "gal":
            multiplier = multiplier * 160
        case "ml":
            multiplier = multiplier
        case "cg":
            multiplier = multiplier * 10
        case "dl":
            multiplier = multiplier * 100
        case "l":
            multiplier = multiplier * 1000
        case "dal":
            multiplier = multiplier * 10000
        case "hl":
            multiplier = multiplier * 100000
        case "kl":
            multiplier = multiplier * 1000000

    match output_unit:
        case "th":
            multiplier = multiplier * 1000
        case "bc":
            multiplier = multiplier * 3
        case "in":
            multiplier = multiplier
        case "h":
            multiplier = multiplier / 4
        case "ft":
            multiplier = multiplier / 12
        case "yd":
            multiplier = multiplier / 36
        case "ftm":
            multiplier = multiplier / 72.9132
        case "ch":
            multiplier = multiplier / 792
        case "fur":
            multiplier = multiplier / 7920
        case "mi":
            multiplier = multiplier / 63360
        case "nmi":
            multiplier = multiplier / 72913.2
        case "lea":
            multiplier = multiplier / 190080
        case "mm":
            multiplier = multiplier
        case "cm":
            multiplier = multiplier / 10
        case "dm":
            multiplier = multiplier / 100
        case "m":
            multiplier = multiplier / 1000
        case "dam":
            multiplier = multiplier / 10000
        case "hm":
            multiplier = multiplier / 100000
        case "km":
            multiplier = multiplier / 1000000
        case "gr":
            multiplier = multiplier * 7000
        case "dr":
            multiplier = multiplier * 256
        case "oz":
            multiplier = multiplier * 16
        case "lb":
            multiplier = multiplier
        case "st":
            multiplier = multiplier / 14
        case "qtr":
            multiplier = multiplier / 28
        case "cwt-l":
            multiplier = multiplier / 112
        case "cwt-s":
            multiplier = multiplier / 100
        case "t-l":
            multiplier = multiplier / 2240
        case "t-s":
            multiplier = multiplier / 2000
        case "mg":
            multiplier = multiplier
        case "cg":
            multiplier = multiplier / 10
        case "dg":
            multiplier = multiplier / 100
        case "g":
            multiplier = multiplier / 1000
        case "dag":
            multiplier = multiplier / 10000
        case "hg":
            multiplier = multiplier / 100000
        case "kg":
            multiplier = multiplier / 1000000
        case "fl oz":
            multiplier = multiplier
        case "gi":
            multiplier = multiplier / 5
        case "pt":
            multiplier = multiplier / 20
        case "qt":
            multiplier = multiplier / 40
        case "gal":
            multiplier = multiplier / 160
        case "ml":
            multiplier = multiplier
        case "cl":
            multiplier = multiplier / 10
        case "dl":
            multiplier = multiplier / 100
        case "l":
            multiplier = multiplier / 1000
        case "dal":
            multiplier = multiplier / 10000
        case "hl":
            multiplier = multiplier / 100000
        case "kl":
            multiplier = multiplier / 1000000

    return round(value * multiplier, 4)
