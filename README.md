#Challenge 1:Hashing & The Avalanche Effect
##Approach to partA







##Answers to PartC:

1.(a).Avalanche effect-It  is a property in ehich the algorithm works such that a small chnage in the input can make a drastic change in the output.

1.(b).It has been  witnessed in the problem statement which includes hashing the input using SHA-256 and keccak256. I have 
calculated the percentage change in the digest and we make minor change in input.

2.(a)The QR generated has the four inputs combined to make it more unique and harder to predict than if only block.timestamp   were used.

2.(b).Multiple transactions in the same block would have same timestamps.Two products registered at the same second could generate identical salts if no other data is included. So block.timestamp alone does not provide sufficient uniqueness.

3.(a).If the attacker tries to reuse it after 10min of ownership transfer,the verification fail because during transfer ,blockverify generates a new salt and updates the product's verification data.Salt rotation-method to generate new salt replacing the old salt,due to avalanche effect, tiny change in salt produces new digest.Thus the old hashes,qr become invalid.
