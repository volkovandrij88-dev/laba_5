# Імпорт 5 різних бібліотек
import numpy as np
import pandas as pd
import requests
from faker import Faker
import pyfiglet
import matplotlib
from PIL import Image
import dateutil
import rich
import emoji



# 1. NumPy – базова операція над масивом
try:
    arr = np.array([1, 2, 3, 4])
    print("NumPy result:", arr * 10)
except Exception as e:
    print("NumPy error:", e)

# 2. Pandas – створення та вивід DataFrame
try:
    df = pd.DataFrame({
        "City": ["Kyiv", "Lviv", "Odesa"],
        "Population": [3_000_000, 720_000, 1_000_000]
    })
    print("\nPandas DataFrame:\n", df)
except Exception as e:
    print("Pandas error:", e)

# 3. Requests – отримання статусу HTTP
try:
    response = requests.get("https://example.com")
    print("\nRequests status code:", response.status_code)
except Exception as e:
    print("Requests error:", e)

# 4. Faker – генерація випадкових даних
try:
    fake = Faker()
    print("\nFake name:", fake.name())
except Exception as e:
    print("Faker error:", e)

# 5. pyfiglet – ASCII-арт
try:
    ascii_art = pyfiglet.figlet_format("Lab 5")
    print("\nPyFiglet ASCII-art:\n", ascii_art)
except Exception as e:
    print("PyFiglet error:", e)
