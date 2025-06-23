import tkinter as tk
from tkinter import ttk, messagebox
from impact_logic import calculate_impact
from report_generator import ReportGenerator

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("GreenImpact Pro - Forest Report Generator")
        self.root.geometry("500x450")
        self.reporter = ReportGenerator()

        tk.Label(root, text="Area (in sqm):").grid(row=0, column=0, pady=5, padx=5, sticky="w")
        tk.Label(root, text="Tree spacing (sqm/tree):").grid(row=1, column=0, pady=5, padx=5, sticky="w")
        tk.Label(root, text="Tree species:").grid(row=2, column=0, pady=5, padx=5, sticky="w")

        self.area_entry = tk.Entry(root)
        self.spacing_entry = tk.Entry(root)
        self.species_entry = tk.Entry(root)

        self.area_entry.grid(row=0, column=1, padx=10)
        self.spacing_entry.grid(row=1, column=1, padx=10)
        self.species_entry.grid(row=2, column=1, padx=10)

        tk.Button(root, text="Calculate Impact", command=self.calculate).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Export PDF Report", command=self.export_pdf).grid(row=4, column=0, columnspan=2, pady=5)

        self.output_text = tk.Text(root, height=10, width=60)
        self.output_text.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
        self.impact_data = None

    def calculate(self):
        try:
            area = float(self.area_entry.get())
            spacing = float(self.spacing_entry.get())
            species = self.species_entry.get()
            self.impact_data = calculate_impact(area, spacing, species=species)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"Total Trees: {self.impact_data['total_trees']}\n")
            self.output_text.insert(tk.END, f"Annual CO2 Offset: {self.impact_data['annual_co2']} kg\n")
            self.output_text.insert(tk.END, f"5-Year: {self.impact_data['projections']['5_years']} kg\n")
            self.output_text.insert(tk.END, f"10-Year: {self.impact_data['projections']['10_years']} kg\n")
            self.output_text.insert(tk.END, f"20-Year: {self.impact_data['projections']['20_years']} kg\n")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric input.")

    def export_pdf(self):
        if not self.impact_data:
            messagebox.showerror("Error", "Please calculate impact first.")
            return
        area = float(self.area_entry.get())
        spacing = float(self.spacing_entry.get())
        species = self.species_entry.get()
        path = self.reporter.generate(area, spacing, species, self.impact_data)
        messagebox.showinfo("Success", f"PDF saved to: {path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
