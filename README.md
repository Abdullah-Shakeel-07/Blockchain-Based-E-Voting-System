# Blockchain-Based E-Voting System

## Overview

This project implements a secure and tamper-proof electronic voting system using blockchain technology. The primary goal is to ensure the integrity and transparency of the voting process, preventing any unauthorized alterations or duplications of votes.

### Motivation

Elections in many regions have been plagued by allegations of tampering and fraud. This project aims to address these issues by leveraging the inherent security features of blockchain technology. By doing so, we can ensure a fair and transparent voting process, reducing the risk of manipulated results and restoring public trust in the electoral system.

### Features

- **Blockchain-Based Voting**: Ensures that every vote is securely recorded and cannot be tampered with.
- **Voter Authentication**: Validates voters against a pre-defined list to prevent double voting and unauthorized access.
- **Real-Time Results**: Displays the current state of the election in real-time, ensuring transparency.
- **Proof of Work**: Implements a proof-of-work algorithm to secure the blockchain and validate new blocks.

### Prerequisites

- Python 3.x
- Flask
- Pandas
- Numpy
- Flask-CORS

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Abdullah-Shakeel-07/Blockchain-Based-E-Voting-System.git
   cd Blockchain-Based-E-Voting-System
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Place the `candidates.csv` and `voters.csv` files in the root directory of the project.

### Usage

1. Start the Flask application:
   ```sh
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:8000` to access the voting system.

### API Endpoints

- **`/`**: Landing page of the voting system.
- **`/SendInformation`** (POST): Endpoint to cast a vote. Expects JSON data with voter credentials and selected candidate.

### Code Structure

- **`app.py`**: Main Flask application file.
- **`blockchain.py`**: Contains the `Blockchain` class and related functions for handling blockchain operations.
- **`templates/index.html`**: HTML template for the landing page.
- **`static/`**: Directory for static files (CSS, JS, images).

### Blockchain Implementation

#### Blockchain Class

- **`__init__`**: Initializes the blockchain with the genesis block.
- **`create_block`**: Creates a new block and adds it to the chain.
- **`print_previous_block`**: Returns the previous block in the chain.
- **`proof_of_work`**: Implements the proof-of-work algorithm to secure the blockchain.
- **`hash`**: Generates the hash of a block.
- **`chain_valid`**: Validates the entire blockchain to ensure its integrity.

#### Helper Functions

- **`mine_block`**: Mines a new block with the given credentials and vote.
- **`display_chain`**: Returns the entire blockchain.
- **`valid`**: Checks if the blockchain is valid.

### Voting Process

1. Voter provides their ID and selected candidate.
2. The system validates the voter ID against the list of registered voters.
3. If valid, a new block is mined and added to the blockchain.
4. The vote is recorded and the voter is removed from the list of eligible voters.

### Result Calculation

- The results are calculated by tallying the votes recorded in the blockchain.
- If there are no more eligible voters, the final results are displayed.
- In the case of a tie, the system indicates a draw.

### Conclusion

This project demonstrates the potential of blockchain technology in ensuring secure and transparent elections. By leveraging the cryptographic and decentralized nature of blockchain, we can create a robust voting system that is resistant to tampering and fraud.

### Authors

- Abdullah Shakeel

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.
