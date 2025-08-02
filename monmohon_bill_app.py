
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from datetime import datetime

class BillCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)

        self.add_widget(Label(text='Previous Reading:'))
        self.prev_reading = TextInput(multiline=False, input_filter='int')
        self.add_widget(self.prev_reading)

        self.add_widget(Label(text='Current Reading:'))
        self.curr_reading = TextInput(multiline=False, input_filter='int')
        self.add_widget(self.curr_reading)

        self.add_widget(Label(text='Start Date (DD-MM-YYYY):'))
        self.start_date = TextInput(multiline=False)
        self.add_widget(self.start_date)

        self.add_widget(Label(text='End Date (DD-MM-YYYY):'))
        self.end_date = TextInput(multiline=False)
        self.add_widget(self.end_date)

        self.result_label = Label(text='')
        self.add_widget(self.result_label)

        calc_btn = Button(text='Calculate Bill')
        calc_btn.bind(on_press=self.calculate)
        self.add_widget(calc_btn)

    def calculate(self, instance):
        try:
            prev = int(self.prev_reading.text)
            curr = int(self.curr_reading.text)
            start = datetime.strptime(self.start_date.text, "%d-%m-%Y")
            end = datetime.strptime(self.end_date.text, "%d-%m-%Y")

            units = curr - prev
            days = (end - start).days
            avg_per_day = units / days if days > 0 else 0

            # Bill calculation
            if units <= 50:
                bill = units * 5.38
            else:
                bill = 50 * 5.38 + (units - 50) * 6.78

            bill += 10  # Meter Rent
            bill += 18  # Duty
            bill += 45.48  # FPPC

            result = f"Total Units: {units}\nTotal Days: {days}\nAvg/Day: {avg_per_day:.2f}\nEstimated Bill: ₹{bill:.2f}"
        except Exception as e:
            result = f"Error: {str(e)}"

        self.result_label.text = result

class MonmohonBillApp(App):
    def build(self):
        return BillCalculator()

if __name__ == '__main__':
    MonmohonBillApp().run()
