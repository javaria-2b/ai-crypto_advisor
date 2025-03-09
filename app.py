from web3 import Web3, EthereumTesterProvider
import json
import vyper
import advisor
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Use EthereumTesterProvider instead of Ganache
w3 = Web3(EthereumTesterProvider())
print(f"Connected to local Ethereum test network: {w3.is_connected()}")
print(f"Available accounts: {w3.eth.accounts}")

def compile_and_deploy():
    print("Compiling contract...")
    # Compile the contract
    with open('AdvisorStorage.vy', 'r') as file:
        contract_source = file.read()

    compiled_contract = vyper.compile_code(contract_source)
    abi = compiled_contract['abi']
    bytecode = compiled_contract['bytecode']

    # Save ABI to file for future reference
    with open('contract_abi.json', 'w') as abi_file:
        json.dump(abi, abi_file)

    print("Deploying contract...")
    # Deploy the contract
    account = w3.eth.accounts[0]
    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = contract.constructor().transact({'from': account})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    
    contract_address = tx_receipt.contractAddress
    print(f"Contract deployed at: {contract_address}")
    
    # Save contract address for future use
    with open('contract_address.txt', 'w') as address_file:
        address_file.write(contract_address)
    
    return w3.eth.contract(address=contract_address, abi=abi)

def load_existing_contract():
    try:
        # Load ABI
        with open('contract_abi.json', 'r') as abi_file:
            abi = json.load(abi_file)
        
        # Load contract address
        with open('contract_address.txt', 'r') as address_file:
            contract_address = address_file.read().strip()
        
        print(f"Loading existing contract at: {contract_address}")
        return w3.eth.contract(address=contract_address, abi=abi)
    except FileNotFoundError:
        print("No existing contract found. Deploying new contract...")
        return compile_and_deploy()

def main():
    # Check if Web3 is connected
    if not w3.is_connected():
        print("Error: Cannot connect to Ethereum test network")
        return
    
    # Deploy or load contract
    contract = None
    try:
        contract = compile_and_deploy()  # Always deploy a fresh contract for simplicity
    except Exception as e:
        print(f"Error deploying contract: {e}")
        return
    
    if not contract:
        print("Failed to set up contract. Exiting.")
        return
    
    # Get user input
    try:
        risk = int(input("Enter your risk tolerance (1-10): "))
        if risk < 1 or risk > 10:
            print("Risk tolerance must be between 1 and 10")
            return
        
        amount = float(input("Enter your investment amount ($): "))
        if amount <= 0:
            print("Investment amount must be positive")
            return
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    # Generate AI advice
    print("\nGenerating AI advice...")
    try:
        advice = advisor.generate_advice(risk, amount)
        print("\nAI-Generated Advice:")
        print(advice)
    except Exception as e:
        print(f"Error generating advice: {e}")
        return
    
    # Store advice on-chain
    print("\nStoring advice on-chain...")
    account = w3.eth.accounts[0]
    try:
        tx_hash = contract.functions.store_advice(
            account, 
            advice
        ).transact({'from': account})
        w3.eth.wait_for_transaction_receipt(tx_hash)
        print("Advice stored successfully!")
    except Exception as e:
        print(f"Error storing advice: {e}")
        return
    
    # Retrieve advice from chain
    print("\nRetrieving advice from chain...")
    try:
        stored_advice = contract.functions.get_advice(account).call()
        print("Retrieved from blockchain:")
        print(stored_advice)
        
        if stored_advice == advice:
            print("\n✅ Verification successful: Blockchain data matches generated advice.")
        else:
            print("\n❌ Verification failed: Blockchain data doesn't match generated advice.")
    except Exception as e:
        print(f"Error retrieving advice: {e}")

if __name__ == "__main__":
    main() 