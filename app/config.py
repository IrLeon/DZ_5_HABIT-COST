 # config.py — налаштування: де лежать файли і сталі числа.
 
from pathlib import Path

# config.py лежить у папці app, тому корінь проєкту — на одну папку вище.
# Так програма знайде файли, звідки б її не запустили.
Base_Dir = Path(__file__).resolve().parent.parent

HABITS_FILE = Base_Dir/'data'/'habits.csv'
DREAMS_FILE = Base_Dir/'data'/'dreams.csv'

#52 тижні у році
WEEKS_IN_YEAR = 52

