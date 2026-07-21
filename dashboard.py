import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

df = pd.read_csv('data/final_linked_dataset.csv')

root = tk.Tk()
root.title("Pakistan Election Turnout Dashboard")
root.geometry("900x650")

label = tk.Label(root, text="Select a Constituency:", font=("Arial", 12))
label.pack(pady=10)

constituency_list = sorted(df['constituency_name_2008'].dropna().unique().tolist())
selected_constituency = tk.StringVar()
dropdown = ttk.Combobox(root, textvariable=selected_constituency, values=constituency_list, width=40)
dropdown.pack(pady=5)

chart_frame = tk.Frame(root)
chart_frame.pack(fill=tk.BOTH, expand=True, pady=10)


def show_chart(event=None):
    try:
        for widget in chart_frame.winfo_children():
            widget.destroy()

        name = selected_constituency.get()
        row = df[df['constituency_name_2008'] == name]

        if row.empty:
            return
        row = row.iloc[0]

        years = ['2008', '2013', '2018']
        values = [row['turnout_2008'] * 100, row['turnout_2013'] * 100, row['turnout'] * 100]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(years, values, marker='o', color='steelblue')
        ax.set_title('Turnout Trend: ' + name)
        ax.set_ylabel('Turnout (%)')
        ax.set_ylim(0, 100)

        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        info_text = 'Turnout 2008: ' + str(round(values[0],1)) + '%\n'
        info_text += 'Turnout 2013: ' + str(round(values[1],1)) + '%\n'
        info_text += 'Turnout 2018: ' + str(round(values[2],1)) + '%\n'
        info_text += 'Swing 2008-2018: ' + str(round(values[2]-values[0],1)) + ' pp'

        info_label = tk.Label(chart_frame, text=info_text, font = ("Arial", 11), justify = "left")
        info_label.pack(pady=10)

    except Exception as e:
        print ("ERROR:", e)


dropdown.bind("<<ComboboxSelected>>", show_chart)

root.mainloop()