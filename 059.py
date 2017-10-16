# XOR decryption

from operator import itemgetter

character_frequency = {
    'e': 27,
    't': 26,
    'a': 25,
    'o': 24,
    'i': 23,
    'n': 22,
    's': 21,
    'r': 20,
    'h': 19,
    'l': 18,
    'd': 17,
    'c': 16,
    'u': 15,
    'm': 14,
    'f': 13,
    'p': 12,
    'g': 11,
    'w': 10,
    'y': 9,
    'b': 8,
    'v': 7,
    'k': 6,
    'x': 5,
    ' ': 4,
    'j': 3,
    'q': 2,
    'z': 1
}


def score_text(text_binary):
	return sum([character_frequency.get(chr(asc),0) for asc in  text_binary])	

def single_byte_xor(input_bytes, ascii_code):
    return bytearray( byte ^ ascii_code  for byte in input_bytes   )


def single_byte_xor_cypher(ciphertext):
	candidates = []

	for key_candidate in range(256):
		total_score = 0.0
		text_binary = single_byte_xor(ciphertext, key_candidate)
		char_score = score_text(text_binary)

		result = {
		'key': key_candidate,
		'score': char_score,
		'text_binary': text_binary
		}

		candidates.append(result)

	result = max(candidates, key=itemgetter('score'))
	return  result

def repeating_xor_in_binary(input_bytes, binary_key):
	length =  len(binary_key)
	return bytearray( byte ^ binary_key[i%length]  for i, byte in enumerate(input_bytes)   )




def xor_guess_repeated_multikey(ciphertext,keysize):
	# the ith character in the key only interacts with every keysize-th character in the cyphertext, starting from index i
	return bytearray([  single_byte_xor_cypher( ciphertext[i::keysize]    )['key'] 	for i in range(keysize)] )

def main():
	keysize = 3

	ciphertext = ''.join( chr(int(code)) for code in open("059.txt", 'r').read().split(',')).encode()

	key = xor_guess_repeated_multikey(ciphertext,keysize)
	plaintext = repeating_xor_in_binary(ciphertext,key)

	assert sum(char for char in plaintext) == 107359




if __name__ == '__main__':
	main()
