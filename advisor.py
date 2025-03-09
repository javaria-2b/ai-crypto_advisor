import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_advice(risk_tolerance, investment_amount):
    prompt = f"""
    Generate cryptocurrency investment advice for someone with:
    - Risk tolerance: {risk_tolerance}/10
    - Investment amount: ${investment_amount}
    
    Provide a brief, concise strategy (max 150 words).
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

# Test function
if __name__ == "__main__":
    # Simple test to ensure the API works
    test_advice = generate_advice(5, 1000)
    print("Test advice generation:")
    print(test_advice) 