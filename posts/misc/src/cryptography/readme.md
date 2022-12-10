# Cryptography

---

> Rand: 1110111 1110000 1110001 1100101 1100001 1100010 1110000 1101011 1101011 1111011

> Alek: Wow! Is that a super secret message encrypted with a one time pad? Those look like binary for ascii!

> Rand: Nope I just generated a bunch of random numbers

> Alek: No way! With my secret key I decoded your message! 

> Rand: lol, you made your secret key by xor-ing your message with my supposed "ciphertext"

> Alek: Dang, you got me

---

# History - Caesar Cipher

The first program I wrote after "Hello World" in Python was a Caesar Cipher encryption program. It was very rudimentary: the user typed a short phrase into the terminal and then the computer shifted the letters (cyclically with wraparound) to produce the cipher-text. I derived great enjoyment from encrypting messages, and decrypting them with my secret key.
I got one of my sisters to try out my program, and realized that I didn't actually need to know her secret key to decrypt her message: there are only 26 possible shifts (really 25 discounting the identity shift which shifts by 0), which I could quickly inspect all of to uncover her message!

This made me interested in learning about more secure encryption schemes. 
I read around on the internet and found out that the Caesar Cipher was part of a class of ciphers called "substitution ciphers" in which each letter is mapped to a (unique) other letter (or symbol).
And although you can't brute force check every possible substitution key (one problem with doing so is that there are over a trillion trillion such substitution ciphers), you can still crack these via a "frequency analysis".
This entails looking at the frequencies of symbols in the cipher-text and comparing them to standard English frequencies: for example, the symbol in the cipher-text with highest frequency probably corresponds to 'e'.


begin rmk

Courtesy of [this website by Cornell's math department](http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html) here are the frequencies for the english language, in-case you want to try out frequency analysis yourself.

`{"E": 0.1202, "T": 0.091, "A": 0.0812, "O": 0.0768, "I": 0.0731, "N": 0.0695, "S": 0.06280000000000001, "R": 0.0602, "H": 0.0592, "D": 0.0432, "L": 0.0398, "U": 0.0288, "C": 0.0271, "M": 0.026099999999999998, "F": 0.023, "Y": 0.021099999999999997, "W": 0.0209, "G": 0.0203, "P": 0.0182, "B": 0.0149, "V": 0.0111, "K": 0.0069, "X": 0.0017000000000000001, "Q": 0.0011, "J": 0.001, "Z": 0.0007000000000000001}`

end rmk

# History - Vignere Cipher

After learning about the insecurity of substitution ciphers I read about an even cooler cipher: the "Vignere Cipher". 
This cipher essentially consists of interleaved Caesar ciphers, where the shift keys are often derived from a word.
I found this cipher awesome, because of some neat pictures I saw of how it smooths the frequency distributions of symbols to a nearly uniform distribution.
But again, my enthusiasm was heightened by the same fact that shocked the French in 1863 after the cipher had remained un-cracked for centuries: rather than being "the indecipherable cipher", the cipher can be broken by a modified version of frequency analysis by repeatedly guessing the key length.

# One Time Pad

I next learned about what superficially sounds like the perfect solution to the encryption problem: the "one time pad". When encrypting with a one time pad both parties must share a long key, as long as the message in fact. Although this method guarantees perfect secrecy, it has major problems: namely the key length. The key can't be reused (or it wouldn't be a "one time pad" (i.e. it could be broken by frequency analysis eventually), but then instead of exchanging a key the parties might as well just exchange their message, so this method is practically useless.

In fact, there is a result that says "any perfectly secure encryption scheme must have a key as long as the message".

I knew, however, that Edgar Allan Poe was mistaken in his claim "Human ingenuity cannot concoct a cipher which human ingenuity cannot resolve."; rather, secure practical encryption is crucial in our digital age.

# RSA

And then I learned about the thing that really blew my mind: RSA. RSA is a super cool encryption scheme. The idea of RSA is nicely summarized by the following story:
"Alice and Bob want to communicate, but they really don't want Eve to be able to know about their communications, and they can't communicate in person. So, Alice makes available a public key that Bob (or anyone) can use to close Alice's lock. Alice then sends Bob a safe with her lock (unlocked). Bob puts his message in the safe, and locks the lock with Alice's public key. But NO ONE can unlock the lock. So Eve is stumped. But if the box gets back to Alice, she has a private key to a "back-door" in the box, so she can access the message!"
I found the secrecy in this to be super cool, and of course implemented the algorithm.
Along the same vein, I learned about hash functions, which are also super cool, and added password protection to player accounts in a game that I made ("theland").

Here is a demonstration about RSA that I made a _long_ time ago (use it at your own risk, the css is pretty cringe) [demo](rsademo.html)

# Other Cool Topics (TODO)

- elliptic curve cryptography
- lattice based encryption schemes (resistant to attacks by quantum computers, unlike prime factorization!!)
- fully homomorhpic encryption
- zero knowledge proofs
- hashing 
- information theory
  * error correcting codes
    - hamming codes
  * compression
    - huffman coding

