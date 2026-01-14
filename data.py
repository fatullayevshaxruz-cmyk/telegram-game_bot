# data.py - FotMob Mini App Mock Data

# =============================
# O'YINCHILAR (Players)
# =============================
PLAYERS = {
    1: {
        "id": 1,
        "name": "Dragan Ceran",
        "name_ru": "Драган Церан",
        "team": "Pakhtakor",
        "team_ru": "Пахтакор",
        "position": "Forward",
        "position_uz": "Hujumchi",
        "position_ru": "Нападающий",
        "number": 9,
        "nationality": "🇷🇸 Serbiya",
        "nationality_ru": "🇷🇸 Сербия",
        "age": 29,
        "photo": "https://img.a.transfermarkt.technology/portrait/big/346971-1663841773.jpg",
        "goals": 18,
        "assists": 7,
        "matches": 24
    },
    2: {
        "id": 2,
        "name": "Husniddin Aliqulov",
        "name_ru": "Хусниддин Аликулов",
        "team": "Pakhtakor",
        "team_ru": "Пахтакор",
        "position": "Midfielder",
        "position_uz": "Yarim himoyachi",
        "position_ru": "Полузащитник",
        "number": 10,
        "nationality": "🇺🇿 O'zbekiston",
        "nationality_ru": "🇺🇿 Узбекистан",
        "age": 27,
        "photo": "https://img.a.transfermarkt.technology/portrait/big/577047-1695281551.jpg",
        "goals": 8,
        "assists": 12,
        "matches": 26
    },
    3: {
        "id": 3,
        "name": "Oston Urunov",
        "name_ru": "Остон Урунов",
        "team": "Nasaf",
        "team_ru": "Насаф",
        "position": "Midfielder",
        "position_uz": "Yarim himoyachi",
        "position_ru": "Полузащитник",
        "number": 7,
        "nationality": "🇺🇿 O'zbekiston",
        "nationality_ru": "🇺🇿 Узбекистан",
        "age": 25,
        "photo": "https://img.a.transfermarkt.technology/portrait/big/503211-1683616142.jpg",
        "goals": 11,
        "assists": 5,
        "matches": 25
    },
    4: {
        "id": 4,
        "name": "Eldor Shomurodov",
        "name_ru": "Элдор Шомуродов",
        "team": "Roma (arendada)",
        "team_ru": "Рома (аренда)",
        "position": "Forward",
        "position_uz": "Hujumchi",
        "position_ru": "Нападающий",
        "number": 14,
        "nationality": "🇺🇿 O'zbekiston",
        "nationality_ru": "🇺🇿 Узбекистан",
        "age": 29,
        "photo": "https://img.a.transfermarkt.technology/portrait/big/434556-1704700761.jpg",
        "goals": 5,
        "assists": 2,
        "matches": 18
    },
    5: {
        "id": 5,
        "name": "Jaloliddin Masharipov",
        "name_ru": "Джалолиддин Машарипов",
        "team": "Pakhtakor",
        "team_ru": "Пахтакор",
        "position": "Winger",
        "position_uz": "Chap qanotchi",
        "position_ru": "Вингер",
        "number": 11,
        "nationality": "🇺🇿 O'zbekiston",
        "nationality_ru": "🇺🇿 Узбекистан",
        "age": 31,
        "photo": "https://img.a.transfermarkt.technology/portrait/big/346971-1663841773.jpg",
        "goals": 9,
        "assists": 14,
        "matches": 27
    },
    6: {
        "id": 6,
        "name": "Eldorbek Suyunov",
        "name_ru": "Элдорбек Суюнов",
        "team": "Bunyodkor",
        "team_ru": "Бунёдкор",
        "position": "Goalkeeper",
        "position_uz": "Darvozabon",
        "position_ru": "Вратарь",
        "number": 1,
        "nationality": "🇺🇿 O'zbekiston",
        "nationality_ru": "🇺🇿 Узбекистан",
        "age": 28,
        "photo": "https://img.a.transfermarkt.technology/portrait/big/468115-1695281551.jpg",
        "goals": 0,
        "assists": 0,
        "matches": 28
    }
}

