from ascii.win1252 import Win1252


def show_dec():
    dec = Win1252.Control_Characters()
    print(dec.dec_to_oct_0_31().keys())

def show_oct():
    oct = Win1252.Control_Characters()
    print(oct.dec_to_oct_0_31().values())

def show_bin():
    bin = Win1252.Control_Characters()
    print(bin.dec_to_bin_0_31())

def show_char():
    char = Win1252.Control_Characters()
    print(char.dec_to_char_0_31().values())

show_dec()
show_oct()
show_bin()
show_char()