import tkinter as tk
import requests
import json

def send_data():
    patient_data = {
        'name': name_entry.get(),
        'condition': condition_var.get(),
        'timestamp': '2024-09-19T10:00:00'  # Example timestamp
    }
    url = 'http://127.0.0.1:5000/api/patient_data'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(patient_data))
    print(response.text)

app = tk.Tk()
app.title('Patient Data Entry')

tk.Label(app, text='Name').grid(row=0)
tk.Label(app, text='Condition').grid(row=1)

name_entry = tk.Entry(app)
condition_var = tk.StringVar(app)
condition_var.set('Select Condition')
conditions = ['Asthma Attack', 'Fire', 'Other']
condition_menu = tk.OptionMenu(app, condition_var, *conditions)

name_entry.grid(row=0, column=1)
condition_menu.grid(row=1, column=1)

submit_button = tk.Button(app, text='Submit', command=send_data)
submit_button.grid(row=2, column=1)

app.mainloop()