# =============================
# LIGALAR (Leagues)
# =============================
LEAGUES = {
    "uz_super": {
        "id": "uz_super",
        "name": "O'zbekiston Superligasi",
        "name_ru": "Суперлига Узбекистана",
        "country": "🇺🇿 O'zbekiston",
        "logo": "https://upload.wikimedia.org/wikipedia/en/d/d3/Uzbekistan_Super_League_logo.png"
    },
    "uz_cup": {
        "id": "uz_cup",
        "name": "O'zbekiston Kubogi",
        "name_ru": "Кубок Узбекистана",
        "country": "🇺🇿 O'zbekiston",
        "logo": "https://upload.wikimedia.org/wikipedia/en/d/d3/Uzbekistan_Super_League_logo.png"
    },
    "apl": {
        "id": "apl",
        "name": "Premier Liga",
        "name_ru": "Премьер-лига",
        "country": "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Angliya",
        "logo": "https://upload.wikimedia.org/wikipedia/en/f/f2/Premier_League_Logo.svg"
    },
    "laliga": {
        "id": "laliga",
        "name": "La Liga",
        "name_ru": "Ла Лига",
        "country": "🇪🇸 Ispaniya",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/5/54/LaLiga_EA_Sports_2023_Vertical_Logo.svg"
    },
    "ucl": {
        "id": "ucl",
        "name": "UEFA Chempionlar Ligasi",
        "name_ru": "Лига Чемпионов УЕФА",
        "country": "🇪🇺 Yevropa",
        "logo": "https://upload.wikimedia.org/wikipedia/en/b/bf/UEFA_Champions_League_logo_2.svg"
    }
}

# =============================
# O'ZBEKISTON SUPERLIGASI JADVALI
# =============================
STANDINGS = {
    "uz_super": [
        {"pos": 1, "team": "Pakhtakor", "team_ru": "Пахтакор", "logo": "⚪", "played": 28, "won": 22, "draw": 4, "lost": 2, "gf": 68, "ga": 18, "gd": 50, "points": 70},
        {"pos": 2, "team": "Nasaf", "team_ru": "Насаф", "logo": "🟢", "played": 28, "won": 19, "draw": 5, "lost": 4, "gf": 52, "ga": 22, "gd": 30, "points": 62},
        {"pos": 3, "team": "AGMK", "team_ru": "АГМК", "logo": "🔵", "played": 28, "won": 17, "draw": 6, "lost": 5, "gf": 48, "ga": 25, "gd": 23, "points": 57},
        {"pos": 4, "team": "Navbahor", "team_ru": "Навбахор", "logo": "🟡", "played": 28, "won": 15, "draw": 7, "lost": 6, "gf": 41, "ga": 28, "gd": 13, "points": 52},
        {"pos": 5, "team": "Bunyodkor", "team_ru": "Бунёдкор", "logo": "🟢", "played": 28, "won": 14, "draw": 6, "lost": 8, "gf": 38, "ga": 30, "gd": 8, "points": 48},
        {"pos": 6, "team": "Sogdiyona", "team_ru": "Согдиана", "logo": "🔴", "played": 28, "won": 12, "draw": 8, "lost": 8, "gf": 35, "ga": 31, "gd": 4, "points": 44},
        {"pos": 7, "team": "Qizilqum", "team_ru": "Кызылкум", "logo": "🔴", "played": 28, "won": 11, "draw": 9, "lost": 8, "gf": 33, "ga": 32, "gd": 1, "points": 42},
        {"pos": 8, "team": "Metallurg", "team_ru": "Металлург", "logo": "⚪", "played": 28, "won": 10, "draw": 9, "lost": 9, "gf": 30, "ga": 30, "gd": 0, "points": 39},
        {"pos": 9, "team": "Andijon", "team_ru": "Андижан", "logo": "🟢", "played": 28, "won": 10, "draw": 7, "lost": 11, "gf": 28, "ga": 35, "gd": -7, "points": 37},
        {"pos": 10, "team": "Neftchi", "team_ru": "Нефтчи", "logo": "⚫", "played": 28, "won": 9, "draw": 8, "lost": 11, "gf": 27, "ga": 34, "gd": -7, "points": 35},
        {"pos": 11, "team": "Lokomotiv", "team_ru": "Локомотив", "logo": "🔴", "played": 28, "won": 8, "draw": 9, "lost": 11, "gf": 26, "ga": 33, "gd": -7, "points": 33},
        {"pos": 12, "team": "Qo'qon-1912", "team_ru": "Коканд-1912", "logo": "🟢", "played": 28, "won": 7, "draw": 8, "lost": 13, "gf": 24, "ga": 38, "gd": -14, "points": 29},
        {"pos": 13, "team": "Dinamo", "team_ru": "Динамо", "logo": "🔵", "played": 28, "won": 6, "draw": 9, "lost": 13, "gf": 22, "ga": 40, "gd": -18, "points": 27},
        {"pos": 14, "team": "Turon", "team_ru": "Турон", "logo": "🟡", "played": 28, "won": 5, "draw": 8, "lost": 15, "gf": 20, "ga": 42, "gd": -22, "points": 23},
    ]
}

