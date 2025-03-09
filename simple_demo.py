import os
import openai
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Simple in-memory storage to simulate blockchain
blockchain_storage = {}

def generate_advice(risk_tolerance, investment_amount):
    """Generate investment advice using OpenAI API"""
    prompt = f"""
    Generate cryptocurrency investment advice for someone with:
    - Risk tolerance: {risk_tolerance}/10 (where 1 is very conservative and 10 is very aggressive)
    - Investment amount: ${investment_amount}
    
    Provide a brief, concise strategy (max 100 words).
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return "Unable to generate advice. Using default conservative strategy: Consider allocating 70% to stable coins, 20% to established cryptocurrencies like Bitcoin and Ethereum, and 10% to newer altcoins."

def store_on_blockchain(user_id, advice):
    """Simulate storing data on blockchain"""
    print("\nStoring advice on simulated blockchain...")
    
    # Add transaction hash to simulate blockchain transaction
    tx_hash = f"0x{''.join(['abcdef0123456789'[hash(user_id + advice) % 16] for _ in range(64)])}"
    
    # Store in our simulated blockchain
    blockchain_storage[user_id] = {
        "advice": advice,
        "timestamp": "2025-03-09T16:30:00Z",
        "transaction_hash": tx_hash
    }
    
    print(f"Transaction hash: {tx_hash}")
    return tx_hash

def retrieve_from_blockchain(user_id):
    """Simulate retrieving data from blockchain"""
    print("\nRetrieving advice from simulated blockchain...")
    
    if user_id in blockchain_storage:
        return blockchain_storage[user_id]
    else:
        return None

def display_blockchain_data(data):
    """Display blockchain data in a formatted way"""
    if not data:
        print("No data found on blockchain for this user ID.")
        return
    
    print("\n" + "="*50)
    print("BLOCKCHAIN DATA")
    print("="*50)
    print(f"Advice: {data['advice']}")
    print(f"Timestamp: {data['timestamp']}")
    print(f"Transaction: {data['transaction_hash']}")
    print("="*50)

def main():
    """Main function to run the demo"""
    print("=" * 50)
    print("CRYPTO ADVISOR: AI + BLOCKCHAIN DEMO")
    print("=" * 50)
    print("\nThis demo simulates blockchain storage of AI-generated investment advice.")
    
    # Get user input
    try:
        user_id = input("\nEnter a user ID (e.g., your name): ")
        risk = int(input("Enter your risk tolerance (1-10): "))
        if risk < 1 or risk > 10:
            print("Risk tolerance must be between 1 and 10. Setting to 5.")
            risk = 5
        
        amount = float(input("Enter your investment amount ($): "))
        if amount <= 0:
            print("Investment amount must be positive. Setting to $1000.")
            amount = 1000
    except ValueError:
        print("Invalid input. Using default values: risk=5, amount=$1000")
        risk = 5
        amount = 1000
    
    # Generate AI advice
    print("\nGenerating AI investment advice...")
    advice = generate_advice(risk, amount)
    
    print("\nAI-Generated Investment Advice:")
    print("-" * 40)
    print(advice)
    print("-" * 40)
    
    # Store on simulated blockchain
    tx_hash = store_on_blockchain(user_id, advice)
    
    # Retrieve from simulated blockchain
    blockchain_data = retrieve_from_blockchain(user_id)
    
    # Display blockchain data
    display_blockchain_data(blockchain_data)
    
    # Verify data integrity
    if blockchain_data and blockchain_data['advice'] == advice:
        print("\n✅ Verification successful: Blockchain data matches generated advice.")
    else:
        print("\n❌ Verification failed: Blockchain data doesn't match generated advice.")
    
    # Save results to file
    with open(f"{user_id}_crypto_advice.json", "w") as f:
        json.dump({
            "user_id": user_id,
            "risk_tolerance": risk,
            "investment_amount": amount,
            "advice": advice,
            "blockchain_data": blockchain_data
        }, f, indent=2)
    
    print(f"\nResults saved to {user_id}_crypto_advice.json")
    print("\nThank you for using CryptoAdvisor!")

if __name__ == "__main__":
    main() 