WIDTH = 200
HEIGHT = 100
FONT = ("Arial", 14)
DEFAULT_INPUT = "ft"
DEFAULT_OUTPUT = "m"

UNITS = {
    "Distance": [
        [
            "th",
            "bc",
            "in",
            "h",
            "ft",
            "yd",
            "ftm",
            "ch",
            "fur",
            "mi",
            "nmi",
            "lea",
        ],
        ["mm", "cm", "dm", "m", "dam", "hm", "km"],
        ["ft", "m"],
        25.4,
    ],
    "Mass": [
        [
            "gr",
            "dr",
            "oz",
            "lb",
            "st",
            "qtr",
            "cwt-l",
            "cwt-s",
            "t-l",
            "t-s",
        ],
        ["mg", "cg", "dg", "g", "dag", "hg", "kg"],
        ["lb", "kg"],
        453592.37,
    ],
    "Volume": [
        ["fl oz", "gi", "pt", "qt", "gal"],
        ["ml", "cl", "dl", "l", "dal", "hl", "kl"],
        ["fl oz", "l"],
        28.4130625,
    ],
}
