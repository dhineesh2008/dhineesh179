import tkinter as tk
from tkinter import messagebox, filedialog
import json
import sqlite3

class ItineraryPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Travel Itinerary Planner")
        self.itinerary = []
        
        # Create database and table
        self.conn = sqlite3.connect('itinerary.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS itinerary (
                id INTEGER PRIMARY KEY,
                destination TEXT,
                activity TEXT,
                accommodation TEXT,
                date TEXT
            )
        ''')
        self.conn.commit()

        # GUI Elements
        tk.Label(root, text="Travel Itinerary Planner", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(root, text="Destination:").pack()
        self.destination_entry = tk.Entry(root)
        self.destination_entry.pack()

        tk.Label(root, text="Activity:").pack()
        self.activity_entry = tk.Entry(root)
        self.activity_entry.pack()

        tk.Label(root, text="Accommodation:").pack()
        self.accommodation_entry = tk.Entry(root)
        self.accommodation_entry.pack()

        tk.Label(root, text="Date (DD-MM-YYYY):").pack()
        self.date_entry = tk.Entry(root)
        self.date_entry.pack()

        tk.Button(root, text="Add to Itinerary", command=self.add_to_itinerary).pack(pady=10)
        tk.Button(root, text="View Itinerary", command=self.view_itinerary).pack(pady=5)
        tk.Button(root, text="Clear Itinerary", command=self.clear_itinerary).pack(pady=5)
        tk.Button(root, text="Save Itinerary", command=self.save_itinerary).pack(pady=5)
        tk.Button(root, text="Load Itinerary", command=self.load_itinerary).pack(pady=5)
        tk.Button(root, text="Save to Database", command=self.save_to_database).pack(pady=5)
        tk.Button(root, text="Load from Database", command=self.load_from_database).pack(pady=5)

    def add_to_itinerary(self):
        destination = self.destination_entry.get()
        activity = self.activity_entry.get()
        accommodation = self.accommodation_entry.get()
        date = self.date_entry.get()

        if not destination or not activity or not accommodation or not date:
            messagebox.showwarning("Warning", "Please fill in all fields.")
            return

        itinerary_entry = {
            "Destination": destination,
            "Activity": activity,
            "Accommodation": accommodation,
            "Date": date
        }
        self.itinerary.append(itinerary_entry)

        # Clear entries after adding
        self.destination_entry.delete(0, tk.END)
        self.activity_entry.delete(0, tk.END)
        self.accommodation_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Added to itinerary!")

    def view_itinerary(self):
        if not self.itinerary:
            messagebox.showinfo("Itinerary", "Your itinerary is empty.")
            return

        itinerary_summary = "\n".join(
            [f"{entry['Date']}: {entry['Activity']} at {entry['Destination']} (Stay: {entry['Accommodation']})"
             for entry in self.itinerary]
        )
        messagebox.showinfo("Your Itinerary", itinerary_summary)

    def clear_itinerary(self):
        self.itinerary.clear()
        messagebox.showinfo("Cleared", "Your itinerary has been cleared.")

    def save_itinerary(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'w') as f:
                json.dump(self.itinerary, f)
            messagebox.showinfo("Saved", "Itinerary saved successfully!")

    def load_itinerary(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'r') as f:
                self.itinerary = json.load(f)
            messagebox.showinfo("Loaded", "Itinerary loaded successfully!")

    def save_to_database(self):
        for entry in self.itinerary:
            self.cursor.execute('''
                INSERT INTO itinerary (destination, activity, accommodation, date)
                VALUES (?, ?, ?, ?)
            ''', (entry['Destination'], entry['Activity'], entry['Accommodation'], entry['Date']))
        self.conn.commit()
        messagebox.showinfo("Saved", "Itinerary saved to database successfully!")

    def load_from_database(self):
        self.cursor.execute('SELECT * FROM itinerary')
        rows = self.cursor.fetchall()
        if not rows:
            messagebox.showinfo("Database", "No entries found in the database.")
            return

        self.itinerary = []
        for row in rows:
            itinerary_entry = {
                "Destination": row[1],
                "Activity": row[2],
                "Accommodation": row[3],
                "Date": row[4]
            }
            self.itinerary.append(itinerary_entry)

        messagebox.showinfo("Loaded", "Itinerary loaded from database successfully!")

    def __del__(self):
        self.conn.close()

# ---------------- GUI ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ItineraryPlanner(root)
    root.mainloop()









