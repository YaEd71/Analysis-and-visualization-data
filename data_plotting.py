import matplotlib.pyplot as plt
import pandas as pd


def create_and_save_plot(data, ticker, period, filename=None, plot_type='all'):
    """
    Создает и сохраняет расширенные графики с техническими индикаторами

    :param data: DataFrame с данными об акциях
    :param ticker: Тикер акции
    :param period: Период данных
    :param filename: Имя файла для сохранения
    :param plot_type: Тип графика ('default', 'rsi', 'macd', 'all')
    """
    try:
        if data is None:
            print("Нет данных для построения графика.")
            return

        # Определение даты для оси X
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
        else:
            print("Информация о дате отсутствует.")
            return

        # Настройка количества субграфиков в зависимости от выбранного типа
        if plot_type == 'all':
            fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(15, 15),
                                                gridspec_kw={'height_ratios': [2, 1, 1]})
        elif plot_type in ['rsi', 'macd']:
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10),
                                           gridspec_kw={'height_ratios': [2, 1]})
        else:
            fig, ax1 = plt.subplots(figsize=(15, 6))

        # График цены акций
        ax1.plot(dates, data['Close'], label='Цена закрытия', color='blue', linewidth=2)
        ax1.plot(dates, data['Moving_Average'], label='Скользящее среднее', color='red', linestyle='--')
        ax1.set_title(f"{ticker} - Цена акций")
        ax1.set_ylabel("Цена")
        ax1.legend()
        ax1.grid(True, linestyle=':', alpha=0.7)

        # Графики технических индикаторов
        if 'RSI' in data.columns and (plot_type == 'rsi' or plot_type == 'all'):
            target_ax = ax2 if plot_type == 'all' else ax2
            target_ax.plot(dates, data['RSI'], label='RSI', color='green', linewidth=2)
            target_ax.axhline(y=70, color='r', linestyle='--', alpha=0.7)  # Верхняя граница перекупленности
            target_ax.axhline(y=30, color='g', linestyle='--', alpha=0.7)  # Нижняя граница перепроданности
            target_ax.set_title(f"{ticker} - RSI")
            target_ax.set_ylabel("RSI")
            target_ax.set_ylim(0, 100)
            target_ax.legend()
            target_ax.grid(True, linestyle=':', alpha=0.7)

        if 'MACD' in data.columns and (plot_type == 'macd' or plot_type == 'all'):
            target_ax = ax3 if plot_type == 'all' else ax2
            target_ax.plot(dates, data['MACD'], label='MACD', color='blue', linewidth=2)
            target_ax.plot(dates, data['Signal_Line'], label='Сигнальная линия', color='red', linestyle='--')
            target_ax.bar(dates, data['Histogram'], label='Гистограмма', color='gray', alpha=0.5)
            target_ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)  # Нулевая линия
            target_ax.set_title(f"{ticker} - MACD")
            target_ax.set_ylabel("MACD")
            target_ax.legend()
            target_ax.grid(True, linestyle=':', alpha=0.7)

        plt.tight_layout()

        # Сохранение графика
        if filename is None:
            filename = f"{ticker}_{period}_stock_indicators_chart.png"
        plt.savefig(filename, dpi=300)  # Высокое разрешение
        print(f"График сохранен как {filename}")

    except Exception as e:
        print(f"Ошибка при создании графика: {e}")