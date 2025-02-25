
# import streamlit as st
# # from forex_python.converter import CurrencyRates
# import pint
# import time
# import plotly.express as px
# import random

# st.set_page_config(page_title="Unit Converter", layout="centered")

# st.title("Unit Converter 🔄")
# st.markdown("### Created by Nabiya Faheem")

# categories = {
#     "Length": ["meters", "kilometers", "miles", "feet", "inches", "centimeters", "millimeters"],
#     "Weight": ["kilograms", "grams", "pounds", "ounces", "tonnes"],
#     "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
#     "Speed": ["meters per second", "kilometers per hour", "miles per hour"],
#     "Volume": ["liters", "milliliters", "gallons", "cups", "pints"],
#     "Area": ["square meters", "square feet", "square miles", "hectares", "acres"],
#     "Currency": ["USD", "EUR", "GBP", "PKR", "INR", "CAD", "AUD"],
#     "Time": ["seconds", "minutes", "hours", "days"],
#     "Data Storage": ["bytes", "kilobytes", "megabytes", "gigabytes", "terabytes"],
#     "Fuel Efficiency": ["miles per gallon", "liters per 100 km"]
# }

# fun_facts = {
#     "Length": ["A light-year is about 9.46 trillion kilometers!", "Mount Everest is 8,848 meters tall!"],
#     "Weight": ["The heaviest animal on Earth is the blue whale, weighing up to 200 tons!", "A grain of sand weighs around 0.004 grams!"],
#     "Temperature": ["The hottest recorded temperature on Earth was 56.7°C in Death Valley!", "Absolute zero is -273.15°C, where all molecular motion stops!"],
#     "Speed": ["The speed of light is approximately 299,792 kilometers per second!", "A cheetah can reach speeds up to 120 km/h!"],
#     "Volume": ["The Pacific Ocean holds over 710 million cubic kilometers of water!", "A single raindrop contains millions of water molecules!"],
#     "Area": ["Russia is the largest country in the world, covering over 17 million square kilometers!", "Vatican City is the smallest country in the world!"] ,
#     "Currency": ["The first paper money was used in China over 1,400 years ago!", "The most expensive currency is the Kuwaiti Dinar!"] ,
#     "Time": ["One year on Venus is shorter than one day on Venus!", "There are 31,536,000 seconds in a year!"] ,
#     "Data Storage": ["One gigabyte can store about 230 songs!", "A 1-terabyte hard drive can hold over 250,000 photos!"] ,
#     "Fuel Efficiency": ["The most fuel-efficient car in the world can travel over 500 miles on a gallon!", "Electric cars have much higher efficiency than gasoline cars!"]
# }

# def easter_egg(value):
#     if value == 42:
#         return "The answer to life, the universe, and everything!"
#     return ""

# category = st.radio("Choose a category", list(categories.keys()))

# col1, col3 = st.columns([3, 3])

# with col1:
#     amount = st.number_input("Enter value", value=1.0, step=0.1)
# with col3:
#     unit_from = st.selectbox("From", categories[category])
#     unit_to = st.selectbox("To", categories[category])

# c = CurrencyRates()
# ureg = pint.UnitRegistry()

# history = []
# favorites = []

# def convert_units(value, from_unit, to_unit, category):
#     with st.spinner("Converting..."):
#         time.sleep(1)  # Simulating a loading effect
        
#     if category == "Currency":
#         try:
#             result = c.convert(from_unit, to_unit, value)
#         except:
#             return "Error fetching rates"
#     elif category == "Temperature":
#         if from_unit == "Celsius":
#             result = value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
#         elif from_unit == "Fahrenheit":
#             result = (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
#         elif from_unit == "Kelvin":
#             result = value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32
#     else:
#         try:
#             result = (value * ureg(from_unit)).to(to_unit).magnitude
#         except:
#             return "Invalid Conversion"
    
#     history.append(f"{value} {from_unit} = {result} {to_unit}")
#     return result

# result = convert_units(amount, unit_from, unit_to, category)
# st.subheader(f"{amount} {unit_from} = {result} {unit_to}")

# if st.button("⭐ Add to Favorites"):
#     favorites.append(f"{amount} {unit_from} = {result} {unit_to}")

# st.sidebar.header("Conversion History")
# for entry in history[-5:]:
#     st.sidebar.write(entry)

# st.sidebar.header("Favorites ⭐")
# for fav in favorites:
#     st.sidebar.write(fav)

# if category in ["Currency", "Temperature"]:
#     st.subheader("Conversion Trends 📈")
#     data = {
#         "Time": ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"],
#         "Value": [result * (1 + i * 0.01) for i in range(5)]
#     }
#     fig = px.line(data, x="Time", y="Value", title=f"{unit_from} to {unit_to} Trends")
#     st.plotly_chart(fig)

