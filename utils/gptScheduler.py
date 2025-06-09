import openai
import json

openai.api_key = "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"

def generateSchedule(goal):
    prompt = f"""You are a weekly schedule and planning assistant. Based on the user's goal:
    "{goal}"
    Create a weekly schedule in json format like:
    {{
        "Monday": ["Task 1", "Task 2"],
        "Tuesday": ["Task1", "Task 2"],
        ...
    }}
    """
    client = openai.OpenAI(api_key=openai.api_key)
    response = client.chat.completions.create(
        model="gpt-3.5",
        messages=[{"role": "user", "content": "Hello"}],
        max_tokens=100,  # reduce output length
        temperature=0.7
    )

    content = response.choices[0].message.content
    try:
        schedule = json.loads(content)
        return schedule
    except json.JSONDecodeError:
        print("Failed to parse GPT response")
        return
    
def saveSChedule(schedule):
    with open("data/schchedule.json" "w") as f:
        json.dump(schedule, f , indent=4)
        print("schedule saved from gpt")
        
if __name__ == "__main__":
    userGoal = input("What is your goal for this week?")
    schedule = generateSchedule(userGoal)
    if schedule:
        saveSChedule(schedule)
