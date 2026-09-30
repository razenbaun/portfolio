PROJECT = {
    "slug": "campus-api",
    "title": "Campus Management API",
    "short_description": (
        "REST API для управления ИТ-инфраструктурой кампуса: аудитории, рабочие места, "
        "устройства и заявки на неисправности. FastAPI + Tortoise ORM + PostgreSQL, "
        "асинхронные запросы, bcrypt-аутентификация, автоматический Swagger."
    ),
    "image": "images/projects/campus-api/cover.png",

    "tagline": "Backend для учёта и обслуживания компьютерного парка университета",
    "badges": ["Python 3.9", "FastAPI", "Tortoise ORM", "PostgreSQL", "AsyncIO", "JWT-free auth"],

    "links": {
        "github": "https://github.com/razenbaun/API_v_1",
    },

    "problem": (
        "Учёт компьютерного парка в учебных заведениях часто ведётся в Excel или "
        "бумажных журналах. Когда устройство ломается, информация теряется между "
        "сотрудниками, а статус проблемы никто не отслеживает. Нужна система, "
        "которая привязывает каждое устройство к конкретному месту в аудитории, "
        "хранит историю заявок и автоматически синхронизирует статус."
    ),
    "solution": (
        "Спроектирована иерархия Campus → Classroom → Place → Device с "
        "привязкой заявок (Problem) к устройствам и пользователям. FastAPI "
        "предоставляет REST API, Tortoise ORM — асинхронную работу с PostgreSQL. "
        "Сигналы (post_save/post_delete) автоматически обновляют статус устройства "
        "при изменении его активных заявок."
    ),

    "features": [
        {"icon": "🏛️", "title": "6 связанных сущностей",
         "text": "Campus → Classroom → Place → Device → Problem, а также User. FK, reverse relations, каскадные удаления."},
        {"icon": "⚡", "title": "AsyncIO-стек",
         "text": "FastAPI + Tortoise ORM + asyncpg: неблокирующие запросы к Postgres."},
        {"icon": "🔐", "title": "Аутентификация",
         "text": "bcrypt-хеширование паролей, восстановление по email через SMTP + BackgroundTasks."},
        {"icon": "🧩", "title": "Signals и транзакции",
         "text": "post_save/post_delete на Problem автоматически синхронизируют статус Device. Удаление Place с устройствами — в одной транзакции."},
        {"icon": "✅", "title": "Валидация на уровне API",
         "text": "Уникальные координаты места в аудитории, проверка существования FK, unique login/email."},
        {"icon": "📚", "title": "Auto-Swagger",
         "text": "FastAPI автоматически генерирует OpenAPI-документацию: /docs и /redoc."},
        {"icon": "🧪", "title": "Pydantic-схемы",
         "text": "Разделение Create / Update / Response схем. Паттерны для полей (например, статус проблемы)."},
        {"icon": "📧", "title": "Уведомления по email",
         "text": "Отправка временного пароля через Gmail SMTP, асинхронно через BackgroundTasks."},
    ],

    "code_snippet": {
        "lang": "python",
        "code": (
            "from fastapi import APIRouter, HTTPException\n"
            "from app.models import Place, Device\n"
            "from tortoise.transactions import in_transaction\n"
            "\n"
            "router = APIRouter(prefix=\"/places\", tags=[\"Places\"])\n"
            "\n"
            "@router.delete(\"/{place_id}\")\n"
            "async def delete_place_with_devices(place_id: int):\n"
            "    async with in_transaction():\n"
            "        place = await Place.get_or_none(place_id=place_id)\n"
            "        if not place:\n"
            "            raise HTTPException(status_code=404, detail=\"Place not found\")\n"
            "\n"
            "        # Каскадно удаляем устройства места\n"
            "        await Device.filter(place_id=place_id).delete()\n"
            "        await place.delete()\n"
            "\n"
            "    return {\"message\": \"Place and all attached devices were deleted\"}"
        ),
    },

    "architecture_image": "images/projects/campus-api/architecture.png",
    "architecture_note": (
        "Клиент → FastAPI-роутеры (campus, classrooms, places, devices, users, problems) "
        "→ Tortoise ORM → PostgreSQL. Сигналы на Problem автоматически обновляют "
        "статус Device. BackgroundTasks отправляют email при восстановлении пароля."
    ),

    "gallery": [
        {"src": "images/projects/campus-api/swagger.png",
         "caption": "Swagger UI: все 6 групп эндпоинтов доступны через /docs"},
        {"src": "images/projects/campus-api/models_diagram.png",
         "caption": "ER-диаграмма: 6 сущностей со связями one-to-many"},
        {"src": "images/projects/campus-api/postman_auth.png",
         "caption": "Тестирование /users/auth в Postman"},
        {"src": "images/projects/campus-api/postman_problem.png",
         "caption": "Создание заявки на неисправность через /problems"},
        {"src": "images/projects/campus-api/postgres_tables.png",
         "caption": "Таблицы в pgAdmin после автогенерации Tortoise"},
        {"src": "images/projects/campus-api/email_password.jpg",
         "caption": "Письмо с временным паролем от /users/send-password"},
    ],

    "endpoints": [
        {"method": "GET",    "path": "/campus/",                          "desc": "Список всех кампусов"},
        {"method": "POST",   "path": "/campus/",                          "desc": "Создать кампус"},
        {"method": "GET",    "path": "/campus/{id}/classrooms",           "desc": "Аудитории кампуса"},
        {"method": "GET",    "path": "/classrooms/{id}/places",           "desc": "Места в аудитории"},
        {"method": "GET",    "path": "/classrooms/{id}/devices",          "desc": "Устройства в аудитории"},
        {"method": "POST",   "path": "/places/",                          "desc": "Создать место (проверка уникальности x,y)"},
        {"method": "DELETE", "path": "/places/{id}",                      "desc": "Удалить место со всеми устройствами (транзакция)"},
        {"method": "GET",    "path": "/devices/{id}",                     "desc": "Устройство с его заявками"},
        {"method": "POST",   "path": "/problems/",                        "desc": "Создать заявку на неисправность"},
        {"method": "POST",   "path": "/users/auth",                       "desc": "Аутентификация по логину и паролю"},
        {"method": "POST",   "path": "/users/send-password/{email}",      "desc": "Восстановление пароля по email"},
    ],
    "endpoints_note": (
        "Полная документация доступна в Swagger по адресу /docs после запуска. "
        "Все эндпоинты возвращают JSON и валидируются через Pydantic."
    ),

    "tech": ["Python 3.9", "FastAPI", "Tortoise ORM", "PostgreSQL", "asyncpg",
             "Pydantic", "passlib (bcrypt)", "Uvicorn", "python-dotenv", "SMTP (Gmail)"],

    "roadmap": [
        {"status": "done",    "text": "6 сущностей + CRUD + связанные выборки"},
        {"status": "done",    "text": "Signals: автосинхронизация статуса Device"},
        {"status": "done",    "text": "Транзакции при каскадных удалениях"},
        {"status": "done",    "text": "bcrypt-аутентификация и восстановление пароля по email"},
        {"status": "done",    "text": "Auto-Swagger и Pydantic-схемы"},
        {"status": "planned", "text": "JWT-токены вместо простой проверки сессии"},
        {"status": "planned", "text": "Роли и права доступа (admin / technician / user)"},
        {"status": "planned", "text": "Alembic-миграции вместо auto-generate"},
        {"status": "planned", "text": "Docker-compose для локального запуска"},
    ],

    "sources": [
        {"label": "GitHub репозиторий", "url": "https://github.com/razenbaun/API_v_1"},
        {"label": "FastAPI — документация", "url": "https://fastapi.tiangolo.com"},
        {"label": "Tortoise ORM — документация", "url": "https://tortoise.github.io"},
    ],
}