# st.sidebar.header("Did You Know? 🎉")
# st.sidebar.write(random.choice(fun_facts.get(category, ["Here's an interesting fact for you!"])))

# st.sidebar.write(easter_egg(amount))

# st.sidebar.write("💡 Fun Fact changes dynamically when you switch categories!")

# # python -m streamlit run app.py

































import streamlit as st
import pint
import time
import plotly.express as px
import random

st.set_page_config(page_title="Unit Converter", layout="centered")

st.title("Unit Converter 🔄")
st.markdown("### Created by Nabiya Faheem")

categories = {
    "Length": ["meters", "kilometers", "miles", "feet", "inches", "centimeters", "millimeters"],
    "Weight": ["kilograms", "grams", "pounds", "ounces", "tonnes"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Speed": ["meters per second", "kilometers per hour", "miles per hour"],
    "Volume": ["liters", "milliliters", "gallons", "cups", "pints"],
    "Area": ["square meters", "square feet", "square miles", "hectares", "acres"],
    "Time": ["seconds", "minutes", "hours", "days"],
    "Data Storage": ["bytes", "kilobytes", "megabytes", "gigabytes", "terabytes"],
    "Fuel Efficiency": ["miles per gallon", "liters per 100 km"]
}

fun_facts = {
    "Length": ["A light-year is about 9.46 trillion kilometers!", "Mount Everest is 8,848 meters tall!"],
    "Weight": ["The heaviest animal on Earth is the blue whale, weighing up to 200 tons!", "A grain of sand weighs around 0.004 grams!"],
    "Temperature": ["The hottest recorded temperature on Earth was 56.7°C in Death Valley!", "Absolute zero is -273.15°C, where all molecular motion stops!"],
    "Speed": ["The speed of light is approximately 299,792 kilometers per second!", "A cheetah can reach speeds up to 120 km/h!"],
    "Volume": ["The Pacific Ocean holds over 710 million cubic kilometers of water!", "A single raindrop contains millions of water molecules!"],
    "Area": ["Russia is the largest country in the world, covering over 17 million square kilometers!", "Vatican City is the smallest country in the world!"] ,
    "Time": ["One year on Venus is shorter than one day on Venus!", "There are 31,536,000 seconds in a year!"] ,
    "Data Storage": ["One gigabyte can store about 230 songs!", "A 1-terabyte hard drive can hold over 250,000 photos!"] ,
    "Fuel Efficiency": ["The most fuel-efficient car in the world can travel over 500 miles on a gallon!", "Electric cars have much higher efficiency than gasoline cars!"]
}

def easter_egg(value):
    if value == 42:
        return "The answer to life, the universe, and everything!"
    return ""

category = st.radio("Choose a category", list(categories.keys()))

col1, col3 = st.columns([3, 3])

with col1:
    amount = st.number_input("Enter value", value=1.0, step=0.1)
with col3:
    unit_from = st.selectbox("From", categories[category])
    unit_to = st.selectbox("To", categories[category])

ureg = pint.UnitRegistry()

history = []
favorites = []

def convert_units(value, from_unit, to_unit, category):
    with st.spinner("Converting..."):
        time.sleep(1)  # Simulating a loading effect
    
    if category == "Temperature":
        if from_unit == "Celsius":
            result = value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
        elif from_unit == "Fahrenheit":
            result = (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            result = value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32
    else:
        try:
            result = (value * ureg(from_unit)).to(to_unit).magnitude
        except:
            return "Invalid Conversion"
    
    history.append(f"{value} {from_unit} = {result} {unit_to}")
    return result

result = convert_units(amount, unit_from, unit_to, category)
st.subheader(f"{amount} {unit_from} = {result} {unit_to}")

if st.button("⭐ Add to Favorites"):
    favorites.append(f"{amount} {unit_from} = {result} {unit_to}")

st.sidebar.header("Conversion History")
for entry in history[-5:]:
    st.sidebar.write(entry)

st.sidebar.header("Favorites ⭐")
for fav in favorites:
    st.sidebar.write(fav)

if category == "Temperature":
    st.subheader("Conversion Trends 📈")
    data = {
        "Time": ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"],
        "Value": [result * (1 + i * 0.01) for i in range(5)]
    }
    fig = px.line(data, x="Time", y="Value", title=f"{unit_from} to {unit_to} Trends")
    st.plotly_chart(fig)

st.sidebar.header("Did You Know? 🎉")
st.sidebar.write(random.choice(fun_facts.get(category, ["Here's an interesting fact for you!"])))

st.sidebar.write(easter_egg(amount))

st.sidebar.write("💡 Fun Fact changes dynamically when you switch categories!")

# python -m streamlit run app.py
