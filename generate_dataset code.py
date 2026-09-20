import csv
import random
from datetime import datetime, timedelta

# ==========================================
# FESTIVAL DATES
# ==========================================

festival_dates = {

    # 2024
    "01-01-2024": "New Year",
    "15-01-2024": "Makar Sankranti",
    "26-01-2024": "Republic Day",
    "08-03-2024": "Maha Shivratri",
    "25-03-2024": "Holi",
    "09-04-2024": "Ugadi",
    "11-04-2024": "Eid-ul-Fitr",
    "17-04-2024": "Ram Navami",
    "21-04-2024": "Mahavir Jayanti",
    "23-05-2024": "Buddha Purnima",
    "17-06-2024": "Bakrid",
    "07-07-2024": "Rath Yatra",
    "19-08-2024": "Raksha Bandhan",
    "26-08-2024": "Janmashtami",
    "07-09-2024": "Ganesh Chaturthi",
    "16-09-2024": "Eid-e-Milad",
    "02-10-2024": "Gandhi Jayanti",
    "12-10-2024": "Dussehra",
    "31-10-2024": "Diwali",
    "15-11-2024": "Guru Nanak Jayanti",
    "25-12-2024": "Christmas",

    # 2025
    "01-01-2025": "New Year",
    "14-01-2025": "Makar Sankranti",
    "26-01-2025": "Republic Day",
    "26-02-2025": "Maha Shivratri",
    "14-03-2025": "Holi",
    "30-03-2025": "Ugadi",
    "31-03-2025": "Eid-ul-Fitr",
    "06-04-2025": "Ram Navami",
    "10-04-2025": "Mahavir Jayanti",
    "12-05-2025": "Buddha Purnima",
    "07-06-2025": "Bakrid",
    "27-07-2025": "Rath Yatra",
    "09-08-2025": "Raksha Bandhan",
    "16-08-2025": "Janmashtami",
    "27-08-2025": "Ganesh Chaturthi",
    "05-09-2025": "Eid-e-Milad",
    "02-10-2025": "Gandhi Jayanti & Dussehra",
    "20-10-2025": "Diwali",
    "05-11-2025": "Guru Nanak Jayanti",
    "25-12-2025": "Christmas"
}

# ==========================================
# HEADERS
# ==========================================

headers = [
    "Date",
    "Day_of_Week",
    "Weather",
    "Temperature",
    "Weekend",
    "Festival",
    "Festival_Name",
    "Holiday",
    "Previous_Day_Sales",
    "Meals_Prepared",
    "Meals_Sold",
    "Food_Wasted",
    "Revenue"
]

# ==========================================
# START DATE
# ==========================================

start_date = datetime(2024, 1, 1)

# ==========================================
# WEATHER
# ==========================================

weather_list = [
    "Sunny",
    "Cloudy",
    "Rainy"
]

# ==========================================
# INITIAL SALES
# ==========================================

previous_day_sales = 180

# ==========================================
# BASE DEMAND
# ==========================================

base_demand = 180

# ==========================================
# GENERATE DATA
# ==========================================

with open("restaurant_data.csv", "w", newline="") as file:

    writer = csv.writer(file)

    # Write CSV headers
    writer.writerow(headers)

    # Generate 730 days
    for i in range(730):

        # ==========================================
        # CURRENT DATE
        # ==========================================

        current_date = start_date + timedelta(days=i)

        date = current_date.strftime("%d-%m-%Y")

        # ==========================================
        # DAY
        # ==========================================

        day = current_date.strftime("%A")

        # ==========================================
        # WEATHER
        # ==========================================

        weather = random.choice(weather_list)

        # ==========================================
        # TEMPERATURE
        # ==========================================

        if weather == "Sunny":
            temperature = random.randint(30, 40)

        elif weather == "Cloudy":
            temperature = random.randint(24, 32)

        else:
            temperature = random.randint(18, 28)

        # ==========================================
        # WEEKEND
        # ==========================================

        if day in ["Saturday", "Sunday"]:
            weekend = "Yes"
        else:
            weekend = "No"

        # ==========================================
        # FESTIVAL
        # ==========================================

        if date in festival_dates:

            festival = "Yes"
            festival_name = festival_dates[date]

        else:

            festival = "No"
            festival_name = "None"

        # ==========================================
        # HOLIDAY
        # ==========================================

        if weekend == "Yes" or festival == "Yes":
            holiday = "Yes"
        else:
            holiday = "No"

        # ==========================================
        # SAVE PREVIOUS DAY SALES
        # ==========================================

        today_previous_day_sales = previous_day_sales

        # ==========================================
        # MEALS SOLD
        # ==========================================

        meals_sold = int(
            (0.7 * previous_day_sales) +
            (0.3 * base_demand)
        )

        # Weekend Effect
        if weekend == "Yes":
            meals_sold += random.randint(20, 40)

        # Festival Effect
        if festival == "Yes":
            meals_sold += random.randint(40, 70)

        # Rain Effect
        if weather == "Rainy":
            meals_sold -= random.randint(10, 25)

        # Daily Variation
        meals_sold += random.randint(-8, 8)

        # Minimum Sales
        if meals_sold < 50:
            meals_sold = 50

        # ==========================================
        # MEALS PREPARED
        # ==========================================

        extra_percentage = random.randint(5, 15)

        extra_meals = int(
            (extra_percentage / 100) * meals_sold
        )

        meals_prepared = meals_sold + extra_meals

        # ==========================================
        # FOOD WASTED
        # ==========================================

        food_wasted = meals_prepared - meals_sold

        # ==========================================
        # REVENUE
        # ==========================================

        price_per_meal = random.randint(180, 300)

        revenue = meals_sold * price_per_meal

        # ==========================================
        # WRITE DATA TO CSV
        # ==========================================

        writer.writerow([
            date,
            day,
            weather,
            temperature,
            weekend,
            festival,
            festival_name,
            holiday,
            today_previous_day_sales,
            meals_prepared,
            meals_sold,
            food_wasted,
            revenue
        ])

        # ==========================================
        # UPDATE SALES FOR NEXT DAY
        # ==========================================

        previous_day_sales = meals_sold

# ==========================================
# COMPLETION MESSAGE
# ==========================================

print("Dataset generated successfully!")
print("File: restaurant_data.csv")
print("Total records: 730")