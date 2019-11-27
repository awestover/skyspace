"""
Alek Westover

Implements the hamming coding method for correcting
data that may have been corrupted


"""
from numpy.random import random

def corrupt(signal, er=0.1):
	out = []
	ERROR_RATE = er
	for i in range(0, len(signal)):
		if random() < ERROR_RATE:
			out.append((1 + signal[i])%2)
		else:
			out.append(signal[i])
	return out

def add_correction_bits(signal):
	pass

def rectify(signal):
	pass

def IO():
	signal = input("Input string\n")
	signal = list(signal)

	signal = [int(ii) for ii in signal]
	print("Original\n")
	print(signal)
	
	signal = add_correction_bits(signal)
	print("With correction bits\n")
	print(signal)
	
	signal = corrupt(signal)
	print("Corrupted\n")
	print(signal)

	signal = rectify(signal)
	print("Corrected?\n")
	print(signal)


