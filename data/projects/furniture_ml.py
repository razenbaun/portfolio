PROJECT = {
    "slug": "furniture-ml",
    "title": "ML-система распознавания мебели",
    "short_description": (
        "Веб-приложение на Flask: детекция мебели через YOLOv5, классификация "
        "через CNN и Dense-сеть. Загрузка изображений, распознавание в реальном "
        "времени с веб-камеры, REST API для всех моделей."
    ),
    "image": "images/projects/furniture-ml/cover.png",

    "tagline": "Распознавание мебели на изображениях: YOLOv5 + CNN + Dense-сеть в едином Flask-приложении",
    "badges": ["Python", "Flask", "PyTorch", "TensorFlow", "OpenCV", "YOLOv5"],

    "links": {
        "github": "https://github.com/razenbaun/yolov5FlaskProject",
    },

    "problem": (
        "Мебельная индустрия генерирует огромные объёмы визуальных данных: "
        "фото товаров, интерьеры клиентов, контроль качества на производстве. "
        "Ручная разметка и классификация таких изображений медленны и дороги, "
        "а существующие ML-инструменты не учитывают специфику мебели — "
        "разнообразие форм, стилей и условий съёмки."
    ),
    "solution": (
        "Разработано веб-приложение, которое в реальном времени распознаёт "
        "мебель трёх способами: YOLOv5 для детекции объектов с bounding box, "
        "CNN для классификации категорий (стул, стол, диван, шкаф, плита) "
        "и Dense-сеть для быстрого прототипа по геометрическим признакам. "
        "Все модели доступны как через веб-интерфейс, так и через REST API."
    ),

    "features": [
        {"icon": "🎯", "title": "YOLOv5 — детекция объектов",
         "text": "Обводка мебели bounding box с метками класса и confidence. Accuracy 97%, F1 97%."},
        {"icon": "🧠", "title": "CNN-классификатор",
         "text": "Свёрточная сеть на TensorFlow/Keras для категоризации: accuracy 86%."},
        {"icon": "⚡", "title": "Dense-модель",
         "text": "Лёгкая сеть по геометрии изображения — быстрый прототип и сравнение подходов."},
        {"icon": "📷", "title": "Работа с камерой",
         "text": "Потоковая детекция через OpenCV: MJPEG-стрим прямо в браузере."},
        {"icon": "🌐", "title": "Веб-интерфейс",
         "text": "Отдельные страницы для каждой модели: загрузка файла, результат, визуализация."},
        {"icon": "🔌", "title": "REST API",
         "text": "Эндпоинты /api/upload, /api/cnn, /api/model_dense возвращают JSON — удобно тестировать в Postman."},
        {"icon": "🏷️", "title": "Разметка через Roboflow",
         "text": "Аннотирование ~1000+ изображений мебели, аугментация и подготовка датасета."},
        {"icon": "📊", "title": "Сравнение моделей",
         "text": "Confusion matrices, F1-confidence кривые, графики loss/accuracy по эпохам."},
    ],

    "code_snippet": {
        "lang": "python",
        "code": (
            "from flask import Blueprint, request, jsonify, url_for\n"
            "from tensorflow.keras.models import load_model\n"
            "from PIL import Image\n"
            "import numpy as np\n"
            "\n"
            "model_dense = Blueprint('model_dense', __name__)\n"
            "model = load_model('models/model_dense.keras')\n"
            "classes = [\"Chair\", \"furniture\", \"table\", \"sofa\", \"oven\"]\n"
            "\n"
            "@model_dense.route('/api/model_dense', methods=['POST'])\n"
            "def model_dense_predict():\n"
            "    file = request.files['file']\n"
            "    img = Image.open(file).convert(\"RGB\")\n"
            "    input_data = np.array([[img.width, img.height]]) / [640, 640]\n"
            "    label = classes[np.argmax(model.predict(input_data))]\n"
            "    return jsonify({\"label\": label})"
        ),
    },

    "architecture_image": "images/projects/furniture-ml/architecture.png",
    "architecture_note": (
        "Клиент (HTML) → Flask API → три модели: YOLOv5 (torch.hub), "
        "CNN (TensorFlow/Keras), Dense (Keras). OpenCV обрабатывает изображения "
        "и видеопоток, PIL — загрузку. Всё логируется через logging."
    ),

    "gallery": [
        {"src": "images/projects/furniture-ml/demo_yolov5.png",
         "caption": "YOLOv5: детекция дивана и кресла на фото интерьера"},
        {"src": "images/projects/furniture-ml/demo_cnn.png",
         "caption": "CNN: классификация загруженного изображения (класс table)"},
        {"src": "images/projects/furniture-ml/demo_dense.png",
         "caption": "Dense-модель: предсказание класса Chair"},
        {"src": "images/projects/furniture-ml/demo_camera.png",
         "caption": "Распознавание в реальном времени через веб-камеру"},
        {"src": "images/projects/furniture-ml/cm_yolov5.png",
         "caption": "Confusion matrix для YOLOv5: точность по классам ~1.00"},
        {"src": "images/projects/furniture-ml/cm_cnn.png",
         "caption": "Confusion matrix для CNN: видны смешения furniture ↔ sofa"},
        {"src": "images/projects/furniture-ml/f1_curve.png",
         "caption": "F1-confidence кривая: пик 0.97 при threshold 0.483"},
        {"src": "images/projects/furniture-ml/postman_api.png",
         "caption": "Тестирование API через Postman: ответ с image_url и label"},
    ],

    "benchmark_columns": ["Модель", "Accuracy", "Precision", "Recall", "F1-score"],
    "benchmarks": [
        {"cells": ["YOLOv5s", "97%", "95.9%", "98.2%", "97.0%"], "best": True},
        {"cells": ["CNN (3 conv-блока)", "86%", "87%", "86%", "86%"]},
        {"cells": ["Dense (2 скрытых слоя)", "37%", "15%", "37%", "21%"]},
    ],
    "benchmark_note": (
        "YOLOv5 уверенно побеждает за счёт предобученных весов на COCO и "
        "способности локализовать объекты. CNN показывает признаки переобучения "
        "после 15-й эпохи (лечится Dropout). Dense-сеть по геометрии предсказуемо "
        "слаба — её ценность в скорости, а не в точности; оставлена как baseline."
    ),

    "tech": ["Python 3", "Flask", "PyTorch", "TensorFlow / Keras",
             "OpenCV", "PIL", "NumPy", "Roboflow", "Postman"],

    "roadmap": [
        {"status": "done",    "text": "YOLOv5: обучение на кастомном датасете, accuracy 97%"},
        {"status": "done",    "text": "CNN + Dense: обучение и сравнение метрик"},
        {"status": "done",    "text": "Flask-приложение с 4 страницами и REST API"},
        {"status": "done",    "text": "Распознавание в реальном времени через веб-камеру"},
        {"status": "planned", "text": "Развёртывание на GPU-сервере (Render Free не подходит для TF/PyTorch)"},
        {"status": "planned", "text": "Расширение классов: освещение, декор, текстиль"},
        {"status": "planned", "text": "Интеграция с рекомендательной системой для интерьеров"},
    ],

    "sources": [
        {"label": "GitHub репозиторий", "url": "https://github.com/razenbaun/yolov5FlaskProject"},
        {"label": "YOLOv5 (Ultralytics)", "url": "https://github.com/ultralytics/yolov5"},
        {"label": "Roboflow — платформа разметки", "url": "https://roboflow.com"},
    ],
}
