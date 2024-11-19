from api.types.types import ProjectT

""" 
    Size: 1 - 5; theory, task, project, service, all (5)

"""

PROJECTS: list[ProjectT] = [
    {
        "name": "animated_underline",
        
        "language": "html_css",
        "size": 2,

        "isTeamProject": False, 
        "difficulty": 1,
        
        "category": "markup",
        "subcategory": "styling",

        "difficultyMetrics": {
            "html": 5,
            "css": 10,
            "animations": 40,     
            
            "new_code": 50,    
        },

        "title": "Красивое подчёркивание текста",
        "description": "На этот раз нам предстоит сделать красивое анимированное подчёркивание текста",
        
        "skillsToImprove": ["css", "animations", "new_code"],
        "reward": "+5 очков по владению CSS-анимациями",
        
        "link": "https://codepen.io/Kseso/pen/ApYVoW", 
        "previewImage": "/img/markup/animated_underline.gif",

        "otherLanguages": [],
    },
    
    {
        "name": "moving_cursor_menu",
        
        "language": "html_css",
        "size": 2,
        
        "category": "markup",
        "subcategory": "site_parts",
        
        "difficulty": 1,
        "isTeamProject": False, 

        "difficultyMetrics": {
            "html": 15,
            "css": 25,
            "logic": 60,         
        },

        "title": "Бегающий курсор за меню",
        "description": "Хитрая, чисто логичная задача на CSS",
        
        "skillsToImprove": ["html", "css", "logic"],
        "reward": "+10 очков по владению CSS-анимациями",
        
        "link": "https://codepen.io/Patak/details/QpLpOV", 
        "previewImage": "/img/markup/moving_cursor_menu.gif",

        "otherLanguages": [],
    },
    
    {
        "name": "bulma_css_library",
        
        "language": "html_css",
        "size": 1,
        
        "category": "markup",
        "subcategory": "library",
        
        "isTeamProject": False, 
        "difficulty": 2,

        "difficultyMetrics": {
            "html": 10,
            "css": 50,
            
            "logic": 35,         
            "new_code": 40,
        },

        "title": "Bulma: CSS-фреймворк",
        "description": "Цель этой задачи — разобраться с тем, как работает популярная библиотека Bulma",
        
        "skillsToImprove": ["html", "css", "logic"],
        "reward": "Тебе больше не придётся писать CSS: всю работу на себя возьмёт Bulma. \n +10 очков по владению CSS",
        
        "link": "https://bulma.io/", 
        "previewImage": "/img/markup/bulma.gif",

        "otherLanguages": [],
    },
    
     {
        "name": "web_studio_landing",
        
        "language": "html_css",
        "size": 3,
        
        "category": "markup",
        "subcategory": "website",

        "isTeamProject": True, 
        "difficulty": 2,

        "difficultyMetrics": {
            "html": 40,
            "css": 60,
            
            "logic": 25,         
        },

        "title": "Web Studio: твой первый лендинг",
        "description": "Тебе предстоит совершить прыжок в навыках и сделать вот такой простой сайт-лендинг. Здесь будет над чем подумать",
        
        "skillsToImprove": ["html", "css", "logic"],
        "reward": "Свой первый лендинг в копилочку!",
        
        "link": "https://www.figma.com/design/rKBKNUrq6jEPoVswEKFji5/Web-Studio-(Version-2.1)-(Copy)-(Copy)?node-id=0-1&node-type=canvas", 
        "previewImage": "/img/markup/web_studio_landing.gif",

        "otherLanguages": [],
    },
    
]