#!/usr/bin/env python3
"""
Debug script to check environment variable loading and API configuration
"""

import os
from dotenv import load_dotenv

print("=" * 60)
print("Environment Variable Debug Script")
print("=" * 60)

# Load .env file
print("\n1. Loading .env file...")
load_dotenv()
print("   ✓ load_dotenv() called")

# Check OPENAI_API_KEY
api_key = os.getenv("OPENAI_API_KEY")
print(f"\n2. OPENAI_API_KEY:")
if api_key:
    print(f"   ✓ Found: {api_key[:10]}...{api_key[-4:]}")
    print(f"   Length: {len(api_key)} characters")
else:
    print("   ✗ NOT FOUND")

# Check OPENAI_API_BASE
api_base = os.getenv("OPENAI_API_BASE")
print(f"\n3. OPENAI_API_BASE:")
if api_base:
    print(f"   ✓ Found: {api_base}")
else:
    print("   ✗ NOT FOUND (will use default OpenAI endpoint)")

# Check WORKSPACE_DIR
workspace = os.getenv("WORKSPACE_DIR")
print(f"\n4. WORKSPACE_DIR:")
if workspace:
    print(f"   ✓ Found: {workspace}")
else:
    print("   ✗ NOT FOUND")

# Test Gemini API connection
print("\n5. Testing Gemini API connection...")
try:
    from openai import OpenAI
    
    client = OpenAI(
        api_key=api_key,
        base_url=api_base
    )
    
    response = client.chat.completions.create(
        model="gemini-2.0-flash-exp",
        messages=[{"role": "user", "content": "Say 'API works!' if you can read this."}],
        max_tokens=10
    )
    
    print(f"   ✓ SUCCESS! Response: {response.choices[0].message.content}")
except Exception as e:
    print(f"   ✗ FAILED: {str(e)[:100]}")

print("\n" + "=" * 60)
print("Debug Complete")
print("=" * 60)
