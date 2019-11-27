"""
Alek Westover

Implements the grid coding method for correcting
data that may have been corrupted

"""

from numpy.random import random
import matplotlib.pyplot as plt
from pprint import pprint
from copy import deepcopy

def flip_bit(bit):
	return (bit+1)%2

def corrupt(chunk, er=0.05):
	out = []
	ERROR_RATE = er
	for i in range(0, len(chunk)):
		out.append([])
		for j in range(0, len(chunk[i])):
			if random() < ERROR_RATE:
				out[-1].append(flip_bit(chunk[i][j]))
			else:
				out[-1].append(chunk[i][j])
	return out

def corrupt_1(chunk):
	i = int(random()*len(chunk))
	j = int(random()*len(chunk[0]))
	out = deepcopy(chunk)
	out[i][j] = flip_bit(out[i][j])
	return out

def difference(a, b):
	s = 0
	for i in range(0, len(a)):
		s+=abs(a[i]-b[i])
	return s

def add_correction_bits(chunk):
	out = []
	final = []
	for r in chunk:
		out.append(r+[sum(r)%2])
	for col in range(0, len(out[0])):
		final.append(sum([out_i[col] for out_i in out]) %2)
	out.append(final)
	return out

def get_new_correction_bits(chunk):
	rows = []
	cols = []
	for r in chunk:
		rows.append((sum(r)-r[-1])%2)
	for col in range(0, len(chunk)):
		cols.append((sum([chunk_i[col] for chunk_i in chunk])-chunk[-1][col])%2)
	return rows, cols

def rectify(chunk):
	rows, cols = get_new_correction_bits(chunk)
	for i in range(0, len(rows)):
		for j in range(0, len(cols)):
			c = False; r = False
			if chunk[-1][j] != cols[j]:
				c = True
			if chunk[i][-1] != rows[i]:
				r = True
			if c and r:
				chunk[i][j] = flip_bit(chunk[i][j])
				return chunk
	return chunk

def get_chunks(signal):
	"""
	Change data into sequence of 
	4X4 square blocks,
	pad 0s as necessary
	"""
	CHUNK_SIZE = 4
	chunks = []
	cur_chunk = [[]]
	i = 0
	while i < len(signal):
		cur_chunk[-1].append(signal[i])
		i+=1
		if i % CHUNK_SIZE == 0:
			if i % (CHUNK_SIZE**2) == 0:
				chunks.append(cur_chunk)
				cur_chunk = [[]]
			else:
				cur_chunk.append([])

	while len(cur_chunk) < CHUNK_SIZE or len(cur_chunk[-1]) < CHUNK_SIZE:
		cur_chunk[-1].append(0)
		i+= 1
		if i % CHUNK_SIZE == 0:
			if i % (CHUNK_SIZE**2) == 0:
				chunks.append(cur_chunk)
			else:
				cur_chunk.append([])

	return chunks


def IO():
	data = {}

	print("IO for grid code")

	signal = input("\nInput string\n")
	signal = list(signal)

	signal = [int(ii) for ii in signal]
	print("\nOriginal")
	print(signal)
	
	signal = get_chunks(signal)
	print("\nChunked")
	print(signal)

	temp = []
	for chunk in signal:
		temp.append(add_correction_bits(chunk))
	signal = temp
	data["orig"] = deepcopy(signal[0])
	print("\nWith correction bits")
	print(signal)
	
	temp = []
	for chunk in signal:
		temp.append(corrupt_1(chunk))
	signal = temp
	data["corrupt"] = deepcopy(signal[0])
	print("\nCorrupted")
	print(signal)

	temp = []
	for chunk in signal:
		temp.append(rectify(chunk))
	signal = temp
	data["fixed"] = deepcopy(signal[0])
	print("\nCorrected? (hopefully)")
	print(signal)

	return data


# pprint(get_chunks([1 for i in range(0, 100)]))

data = IO()

print(data)

fig = plt.figure()
ax1 = fig.add_subplot(313)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(311)
ax1.imshow(data["orig"])
ax2.imshow(data["corrupt"])
ax3.imshow(data["fixed"])
plt.show()

