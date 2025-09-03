# Dynamic-Pricing-Strategy-with-Market-Signals

# 🥤 Dynamic Pricing for Plant-Based Beverages

**Goal:** Apply data analytics + business reasoning to explore pricing strategy for plant-based beverages (oat milk, almond milk, kombucha, protein shakes).  
This mini case study shows how pricing, promotions, and competitors affect demand — and demonstrates technical + business storytelling.

---

## 📊 Week 1 Highlights

### Pricing Landscape
![Price vs Competitors](reports/figures/price_vs_competitors.png)

> **Insight:** Our price is consistently positioned between discounter and premium competitors, with weekend dips driven by promotions.

---

### Promotion Impact
![Promo Units](reports/figures/promo_units_bar.png)

> **Insight:** Promotions increase average units sold by ~XX%. Revenue impact depends on discount depth.

---

### Price Sensitivity
![Units vs Price](reports/figures/units_vs_price_scatter.png)

> **Insight:** Clear negative relationship between price and demand, especially strong for kombucha.

---

## 📂 Deliverables

- **Notebook:** [01_case_study_week1.ipynb](notebooks/01_case_study_week1.ipynb)  
- **Figures:** in [`reports/figures/`](reports/figures/)  
- **Tables:** in [`reports/tables/`](reports/tables/)  

---

## 🧑‍💻 How to Reproduce
# 1. Clone repo & cd into folder
git clone https://github.com/<your-username>/dynamic-pricing-beverages.git
cd dynamic-pricing-beverages

# 2. Create & activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
# .venv\Scripts\Activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Generate dataset
python src/make_data.py

# 5. Explore notebook
jupyter notebook notebooks/01_case_study_week1.ipynb
