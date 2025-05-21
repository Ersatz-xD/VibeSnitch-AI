from ai.gemini_wrapper import get_personality_report

# Sample data
sample_mbti = "ENFP"
sample_posts = [
    "I could never work a 9-5 forever. I need to create or I’ll lose it.",
    "Last-minute road trip? Count me in. Life’s too short to overthink everything.",
    "People who can’t vibe with memes are not my kind of people.",
    "I swear I’m trying to focus… wait, what was I doing again?",
    "Deep convos at 2am hit different. Let’s talk about the universe and stuff."
]

# Run the test
report = get_personality_report(sample_mbti, sample_posts)

# Print the response
if report:
    print(" Gemini Personality Report:")
    print(report)
else:
    print(" Failed to get valid response.")
