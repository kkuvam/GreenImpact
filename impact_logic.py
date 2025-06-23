import json

# Load CO2 rates from external JSON
with open("tree_data.json") as f:
    species_co2_rates = json.load(f)

def calculate_impact(area_sqm, spacing, age_years=3, species="Neem"):
    species_key = species.strip().lower()
    co2_per_tree = species_co2_rates.get(species_key, 20)  # default fallback
    total_trees = int(area_sqm / spacing)
    annual_co2 = total_trees * co2_per_tree

    projections = {
        "5_years": annual_co2 * 5,
        "10_years": annual_co2 * 10,
        "20_years": annual_co2 * 20
    }
    return {
        "total_trees": total_trees,
        "annual_co2": annual_co2,
        "projections": projections
    }
