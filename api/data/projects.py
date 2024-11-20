from api.types.types import ProjectT


PROJECTS: list[ProjectT] = [
    {
        "slug": "animated_underline",
        
        "language": "html_css",
        "size": 2,

        "isTeamProject": False, 
        "difficulty": 1,
        
        "category": "markup",
        "subcategory": "styling",

        "difficultyMetrics": {
            "css": 20,
            "cssAnimations": 40,     
            "newCode": 50,
            "logic": 30,         
        },

        "title": "Красивое подчёркивание текста",
        "description": "На этот раз нам предстоит сделать красивое анимированное подчёркивание текста",
        
        "reward": "+5 очков по владению CSS-анимациями",
        
        "link": "https://codepen.io/Kseso/pen/ApYVoW", 
        "previewImage": "/img/markup/animated-underline.gif",

        "otherLanguages": [],
    },
    
    {
        "slug": "moving_cursor_menu",
        
        "language": "html_css",
        "size": 2,
        
        "category": "markup",
        "subcategory": "site_parts",
        
        "difficulty": 1,
        "isTeamProject": False, 

        "difficultyMetrics": {
            "css": 25,
            "logic": 60,         
        },

        "title": "Бегающий курсор за меню",
        "description": "Хитрая, чисто логичная задача на CSS",
        
        "reward": "+10 очков по владению CSS-анимациями",
        
        "link": "https://codepen.io/Patak/details/QpLpOV", 
        "previewImage": "/img/markup/moving_cursor_menu.gif",

        "otherLanguages": [],
    },
    
    {
        "slug": "bulma_css_library",
        
        "language": "html_css",
        "size": 1,
        
        "category": "markup",
        "subcategory": "library",
        
        "isTeamProject": False, 
        "difficulty": 2,

        "difficultyMetrics": {
            "css": 50,
            
            "logic": 35,         
            "newCode": 40,
        },

        "title": "Bulma: CSS-фреймворк",
        "description": "Цель этой задачи — разобраться с тем, как работает популярная библиотека Bulma",
        
        "reward": "Тебе больше не придётся писать CSS: всю работу на себя возьмёт Bulma. \n +10 очков по владению CSS",
        
        "link": "https://bulma.io/", 
        "previewImage": "/img/markup/bulma.gif",

        "otherLanguages": [],
    },
    
    {
        "slug": "web_studio_landing",
        
        "language": "html_css",
        "size": 3,
        
        "category": "markup",
        "subcategory": "website",

        "isTeamProject": True, 
        "difficulty": 2,

        "difficultyMetrics": {
            "css": 60,
            
            "logic": 25,         
        },

        "title": "Web Studio: твой первый лендинг",
        "description": "Тебе предстоит совершить прыжок в навыках и сделать вот такой простой сайт-лендинг. Здесь будет над чем подумать",
        
        "reward": "Свой первый лендинг в копилочку!",
        
        "link": "https://www.figma.com/design/rKBKNUrq6jEPoVswEKFji5/Web-Studio-(Version-2.1)-(Copy)-(Copy)?node-id=0-1&node-type=canvas", 
        "previewImage": "/img/markup/web_studio_landing.gif",

        "otherLanguages": [],
    },
    {
        "slug": "dating_bot",
        
        "language": "python",
        "otherLanguages": ["php", "nodejs"],
        
        "size": 4,
        
        "niche": "dating",
        "category": "bots",
        "subcategory": "",

        "isTeamProject": True, 
        "difficulty": 4,

        "difficultyMetrics": {
            "python": 85,
            "logic": 80,         
            "deploy": 75,
            "automation": 75,
            "backend": 60,
        },

        "title": "Бот для знакомств (Украина + заграница)",
        "description": "Одно из древних, сокровенных и почти забытых желаний Дамира (и почти каждого холостяка) - найти девушку, которая станет спутницей жизни.\nТебе предстоит разработать сервис для знакомств и помочь Дамиру найти вторую половинку.\nОдиноким - найти друзей, желающим изучать языки - партнёра по языкам, а нелюбимым - заново поверить в любовь!",
        
        "reward": "Не каждый день тебя зовут стать частью большого сервиса для знакомств, которому не будет аналогов. Почему бы не взяться за это прямо сегодня?",
        
        "link": "./", 
        "previewImage": "/img/bots/dating.jpg",
    },
    {
        "slug": "sign_up_login_expand",
        
        "language": "javascript",
        "otherLanguages": ["python"],
        
        "size": 4,
        
        "niche": "education",
        "category": "websites",
        "subcategory": "user-management",

        "isTeamProject": True, 
        "difficulty": 3,

        "difficultyMetrics": {
            "javascript": 90,         
            "logic": 80,         
            "deploy": 40,
            "automation": 40,
            "python": 50,
            "backend": 50,
        },

        "title": "Монетизация EXPAND: логин и регистрация на сайте",
        "description": "Дамир снова просит твоей помощи: помоги ему сделать логин и регистрацию на сайте платформы, чтобы в будущем Дамир смог ",
        
        "reward": {
            "description": "Сделать логин и регистрацию на сайте - лишь первый шаг к тому, чтобы начать продавать контент на сайте EXPAND PLATFORM.\nТы можешь стать частью куда большой затеи. К тому же, не безвыгодной - для тебя в первую очередь!",
            "has_money_compensation": True,
        }
    
        
        "link": "./", 
        "previewImage": "/img/platform/expand-home.png",
    },
    
]