// Imagine a variable-length encoding, where each character can be 1-byte or 2-bytes long. 
// If the MSB of a byte is '0', then the whole byte is a character. If the MSB of the byte is '1', then the character comprises that byte and the following byte.

// e.g. [01101110] is a 1-byte character. [11101000][10000100] and [11101001][00010110] are valid 2-byte characters. 
// [11000001] is not a valid character; the leading 1-bit requires a subsequent byte to make up a character.

// Given a byte-array of characters in this encoding, return the length of the last character.

// int size_of_last_character(vector<char> data);
// The behaviour is undefined if the input data is invalid.

const size_of_last_character = (num) => {
    secondToLastLeadingBit = getBit(num, 15)
    if (! secondToLastLeadingBit) {
        return 1
    }
    thirdToLastLeadingBit = getBut(num, 23)
    if (! secondToLastLeadingBit) {
        return 2
    }
    return 1
}

const getBit = (num, index) => {
    if (num & 2 ** index > 0) {
        return 1
    }
    return 0
}