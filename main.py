from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView


class TaskManager(App):
    def build(self):
        self.score = {'Т': 0, 'Р': 0, 'Д': 0}
        self.task_list = []

        main_layout = BoxLayout(orientation='vertical')

        # Score Label
        self.score_label = Label(text=self.get_score_text(), size_hint=(1, 0.1))
        main_layout.add_widget(self.score_label)

        # Task ScrollView
        self.task_scroll = ScrollView(size_hint=(1, 0.8))
        self.task_container = BoxLayout(orientation='vertical', size_hint_y=None)
        self.task_container.bind(minimum_height=self.task_container.setter('height'))
        self.task_scroll.add_widget(self.task_container)
        main_layout.add_widget(self.task_scroll)

        # Add Task Button
        add_button = Button(text="+", size_hint=(1, 0.1))
        add_button.bind(on_release=self.show_add_task_popup)
        main_layout.add_widget(add_button)

        return main_layout

    def get_score_text(self):
        return f"{self.score['Т']}/{self.score['Р']}/{self.score['Д']}"

    def show_add_task_popup(self, instance):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Task Text Input
        self.task_input = TextInput(hint_text="Введите задачу", multiline=False)
        popup_layout.add_widget(self.task_input)

        # Category Buttons
        category_layout = BoxLayout(size_hint=(1, 0.2))
        self.category_buttons = {}
        for category in ['Т', 'Р', 'Д']:
            btn = Button(text=category)
            btn.bind(on_release=lambda instance, cat=category: self.select_category(cat))
            self.category_buttons[category] = btn
            category_layout.add_widget(btn)
        popup_layout.add_widget(category_layout)

        # OK Button
        ok_button = Button(text="OK", size_hint=(1, 0.2))
        ok_button.bind(on_release=self.add_task)
        popup_layout.add_widget(ok_button)

        self.selected_category = None
        self.popup = Popup(title="Добавить задачу", content=popup_layout, size_hint=(0.8, 0.6))
        self.popup.open()

    def select_category(self, category):
        self.selected_category = category
        for cat, btn in self.category_buttons.items():
            btn.background_color = (1, 0, 0, 1) if cat == category else (1, 1, 1, 1)

    def add_task(self, instance):
        task_text = self.task_input.text
        if task_text.strip() and self.selected_category:
            self.popup.dismiss()
            task_box = BoxLayout(size_hint_y=None, height=50)

            # Fail Button
            fail_button = Button(text="*")
            fail_button.bind(on_release=lambda instance: self.update_score(task_box, self.selected_category, -1))
            task_box.add_widget(fail_button)

            # Task Label
            task_label = Label(text=task_text)
            task_box.add_widget(task_label)

            # Complete Button
            complete_button = Button(text="\/")
            complete_button.bind(on_release=lambda instance: self.update_score(task_box, self.selected_category, 1))
            task_box.add_widget(complete_button)

            self.task_container.add_widget(task_box)
            self.task_list.append(task_box)

    def update_score(self, task_box, category, value):
        self.score[category] += value
        self.score_label.text = self.get_score_text()
        self.task_container.remove_widget(task_box)


if __name__ == '__main__':
    TaskManager().run()