# report.py — як результат побачить людина: збираємо текст звіту.



def make_report(habit, times_per_week, week,year, month, affordable):
    """Повертає готовий текст звіту."""
    lines=[]
    lines.append(f'Звичка: {habit}, {times_per_week} раз(и) на тиджень')
    lines.append("-" * 40)
    lines.append(f'За тиждень: {week} грн')
    lines.append(f'За місяць:  {month} грн')
    lines.append(f'За рік:     {year} грн')
    lines.append('')

    if len(affordable) == 0:
        lines.append('Поки що грошей не вистачає на жодну мрію зі списку.')
    else:
        lines.append('За рік на ці гроші можна було б:')
        for dream in affordable:
            lines.append(f'+ {dream}')        
    # "\n".join склеює всі рядки в один текст, кожен з нового рядка
    return "\n".join(lines)

# times = 2
# habit = 'taxi'
# price = 100
# w = c.cost_per_week(price,times)
# y = c.cost_per_year(price,times)
# m = c.cost_per_month(price,times)
# #c.dreams_i_can_afford(dream, money)

# print(make_report(habit, times,w, y, m, ['dream 1', 'dream 2']))
