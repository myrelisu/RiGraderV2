from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

class RiWriter(Screen):
    pass

class Classes(Screen):
    pass

class User_manual(Screen):
    pass


class RiGrader(Screen):
    test_input = ObjectProperty(None)
    class_input = ObjectProperty(None)
    name_input = ObjectProperty(None)
    
    reading_input = ObjectProperty(None)
    listening_input = ObjectProperty(None)
    writing1_input = ObjectProperty(None)
    writing2_input = ObjectProperty(None)
    speaking_input = ObjectProperty(None)

    results_text = ObjectProperty(None)

    reading_per_display = ObjectProperty(None)
    list_per_display = ObjectProperty(None)
    writing_per_display = ObjectProperty(None)
    speaking_per_display = ObjectProperty(None)


class MainApp(MDApp):
    def build(self):
        self.title = "RiGrader"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "Gray"
        # Window.size = (400, 800)

        # create instance of RiGrader screen
        screen_manager = ScreenManager()
        rigrader_app = RiGrader(name="rigrader_app")
        screen_manager.add_widget(rigrader_app)

        # create instance of RiWriter screen
        riwriter_app = RiWriter(name='riwriter_app')
        screen_manager.add_widget(riwriter_app)

        # create instance of Classes screen
        classes_app = Classes(name='classes_app')
        screen_manager.add_widget(classes_app)

        # create instance of User Manual screen
        user_manual_app = User_manual(name='user_manual_app')
        screen_manager.add_widget(user_manual_app)

    
        return screen_manager

    def calculate(self):
        rigrader = self.root.get_screen('rigrader_app')
        name = rigrader.name_input.text
        reading = int(rigrader.reading_input.text)
        reading_p = reading/32*100
        listening = int(rigrader.listening_input.text)
        listening_p = listening/25*100
        writing1 = int(rigrader.writing1_input.text)
        writing2 = int(rigrader.writing2_input.text)
        writing = writing1 + writing2
        writing_p = writing/40*100
        speaking = int(rigrader.speaking_input.text)
        speaking_p = speaking/20*100
        total = reading + listening + writing1 + writing2 + speaking
        total_p = round(total/117*100)

        rigrader.reading_per_display.text = f"{reading_p}%"
        rigrader.list_per_display.text = f"{listening_p}%"
        rigrader.writing_per_display.text = f"{writing_p}%"
        rigrader.speaking_per_display.text = f"{speaking_p}%"
        if total_p > 70:
            rigrader.results_text.text = f"Total:   {total}\nTotal percentage:{total_p}%.\n{name} passed the exam."
        else:
            rigrader.results_text.text = f"Total:   {total}/117     {total_p}%.\n{name} failed the exam." 

    def clear(self):
        rigrader = self.root.get_screen('rigrader_app')
        rigrader.reading_input.text = ""
        rigrader.listening_input.text = ""
        rigrader.writing1_input.text = ""
        rigrader.writing2_input.text = ""
        rigrader.speaking_input.text = ""
        rigrader.name_input.text = ""
        rigrader.results_text.text = ""
        rigrader.reading_per_display.text = "/32"
        rigrader.list_per_display.text = "/25"
        rigrader.writing_per_display.text = "/40"
        rigrader.speaking_per_display.text = "/20"


if __name__ == '__main__':
    MainApp().run()