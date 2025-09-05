<h1 align="center">🥤 Dynamic Pricing Case Study: Plant-Based Beverages</h1>

<p align="center">
  <i>Exploring how pricing, promotions, and competitors shape demand in the plant-based beverage market</i>
</p>

---

## 🌟 Overview  

This mini case study combines **data analytics** with **business insights** to explore pricing strategy across four categories:  
- Oat Milk  
- Almond Milk  
- Kombucha  
- Protein Shakes  

**Key themes:**  
- How do our prices compare to competitors (premium vs. discounter)?  
- What impact do promotions have on sales & revenue?  
- How sensitive is demand to price changes (elasticity)?  
- What-if: Does cutting prices *always* raise revenue?  

---

## 📊 Week 1 Results  

### 🏷️ Pricing Landscape
<p align="center">
  <img src="reports/figures/price_vs_competitors.png" width="600"/>
</p>  

> **Story:** Our pricing consistently sits between discounter (lower) and premium (higher) competitors. Promotions and weekend effects cause visible dips.  

---

### 🎉 Promotion Impact
<p align="center">
  <img src="reports/figures/promo_units_bar.png" width="400"/>
</p>  

> **Story:** Promotions boost unit sales by **~XX%**. However, revenue gains are not always guaranteed — the depth of discount matters.  

---

### 📉 Price Sensitivity
<p align="center">
  <img src="reports/figures/units_vs_price_scatter.png" width="500"/>
</p>  

> **Story:** As price rises, units sold decline — classic elasticity. Kombucha shows the steepest sensitivity, suggesting aggressive price cuts could backfire.  

---

## 🧾 Business Insights (Week 1)

- **Positioning:** We are cheaper than premium on 100% of days, but only undercut the discounter 0%.  
- **Promotions:** On average, promo days increase units sold by 10%. The trade-off in revenue needs careful balancing.  
- **Elasticity:** Kombucha demand is highly price sensitive (elasticity -1.16_), while almond milk is steadier (elasticity -1.24_).  
- **What-if Simulation:** A 5% price cut is projected to **(increase)** revenue almond milk (+0.9%) and kombucha (+0.5%), but hurts protein shakes (-0.9%) and oat milk (-0.9%)%.  

---

## 📂 Deliverables  

- **Notebook** → [01_case_study_week1.ipynb](notebooks/01_case_study_week1.ipynb)  
- **Figures** → [`reports/figures/`](reports/figures/)  
- **Tables** → [`reports/tables/`](reports/tables/)  

---

## ⚙️ How to Reproduce  

```bash
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

# 5. Explore case study
jupyter notebook notebooks/01_case_study_week1.ipynb


📊 Week 2 Results — Demand Modeling

This week, we move beyond descriptive analysis into predictive demand modeling. Using regression and simulated demand curves, we explored:

How demand responds to our own price changes

How promotions shift demand

How competitor pricing shapes outcomes

📈 Demand Curves
<p align="center"> <img src="reports/figures/week2_demand_curve.png" width="500"/> </p>

Story: As expected, demand falls as price rises. Among categories, almond milk and kombucha show steeper drops, signaling higher price sensitivity.

💰 Revenue Curves
<p align="center"> <img src="reports/figures/week2_revenue_curve_almond_milk.png" width="500"/> </p>

Story: Revenue initially rises with price (higher margin per unit) but eventually declines as volume falls. Protein shakes sustain revenue better at higher price points, while kombucha collapses fastest.

🎉 Promotion Effects
<p align="center"> <img src="reports/figures/week2_promo_effect_almond_milk.png" width="500"/> </p>

Story: Promotions shift demand upward across price levels, but not dramatically. For almond milk, promos lift demand modestly (~10%). For kombucha, promos have limited effect — price is the bigger driver.

⚔️ Competitor Sensitivity
<p align="center"> <img src="reports/figures/week2_competitor_sensitivity_almond_milk.png" width="500"/> </p>

Story: When the discounter raises price, our demand curve shifts up slightly — we “inherit” some of their lost customers. Premium competitor movements have weaker effects, suggesting our segment is closer to the discounter’s shoppers.

🧾 Business Insights (Week 2)

Elasticity Evidence:

Oat milk: Mildly sensitive (elasticity ≈ -0.59, not statistically strong).

Almond milk: Strongly price sensitive (elasticity ≈ -1.72, significant).

Kombucha: Elastic (≈ -1.82), unstable demand at higher prices.

Protein shakes: Elastic (≈ -2.10), promotions and discounts matter most.

Promotions: Lift unit sales by ~10%, but may not always increase revenue — especially for protein shakes, where discounts erode margin.

Competitor Effects: Discounter pricing shifts affect us more than premium pricing. We compete more directly with value-oriented shoppers.

📂 Deliverables

Figures: reports/figures/

Demand curves, revenue curves, promo effects, competitor sensitivity

Tables: reports/tables/

Regression coefficients and elasticity estimates


