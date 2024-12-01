from api.types.types import ProjectT

""" 
TODO: полностью подготовить ProjectPicker для студентов EXPAND


! Кирилл
? - fetch и API ✅
? - 2-3 задачки про API
? - корзина fetch, api + LS как усложнение (https://codepen.io/Dimasion/pen/oBoqBM)
? - Локалсторейдж + задачки (корзины 2 варианта)

! Ярослав
? - 2-3 задачки про API
? - Локалсторейдж + задачки (корзины 2 варианта)

! Максим Седюк


! Артём Лысюк

"""


PROJECTS: list[ProjectT] = [
    # underline animation css
    {
        "slug": "animated_underline",
        "languages": ["html_css"],
        "taskType": 2,
        "isTeamProject": False,
        "difficulty": 1,
        "niche": "webdev",
        "category": "markup",
        "subcategory": "animations",
        "difficultyMetrics": {
            "new": 50,
            "animations": 50,
            "logic": 30,
            "css": 20,
        },
        "title": "Анимированное подчёркивание текста",
        "description": "На этот раз нам предстоит сделать красивое анимированное подчёркивание текста.<br/>Хорошая тренировка для твоих навыков CSS + учимся разбираться в новом коде",
        "reward": {
            "description": "<ol><li>+10 очков владения CSS-анимациями 💅</li></ol>",
        },
        "link": "https://codepen.io/Kseso/pen/ApYVoW",
        "previewImage": "/img/html-css/animations/animated-underline.gif",
    },
    # moving cursor menu animation
    {
        "slug": "moving_cursor_menu",
        "languages": ["html_css"],
        "taskType": 2,
        "niche": "webdev",
        "category": "markup",
        "subcategory": "site_parts",
        "difficulty": 1,
        "isTeamProject": False,
        "difficultyMetrics": {
            "logic": 60,
            "css": 40,
            "new": 35,
        },
        "title": "Бегающее меню",
        "description": "Хитрая, и в то же время <b>чисто логичная</b> задача на CSS - сделать курсор, который будет преследовать меню. <br/>Без JavaScript",
        "reward": {
            "description": "<ol><li>+10 очков по владению CSS</li><li>+10 очков ко владению CSS-анимациями</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://codepen.io/Patak/details/QpLpOV",
        "previewImage": "/img/html-css/animations/moving_cursor_menu.gif",
    },
    # bulma css
    {
        "slug": "bulma_css_library",
        "languages": ["html_css"],
        "taskType": 1,
        "niche": "webdev",
        "category": "markup",
        "subcategory": "library",
        "isTeamProject": False,
        "difficulty": 2,
        "difficultyMetrics": {
            "new": 65,
            "css": 55,
            "logic": 30,
        },
        "title": "Bulma: CSS-фреймворк",
        "description": "Цель нашей тренировки — разобраться с тем, как работает популярная библиотека Bulma: <ul><li>1. Сначала нужно установить её.</li><li>2. Затем разобраться с тем, как она устроена и</li><li>3. После - освоить её документацию, чтобы найти полезные компоненты и CSS-классы</li></ul>",
        "reward": {
            "description": "<ol><li>Больше никаких CSS-классов: всю работу возьмёт на себя Bulma</li><li>+25 очков ко владению CSS</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://bulma.io/",
        "previewImage": "/img/html-css/libraries/bulma.gif",
    },
    # web studio landing
    {
        "slug": "web_studio_landing",
        "languages": ["html_css"],
        "taskType": 3,
        "niche": "webdev",
        "category": "markup",
        "subcategory": "website",
        "isTeamProject": True,
        "difficulty": 2,
        "difficultyMetrics": {
            "css": 60,
            "size": 60,
            "logic": 25,
        },
        "title": "Web Studio: твой первый лендинг!",
        "description": "Тебе предстоит совершить <b>прыжок в навыках</b> и сделать вот такой сайт-лендинг.<br/>Поверь: несмотря на кажущююся простоту здесь будет над чем подумать!",
        "reward": {
            "description": "<ol><li>Свой первый лендинг в копилочку!</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://www.figma.com/design/rKBKNUrq6jEPoVswEKFji5/Web-Studio-(Version-2.1)-(Copy)-(Copy)?node-id=0-1&node-type=canvas",
        "previewImage": "/img/html-css/landing/web_studio_landing.gif",
    },
    # dating bot
    {
        "slug": "dating_bot",
        "languages": ["python"],
        "taskType": 4,
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
        "description": "Одно из древних, сокровенных и почти забытых желаний Дамира (и почти каждого холостяка) - найти девушку, которая станет спутницей жизни.<br/>Тебе предстоит разработать сервис для знакомств и помочь Дамиру найти вторую половинку.<br/> Ладно, чего уж кривить душой: затея это с куда большим размахом:<ol><li>Одиноким - найти друзей</li><li>Желающим изучать языки - найти партнёров по языку</li><li>А нелюбимым - заново поверить в любовь и вернуть счастье в личную жизнь!</li></ol>",
        "reward": {
            "description": "Не каждый день тебя зовут стать частью <b>большого сервиса</b> для знакомств, которому не будет аналогов - в Украине так точно.<br/>Почему бы не взяться за такую масштабную затею прямо сегодня?",
            "has_money_compensation": False,
        },
        "link": "./",
        "previewImage": "/img/bots/dating.jpg",
    },
    # login / sign up expand
    {
        "slug": "sign_up_login_expand",
        "languages": ["javascript"],
        "taskType": 4,
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
        "description": "Дамир снова просит твоей помощи: помоги ему сделать логин и регистрацию на сайте платформы!<br/>В будущем Дамир хочет заняться продажей материалов и курсов прямо на сайте и логин/регистрация - лишь первый шаг к достижению цели!",
        "reward": {
            "description": "Сделать логин и регистрацию на сайте - лишь первый шаг к тому, чтобы начать продавать контент на сайте EXPAND PLATFORM.<br/> Но, логичный вопрос: при чём тут ты? Рассказываю: ты станешь частью куда большой затеи! К тому же, <b>не безвыгодной</b>. И в первую очередь - для тебя!",
            "has_money_compensation": True,
        },
        "link": "./",
        "previewImage": "/img/platform/expand-home.png",
    },
    # bootstrap css library
    {
        "slug": "bootstrap_css_library",
        "languages": ["html_css"],
        "taskType": 1,
        "niche": "",
        "category": "markup",
        "subcategory": "library",
        "isTeamProject": False,
        "difficulty": 2,
        "difficultyMetrics": {
            "new": 75,
            "css": 70,
            "logic": 35,
        },
        "title": "Bootstrap: CSS-фреймворк",
        "description": "Цель нашей тренировки — разобраться с тем, как работает популярная библиотека CSS-классов — Bootstrap: <ul><li>1. Сначала мы установим её в наш проект</li><li>2. Затем разберёмся, как она устроена изнутри</li><li>3. Освоим её документацию</li></ul><p>В результате мы найдём и выберем для себя полезные CSS-классы и готовые компоненты (части) сайтов, чтобы забыть о CSS-стилях раз и навсегда (ну, почти, хихи)</p>",
        "reward": {
            "description": "<ol><li>Больше никаких CSS-классов: всю работу возьмёт на себя Bootstrap</li><li>+35 очков ко владению CSS</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://getbootstrap.com/",
        "previewImage": "/img/html-css/libraries/bootstrap.gif",
    },
    # vue email autocomplete
    {
        "slug": "email_autocomplete",
        "languages": ["javascript"],
        "taskType": 2,
        "niche": "",
        "category": "markup",
        "subcategory": "forms",
        "isTeamProject": False,
        "difficulty": 1,
        "difficultyMetrics": {
            "vue": 35,
            "logic": 20,
            "javascript": 10,
        },
        "title": "Автокомплит имейла: задачка на Vue",
        "description": "Нам поручили написать поле, которое автоматически будет добавлять <i>@gmail.com</i> к имейлу, который придумывает себе пользователь. <p>Удобно, когда регистрируешь новый имейл, согласен?</p>",
        "reward": {
            "description": "<ol><li>+5 очков владения VueJS</li><li>Небольшая тренировочка. Почему нет?</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://www.notion.so/expnd/Email-autocomplete-978fae419e104f51a2a6a2e82f3520d2",
        "previewImage": "/img/vue/tasks/easy/email-autocomplete.gif",
    },
    # reactive form fields + component practice
    {
        "slug": "reactive_form_fields",
        "languages": ["javascript"],
        "taskType": 2,
        "niche": "",
        "category": "markup",
        "subcategory": "forms",
        "isTeamProject": False,
        "difficulty": 1,
        "difficultyMetrics": {
            "vue": 55,
            "logic": 40,
            "javascript": 15,
        },
        "title": "Реактивная форма: тренировка компонентов на Vue",
        "description": "Твоя задача следующая: <ol><li>Как только ты вводишь что-то в инпут</li><li>Это что-то тут же появляется на страничке — внизу, под формой</li></ol> <p>Это — достойная тренировка достойного VueJS-разработчика, который хочет освоить реактивность, компоненты и вечно бороздить моря JavaScript-разработки</p><p>Берёмся?</p>",
        "reward": {
            "description": "<ol><li>+10 очков владения VueJS</li><li>Небольшая тренировка твоих навыков. Почему бы и нет?</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://codepen.io/soufiane-khalfaoui-hassani/pen/LYpPWda",
        "previewImage": "/img/vue/tasks/easy/reactive-form-fields.gif",
    },
    # fetch + API (javascript or Vue)
    {
        "slug": "fetch_api",
        "languages": ["javascript"],
        "taskType": 1,
        "niche": "",
        "category": "technology",
        "subcategory": "API",
        "isTeamProject": False,
        "difficulty": 2,
        "difficultyMetrics": {
            "javascript": 65,
            "logic": 65,
        },
        "title": "Fetch: работа с запросами и API",
        "description": "Чтобы показать проект, который ты сейчас смотришь, браузеру понадобилось сделать следующее: <ol><li>Отправить запрос на API платформы EXPAND</li><li>Вытянуть из API базу данных проектов</li><li>Отфильтровать проект по твоему критерию</li><li>И только после — показать проект на сайте</li></ol><p>Это — дело рук fetch и API: важных инструментов для работы с запросами, без которых настоящий JavaScript-разработчик не представляет свою жизнь.</p><p>Освоим новый навык?</p>",
        "reward": {
            "description": "<ol><li>+25 очков владения JavaScript</li><li>Интересный ресёрч с обучающими материалами</li><li>Много нового и интересного (а кода по факту будет мало)</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://www.notion.so/expnd/Fetch-API-0712e49ed3ee4bff8be2e50937805d08",
        "previewImage": "/img/js/technologies/fetch-api.gif",
    },
    # лендинг твоей мечты: landing page html / css / tilda
    {
        "slug": "your_dream_landing_page",
        "languages": ["html_css"],
        "taskType": 3,
        "niche": "marketing",
        "category": "sales",
        "subcategory": "design",
        "isTeamProject": False,
        "difficulty": 1,
        "difficultyMetrics": {
            "marketing": 50,
            "design": 35,
            "website_builders": 35,
            "new": 35,
        },
        "title": "Лендинг твоей мечты!",
        "description": "Давно хотел сделать сайт для себя и для развития своего дела? Негоже такое откладывать! <p>На этом проекте мы научимся:</p><ol><li>Пользоваться конструктором сайтов Тильда</li><li>Узнаем о том, как создавать продающие сайты</li><li>Сделаем феерически красивый лендинг своими руками!</li></ol><p>И покажем всем клиентам, что мы способны не только хорошо делать свою работу, но и красиво преподать себя!</p><p>Займёмся маркетингом тебя любимого?</p>",
        "reward": {
            "description": "<ol><li>+10 очков владения веб-дизайном</li><li>+10 очков владения продажами!</li><li>Много нового и интересного</li></ol><p>И да, приятный бонус: на это проекте не нужно писать код!</p>",
            "has_money_compensation": False,
        },
        "link": "https://www.expandplatform.com/web/projects/tilda/",
        "previewImage": "/img/html-css/landing/your-dream-landing-page.png",
    },
    # Тильда + каталог своими руками
    {
        "slug": "tilda_catalogue",
        "languages": ["html_css"],
        "taskType": 3,
        "niche": "marketing",
        "category": "sales",
        "subcategory": "design",
        "isTeamProject": False,
        "difficulty": 1,
        "difficultyMetrics": {
            "marketing": 50,
            "design": 35,
            "website_builders": 35,
            "new": 35,
        },
        "title": "Каталог твоей мечты: изучаем Тильду!",
        "description": "Давно хотел сделать интернет-магазин для себя и для своего бизнеса? Негоже такое откладывать!<p>На этом проекте мы научимся:</p><ol><li>Пользоваться конструктором сайтов Тильда</li><li>Узнаем о том, как создавать продающие сайты</li><li>Сделаем феерически красивый каталог своими (по факту - твоими) руками!</li></ol><p>И покажем твоим клиентам, что ты способен не только хорошо продать себя, но и красиво оформить свой сайт!</p>",
        "reward": {
            "description": "<ol><li>+10 очков владения веб-дизайном</li><li>+10 очков владения продажами!</li><li>Много нового и интересного + <b>каталог в придачу!</b></li></ol><p>И да, приятный бонус: на это проекте мы отдыхаем от написания кода!</p>",
            "has_money_compensation": False,
        },
        "link": "https://www.expandplatform.com/web/projects/tilda/",
        "previewImage": "/img/tools/simple/tilda.png",
    },
    # Cinema visitors: посетители кинотеатра
    {
        "slug": "cinema_visitors",
        "languages": ["javascript", "php", "cpp", "c#"],
        "taskType": 2,
        "niche": "",
        "category": "logic",
        "subcategory": "",
        "isTeamProject": False,
        "difficulty": 1,
        "difficultyMetrics": {
            "logic": 55,
            "new": 30,
        },
        "title": "Важный посетитель кинотеатра",
        "description": "В кинотеатр твоего города стало ходить куда больше людей, нежели раньше! То ли отсутствие COVID-а повлияло, то ли Голливуд стали фильмы делать лучше... Кхм, нет, конечно дело в COVID-е.<p>Так вот, в чём проблема: раньше вахтёр знал всех клиентов в лицо и раз в месяц выдавал бесплатный билет самому активному киноману: <b>тому, кто ходил в кино чаще других</b></p><p>А теперь наш дражайший вахтёр в замешательстве! Поможешь ему отыскать среди базы данных того, кто ходит в кино чаще других?</p>С чего начать: <ol><li>Сохрани данные о 20 посетителях в массив: имя и число визитов</li><li>Пройдись циклом по массиву</li><li>И отыщи того самого-самого</li></ol>",
        "extraTasks": "<ul>Добавь ввод имён из терминала или из поля сайта (инпута)</ul><p>Ты будешь считывать имена и на основе данных массива вычислять, кто же в этом месяце наш топовый посетитель!</p>",
        "reward": {
            "description": "<ol><li>+10 очков владения выбранным языком программирования</li><li>+10 очков к логике!</li></ol>",
            "has_money_compensation": False,
        },
        "link": "#",
        "previewImage": "/img/logic/tasks/cinema_visitors.jpg",
    },
    # Jack Sparrow: Джек Воробей идёт на работу (резюме на HTML / CSS)
    {
        "slug": "jack_sparrow_cv",
        "languages": ["html_css"],
        "taskType": 2,
        "niche": "",
        "category": "logic",
        "subcategory": "",
        "isTeamProject": False,
        "difficulty": 1,
        "difficultyMetrics": {
            "new": 65,
            "html": 50,
            "css": 50,
            "logic": 40,
        },
        "title": "Джек Воробей идёт на работу: резюме на HTML / CSS",
        "description": "Мир изменился. Джек Воробей, заядлый пират и искатель приключений, вынужден идти на поклон к... Ост-Индской компании! <p>Там его встречает Барбосса, в прошлом — злейший конкурент Джека, и предлагает Джеку… работу!</p><p>Нашему капитану всё это чертовски не по душе, но что поделать — времена изменились, и, чтобы устроиться на работу, Джек <b>вынужден</b> подготовить резюме.</p> <p>Поможем Джеку?</p> ",
        "reward": {
            "description": "<ol><li>+20 очков владения HTML — языком разметки веб-страниц</li><li>+20 очков владения CSS — языком стилей веб-страниц</li><li>+10 очков к логике, без которой программисту ну никуда</li></ol><p>И, конечно же — первый проект в твою копилку навыков</p>",
            "has_money_compensation": False,
        },
        "link": "https://www.notion.so/expnd/HTML-CSS-e850ee249791417abda5ca8cc7573305",
        "previewImage": "/img/html-css/tasks/jack-sparrow-cv.gif",
    },
    # Stamina online: тренажёр слепой печати стамина онлайн
    {
        "slug": "blind_typing_stamina_online",
        "languages": ["html_css", "javascript", "python", "php", "cpp", "nodejs", "c#"],
        "taskType": 1,
        "niche": "",
        "category": "other",
        "subcategory": "",
        "isTeamProject": False,
        "difficulty": 1,
        "difficultyMetrics": {
            "new": 50,
            "logic": 15,
        },
        "title": "Stamina: слепая печать за 2 недели",
        "description": "Слепая печать — навык, без которого лично я не представляю свою жизнь. <p>Набирать текст и не смотреть на клавиатуру (прямо, как я и делаю сейчас) — обыденный процесс для программиста и любого, кто хочет перейти с компьютерами от «Вы» на «ты».</p>  <p>Мир изменился. Иди же вслед за ним нога в ногу и не отставай!</p>",
        "reward": {
            "description": "<ol><li>Навык, который останется с тобой на всю жизнь — <b>слепая печать</b></li><li>+15 очков владения собственным компьютером</li><li>+5 очков к логике</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://www.notion.so/expnd/Stamina-2-69fb7a581f82465e98e430c386fe512e",
        "previewImage": "/img/tools/simple/stamina.gif",
    },
    # Тайны VS Code
    {
        "slug": "vs_code_secrets",
        "languages": ["html_css", "javascript", "python", "php", "cpp", "nodejs", "c#"],
        "taskType": 1,
        "niche": "",
        "category": "other",
        "subcategory": "",
        "isTeamProject": False,
        "difficulty": 2,
        "difficultyMetrics": {
            "new": 60,
            "logic": 30,
        },
        "title": "Секреты VS Code",
        "description": "VS Code, она же Вижуал Студия — любимый инструмент сотен, тысяч, миллионов разработчиков по всему миру! <p>Покорить VS Code и освоить её секреты значит выйти на новый уровень комфорта при разработке.</p><p>Готов инвестировать силы в своё развитие как девелопера?</p> ",
        "reward": {
            "description": "<ol><li>Навык, который останется с тобой на всю жизнь — <b>работа с VS Code</b></li><li>+15 очков к логике</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://www.notion.so/expnd/VS-Code-Emmet-b1c77256772a4e379fc9c33270c63a39",
        "previewImage": "/img/tools/simple/vs_code.gif",
    },
    # Лендинг для барона: первый сайт-визитка своими руками
    {
        "slug": "landing_for_baron",
        "languages": ["html_css"],
        "taskType": 3,
        "niche": "",
        "category": "",
        "subcategory": "",
        "isTeamProject": False,
        "difficulty": 2,
        "difficultyMetrics": {
            "size": 80,
            "new": 75,
            "html": 70,
            "css": 70,
            "logic": 35,
        },
        "title": "Лендинг для пиратского барона: первый сайт своими руками",
        "description": "После того, как мы успешно трудоустроили капитана Джека Воробья в Ост-Индскую компанию, он рассказал о наших талантах своим коллегам-пиратам... И те тоже захотели сделать у нас заказ! <p>В том числе и один очень влиятельный пиратский Барон, гроза Восточных морей и владелец 13 кораблей-крушителей.</p><p>Его задание: сделать лендинг о пиратах, которые могут доставить путешественника к его заветным сокровищам.</p><p>Возьмёшься за столь неожиданное предложение Барона — или откажешься?</p><p>Учти, моряк: <i>такой</i> шанс выпадает только один раз в жизни!</p>",
        "reward": {
            "description": "<ol><li>+30 очков владения HTML и CSS</li><li>+15 очков логики</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://www.notion.so/expnd/baca1bb3b01744759f3b9df5fa60f127",
        "previewImage": "/img/html-css/landing-for-baron.png",
    },
    # Терминал: возможности компьютера в одной строке
    {
        "slug": "terminal_vs_code",
        "languages": ["html_css", "cpp", "c#", "php"],
        "taskType": 1,
        "niche": "",
        "category": "",
        "subcategory": "",
        "isTeamProject": False,
        "difficulty": 1,
        "difficultyMetrics": {
            "new": 40,
            "logic": 15,
        },
        "title": "Терминал: возможности компьютера в одной строке",
        "description": "Ещё один инструмент в твою копилку как будущего хакера — терминал.<p>Дают 100%: ты видел фильмы, где показано, как программисты ломают Пентагон и взламывают сервера своих недоброжелателей... И делают они это как раз через терминал!</p><p>В будущем терминал пригодится нам, чтобы работать с Python, VueJS, C++, так что откладывать столь важную тему не стоит — тем более, она вовсе не сложная</p>",
        "reward": {
            "description": "<ol><li>Новый инструмент в арсенале — терминал</li></ol><p><b>Приятный бонус:</b> это тема, в которой не нужно писать код!</p>",
            "has_money_compensation": False,
        },
        "link": "https://www.notion.so/expnd/2b337b48d5c1488b96f1b4a71839cef2",
        "previewImage": "/img/tools/simple/terminal.gif",
    },
    # Калькулятор для тёти Ларисы на чистом JavaScript
    {
        "slug": "calculator-aunt-larisa",
        "languages": ["javascript"],
        "taskType": 3,
        "difficulty": 3,
        "difficultyMetrics": {
            "new": 70,
            "javascript": 65,
            "html_css": 60,
            "logic": 60,
        },
        "title": "Калькулятор для тёти Ларисы на чистом JavaScript",
        "description": "<p>На этом проекте нас предстоит написать настоящий калькулятор. </p><p>Сделать работу нужно в сроки, ведь просит нас об этом не абы кто, а сама тётя Лариса — наша подружка из продуктового магазина за углом!</p><p>Прелесть проекта в том, что здесь будет мало вёрстки и много JavaScript'а.</p><p>Для тех, кто жаждет выучить JavaScript и стать Junior разработчиком, этот проект — is a must!</p> ",
        "reward": {
            "description": "<ol><li>+20 очков владения JavaScript</li><li>Интересный проект, от которого на душе остаётся приятное послевкусие!</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://www.notion.so/expnd/fb98f45ef2ae4ec594da4bce0603db69",
        "previewImage": "/img/js/projects/calculator.gif",
        "isTeamProject": False,
        "niche": "",
        "category": "",
        "subcategory": "",
    },
    # Codewars: тренировка навыков на любом языке
    {
        "slug": "codewars-practice",
        "languages": ["javascript", "python", "php", "cpp", "nodejs", "c#"],
        "taskType": 2,
        "difficulty": 2,
        "difficultyMetrics": {
            "logic": 75,
            "language": 60,
            "size": 30,
        },
        "title": "Codewars: тхеквондо навыков на любимом языке",
        "description": "Мы пришли на Codewars, чтобы тренировать навыки — и мы получим их любой ценой! <p>Codewars — известнейшая площадка для тренировок навыков на любом языке программирования</p> <p>Создай аккаунт, выбери первую задачу — и мы выступаем!</p>",
        "reward": {
            "description": "<ol><li>+15 очков владения выбранным языком</li><li>Интересный опыт от прохождения нетипичных задач!</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://www.codewars.com/",
        "previewImage": "/img/logic/tasks/codewars.gif",
        "isTeamProject": False,
        "niche": "",
        "category": "",
        "subcategory": "",
    },
    # Codewars: тренировка функций
    {
        "slug": "functions_codewars",
        "languages": ["javascript", "python", "php", "cpp", "nodejs", "c#"],
        "taskType": 2,
        "difficulty": 2,
        "difficultyMetrics": {
            "logic": 75,
            "language": 60,
            "size": 30,
        },
        "title": "Тренировка функций на Codewars",
        "description": "Мы пришли на Codewars, чтобы тренировать навыки — и мы получим их любой ценой! <p>Codewars — известнейшая площадка для тренировок навыков на любом языке программирования</p> <p>Создай аккаунт, выбери первую задачу — и мы выступаем!</p>",
        "reward": {
            "description": "<ol><li>+15 очков владения выбранным языком</li><li>Интересный опыт от прохождения нетипичных задач!</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://www.codewars.com/",
        "previewImage": "/img/logic/tasks/codewars.gif",
        "isTeamProject": False,
        "niche": "",
        "category": "",
        "subcategory": "",
    },
    # VueJS: введение. 25 туториалов для изучения Vue
    {
        "slug": "vue-basics-tutorials",
        "languages": ["javascript"],
        "taskType": 1,
        "difficulty": 3,
        "difficultyMetrics": {
            "logic": 80,
            "javascript": 65,
            "language": 60,
            "size": 55,
        },
        "title": "Знакомимся с VueJS: введение и 25 туториалов для освоения Vue",
        "description": "На чистом JavaScript можно написать что-угодно: <ul><li>Музыкальный плеер (Spotify, YouTube Music)</li><li>Мессенджер (Telegram, Viber, WhatsApp)</li><li>Игру или целую платформу: Flexbox Froggy, Codewars, Notion</li></ul> <p>JavaScript поистине всемогущ, а VueJS делает его сверхбожеством с 10 руками, с острыми как бритва клинками. </p><p>Vue — серьёзное оружение в руках тех, кто готов его освоить и сделать своим.</p> <p>Как думаешь: пришло время перейти из чистого JS на Vue?</p>",
        "reward": {
            "description": "<ol>Новый инструмент, который останется с тобой на всю жизнь — VueJS<li>+30 очков владения VueJS</li><li>+30 очков владения JavaScript</li> <li>Неимоверно сложная и интересная теория</li></ol><p>Чуть не забыл сказать: если освоишь тему <i>сам</i>, можешь считать себя настоящим JavaScript-разработчиком</p>",
            "has_money_compensation": False,
        },
        "link": "https://www.expandplatform.com/web/lessons/vue/1-tutorials/",
        "previewImage": "/img/vue/lessons/vue-intro.gif",
        "isTeamProject": False,
        "niche": "",
        "category": "",
        "subcategory": "",
    },
    # Калькулятор цен (как на Экспанде)
    {
        "slug": "price-calculator",
        "languages": ["javascript"],
        "taskType": 3,
        "difficulty": 3,
        "difficultyMetrics": {
            "logic": 75,
            "javascript": 70,
            "new": 50,
            "size": 40,
        },
        "title": "Калькулятор цен, как на EXPAND",
        "description": "На этот раз Дамир поручает тебе нелёгкую задачу: написать калькулятор цен для его курсов. Ниже, на фотке, ты увидишь прототип того, что нужно сделать. <p>В идеале — переплюнуть его и сделать лучше!</p><p>К примеру, дописать к нему рекомендательную систему на основе выбранного тарифа или перевод на разные языки.</p><p>По факту калькулятор может быть любой, ну, скажем — твоего времени как разработчика. Да ещё и в долларах. Что купишь, то и приготовим.</p><p>Ну так как: возьмёшься за создание онлайн-калькулятора?</p> ",
        "reward": {
            "description": "<ol><li>Научишься создавать реактивные мини-приложения на Vue (навык, который — поверь — никогда не будет лишним)</li><li>+30 очков владения VueJS</li><li>+30 очков владения JavaScript</li><li>Нетипичная, интересная практика</li></ol><p><i>Как бонус:</i> после темы ты сможешь считать себя настоящим JavaScript-разработчиком — без вариантов!</p>",
            "has_money_compensation": False,
        },
        "link": "https://www.expandplatform.com/students/plan-picker/",
        "previewImage": "/img/js/projects/web-calculator.gif",
        "isTeamProject": True,
        "niche": "finance",
        "category": "mini-app",
        "subcategory": "calculators",
    },
    # Добавляем перевод в мини-приложение
    {
        "slug": "mini-app-translation",
        "languages": ["javascript"],
        "taskType": 3,
        "difficulty": 2,
        "difficultyMetrics": {
            "logic": 65,
            "javascript": 60,
            "new": 40,
        },
        "title": "Перевод на разные языки в мини-приложении",
        "description": "<p>Звучит как задача на фрилансе, правда?</p><p>В чём-то оно так и есть, ведь нам предстоит добавить перевод на три языка: русский, украинский и английский в выбранное (или сделанное) тобой приложение: веб-плеер, калькулятор, на сайт... You name it</p><p>Тебе предстоит чисто логичная задача на JavaScript и TypeScript. Всё верно: как раз научишься им пользоваться!</p><p>Если бы это была задача на фрилансе, тебе бы ещё и золотых немного отсыпали. Неплохой идеей после проекта будет зайти на какой-нибудь Upwork и разузнать, сколько же платят за такую задачу...</p>",
        "reward": {
            "description": "<ol><li>Научишься улучшать реактивные mini-apps на VueJS и работать с TypeScript (навык, который никогда не будет лишним)</li><li>+20 очков владения VueJS</li><li>+15 очков владения JavaScript и TypeScript</li><li>Интересная задача, применимая на практике</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://www.expandplatform.com/developer/services/password-generator/",
        "previewImage": "/img/js/tasks/translation.gif",
        "isTeamProject": False,
        "niche": "security",
        "category": "mini-app",
        "subcategory": "generators",
    },
    # Веб-плеер на Vue
    {
        "slug": "web-player-vue",
        "languages": ["javascript"],
        "taskType": 3,
        "difficulty": 2,
        "difficultyMetrics": {
            "logic": 65,
            "javascript": 55,
            "size": 45,
            "new": 35,
        },
        "title": "Веб-плеер на Vue (+TypeScript)",
        "description": "<p>Звучит как челлендж, правда: с нуля создать плеер на Vue, да ещё и с использованием TypeScript!</p><p>Но, если разобраться, бояться на самом деле нечего: </p><ul><li>UI-ка здесь не такая уж и сложная (сам посмотри)</li><li>Ключевая задача здесь — логика. Но мы-то с тобой воробьи уже стрелянные и не с таким сталкивались, верно?</li></ul><p>Выходит, нужно заранее продумать логику, сделать UI и привязать JS (Vue) к вёрстке.</p><p>Предлагаю не откладывать столь интересный проект в тёмный и длинный ящик</p>",
        "extraTasks": "<ol><li>Добавить типы — TypeScript — в наш код</li><li>Найти API, из которого мы будем подгружать треки (супер-дополнение)</li></ol>",
        "reward": {
            "description": "<ol><li>+20 к разработке реактивных mini-apps на VueJS / TypeScript</li><li>+20 очков владения VueJS</li><li>+15 очков владения JavaScript / TypeScript</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://codepen.io/alexdevero/pen/aZjLNw",
        "previewImage": "/img/vue/projects/web-player-vue.png",
        "isTeamProject": True,
        "niche": "media",
        "category": "mini-app",
        "subcategory": "players",
    },
    # Поле с автокомплитом
    {
        "slug": "search-field-autocomplete",
        "languages": ["javascript"],
        "taskType": 2,
        "difficulty": 2,
        "difficultyMetrics": {
            "logic": 65,
            "javascript": 55,
        },
        "title": "Поле с автокомплитом (JS/TS на выбор)",
        "description": "<p>Поиск должен быть удобным — именно так решили Сергей Брин и Ларри Пейдж в далёком 1998 году... И изобрели Google: компанию, которая сегодня стоит 2 триллиона долларов (2 и 12 нолей)</p><p>Конечно, новый Google изобретать ни к чему: нам предстоит всего лишь разработать поле с удобным поиском, как на картинке ниже.</p>",
        "extraTasks": "<ul><li>Дополнить свой код типами — подключить и использовать TypeScript</li></ul>",
        "reward": {
            "description": "<ol><li>+10 очков владения VueJS</li><li>+10 очков владения TypeScript</li><li>+10 очков владения JavaScript</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://www.naiveui.com/en-US/light/components/auto-complete",
        "previewImage": "/img/vue/tasks/input-autocomplete.gif",
        "isTeamProject": False,
        "niche": "",
        "category": "",
        "subcategory": "",
    },
    # Счётчик слов и знаков: классическая задача на JavaScript
    {
        "slug": "word-character-counter",
        "languages": ["javascript", "python", "php", "cpp", "nodejs", "c#"],
        "taskType": 2,
        "difficulty": 2,
        "difficultyMetrics": {
            "logic": 55,
            "language": 45,
        },
        "title": "Счётчик слов и знаков",
        "description": "<p>Классическая задача на любом языке программирования — создать штуку, которая будет считать слова и знаки.</p><p>Эта задача не нуждается в прелюдиях: просто возьми и сделай её</p>",
        "reward": {
            "description": "<ol><li>+1 level по выбранному языку</li><li>+10 очков владения выбранным языком</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://wordcounter.net/",
        "previewImage": "/img/logic/tasks/word-counter.gif",
        "isTeamProject": False,
        "niche": "",
        "category": "",
        "subcategory": "",
    },
    # 2D-платформер на игровом движке
    {
        "slug": "2d-platformer",
        "languages": ["python", "php", "cpp", "nodejs", "c#"],
        "taskType": 3,
        "difficulty": 3,
        "difficultyMetrics": {
            "new": 85,
            "size": 80,
            "language": 70,
            "logic": 65,
            "design": 40,
        },
        "title": "2D-платформер на игровом движке",
        "description": "<p>Мечтал сделать 2D-игру? Твоя мечта вот-вот может начать ходить, прыгать, собирать монетки... И конечно же встретить злейших врагов!</p><p>На этом проекте мы сделаем 2D-платформер, аналогичный Hollow Knight, Super Meat Boy и другим культовым инди-играм.</p><p>И да: <b>движок для игры выбираешь ты сам!</b></p>",
        "reward": {
            "description": "<ol><li>+3 уровня в Gamedev-разработке</li><li>+30 очков владения выбранным игровым движком</li><li>+20 очков владения выбранным языком (если движок предусматривает работу с языком)</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://www.construct.net/en/make-games/showcase",
        "previewImage": "/img/engines/games/2d-platformer.gif",
        "isTeamProject": True,
        "niche": "gamedev",
        "category": "2D-platformers",
        "subcategory": "arcade",
    },
    # 2D-платформер на движке Construct 3
    {
        "slug": "2d-platformer-construct-3",
        "languages": ["javascript"],
        "taskType": 3,
        "difficulty": 3,
        "difficultyMetrics": {
            "new": 75,
            "size": 70,
            "logic": 60,
            "design": 40,
            "javascript": 40,
        },
        "title": "2D-платформер на движке Construct 3 (платная версия)",
        "description": "<p>Хочешь, я оплачу для пару-тройку месяцев платной версии Construct 3, чтобы ты сделал свой небольшой 2D-платформер в стиле Hollow Knight и других культовых инди-игр?</p><h4>Что интересного нас ждёт на проекте?</h4><ol><li>Нам предстоит самим придумать сюжет и главного героя</li><li>Предстоит придумать мир и разработать под него дизайн</li><li>Продумать игровую механику и логику</li></ol><p>И это не говоря о дизайне самой игры!</p> <p>В общем, работы нас ждёт вагон и маленькая тележка, которая едёт в след за... О, вагонный 2D-платформер. Чем не игра?</p>",
        "extraTasks": "",
        "reward": {
            "description": "<ol><li>+3 уровня в Gamedev-разработке</li><li>+30 очков владения выбранным игровым движком</li><li>+20 очков владения выбранным языком (если движок предусматривает работу с языком)</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://www.construct.net/en/make-games/showcase",
        "previewImage": "/img/engines/games/construct-2d-game.gif",
        "isTeamProject": True,
        "niche": "gamedev",
        "category": "2D-platformers",
        "subcategory": "arcade",
    },
    # Корзина товаров и навыков: практика fetch, API и localStorage
    {
        "slug": "shopping-cart-js",
        "languages": ["javascript"],
        "taskType": 3,
        "difficulty": 3,
        "difficultyMetrics": {
            "logic": 80,
            "javascript": 70,
            "size": 70,
            "new": 40,
        },
        "title": "Корзина товаров: практика localStorage",
        "description": "Далеко не самая красивая (не сказать — кособокая) корзина на чистом JS... <p>Почему же я выбрал именно её, когда учил localStorage? Не знаю</p><p>Видимо, именно тогда Сатурн находился в третьем доме Луны... Так вот, практика localStorage</p><h3>Что тебя ждёт?</h3><p>Несмотря на простой UI, перед тобой одна из самых серьёзных задач в твоей карьере — и я сейчас не преувеличиваю.</p><p>На этом проекте ты докажешь, что был рождён для программирования, или... Или по-другому и быть не может!</p>",
        "extraTasks": "<ol><li>Сделать так, чтобы товары грузились из API, например, <a href='https://fakestoreapi.com/' target='_blank'>из fakeStoreAPI</a></li><li>Используй TypeScript для типизации своего кода</li></ol>",
        "reward": {
            "description": "<ol><li>+3 уровня к JavaScript-разработке</li><li>+2 уровня к логике</li><li>+30 очков владения JS</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://codepen.io/Dimasion/pen/oBoqBM",
        "previewImage": "/img/js/projects/shopping-cart-js.gif",
        "isTeamProject": False,
        "niche": "online-stores",
        "category": "sales",
        "subcategory": "site-parts",
    },
    # Генератор товаров: fakeStoreAPI
    {
        "slug": "products-generator-fakestore-api.gif",
        "languages": ["javascript"],
        "taskType": 3,
        "difficulty": 3,
        "difficultyMetrics": {
            "logic": 75,
            "javascript": 65,
            "size": 50,
        },
        "title": "Генератор товаров: fakeStoreAPI",
        "description": "<p>Взгляни на эту шикарную админку!</p>Единственное, чего ей не хватает — это добавления товаров. И мы можем с этим помочь:<ol><li>Товары возьмём на <a href='https://fakestoreapi.com/' target='_blank'>fakeStoreAPI</a></li><li>Сгенерируем для них карточки</li><li>И добавим это на сайт</li></ol><p>План прост, вот только будет ли просто это в реализации?</p>",
        "extraTasks": "<ol><li>Добавить поиск по товарам (фильтрация при вводе в инпут)</li><li>Добавить фильтры по категориям и статусам (filters)</li></ol>",
        "reward": {
            "description": "<ol><li>+3 уровня JavaScript-разработки</li><li>+2 уровня к логике</li><li>+25 очков по навыкам JS</li></ol>",
            "has_money_compensation": False,
        },
        "link": "https://codepen.io/aybukeceylan/pen/PopNYeJ",
        "previewImage": "/img/js/projects/products-generator-fakestore-api.gif",
        "isTeamProject": False,
        "niche": "online-stores",
        "category": "",
        "subcategory": "",
    },
]


""" 
? HTMl / CSS

- flexbox froggy
- 

"""


""" 
? JS

- Меню как в Notion
- Динамичные таблицы как в Notion
- Карусель (слайдер на чистом JS, проект)
https://www.naiveui.com/en-US/light/components/carousel
- Календарь (по типу Google Calendar, только мини-версия, проекта)
https://www.naiveui.com/en-US/light/components/date-picker
https://www.naiveui.com/en-US/light/components/time-picker
- Звёздочки (рейтинг, оценка) на чистом JS
https://www.naiveui.com/en-US/light/components/rate
- шифр (и дешифратор) Цезаря
- драг-н-дроп заметка 
https://www.naiveui.com/en-US/light/components/transfer


"""


""" 
? Vue

- CRM-система для партнёров EXPAND (интеграция с рекламынм ботом + дизайн и стиль как в Notion)
- Админка на Vue для EXPAND: гибкий интерфейс лейаутов, вывод контента, интеграция сервисов, обновление контента в режиме реального времени (как в Notion)
- Система риал-тайм контента: обновление контента в режиме реального времени (как в Notion)

"""


""" 
! Python

- API своими руками
- телеграм-бот

"""

""" 
Теория джс:
- ООП
- методы массивов + тренировка
- методы объектов + задачка
- все циклы ДЖС + тренировка
- локалсторедж

? Проекты JS:
- корзина товаров + подсчет стоимости (проект для локалсторедж)
- вечная прокрутка сайта (добавление / генерация текста + карточек при прокрутке)
- подгрузка товаров, как в интернет-магазине
- добавление товаров на сайт (кнопка для показа товаров + генерация их из API)
- memory cards

? Усложнения:
- Плеер: брать музыку из API, можно из самописного

? Фулл-стек:
- загрузка товаров на сайт из поля (для CSV или Эксел файлов) + генерировать товары на основе этих данных 
- система управления контентом: CMS своими руками 
- CMS: OpenCart (теория PHP + проект)
- CMS: WordPress (теория PHP + проект)
- логин и регистрация (командный)



"""

""" 

! Сюда нужно перенести темы / проекты / задачи из полного списка тем и проектов
https://www.expandplatform.com/students/projects/

"""