# =============================
# O'YINLAR (Matches)
# =============================
MATCHES = [
    # Bugungi o'yinlar - O'zbekiston Superligasi
    {
        "id": 1,
        "league_id": "uz_super",
        "league": "O'zbekiston Superligasi",
        "league_ru": "Суперлига Узбекистана",
        "home_team": "Pakhtakor",
        "home_team_ru": "Пахтакор",
        "away_team": "Nasaf",
        "away_team_ru": "Насаф",
        "home_logo": "⚪",
        "away_logo": "🟢",
        "home_score": 2,
        "away_score": 1,
        "status": "LIVE",
        "minute": 67,
        "date": "2026-01-15",
        "time": "18:00",
        "datetime_utc": "2026-01-15T13:00:00Z",
        "stadium": "Milliy stadion",
        "stadium_ru": "Национальный стадион",
        "watch_uz": "https://sporttv.uz",
        "watch_ru": "https://matchtv.ru",
        "stats": {
            "possession": [62, 38],
            "shots": [14, 8],
            "shots_on_target": [6, 3],
            "corners": [7, 4],
            "fouls": [9, 12]
        },
        "lineup": {
            "home": {
                "formation": "4-3-3",
                "players": [
                    {"id": 6, "name": "E. Suyunov", "number": 1, "position": "GK", "x": 50, "y": 92},
                    {"id": None, "name": "A. Yusupov", "number": 2, "position": "RB", "x": 85, "y": 75},
                    {"id": None, "name": "S. Sayfiev", "number": 4, "position": "CB", "x": 60, "y": 75},
                    {"id": None, "name": "D. Iskandarov", "number": 5, "position": "CB", "x": 40, "y": 75},
                    {"id": None, "name": "M. Abdullayev", "number": 3, "position": "LB", "x": 15, "y": 75},
                    {"id": 2, "name": "H. Aliqulov", "number": 10, "position": "CM", "x": 50, "y": 55},
                    {"id": None, "name": "J. Komilov", "number": 8, "position": "CM", "x": 30, "y": 55},
                    {"id": None, "name": "O. Ashurmatov", "number": 6, "position": "CM", "x": 70, "y": 55},
                    {"id": 5, "name": "J. Masharipov", "number": 11, "position": "LW", "x": 15, "y": 30},
                    {"id": 1, "name": "D. Ceran", "number": 9, "position": "ST", "x": 50, "y": 20},
                    {"id": None, "name": "I. Juraev", "number": 7, "position": "RW", "x": 85, "y": 30}
                ]
            },
            "away": {
                "formation": "4-2-3-1",
                "players": [
                    {"id": None, "name": "N. Ergashev", "number": 1, "position": "GK", "x": 50, "y": 8},
                    {"id": None, "name": "S. Tursunov", "number": 2, "position": "RB", "x": 85, "y": 25},
                    {"id": None, "name": "A. Hakimov", "number": 4, "position": "CB", "x": 60, "y": 25},
                    {"id": None, "name": "F. Davronov", "number": 5, "position": "CB", "x": 40, "y": 25},
                    {"id": None, "name": "B. Boymurodov", "number": 3, "position": "LB", "x": 15, "y": 25},
                    {"id": None, "name": "K. Toshev", "number": 6, "position": "CDM", "x": 35, "y": 45},
                    {"id": None, "name": "N. Haydarov", "number": 8, "position": "CDM", "x": 65, "y": 45},
                    {"id": 3, "name": "O. Urunov", "number": 7, "position": "CAM", "x": 50, "y": 60},
                    {"id": None, "name": "J. Sodiqov", "number": 11, "position": "LW", "x": 20, "y": 70},
                    {"id": None, "name": "M. Sidikov", "number": 9, "position": "ST", "x": 50, "y": 80},
                    {"id": None, "name": "R. Ochilov", "number": 10, "position": "RW", "x": 80, "y": 70}
                ]
            }
        }
    },
    {
        "id": 2,
        "league_id": "uz_super",
        "league": "O'zbekiston Superligasi",
        "league_ru": "Суперлига Узбекистана",
        "home_team": "AGMK",
        "home_team_ru": "АГМК",
        "away_team": "Bunyodkor",
        "away_team_ru": "Бунёдкор",
        "home_logo": "🔵",
        "away_logo": "🟢",
        "home_score": None,
        "away_score": None,
        "status": "SCHEDULED",
        "minute": None,
        "date": "2026-01-15",
        "time": "20:00",
        "datetime_utc": "2026-01-15T15:00:00Z",
        "stadium": "AGMK Arena",
        "stadium_ru": "АГМК Арена",
        "watch_uz": "https://sporttv.uz",
        "watch_ru": "https://matchtv.ru",
        "stats": None,
        "lineup": None
    },
    # O'zbekiston Kubogi - Final
    {
        "id": 3,
        "league_id": "uz_cup",
        "league": "O'zbekiston Kubogi - Final",
        "league_ru": "Кубок Узбекистана - Финал",
        "home_team": "Pakhtakor",
        "home_team_ru": "Пахтакор",
        "away_team": "AGMK",
        "away_team_ru": "АГМК",
        "home_logo": "⚪",
        "away_logo": "🔵",
        "home_score": None,
        "away_score": None,
        "status": "SCHEDULED",
        "minute": None,
        "date": "2026-01-20",
        "time": "19:00",
        "datetime_utc": "2026-01-20T14:00:00Z",
        "stadium": "Milliy stadion",
        "stadium_ru": "Национальный стадион",
        "watch_uz": "https://sporttv.uz",
        "watch_ru": "https://matchtv.ru",
        "stats": None,
        "lineup": None
    },
    # APL
    {
        "id": 4,
        "league_id": "apl",
        "league": "Premier Liga",
        "league_ru": "Премьер-лига",
        "home_team": "Arsenal",
        "home_team_ru": "Арсенал",
        "away_team": "Chelsea",
        "away_team_ru": "Челси",
        "home_logo": "🔴",
        "away_logo": "🔵",
        "home_score": 2,
        "away_score": 2,
        "status": "FT",
        "minute": 90,
        "date": "2026-01-14",
        "time": "23:00",
        "datetime_utc": "2026-01-14T18:00:00Z",
        "stadium": "Emirates Stadium",
        "stadium_ru": "Эмирейтс",
        "watch_uz": "https://sporttv.uz",
        "watch_ru": "https://matchtv.ru",
        "stats": {
            "possession": [58, 42],
            "shots": [18, 12],
            "shots_on_target": [8, 6],
            "corners": [9, 5],
            "fouls": [11, 14]
        },
        "lineup": None
    },
    {
        "id": 5,
        "league_id": "apl",
        "league": "Premier Liga",
        "league_ru": "Премьер-лига",
        "home_team": "Liverpool",
        "home_team_ru": "Ливерпуль",
        "away_team": "Man City",
        "away_team_ru": "Ман Сити",
        "home_logo": "🔴",
        "away_logo": "🔵",
        "home_score": None,
        "away_score": None,
        "status": "SCHEDULED",
        "minute": None,
        "date": "2026-01-16",
        "time": "23:30",
        "datetime_utc": "2026-01-16T18:30:00Z",
        "stadium": "Anfield",
        "stadium_ru": "Энфилд",
        "watch_uz": "https://sporttv.uz",
        "watch_ru": "https://matchtv.ru",
        "stats": None,
        "lineup": None
    },
    # La Liga
    {
        "id": 6,
        "league_id": "laliga",
        "league": "La Liga",
        "league_ru": "Ла Лига",
        "home_team": "Real Madrid",
        "home_team_ru": "Реал Мадрид",
        "away_team": "Barcelona",
        "away_team_ru": "Барселона",
        "home_logo": "⚪",
        "away_logo": "🔵",
        "home_score": None,
        "away_score": None,
        "status": "SCHEDULED",
        "minute": None,
        "date": "2026-01-17",
        "time": "00:00",
        "datetime_utc": "2026-01-16T19:00:00Z",
        "stadium": "Santiago Bernabéu",
        "stadium_ru": "Сантьяго Бернабеу",
        "watch_uz": "https://sporttv.uz",
        "watch_ru": "https://matchtv.ru",
        "stats": None,
        "lineup": None
    },
    # UEFA Champions League
    {
        "id": 7,
        "league_id": "ucl",
        "league": "UEFA Chempionlar Ligasi",
        "league_ru": "Лига Чемпионов УЕФА",
        "home_team": "Bayern Munich",
        "home_team_ru": "Бавария",
        "away_team": "PSG",
        "away_team_ru": "ПСЖ",
        "home_logo": "🔴",
        "away_logo": "🔵",
        "home_score": 3,
        "away_score": 1,
        "status": "FT",
        "minute": 90,
        "date": "2026-01-14",
        "time": "00:00",
        "datetime_utc": "2026-01-13T19:00:00Z",
        "stadium": "Allianz Arena",
        "stadium_ru": "Альянц Арена",
        "watch_uz": "https://sporttv.uz",
        "watch_ru": "https://matchtv.ru",
        "stats": {
            "possession": [54, 46],
            "shots": [16, 10],
            "shots_on_target": [7, 4],
            "corners": [8, 6],
            "fouls": [10, 13]
        },
        "lineup": None
    }
]

