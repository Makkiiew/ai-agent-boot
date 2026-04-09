import os
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("GEMINI_API_KEY not found in environment variables. Check your .env file!")

    client = genai.Client(api_key=api_key)

    prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print(response.text)
    except Exception as e:
        print(f"Error: {e}")

       

if __name__ == "__main__":
    main()
