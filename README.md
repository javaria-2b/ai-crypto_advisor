# CryptoAdvisor: AI-Powered Investment Advice

## Hackathon Submission

**Team:** Solo Project  
**Category:** Vyper + AI Agent

## Project Summary

CryptoAdvisor is a proof-of-concept demonstrating how AI and blockchain technology can be combined to create personalized cryptocurrency investment advice that is permanently recorded and verifiable. The project showcases the integration of OpenAI's API with blockchain concepts in a simple but powerful application.

## Problem Statement

Cryptocurrency investors face two major challenges:
1. Receiving personalized investment advice that matches their risk tolerance and budget
2. Having a verifiable record of the advice they received for future reference or accountability

CryptoAdvisor solves both problems by using AI to generate tailored advice and blockchain technology to create an immutable record of this advice. It demonstrates a novel combination of technologies:

1. **AI + Blockchain Integration**: Shows how AI outputs can be stored and verified on-chain
2. **Personalized Financial Advice**: Demonstrates practical application of AI in financial decision-making
3. **Immutable Record-Keeping**: Showcases blockchain's ability to provide permanent, verifiable records

## Technical Implementation

The project was implemented in two phases:

### Phase 1: Full Vyper Implementation (Planned)
The initial design included a Vyper smart contract that would store AI-generated advice on the blockchain, making it permanently accessible and unalterable.

### Phase 2: Simplified Demo (Completed)
Due to time constraints, we created a simplified demo that still showcases the core concept:
- Uses OpenAI's API to generate personalized investment advice
- Simulates blockchain storage with transaction hashes
- Provides data verification to ensure integrity
- Exports results as JSON for future reference

## Key Features

1. **Personalized AI Advice**: The system generates investment recommendations based on:
   - User's risk tolerance (scale of 1-10)
   - Investment amount
   
2. **Blockchain Storage**:
   - Creates a unique transaction hash for each piece of advice
   - Timestamps the advice for future reference
   - Simulates the retrieval process from a blockchain
   
3. **Verification Process**:
   - Ensures the stored advice matches the generated advice
   - Demonstrates the concept of blockchain verification

4. **Persistent Storage**:
   - Saves complete investment profile and advice as JSON
   - Creates permanent record for future reference


## Usage Instructions

## Setup (2 minutes)

1. Install dependencies:
   ```
   pip install openai python-dotenv
   ```

2. Set up your environment:
   ```
   cp .env.example .env
   ```
   Then edit the `.env` file and add your OpenAI API key.

## Usage (30 seconds)

Run the application:
```
python simple_demo.py
```

## How It Works

1. **User Input**: The app collects user ID, risk tolerance, and investment amount
2. **AI Generation**: OpenAI API creates personalized investment advice
3. **Storage Simulation**: The advice is stored in memory with a simulated transaction hash
4. **Verification**: The stored data is retrieved and verified for integrity
5. **Export**: Results are saved as a JSON file for reference

## Files

- `simple_demo.py`: Complete application logic
- `.env`: Environment variables (API keys)

## Hackathon Criteria Alignment

### Technical Innovation (30%)
- Demonstrates AI integration with blockchain concepts
- Generates unique transaction hashes based on content

### AI Integration (25%)
- Uses OpenAI API for personalized investment advice
- Parameters influence the AI's output for customized results

### Code Quality & Security (25%)
- Clean, well-documented code with clear separation of concerns
- Error handling with graceful fallbacks

### Business Potential (20%)
- Shows potential for AI-powered on-chain advisory services
- Creates permanent record of investment advice with simulated blockchain storage

## What's Next

After the hackathon, this prototype could be expanded to include:
1. Real blockchain integration using Vyper smart contracts
2. More sophisticated AI analysis incorporating market data
3. User authentication and account system
4. Mobile application for accessibility
5. Subscription model for ongoing advice 

## Conclusion

CryptoAdvisor demonstrates that even with limited time (under 1 hour), it's possible to create a functional prototype that combines AI and blockchain concepts in a meaningful way. The project showcases the potential for these technologies to revolutionize financial advisory services by providing personalized, verifiable investment guidance.

We believe this concept has significant potential for further development, particularly as AI models become more sophisticated and blockchain technology becomes more accessible. 