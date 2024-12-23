from api.types.types import ProjectT

JS_PROJECTS: list[ProjectT] = [
    # To do list на Vue
    {
        "slug": "todo-list",
        "languages": ["javascript"],
        "taskType": 3,
        "difficulty": 3.5,
        "difficultyMetrics": {
            "javascript": 75,
            "logic": 75,
            "size": 65,
            "deploy": 60,
        },
        "title": "Todo list: мини-приложение на Vue",
        "description": "<p>Todo list — это программка, в которую записывают задачи:</p><ul><li>Это сделать сейчас</li>А это оставить на потом</ul><p>Чем крут todo list в плане разработке, так это техническими челленджами:</p><ul><li>Тут тебе и реактивное добавление / удаление данных</li><li>И фильтрация</li><li>И классные анимации!</li></ul><p>Зацени появление новых задач в туду-листе на картинке ниже.</p><h3>Но можно пойти ещё дальше!</h3><p>Разработать туду-лист — круто. Использовать в повседневной жизни свою собственную разработку как сервис — ещё круче.</p><p>Вот почему одно из усложнений — захостить Todo list, чтобы пользоваться им даже с телефона.</p>",
        "extraTasks": "<ol><li>Добавить возможность <b>перетаскивать</b> задачи мышкой: drag-n-drop</li>Задеплоить код на платформе для хостинга</ol>",
        "reward": {
            "description": "<ol><li>+2 уровня к логике</li><li>+2 уровня владения JS</li><li>+1 уровень выносливости на проектах</li><li>Навык деплоя и хостинга JavaScript / VueJS-проектов</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://codepen.io/saawsan/pen/jayzeq",
        "previewImage": "/img/js/projects/medium/todo-list.gif",
        "niche": "productivity",
        "isTeamProject": False,
        "category": "mini-apps",
        "subcategory": "",
    }
]