# =============================
# YANGILIKLAR (News)
# =============================
NEWS = [
    {
        "id": 1,
        "title": "Pakhtakor Osiyo Chempionlar Ligasi guruh bosqichiga yo'l oldi!",
        "title_ru": "Пахтакор вышел в групповой этап Лиги Чемпионов Азии!",
        "summary": "Pakhtakor O'zbekiston chempioni sifatida ACL guruh bosqichiga to'g'ridan-to'g'ri yo'llanma oldi.",
        "summary_ru": "Пахтакор как чемпион Узбекистана напрямую вышел в групповой этап АЛЧ.",
        "content": "Pakhtakor futbol klubi O'zbekiston Superligasida g'olib kelib, Osiyo Chempionlar Ligasi guruh bosqichiga to'g'ridan-to'g'ri yo'llanma oldi. Bu klub tarixidagi muhim yutuqlardan biri bo'ldi. Jamoaning bosh murabbiyi bunday muvaffaqiyat uchun barcha futbolchi va muxlislarni tabriklab, kelgusi musobaqalarga tayyorgarlik boshlashini e'lon qildi.",
        "content_ru": "Футбольный клуб Пахтакор, став чемпионом Суперлиги Узбекистана, напрямую вышел в групповой этап Лиги Чемпионов Азии. Это стало одним из важнейших достижений в истории клуба. Главный тренер команды поздравил всех футболистов и болельщиков с успехом и объявил о начале подготовки к предстоящим соревнованиям.",
        "image": "https://images.unsplash.com/photo-1574629810360-7efbbe195018?w=800",
        "source": "Sport.uz",
        "date": "2026-01-15",
        "datetime_utc": "2026-01-15T08:00:00Z"
    },
    {
        "id": 2,
        "title": "Dragan Ceran mavsumning eng yaxshi futbolchisi deb topildi",
        "title_ru": "Драган Церан признан лучшим игроком сезона",
        "summary": "Serbiyalik hujumchi 18 ta gol urib, Superliga to'puri bo'ldi.",
        "summary_ru": "Сербский нападающий забил 18 голов и стал лучшим бомбардиром Суперлиги.",
        "content": "Pakhtakor hujumchisi Dragan Ceran 2025 yilgi mavsumning eng yaxshi futbolchisi unvoniga sazovor bo'ldi. U 28 ta o'yinda 18 gol urib, 7 ta gol uzatish berdi. Ceran: 'Bu mening eng yaxshi mavsumim. Paxtakor muxlislariga rahmat aytaman' - dedi.",
        "content_ru": "Нападающий Пахтакора Драган Церан был признан лучшим футболистом сезона 2025 года. Он забил 18 голов и сделал 7 результативных передач в 28 матчах. Церан сказал: 'Это мой лучший сезон. Благодарю болельщиков Пахтакора'.",
        "image": "https://images.unsplash.com/photo-1431324155629-1a6deb1dec8d?w=800",
        "source": "Championat.asia",
        "date": "2026-01-14",
        "datetime_utc": "2026-01-14T12:00:00Z"
    },
    {
        "id": 3,
        "title": "O'zbekiston Kubogi finali - Pakhtakor vs AGMK",
        "title_ru": "Финал Кубка Узбекистана - Пахтакор против АГМК",
        "summary": "Kubog'i finalida ikki kuchli jamoa to'qnash keladi.",
        "summary_ru": "В финале Кубка встретятся две сильнейшие команды.",
        "content": "O'zbekiston Kubogi finali 20-yanvar kuni Milliy stadionda bo'lib o'tadi. Pakhtakor va AGMK o'rtasidagi ushbu o'yin mavsumning eng qizg'in duellaridan biri bo'lishi kutilmoqda. Har ikki jamoa ham Kubokni qo'lga kiritish uchun kurashmoqda.",
        "content_ru": "Финал Кубка Узбекистана состоится 20 января на Национальном стадионе. Матч между Пахтакором и АГМК обещает стать одной из самых жарких дуэлей сезона. Обе команды борются за Кубок.",
        "image": "https://images.unsplash.com/photo-1489944440615-453fc2b6a9a9?w=800",
        "source": "Football.uz",
        "date": "2026-01-14",
        "datetime_utc": "2026-01-14T10:00:00Z"
    },
    {
        "id": 4,
        "title": "Eldor Shomurodov Serie A'da gollar urishda davom etmoqda",
        "title_ru": "Эльдор Шомуродов продолжает забивать в Серии А",
        "summary": "O'zbek hujumchi Italiyada ajoyib forma namoyish qilmoqda.",
        "summary_ru": "Узбекский нападающий демонстрирует отличную форму в Италии.",
        "content": "Roma hujumchisi Eldor Shomurodov oxirgi 5 ta o'yinda 3 ta gol urib, jamoasini g'alabaga yetaklashda muhim rol o'ynamoqda. Italiya matbuoti shomurodovni 'O'zbek sensatsiyasi' deb atash boshladi.",
        "content_ru": "Нападающий Ромы Эльдор Шомуродов забил 3 гола в последних 5 матчах, играя ключевую роль в победах команды. Итальянская пресса начала называть Шомуродова 'узбекской сенсацией'.",
        "image": "https://images.unsplash.com/photo-1606925797300-0b35e9d1794e?w=800",
        "source": "Gazzetta dello Sport",
        "date": "2026-01-13",
        "datetime_utc": "2026-01-13T16:00:00Z"
    },
    {
        "id": 5,
        "title": "Yangi milliy terma jamoa bosh murabbiyi e'lon qilindi",
        "title_ru": "Объявлен новый главный тренер сборной",
        "summary": "O'zbekiston futbol federatsiyasi muhim qaror qabul qildi.",
        "summary_ru": "Федерация футбола Узбекистана приняла важное решение.",
        "content": "O'zbekiston futbol federatsiyasi milliy terma jamoaning yangi bosh murabiysini tanladi. Tajribali mutaxassis jamoa boshiga kelishi bilan yangi davr boshlanishi kutilmoqda. Birinchi vazifa - Jahon chempionati saralash o'yinlariga tayyorgarlik.",
        "content_ru": "Федерация футбола Узбекистана выбрала нового главного тренера национальной сборной. С приходом опытного специалиста ожидается начало новой эры. Первая задача - подготовка к отборочным матчам Чемпионата мира.",
        "image": "https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=800",
        "source": "UzPFL",
        "date": "2026-01-12",
        "datetime_utc": "2026-01-12T09:00:00Z"
    },
    {
        "id": 6,
        "title": "Superliga transferlar oynasi ochildi",
        "title_ru": "Открылось трансферное окно Суперлиги",
        "summary": "Qish transfer oynasida qanday yangiliklar bo'ladi?",
        "summary_ru": "Какие новости ожидаются в зимнее трансферное окно?",
        "content": "O'zbekiston Superligasi qish transfer oynasi rasman ochildi. Ko'plab klublar saflarini kuchaytirish ustida ishlayotgan bo'lsa, ba'zilari yetakchi futbolchilarini saqlab qolish uchun kurashmoqda. Mutaxassislarning fikricha, bu oynada bir nechta yirik transferlar kutilmoqda.",
        "content_ru": "Зимнее трансферное окно Суперлиги Узбекистана официально открылось. Многие клубы работают над усилением составов, в то время как некоторые борются за сохранение своих ведущих футболистов. По мнению экспертов, в этом окне ожидается несколько крупных трансферов.",
        "image": "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800",
        "source": "Transfermarkt",
        "date": "2026-01-11",
        "datetime_utc": "2026-01-11T14:00:00Z"
    }
]

