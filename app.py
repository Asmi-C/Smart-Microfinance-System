import tkinter as tk
from tkinter import messagebox
from utils import save_application, load_model

model = load_model()

class LoanApplicationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Smart Microfinance Loan Application')
        self.root.geometry('400x400')

        self.labels = ['Income', 'Employment Years', 'Loan Amount', 'Business Experience (years)', 'Credit History Score']
        self.entries = []

        for i, label in enumerate(self.labels):
            tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(root)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries.append(entry)

        submit_btn = tk.Button(root, text='Submit Application', command=self.submit_application)
        submit_btn.grid(row=len(self.labels), columnspan=2, pady=20)

    def submit_application(self):
        try:
            user_data = [float(entry.get()) for entry in self.entries]
            prediction = model.predict([user_data])[0]
            result = "Loan Approved" if prediction == 1 else "Loan Rejected"

            save_application({
                'income': user_data[0],
                'employment_years': user_data[1],
                'loan_amount': user_data[2],
                'business_experience': user_data[3],
                'credit_history': user_data[4],
                'loan_approved': prediction
            })

            messagebox.showinfo('Application Status', result)
        except ValueError:
            messagebox.showerror('Input Error', 'Please enter valid numeric values.')

if __name__ == '__main__':
    root = tk.Tk()
    app = LoanApplicationGUI(root)
    root.mainloop()
