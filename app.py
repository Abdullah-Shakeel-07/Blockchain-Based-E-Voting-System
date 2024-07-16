import pandas as pd
import datetime
import hashlib
import json
from flask import Flask, jsonify, render_template, request, redirect
import json
from numpy import round
from flask_cors import CORS

candidate = pd.read_csv("candidates.csv")
candidates = candidate['candidates'].tolist()

# loading voters from file
voter = pd.read_csv("voters.csv")
voters = voter['voters'].tolist()


app=Flask(__name__)
CORS(app)
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/SendInformation',methods=['POST'])
def addStd():
    data=request.data
    data=json.loads(data.decode('utf-8'))
    responce=votefunction(data)
    

    if(resultcalculation()):
        responce=resultcalculation()
        responce['state']=1
        print(responce)
        print()
        print(display_chain())
        print()
        print(valid())

    return jsonify(responce),200



class Blockchain:
# Genesis Block, hash =  0, credentail(CNIC) = temporay, vote_for = None
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, credential = '12121-1111111-1', vote_for = 'no_one' , previous_hash='0')
# create new block and add proof, time stamp, credentialm, selected candidate (vote for) and previous hash 
    def create_block(self, proof, credential, vote_for, previous_hash):
        block = {'index': len(self.chain) + 1,
                'timestamp': str(datetime.datetime.now()),
                 'Credential': str(credential),
                 'vote_for': vote_for,
                'proof': proof,
                'previous_hash': previous_hash}
        self.chain.append(block)
        return block

# return previous block
    def print_previous_block(self):
        return self.chain[-1]

# proof of work used to mine the block
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:5] == '00000':
                check_proof = True
            else:
                new_proof += 1

        return new_proof

# use sha256 to calucte the hash
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

# check whether the blockchain is valid or not
    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False

            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()

            if hash_operation[:5] != '00000':
                return False
            previous_block = block
            block_index += 1

        return True


blockchain = Blockchain()

# mine new block 
def mine_block(credential, vote_for):
#     print("credential ", credential, " vote_for ", vote_for)
    previous_block = blockchain.print_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block) 
    block = blockchain.create_block(proof, credential,vote_for, previous_hash)

    response = {'message': 'A block is MINED',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'Credential': block['Credential'],
                 'vote_for':block['vote_for'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}

    return response

def display_chain():
    response = {'chain': blockchain.chain, 'length': len(blockchain.chain)}
    return response

def valid():
    valid = blockchain.chain_valid(blockchain.chain)
    if valid:
        response = {'message': 'The Blockchain is valid.'}
    else:
        response = {'message': 'The Blockchain is not valid.'}
    return response

no_voters = len(voters)


def votefunction(data):
    
        # take voter ID as input

        ID = 0
        ID =data['sendData']['cnic']
        choice=data['sendData']['Vote']
        print("choice ",choice,ID)

        if ID not in voters:
            return 0
            print("Voter ID does not exist or you'ver already cast a vote")
        else:   
            try:
                if (len(choice) == 0):
                    print("Wrong input\nExisting...")
                    return 0
                else:
                    # choice = choice - 1
                    mine_block(ID,choice)
                    voters.remove(ID)
                    
                    return 1
            except:
                print("Wrong Input\nExisting... ")
        return 0


def resultcalculation():
    result={}
    for i in range(0, len(candidates)):
        result[candidates[i]] = 0
    if(len(voters)==0):
        response_ = display_chain()
        chain_ = response_[list(response_.keys())[0]]
        for i in range(0, len(chain_)):
            if chain_[i]['vote_for'] in result.keys():
                result[chain_[i]['vote_for']] +=1 
        result = dict(sorted(result.items(), key=lambda item: item[1], reverse = True))
        if result[list(result.keys())[0]] == result[list(result.keys())[1]]:
            print("Draw")
        else:
            print(list(result.keys())[0], " Won")
        return result
    else:
        print("ma ni chlta")
        return 0
    
if __name__ == "__main__":
    app.run(debug=True, port=8000)