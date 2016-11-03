class ColorCode:
    CGREEN = '\33[32m'
    CBLUE = '\33[34m'
    CEND = '\033[0m'


def colored_text(text, color):
    if color in ('green', 'Green', 'GREEN'):
        return ColorCode.CGREEN + text + ColorCode.CEND
    elif color in ('blue', 'Blue', 'BLUE'):
        return ColorCode.CBLUE + text + ColorCode.CEND
