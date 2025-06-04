import openai
import json

openai.api.key = "keyHere"

def generateSchedule(goal):
    prompt = f"""You are a weekly schedule and planning assistant. Based on the user's goal:
    "{goal}"
    Create a weekly schedule in json format like:
    {{
        "Monday": ["Task 1", "Task 2"] ,...,
        "Tuesday": ["Task1", "Task 2"], ......,
        ......
    }}
    """
    
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = [{"role": "user", "content": prompt}],
        temperature = 0.7,
    )
    
    content = response["choices"][0]["message"]["content"]
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
