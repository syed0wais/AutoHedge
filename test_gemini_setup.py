"""
Test script to verify Gemini API configuration for AutoHedge.
Run this before running the main example.py to ensure your setup is correct.
"""

import os
from openai import OpenAI

def test_gemini_connection():
    """Test if Gemini API is configured correctly."""
    
    # Get API key from environment
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_API_BASE", "https://generativelanguage.googleapis.com/v1beta/openai/")
    
    if not api_key:
        print("❌ ERROR: OPENAI_API_KEY environment variable not set!")
        print("\nPlease set your Gemini API key:")
        print("  export OPENAI_API_KEY='your-gemini-api-key'")
        print("\nOr add it to your .env file")
        return False
    
    print("✓ API Key found")
    print(f"✓ Base URL: {base_url}")
    print(f"✓ API Key (first 10 chars): {api_key[:10]}...")
    
    try:
        # Create OpenAI client with Gemini endpoint
        client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        
        print("\n🔄 Testing connection to Gemini API...")
        
        # Make a simple test request
        response = client.chat.completions.create(
            model="gemini-2.0-flash-exp",
            messages=[
                {"role": "user", "content": "Say 'Hello from Gemini!' if you can read this."}
            ]
        )
        
        result = response.choices[0].message.content
        print(f"\n✅ SUCCESS! Gemini API is working!")
        print(f"Response: {result}")
        print("\n🎉 Your AutoHedge system is ready to use Gemini API!")
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: Failed to connect to Gemini API")
        print(f"Error details: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Verify your API key is correct")
        print("2. Check if you have API quota at https://aistudio.google.com/")
        print("3. Ensure OPENAI_API_BASE is set correctly")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("AutoHedge - Gemini API Configuration Test")
    print("=" * 60)
    print()
    
    success = test_gemini_connection()
    
    if success:
        print("\n" + "=" * 60)
        print("Next step: Run 'python3 example.py' to start trading!")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("Please fix the errors above before running AutoHedge")
        print("=" * 60)
