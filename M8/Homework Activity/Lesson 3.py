class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.task = None

    def introduce(self):
        print(f"Hello! I am {self.name}, a robot model {self.model}.")

    def set_task(self, task):
        self.task = task
        print(f"{self.name}'s task set to: {self.task}")

    def show_task(self):
        if self.task:
            print(f"{self.name}'s current task: {self.task}")
        else:
            print(f"{self.name} has no task assigned.")

    def update_model(self, new_model):
        self.model = new_model
        print(f"{self.name}'s model updated to {self.model}.")

class AdvancedRobot(Robot):
    def __init__(self, name, model, skills=None):
        self.name = name
        self.model = model
        self.skills = skills if skills else []

    def add_skill(self, skill):
        self.skills.append(skill)
        print(f"{self.name} learned a new skill: {skill}")

    def show_skills(self):
        if self.skills:
            print(f"{self.name}'s skills: {', '.join(self.skills)}")
        else:
            print(f"{self.name} has no skills yet.")

print("--- Basic Robot Example ---\n")
robot1 = Robot("GitHub Copilot", "AI-2024")
robot1.introduce()
robot1.set_task("Assist with coding")
robot1.show_task()
robot1.update_model("AI-2025")
robot1.introduce()

print("\n--- Advanced Robot Example ---\n")

chatgpt5 = AdvancedRobot("ChatGPT 5", "AI-2025", ["Natural Language Processing", "Code Generation"])
chatgpt5.introduce()
chatgpt5.show_skills()
chatgpt5.add_skill("Creative Writing")
chatgpt5.show_skills()
chatgpt5.set_task("Help users with creative ideas")
chatgpt5.show_task()