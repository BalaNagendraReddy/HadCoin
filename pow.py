# Explanation of proof of work

import hashlib

previous_proof = 2
new_proof = 3

print(new_proof**2 - previous_proof**2)

print(str(new_proof**2 - previous_proof**2))

hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()

print(hash_operation[0:4])

def proof_of_work(previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            print(hash_operation)
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof


a = proof_of_work(1)
print(a)