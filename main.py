# main.py — точка входу. Запуск з папки проєкту: python main.py
# main.py лише з'єднує частини: дані -> розрахунки -> звіт.

from app.data_loader import load_prices
from app.calculator import cost_per_year, cost_per_month, cost_per_week, dreams_i_can_afford
from app.report import make_report
from app.config import HABITS_FILE, DREAMS_FILE


def ask_number(question):
    """Питає число, доки людина не введе правильне."""
    while True:
        answer = input(question)
        try:
            return int(answer)
        except ValueError:
            print("Будь ласка, введіть ціле число, наприклад 5.")

def main():
    
    # 1. Читаємо дані. Якщо файлу немає — пояснюємо людською мовою.
    try:
        habits = load_prices(HABITS_FILE)
        dreams = load_prices(DREAMS_FILE)
    except FileNotFoundError:
        print('Не знайдено файлів у папці data. Перевірте, що вони на місці.')
        return

    # 2. Показуємо список звичок з номерами
    print("СКІЛЬКИ КОШТУЄ МОЯ ЗВИЧКА\n")
    names = list(habits)  #список ключей habits - ['кава з собою', 'таксі', 'доставка їжі', 'перекус у кафе', 'солодощі']
    for number, name in enumerate(names,start=1):
        print(f'{number}. {name} - {habits[name]} грн')       

    # 3. Питаємо, що обрала людина
    choice = ask_number('\nОберіть номер звички:')
    if choice < 1 or choice > len(names):
        print("Такого номера немає в списку.")
        return
    habit = names[choice-1] #обрали звичку
    price = habits[habit]
    times = ask_number('"Скільки разів на тиждень? "') #обрали кількість разів на тиждень
    
    # 4. Рахуємо
    year = cost_per_year(price, times)
    month = cost_per_month(price, times)
    week = cost_per_week(price, times)
    affordable = dreams_i_can_afford(dreams,year)

    # 5. Друкуємо звіт
    print()
    report = make_report(habit, times, week, year, month, affordable)
    print(report)
    

# Цей рядок запускає main(), лише коли ми запускаємо саме цей файл
if __name__ == "__main__":
    main()
  
