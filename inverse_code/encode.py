"""
@NOTE: Formula\n
symbol to binary ()

"""

from .convert import csymb, chex, cbin, cdec


def encode(characters):
    """
    @NOTE: Can only be in maximum `4 characters`.\n
    `decode_raw`: increases from 4 bits up to 32 bits.\n
    """

    if len(characters) > 4:
        raise ValueError("Can only be in maximum 4 characters.")

    cbinary = []
    start_bit = 0
    start_4_bit = 0
    start = 0
    index_x = 0
    decode_raw = []
    encode_bit = ""
    end_of_coding = []
    chexadecimal = []

    characters = single_character(characters)
    cbinary = converts_symbol_to_binary(characters, cbinary)
    decode_raw = increases_4_bits_up_to_32_bits(decode_raw, cbinary, start_bit)

    while start < 32:
        if start_4_bit == 4:
            start_4_bit = 0
            index_x += 1

        encode_bit += decode_raw[start_4_bit][index_x]
        if len(encode_bit) == 8:
            end_of_coding.append(encode_bit)
            encode_bit = ""
        start_4_bit += 1
        start += 1

    return end_of_coding


def single_character(characters: str):
    """
    when encoding a chunk with fewer than four characters, the input should be zero-padded to
    a length of four before encoding.\n

    ### running the code:

    ```python
    characters = "A"

    while len(characters) < 4:
        characters += "0"
    ```
    `out of the code`: A000\n
    """
    while len(characters) < 4:
        characters += "0"
    return characters


def converts_symbol_to_binary(characters: str, cbinary: list):
    """
    @NOTE: Converts symbol to binary.\n
    `characters[::-1]`: reversing the characters.\n
    `cbinary`: converts characters to binary.\n
    \n
    ### running the code:

    ```python
    characters = "FRED"

    for b in characters[::-1]:
        if b == "0":
            cbinary.append(cdec.cdec_binary(0))  # converts decimal [0] to binary
        else:
            cbinary.append(csymb.csymb_binary(b)) # converts symbol to binary
    ```
    `out of the code`: DERF\n
    """
    for b in characters[::-1]:
        if b == "0":
            cbinary.append(cdec.cdec_binary(0))  # converts decimal [0] to binary
        else:
            cbinary.append(csymb.csymb_binary(b))  # converts symbol to binary
    return cbinary


def increases_4_bits_up_to_32_bits(decode_raw: list, cbinary: list, start_bit: int):
    """
    increases from 4 bits up to 32 bits.\n

    ### running the code:

    `4bits`: ['01000100', '01000101', '01010010', '01000110']\n
    `out of the code`:\n
    `8bytes`: [['0', '1', '0', '0', '0', '1', '0', '0'],['0', '1', '0', '0', '0', '1', '0', '1'],
            ['0', '1', '0', '1', '0', '0', '1', '0'],['0', '1', '0', '0', '0', '1', '1', '0']]
    """
    while start_bit < 4:
        decode_raw.append(
            list(cbinary[start_bit])
        )  # increases from 4 bits up to 32 bits
        start_bit += 1
    return decode_raw
