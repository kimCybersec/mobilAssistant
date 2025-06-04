from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from utils.gptScheduler import *
from utils.tracker import *
from reminders import *

class scheduleAssistantApp(App):
    def build(self):
        startReminders()
        return Builder.load_file("gui.kv")
    
    def showGoals(self):
        content = BoxLayout(orietation = 'vertical', spacing = 10)
        inputBox = TextInput(hint_text="Enter your goal for this week", multiline=False)
        submitBtn = Button(text="Genrate schedule", size_hint_y=None, height=50)
        
        content.add_widget(inputBox)
        content.add_widget(submitBtn)
        
        popup = Popup(title="Set weekly goal", content=content, size_hint=(0.8, 0.4))
        
        def onSubmit(instance):
            schedule = generateSchedule(inputBox.text)
            if schedule:
                saveSChedule(schedule)
                popup.dismiss()
                
            submitBtn.bind(on_release=onSubmit)
            popup.open()
            
    def showTasks(self):
        showAllTasks()
        
    def markTaskDone(self):
        content = BoxLayout(orientation='vertical', spacing=10)
        dayInput = TextInput(hint_text="Enter the day (e.g., Monday)", multiline=False)
        taskInput = TextInput(hint_text="Enter the task title to mark as done", multiline=False)
        submitBtn = Button(text="Mark as done", size_hint_y=None, height=50)
        
        content.add_widget(dayInput)
        content.add_widget(taskInput)
        content.add_widget(submitBtn)
        
        popup = Popup(title="Mark Task as Done", content=content, size_hint=(0.8, 0.4))
        
        def onSubmit(instance):
            markDone(dayInput.text, taskInput.text)
            popup.dismiss()
            
        submitBtn.bind(on_release=onSubmit)
        popup.open()
        
    def showSummary(self):
        showSummary()
        
if "__main__" == __name__:
    scheduleAssistantApp().run()
        
        
        