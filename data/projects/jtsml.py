PROJECT = {
    "slug": "jtsml",
    "title": "JTSML - библиотека прогнозирования временных рядов",
    "short_description": (
        "Расширяемая Java-библиотека: 7 моделей прогнозирования, "
        "AutoARIMA/AutoSARIMA по AICc, оптимизация гиперпараметров, "
        "визуализация и Fluent API. Опубликована в Maven Central."
    ),
    "image": "images/projects/jtsml/cover.png",

    "tagline": "Java-библиотека прогнозирования временных рядов «из коробки»",
    "badges": ["Java 11", "Maven Central", "JFreeChart",
               "Apache Commons Math", "Prophet-Adapter"],

    "links": {
        "github": "https://github.com/razenbaun/JTSML",
        "maven":  "https://central.sonatype.com/artifact/io.github.razenbaun/jtsml",
        "pom":    "io.github.razenbaun:jtsml:1.0.0",
    },

    "problem": (
        "На Python и R есть statsmodels, pmdarima, Prophet, forecast. "
        "На Java целостного решения нет: разработчику приходится либо писать "
        "ARIMA с нуля, либо вызывать внешние скрипты - это долго и неудобно."
    ),
    "solution": (
        "JTSML закрывает пробел: единый интерфейс TimeSeriesModel, автоподбор "
        "порядков по AICc, оптимизация гиперпараметров, визуализация и адаптер "
        "к Prophet - всё в одной Maven-зависимости."
    ),

    "features": [
        {"icon": "📈", "title": "7 моделей",
         "text": "Naïve, LinearTrend, ExponentialSmoothing, Holt, ARIMA, SARIMA, ARIMAX"},
        {"icon": "🤖", "title": "AutoARIMA / AutoSARIMA",
         "text": "Автоматический подбор (p,d,q)(P,D,Q,s) по критерию AICc"},
        {"icon": "⚙️", "title": "Оптимизация гиперпараметров",
         "text": "Grid search и Random search через ParameterSpace / ModelFactory"},
        {"icon": "📊", "title": "Визуализация",
         "text": "Графики прогнозов и коррелограммы ACF/PACF на JFreeChart"},
        {"icon": "🔌", "title": "Prophet-адаптер",
         "text": "Прозрачный вызов Python-скрипта через ProcessBuilder"},
        {"icon": "💾", "title": "Экспорт / импорт моделей",
         "text": "Java-сериализация: обучение один раз - прогнозы многократно"},
        {"icon": "🧩", "title": "Fluent API",
         "text": "Весь цикл анализа - от загрузки данных до графика - одной цепочкой вызовов"},
        {"icon": "🧪", "title": "Тесты",
         "text": "JUnit 5: покрытие ключевых моделей и оптимизатора"},
    ],

    "code_snippet": {
        "lang": "java",
        "code": (
            "List<Double> data = TimeSeriesDataLoader.loadFromCSV(\"passengers.csv\", 1);\n"
            "\n"
            "Jtsml.Forecast forecast = Jtsml.analyze()\n"
            "    .data(data)\n"
            "    .horizon(12)\n"
            "    .models(\"naive\", \"autoarima\", \"sarima\")\n"
            "    .withChart(true)\n"
            "    .chartTitle(\"Прогноз авиапассажиров\")\n"
            "    .predict();\n"
            "\n"
            "System.out.println(\"Лучшая модель: \" + forecast.getBestModel());\n"
            "System.out.println(\"MAE: \" + forecast.getBestError());"
        ),
    },

    "architecture_image": "images/projects/jtsml/architecture.png",
    "architecture_note": (
        "Пакеты: core (интерфейсы), models (реализации), optimization "
        "(гиперпараметры), visualization (JFreeChart), adapters (Prophet), "
        "export (сериализация), utils (загрузка CSV)."
    ),

    "gallery": [
        {"src": "images/projects/jtsml/correlogram_passengers.png",
         "caption": "Коррелограмма исходного ряда авиапассажиров"},
        {"src": "images/projects/jtsml/correlogram_passengers_diff.png",
         "caption": "Коррелограмма после первых разностей - ряд становится стационарным"},
        {"src": "images/projects/jtsml/forecast_passengers.png",
         "caption": "Сравнение SARIMA, AutoSARIMA и Prophet на ряде авиапассажиров"},
        {"src": "images/projects/jtsml/correlogram_births.png",
         "caption": "Коррелограмма ежедневного ряда рождений (1959)"},
        {"src": "images/projects/jtsml/forecast_births.png",
         "caption": "Сравнение моделей на ряде рождений - AutoSARIMA переобучается"},
        {"src": "images/projects/jtsml/idea_demo.png",
         "caption": "Запуск демо в IntelliJ IDEA: 4 датасета, вывод метрик в консоль"},
    ],

    "videos": [
        {
            "title": "Демонстрация работы JTSML",
            "youtube_id": "-dxDZmnsma0",
        },
    ],

    "benchmark_columns": ["Датасет", "Модель", "MAE", "sMAPE"],
    "benchmarks": [
        {"cells": ["Passengers (monthly)", "SARIMA(1,0,1)(1,0,1)₁₂", "21.9", "5.6%"], "best": True},
        {"cells": ["Passengers (monthly)", "AutoSARIMA", "461.7", "58.5%"]},
        {"cells": ["Passengers (monthly)", "Prophet", "52.9", "16%"]},
        {"cells": ["Births (daily)", "SARIMA(1,0,1)(1,0,1)₇", "5.4", "16%"], "best": True},
        {"cells": ["Births (daily)", "AutoSARIMA", "32.1", "54.5%"]},
        {"cells": ["Births (daily)", "Prophet", "8.3", "19%"]},
    ],
    "benchmark_note": (
        "AutoSARIMA проиграл ручной настройке на коротких зашумлённых рядах - "
        "классический пример переобучения при переборе по AICc."
    ),

    "tech": ["Java 11", "Maven", "Apache Commons Math 3.6.1",
             "JFreeChart 1.5.4", "JUnit 5", "Prophet (Python)", "Git"],

    "datasets": [
        {"name": "passengers.csv", "path": "files/datasets/passengers.csv",
         "description": "Месячный ряд авиапассажиров, 1949–1960 (144 точки, период 12)"},
        {"name": "births.csv", "path": "files/datasets/births.csv",
         "description": "Ежедневное число рождений за 1959 год (365 точек, период 7)"},
    ],

    "roadmap": [
        {"status": "done",    "text": "7 моделей + AutoARIMA / AutoSARIMA"},
        {"status": "done",    "text": "Оптимизация гиперпараметров (grid + random)"},
        {"status": "done",    "text": "Визуализация: графики прогнозов и коррелограммы"},
        {"status": "done",    "text": "Публикация в Maven Central"},
        {"status": "planned", "text": "Holt-Winters - сезонный ETS"},
        {"status": "planned", "text": "REST-обёртка для вызова прогнозов по сети"},
        {"status": "planned", "text": "Экспорт моделей в JSON (межъязыковой обмен)"},
    ],

    "sources": [
        {"label": "GitHub репозиторий", "url": "https://github.com/razenbaun/JTSML"},
        {"label": "Maven Central", "url": "https://central.sonatype.com/artifact/io.github.razenbaun/jtsml"},
        {"label": "Kaggle: school-student-daily-attendance",
         "url": "https://www.kaggle.com/datasets/sahirmaharajj/school-student-daily-attendance"},
    ],
}