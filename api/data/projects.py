from api.types.types import ProjectT


PROJECTS: list[ProjectT] = [
    {
        "name": "animated_underline",
        
        "language": "HTML / CSS",
        "category": "markup",
        "subcategory": "styling",
        "task_type": "training",

        "difficulty": {
            "level": 1,
            
            "html": 5,
            "css": 10,
            "animations": 40,     
            
            "new_code": 50,    
        },

        "title": "Красивое подчёркивание текста",
        "description": "На этот раз нам предстоит сделать красивое анимированное подчёркивание текста",
        
        "skills_to_improve": ["css", "animations", "new_code"],
        "reward": "+5 очков по владению CSS-анимациями",

        
        "link": "https://codepen.io/Kseso/pen/ApYVoW", 
        "preview_image": "/img/markup/animated_underline.gif",

        "isTeamProject": False, 
        "other_languages": [],
    },
    
    {
        "name": "moving_cursor_menu",
        
        "language": "HTML / CSS",
        "category": "markup",
        "subcategory": "site_parts",
        "task_type": "training",

        "difficulty": {
            "level": 1,
            
            "html": 15,
            "css": 25,
            "logic": 60,         
        },

        "title": "Бегающий курсор за меню",
        "description": "Хитрая, чисто логичная задача на CSS",
        
        "skills_to_improve": ["html", "css", "logic"],
        "reward": "+10 очков по владению CSS-анимациями",
        
        "link": "https://codepen.io/Patak/details/QpLpOV", 
        "preview_image": "/img/markup/moving_cursor_menu.gif",

        "isTeamProject": False, 
        "other_languages": [],
    },
    
    {
        "name": "bulma_css_library",
        
        "language": "HTML / CSS",
        "category": "markup",
        "subcategory": "library",
        "task_type": "learning",

        "difficulty": {
            "level": 2,
            
            "html": 10,
            "css": 50,
            
            "logic": 35,         
            "new_code": 40,
        },

        "title": "Bulma: CSS-фреймворк",
        "description": "Цель этой задачи — разобраться с тем, как работает популярная библиотека Bulma",
        
        "skills_to_improve": ["html", "css", "logic"],
        "reward": "Тебе больше не придётся писать CSS: всю работу на себя возьмёт Bulma. \n +10 очков по владению CSS",
        
        "link": "https://bulma.io/", 
        "preview_image": "/img/markup/bulma.gif",

        "isTeamProject": False, 
        "other_languages": [],
    },
    
     {
        "name": "web_studio_landing",
        
        "language": "HTML / CSS",
        "category": "markup",
        "subcategory": "website",
        "task_type": "project",

        "difficulty": {
            "level": 2,
            
            "html": 40,
            "css": 60,
            
            "logic": 25,         
        },

        "title": "Web Studio: твой первый лендинг",
        "description": "Тебе предстоит совершить прыжок в навыках и сделать вот такой простой сайт-лендинг. Здесь будет над чем подумать",
        
        "skills_to_improve": ["html", "css", "logic"],
        "reward": "Свой первый лендинг в копилочку!",
        
        "link": "https://www.figma.com/design/rKBKNUrq6jEPoVswEKFji5/Web-Studio-(Version-2.1)-(Copy)-(Copy)?node-id=0-1&node-type=canvas", 
        "preview_image": "/img/markup/web_studio_landing.gif",

        "isTeamProject": True, 
        "other_languages": [],
    },
    
]