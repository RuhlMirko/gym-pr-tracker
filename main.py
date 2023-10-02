from kivy.uix.boxlayout import BoxLayout
from kivy.storage.jsonstore import JsonStore
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty

class RootWidget(BoxLayout):
    stored_data = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(BoxLayout, self).__init__(*args, **kwargs)
        self.stored_data = JsonStore('personal_record.json')
        self.exercises = ['bench-press', 'incline-bench', 'fly', 'lateral-raises', 'overhead-press',
                          'skull-crusher', 'push-down', 'triceps-extension']
        self.current_exercise = 0

    def more_kg(self):
        unit = float(self.ids.kg.text)
        self.ids.kg.color = ("#FFDE25")
        new_kg = str(unit + 2.5)
        self.ids.kg.text = new_kg
        return new_kg

    def more_sets(self):
        unit = int(self.ids.sets.text)
        new_unit = str(unit + 1)
        self.ids.sets.text = new_unit
        self.ids.sets.color = ("#FFDE25")
        return new_unit

    def more_reps(self):
        unit = int(self.ids.reps.text)
        new_unit = str(unit + 1)
        self.ids.reps.text = new_unit
        self.ids.reps.color = ("#FFDE25")
        return new_unit

    def less_kg(self):
        unit = float(self.ids.kg.text)
        self.ids.kg.color = ("#FFDE25")
        new_kg = str(unit - 2.5)
        self.ids.kg.text = new_kg
        return new_kg

    def less_sets(self):
        unit = int(self.ids.sets.text)
        new_unit = str(unit - 1)
        self.ids.sets.text = new_unit
        self.ids.sets.color = ("#FFDE25")
        return new_unit

    def less_reps(self):
        unit = int(self.ids.reps.text)
        new_unit = str(unit - 1)
        self.ids.reps.text = new_unit
        self.ids.reps.color = ("#FFDE25")
        return new_unit

    def next_exercise(self):
        if self.current_exercise <= 6:
            self.current_exercise += 1
            self.ids.exercise.text = self.exercises[self.current_exercise]
        else:
            self.current_exercise = 0
            self.ids.exercise.text = self.exercises[self.current_exercise]
        self.ids.kg.color = ("#FFFFFF")
        self.ids.reps.color = ("#FFFFFF")
        self.ids.sets.color = ("#FFFFFF")
    def prev_exercise(self):
        if self.current_exercise >= 0:
            self.current_exercise -= 1
            self.ids.exercise.text = self.exercises[self.current_exercise]
        else:
            self.current_exercise = 6
            self.ids.exercise.text = self.exercises[self.current_exercise]
        self.ids.kg.color = ("#FFFFFF")
        self.ids.reps.color = ("#FFFFFF")
        self.ids.sets.color = ("#FFFFFF")

runTouchApp(Builder.load_file("styles.kv"))
