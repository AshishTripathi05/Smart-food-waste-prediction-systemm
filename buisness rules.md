# Business Rules

## Purpose
These business rules simulate the daily operations of a restaurant. They are used to generate realistic historical data for training the machine learning model.

---

## 1. Base Sales

The restaurant normally sells between **150 and 180 meals per day** under normal conditions.

---

## 2. Weekend Rule

Customer demand increases on weekends.

- Saturday → Sales increase by **12%–18%**
- Sunday → Sales increase by **20%–28%**

Reason:
More people dine out on weekends.

---

## 3. Weather Rule

Weather affects customer visits.

- Sunny → Normal sales
- Cloudy → Sales increase by **3%–8%**
- Rainy → Sales decrease by **10%–20%**

Reason:
Rain reduces walk-in customers.

---

## 4. Festival Rule

During festivals, customer demand increases.

- Festival = Yes
- Sales increase by **25%–35%**

Reason:
Families and groups eat outside more often.

---

## 5. Holiday Rule

Public holidays increase restaurant visits.

- Holiday = Yes
- Sales increase by **10%–15%**

Reason:
People have free time and dine out.

---

## 6. Previous Day Sales Rule

Today's sales usually remain close to yesterday's sales.

Reason:
Restaurant demand changes gradually unless affected by weekends, weather, or festivals.

---

## 7. Meals Prepared Rule

The restaurant always prepares slightly more meals than the expected demand.

Formula:

Meals Prepared = Meals Sold + (5 to 15 meals)

Reason:
To avoid food shortage.

---

## 8. Food Waste Rule

Unsold meals become food waste.

Formula:

Food Wasted = Meals Prepared − Meals Sold

---

## 9. Revenue Rule

Average price of one meal = ₹200

Formula:

Revenue = Meals Sold × 200

---

## 10. Temperature Rule

Temperature follows realistic Indian weather conditions.

- Winter → 10°C–20°C
- Summer → 30°C–42°C
- Monsoon → 22°C–30°C

Reason:
Temperature indirectly affects customer demand.

---

## 11. Dataset Duration

The dataset contains **730 records**, representing **2 years** of daily restaurant operations.

One row = One day.

---

## 12. Target Variable

The machine learning model predicts:

Meals_Sold

All other columns are used as input features.