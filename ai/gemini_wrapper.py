import os
from google import genai
from dotenv import load_dotenv
import json

# Load Gemini client
load_dotenv()
key= os.getenv("GEMINI_API_KEY")
if not key:
    raise ValueError("❌ GEMINI_API_KEY not found in environment variables.")

client = genai.Client(api_key=key)

def get_personality_report(mbti_type, post_list):
    try:
        # Ensure max 5 clean posts
        posts = [p.strip() for p in post_list if p.strip()]
        posts = posts[:5]

        # Format them as numbered list
        post_lines = '\n'.join([f"{i+1}. “{p}”" for i, p in enumerate(posts)])

        # Prompt with correct structure
        prompt = f"""
        You are part of a personality prediction system that receives a predicted MBTI type and user text samples (e.g., social media posts).

        Your job is to return a well-structured analysis of the user's personality in JSON format only. Do not include any explanation or non-JSON content.

        Format strictly like this:

        {{
          "mbti_type": "MBTI_TYPE",
          "vibe_summary": "One-line personality summary",
          "relationship_behavior": "Describe their relationship style",
          "confidence_score": "High / Medium / Low",
          "top_traits": ["Trait1", "Trait2", "Trait3"],
          "friend_compatibility": ["MBTI1 85%", "MBTI2 72%", "MBTI3 87%", "MBTI4 64%"]
        }}

        Use the text samples below and the given MBTI type to make your predictions.

        MBTI Type: {mbti_type}

        User Posts:
        {post_lines}

        Return only valid JSON output. No explanation, no extra text.
        """

        # Call Gemini
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )


        response_text = response.text.strip()

        if response_text.startswith("```json"):
            response_text = response_text[len("```json"):]

        if response_text.endswith("```"):
            response_text = response_text[:-3]

        response_text = response_text.strip()

        # Convert response to dictionary
        json_data = json.loads(response_text)
        return json_data

    except json.JSONDecodeError:
        print("⚠️ Gemini returned invalid JSON:\n", response_text)
        return None
    except Exception as e:
        print("❌ Gemini API Error:", str(e))
        return None
