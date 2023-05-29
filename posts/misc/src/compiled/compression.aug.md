\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\K}{\mathbb{K}}
\newcommand{\F}{\mathbb{F}}
\newcommand{\set}[1]{\{#1\}}
\newcommand{\setof}[2]{\{#1 \mid #2\}}
\newcommand{\im}{\mathrm{im}}

\DeclareMathOperator{\polylog}{\text{polylog}}
\DeclareMathOperator{\poly}{\text{poly}}
\DeclareMathOperator{\E}{\mathbb{E}}
\DeclareMathOperator{\Var}{\text{Var}}
\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}
\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}
\newcommand{\defeq}{\vcentcolon=}



# Compression

## WORK IN PROGRESS

## Its important
makes sending stuff fast

## Entropy

<div class="defn envbox">**Definition.**
Entropy is
$$H = \sum_i p_i \log p_i$$
</div>

<div class="rmk envbox">**Remark.**
You can't beat the entropy in encryption. Probably Shannon proved this.
</div>

<div class="rmk envbox">**Remark.**
No compression scheme works all the time. But who cares.
</div>

## Huffman coding
Cool compression technique. Almost achieves the entropy. Assign short symbols to more common letters in your alphabet.

Python implementation:

```python

class Node():
	"""this is a node in a tree"""
	def __init__(self, val, count):
		self.val = val # e.g. "a"
		self.count = count # e.g. 300
		self.left = None # will be a Node
		self.right = None

	def printTree(self, prefix=""):
		print(f"val: {self.val}, count: {self.count}, prefix: {prefix}")
		if self.left:
			self.left.printTree(prefix+"0")
		if self.right:
			self.right.printTree(prefix+"1")


alphabet = ["a", "b", "c", "d", "e"]
counts = [100,200,300,5000,1]

S = [Node(alphabet[i], counts[i]) for i in range(len(alphabet))]

while len(S) > 1:
	S.sort(key=lambda x: x.count)
	x, y = S[0], S[1]
	S = S[2:]
	# merge the 2 least counts nodes
	mergeNode = Node("dumb internal node", x.count+y.count)
	mergeNode.left = x
	mergeNode.right = y
	S.append(mergeNode)

S[0].printTree()
```


## The End


