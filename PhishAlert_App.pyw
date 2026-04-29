import tkinter as tk
from tkinter import messagebox
import pickle
import sklearn.pipeline
import os
import sys

# Patch Pipeline to avoid unpickling errors with older models
if not hasattr(sklearn.pipeline.Pipeline, 'transform_input'):
    sklearn.pipeline.Pipeline.transform_input = None

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'phishing.pkl')

# Load the model
try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    model = None
    error_msg = str(e)

def check_url(event=None):
    if model is None:
        messagebox.showerror("Error", f"Could not load model 'phishing.pkl'.\nEnsure it is in the same folder as this app.\n\nError details:\n{error_msg}")
        return
        
    url = url_entry.get()
    if not url.strip():
        messagebox.showwarning("Input Error", "Please enter a URL to check.")
        return
        
    try:
        # The pipeline automatically handles tokenization and vectorization
        prediction = model.predict([url])[0]
        
        if prediction == 'bad':
            result_label.config(text="🚨 This is a Phishing Site!", fg="#D32F2F", font=("Helvetica", 14, "bold"))
        else:
            result_label.config(text="✅ This is a safe (good) site.", fg="#388E3C", font=("Helvetica", 14, "bold"))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during prediction:\n{e}")

# Create GUI
root = tk.Tk()
root.title("PhishAlert Detector")
root.geometry("400x250")
root.resizable(False, False)
# Center the window
root.eval('tk::PlaceWindow . center')

# UI Elements
title_label = tk.Label(root, text="PhishAlert URL Checker", font=("Helvetica", 16, "bold"), fg="#333333")
title_label.pack(pady=20)

instruction_label = tk.Label(root, text="Enter a URL below:", font=("Helvetica", 10))
instruction_label.pack()

url_entry = tk.Entry(root, width=35, font=("Helvetica", 12), justify="center")
url_entry.pack(pady=10)
url_entry.bind('<Return>', check_url) # Check when Enter is pressed
url_entry.focus()

check_button = tk.Button(root, text="Check URL", command=check_url, bg="#0078D7", fg="white", font=("Helvetica", 10, "bold"), width=15)
check_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=15)

# Run the app
root.mainloop()
