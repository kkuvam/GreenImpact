from fpdf import FPDF
from datetime import date
import os

class ReportGenerator:
    def __init__(self, save_path="output"):
        self.save_path = save_path
        os.makedirs(save_path, exist_ok=True)

    def generate(self, area, spacing, species, impact_data):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, "Forest Impact Report", ln=True, align='C')
        pdf.set_font("Arial", '', 12)
        pdf.ln(10)

        pdf.cell(0, 10, f"Date: {date.today()}", ln=True)
        pdf.cell(0, 10, f"Area Covered: {area} sqm", ln=True)
        pdf.cell(0, 10, f"Tree Spacing: {spacing} sqm/tree", ln=True)
        pdf.cell(0, 10, f"Tree Species: {species}", ln=True)
        pdf.ln(5)

        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Impact Summary:", ln=True)
        pdf.set_font("Arial", '', 12)
        pdf.cell(0, 10, f"Total Trees Planted: {impact_data['total_trees']}", ln=True)
        pdf.cell(0, 10, f"Annual CO2 Offset: {impact_data['annual_co2']} kg", ln=True)
        pdf.cell(0, 10, f"5-Year CO2 Offset: {impact_data['projections']['5_years']} kg", ln=True)
        pdf.cell(0, 10, f"10-Year CO2 Offset: {impact_data['projections']['10_years']} kg", ln=True)
        pdf.cell(0, 10, f"20-Year CO2 Offset: {impact_data['projections']['20_years']} kg", ln=True)

        file_name = f"Forest_Report_{date.today()}.pdf"
        full_path = os.path.join(self.save_path, file_name)
        pdf.output(full_path)
        return full_path