# =============================
# TARJIMALAR (Translations)
# =============================
TRANSLATIONS = {
    "uz": {
        "matches": "O'yinlar",
        "news": "Yangiliklar",
        "leagues": "Ligalar",
        "following": "Sevimli",
        "live": "LIVE",
        "today": "Bugun",
        "tomorrow": "Ertaga",
        "yesterday": "Kecha",
        "finished": "Tugadi",
        "scheduled": "Rejalashtirilgan",
        "watch_live": "📺 Jonli tomosha",
        "lineup": "Tarkib",
        "stats": "Statistika",
        "possession": "To'p nazorati",
        "shots": "Zarbalar",
        "shots_on_target": "Darvozaga zarbalar",
        "corners": "Burchak to'plari",
        "fouls": "Qoidabuzarliklar",
        "standings": "Jadval",
        "pos": "#",
        "team": "Jamoa",
        "played": "O'yin",
        "won": "G'",
        "draw": "D",
        "lost": "M",
        "gd": "F",
        "points": "O",
        "player_profile": "O'yinchi profili",
        "age": "Yoshi",
        "nationality": "Millati",
        "goals": "Gollar",
        "assists": "Assistlar",
        "matches_played": "O'ynagan o'yinlar",
        "close": "Yopish",
        "read_more": "Batafsil",
        "source": "Manba",
        "no_matches": "Bugun o'yin yo'q",
        "all_leagues": "Barcha ligalar"
    },
    "ru": {
        "matches": "Матчи",
        "news": "Новости",
        "leagues": "Лиги",
        "following": "Избранное",
        "live": "LIVE",
        "today": "Сегодня",
        "tomorrow": "Завтра",
        "yesterday": "Вчера",
        "finished": "Завершён",
        "scheduled": "Запланировано",
        "watch_live": "📺 Смотреть LIVE",
        "lineup": "Состав",
        "stats": "Статистика",
        "possession": "Владение мячом",
        "shots": "Удары",
        "shots_on_target": "В створ ворот",
        "corners": "Угловые",
        "fouls": "Фолы",
        "standings": "Таблица",
        "pos": "#",
        "team": "Команда",
        "played": "И",
        "won": "В",
        "draw": "Н",
        "lost": "П",
        "gd": "Р",
        "points": "О",
        "player_profile": "Профиль игрока",
        "age": "Возраст",
        "nationality": "Страна",
        "goals": "Голы",
        "assists": "Ассисты",
        "matches_played": "Сыграно матчей",
        "close": "Закрыть",
        "read_more": "Подробнее",
        "source": "Источник",
        "no_matches": "Сегодня нет матчей",
        "all_leagues": "Все лиги"
    }
}
