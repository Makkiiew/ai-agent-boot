import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
import argparse
from call_function import available_functions




def main():
    parser = argparse.ArgumentParser(description="chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")    
    args = parser.parse_args()


    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
       raise RuntimeError("GEMINI_API_KEY not found in environment variables. Check your .env file!")

    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(
            role="user", 
            parts=[types.Part(text=args.user_prompt)]
        )
    ]

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=messages,
            config=types.GenerateContentConfig(system_instruction=system_prompt,
                tools=[available_functions]),
        )

        if response.usage_metadata is None:
            raise RuntimeError("API request failed: No usage metadata returned.")
        if not response.usage_metadata:
            raise RuntimeError("Gemini API response appears to be malformed")

        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        if response.function_calls:
            for function_call in response.function_calls:
                print(f"Calling function: {function_call.name}({function_call.args})")
        else:
            if response.text:
                print(response.text)
                
    except Exception as e:
        print(f"Error: {e}")

       

if __name__ == "__main__":
    main()
