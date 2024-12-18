# Analysis-and-visualization-data
Улучшенное управление временными периодами

Основные улучшения:

1. В "data_download.py":
   - Добавлены необязательные параметры `start_date` и `end_date`
   - Реализована логика приоритета конкретных дат над стандартным периодом
   - Добавлена расширенная обработка ошибок при работе с датами
   - Проверка корректности введенных дат

2. В "main.py":
   - Добавлен новый интерактивный выбор периода
   - Возможность указать предустановленный период или ручной диапазон дат
   - Улучшена передача параметров в функцию `fetch_stock_data()`
   - Динамическое формирование имени файла графика и CSV в зависимости от выбранного периода

Рекомендации по использованию:
- При выборе предустановленного периода используйте стандартные обозначения Yahoo Finance ('1d', '5d', '1mo', '3mo' и т.д.)
- При ручном вводе дат используйте формат "ГГГГ-ММ-ДД"
- Система проверяет корректность введенных дат и периодов

Реализация управления временными периодами в проекте была выполнена с учетом нескольких ключевых аспектов:

1. Гибкость выбора периода
В функции `fetch_stock_data()` была создана логика, которая позволяет пользователю выбирать период двумя способами:
- Использовать стандартные периоды Yahoo Finance (1 день, 1 месяц, 3 месяца и т.д.)
- Указывать конкретные даты начала и окончания анализа

2. Приоритезация входных данных
Был реализован механизм приоритета:

 *if start_date and end_date:  
     Приоритет конкретных дат  
    data = stock.history(start=start, end=end)  
 else: 
     Используем стандартный период  
    data = stock.history(period=period)*

Это означает, что если пользователь указывает конкретные даты, они будут использоваться в первую очередь, перекрывая стандартный период.

3. Расширенная обработка ошибок
Добавлена многоуровневая проверка корректности данных:
- Преобразование строк в объекты datetime
- Проверка логики дат (начальная дата должна быть раньше конечной)
- Обработка возможных исключений при парсинге дат

4. Интерактивный выбор в "main()"
В основной функции создано меню с двумя вариантами:
- Предустановленный период
- Ручной выбор дат

5. Динамическое формирование названий
Название файлов графика и CSV теперь зависит от выбранного периода:

*if start_date and end_date:
    period = f"{start_date}_to_{end_date}"*

Технически это реализовано через:
- Модификацию сигнатуры функции `fetch_stock_data()`
- Добавление необязательных параметров `start_date` и `end_date`
- Использование библиотек `yfinance` и `pandas` для работы с датами

Преимущества подхода:
- Высокая гибкость
- Простота использования
- Надёжная обработка различных сценариев
- Интуитивный интерфейс для пользователя

Примеры использования:
1. Стандартный период: `fetch_stock_data('AAPL', period='1mo')`
2. Конкретный диапазон: `fetch_stock_data('AAPL', start_date='2023-01-01', end_date='2023-12-31')`

Это позволяет пользователю максимально гибко настраивать анализ данных об акциях.
Реализованный функционал делает программу более универсальной и удобной для пользователей.
Теперь они могут легко анализировать акции за любой интересующий их период - будь то стандартные интервалы или конкретный временной отрезок.
На рисунке 1 представлена визуализация результата работы программы в виде файла:  AAPL_2024-05-01_to_2024-12-10_stock_indicators_chart

![AAPL_2024-05-01_to_2024-12-10_stock_indicators_chart](https://github.com/user-attachments/assets/a807fb88-28bb-4425-9c93-08f46a02a660)

*Рисунок 1 AAPL_2024-05-01_to_2024-12-10_stock_indicators_chart*


На рисунке 2 представлена визуализация c использованием PyCharm для акции "AAPL"  период с 2024-05-01_по_2024-12-10

![Снимок экрана 2024-12-10-AAPL](https://github.com/user-attachments/assets/e0509864-6338-4951-bdc0-afe4fdce7956)

*Рисунок 2 Терминал PyCharm с визуализацией акции "AAPL" период с 2024-05-01_по_2024-12-10*
