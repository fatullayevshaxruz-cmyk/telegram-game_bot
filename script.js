// =============================
// FOTMOB MINI APP - SCRIPT.JS
// =============================

// =============================
// GLOBAL STATE & CONFIGURATION
// =============================
const API_BASE = window.location.origin;
let currentLang = 'uz';
let translations = {};
let allMatches = [];
let allNews = [];
let allLeagues = [];

// Telegram Web App
const tg = window.Telegram?.WebApp;

// =============================
// INITIALIZATION
// =============================
document.addEventListener('DOMContentLoaded', async () => {
    // Telegram Web App init
    if (tg) {
        tg.ready();
        tg.expand();
        tg.setHeaderColor('#0d0d0d');
        tg.setBackgroundColor('#0d0d0d');
    }

    // URL dan til o'qish
    const urlParams = new URLSearchParams(window.location.search);
    currentLang = urlParams.get('lang') || 'uz';

    // Translation-larni yuklash
    await loadTranslations();

    // Ma'lumotlarni yuklash
    await Promise.all([
        loadMatches(),
        loadNews(),
        loadLeagues()
    ]);

    // Event listeners
    setupEventListeners();

    // UI ni yangilash
    updateUI();
});

// =============================
// API FUNCTIONS
// =============================
async function loadTranslations() {
    try {
        const res = await fetch(`${API_BASE}/api/translations/${currentLang}`);
        translations = await res.json();
    } catch (error) {
        console.error('Translation yuklashda xatolik:', error);
        translations = getDefaultTranslations();
    }
}

async function loadMatches() {
    try {
        const res = await fetch(`${API_BASE}/api/matches`);
        const data = await res.json();
        allMatches = data.matches || [];
        renderMatches();
    } catch (error) {
        console.error('O\'yinlarni yuklashda xatolik:', error);
        renderEmptyMatches();
    }
}

async function loadNews() {
    try {
        const res = await fetch(`${API_BASE}/api/news`);
        const data = await res.json();
        allNews = data.news || [];
        renderNews();
    } catch (error) {
        console.error('Yangiliklar yuklashda xatolik:', error);
    }
}

async function loadLeagues() {
    try {
        const res = await fetch(`${API_BASE}/api/leagues`);
        const data = await res.json();
        allLeagues = data.leagues || [];
        renderLeagues();
    } catch (error) {
        console.error('Ligalar yuklashda xatolik:', error);
    }
}

async function loadMatchDetail(matchId) {
    try {
        const res = await fetch(`${API_BASE}/api/match/${matchId}`);
        return await res.json();
    } catch (error) {
        console.error('O\'yin tafsilotlari yuklashda xatolik:', error);
        return null;
    }
}

async function loadPlayer(playerId) {
    try {
        const res = await fetch(`${API_BASE}/api/player/${playerId}`);
        return await res.json();
    } catch (error) {
        console.error('O\'yinchi ma\'lumoti yuklashda xatolik:', error);
        return null;
    }
}

async function loadStandings(leagueId) {
    try {
        const res = await fetch(`${API_BASE}/api/standings/${leagueId}`);
        return await res.json();
    } catch (error) {
        console.error('Jadval yuklashda xatolik:', error);
        return null;
    }
}

// =============================
// RENDER FUNCTIONS
// =============================
function renderMatches() {
    const container = document.getElementById('matchesList');
    if (!allMatches.length) {
        renderEmptyMatches();
        return;
    }

    // Group matches by league
    const grouped = groupMatchesByLeague(allMatches);

    let html = '';
    for (const [leagueId, matches] of Object.entries(grouped)) {
        const firstMatch = matches[0];
        // 3 til uchun league name
        let leagueName = firstMatch.league;
        if (currentLang === 'ru') leagueName = firstMatch.league_ru || firstMatch.league;
        else if (currentLang === 'en') leagueName = firstMatch.league_en || firstMatch.league;

        html += `
            <div class="league-group">
                <div class="league-header" onclick="openStandingsModal('${leagueId}')">
                    <div class="league-info">
                        <span class="league-logo">🏆</span>
                        <span class="league-name">${leagueName}</span>
                    </div>
                    <span class="league-arrow">›</span>
                </div>
                ${matches.map(match => renderMatchCard(match)).join('')}
            </div>
        `;
    }

    container.innerHTML = html;
}

function renderMatchCard(match) {
    // 3 til uchun team names
    let homeTeam = match.home_team;
    let awayTeam = match.away_team;
    if (currentLang === 'ru') {
        homeTeam = match.home_team_ru || match.home_team;
        awayTeam = match.away_team_ru || match.away_team;
    }
    const localTime = convertToLocalTime(match.datetime_utc);

    let timeDisplay = '';
    let statusClass = '';

    if (match.status === 'LIVE') {
        timeDisplay = `<span class="live">${match.minute}'</span>`;
        statusClass = 'live';
    } else if (match.status === 'FT') {
        timeDisplay = `<span class="time">${translations.finished || 'FT'}</span>`;
    } else {
        timeDisplay = `<span class="time">${localTime}</span>`;
    }

    const homeScore = match.home_score !== null ? match.home_score : '-';
    const awayScore = match.away_score !== null ? match.away_score : '-';

    const homeWinner = match.home_score > match.away_score ? 'winner' : '';
    const awayWinner = match.away_score > match.home_score ? 'winner' : '';

    return `
        <div class="match-card" onclick="openMatchModal(${match.id})">
            <div class="match-time">
                ${timeDisplay}
            </div>
            <div class="match-teams">
                <div class="team-row">
                    <span class="team-logo">${match.home_logo}</span>
                    <span class="team-name">${homeTeam}</span>
                </div>
                <div class="team-row">
                    <span class="team-logo">${match.away_logo}</span>
                    <span class="team-name">${awayTeam}</span>
                </div>
            </div>
            <div class="match-scores">
                <div class="score ${homeWinner}">${homeScore}</div>
                <div class="score ${awayWinner}">${awayScore}</div>
            </div>
        </div>
    `;
}

function renderNews() {
    const container = document.getElementById('newsList');
    if (!allNews.length) return;

    let html = allNews.map(news => {
        // 3 til uchun news
        let title = news.title;
        let summary = news.summary;
        if (currentLang === 'ru') {
            title = news.title_ru || news.title;
            summary = news.summary_ru || news.summary;
        } else if (currentLang === 'en') {
            title = news.title_en || news.title;
            summary = news.summary_en || news.summary;
        }
        const timeAgo = getTimeAgo(news.datetime_utc);

        return `
            <div class="news-card" onclick="openNewsModal(${news.id})">
                <img src="${news.image}" alt="${title}" class="news-image" loading="lazy">
                <div class="news-content">
                    <h3 class="news-title">${title}</h3>
                    <p class="news-summary">${summary}</p>
                    <div class="news-meta">
                        <span>${news.source}</span>
                        <span>${timeAgo}</span>
                    </div>
                </div>
            </div>
        `;
    }).join('');

    container.innerHTML = html;
}

function renderLeagues() {
    const container = document.getElementById('leaguesList');
    if (!allLeagues.length) return;

    let html = allLeagues.map(league => {
        // 3 til uchun league name
        let name = league.name;
        if (currentLang === 'ru') name = league.name_ru || league.name;
        else if (currentLang === 'en') name = league.name_en || league.name;

        return `
            <div class="league-card" onclick="openStandingsModal('${league.id}')">
                <span class="league-logo">🏆</span>
                <div class="league-card-info">
                    <div class="league-card-name">${name}</div>
                    <div class="league-card-country">${league.country}</div>
                </div>
                <span class="league-card-arrow">›</span>
            </div>
        `;
    }).join('');

    container.innerHTML = html;
}

function renderEmptyMatches() {
    const container = document.getElementById('matchesList');
    container.innerHTML = `
        <div class="empty-state">
            <span class="empty-icon">⚽</span>
            <h3>${translations.no_matches || "Bugun o'yin yo'q"}</h3>
        </div>
    `;
}

// =============================
// MODAL FUNCTIONS
// =============================
async function openMatchModal(matchId) {
    const modal = document.getElementById('matchModal');
    const content = document.getElementById('matchDetailContent');

    modal.classList.add('active');
    content.innerHTML = '<div class="skeleton" style="height: 200px;"></div>';

    const match = await loadMatchDetail(matchId);
    if (!match) {
        closeMatchModal();
        return;
    }

    renderMatchDetail(match);
}

function renderMatchDetail(match) {
    const content = document.getElementById('matchDetailContent');
    const homeTeam = currentLang === 'ru' ? match.home_team_ru : match.home_team;
    const awayTeam = currentLang === 'ru' ? match.away_team_ru : match.away_team;
    const leagueName = currentLang === 'ru' ? match.league_ru : match.league;
    const stadium = currentLang === 'ru' ? match.stadium_ru : match.stadium;

    const homeScore = match.home_score !== null ? match.home_score : '-';
    const awayScore = match.away_score !== null ? match.away_score : '-';

    const watchUrl = currentLang === 'ru' ? match.watch_ru : match.watch_uz;
    const watchText = translations.watch_live || '📺 Jonli tomosha';

    let minuteDisplay = '';
    if (match.status === 'LIVE') {
        minuteDisplay = `<div class="minute">${match.minute}'</div>`;
    }

    let html = `
        <div class="match-header">
            <div class="league-name">${leagueName}</div>
            <div class="match-score-board">
                <div class="team-block">
                    <div class="logo">${match.home_logo}</div>
                    <div class="name">${homeTeam}</div>
                </div>
                <div class="score-block">
                    ${homeScore} - ${awayScore}
                    ${minuteDisplay}
                </div>
                <div class="team-block">
                    <div class="logo">${match.away_logo}</div>
                    <div class="name">${awayTeam}</div>
                </div>
            </div>
            <div class="match-info">📍 ${stadium}</div>
        </div>
        
        <div class="match-tabs">
            <button class="match-tab active" onclick="showMatchTab('lineup')">${translations.lineup || 'Tarkib'}</button>
            <button class="match-tab" onclick="showMatchTab('stats')">${translations.stats || 'Statistika'}</button>
        </div>
    `;

    // Lineup section
    if (match.lineup) {
        html += renderLineup(match.lineup);
    } else {
        html += `
            <div id="lineupSection" class="lineup-section">
                <div class="empty-state" style="padding: 40px 0;">
                    <span class="empty-icon">📋</span>
                    <p>Tarkib hali e'lon qilinmagan</p>
                </div>
            </div>
        `;
    }

    // Stats section
    if (match.stats) {
        html += renderStats(match.stats);
    } else {
        html += `
            <div id="statsSection" class="stats-section" style="display: none;">
                <div class="empty-state" style="padding: 40px 0;">
                    <span class="empty-icon">📊</span>
                    <p>Statistika mavjud emas</p>
                </div>
            </div>
        `;
    }

    // Watch Live Button
    if (match.status === 'LIVE' || match.status === 'SCHEDULED') {
        html += `
            <a href="${watchUrl}" target="_blank" class="watch-live-btn">
                ${watchText}
            </a>
        `;
    }

    content.innerHTML = html;
}

function renderLineup(lineup) {
    const homeFormation = lineup.home?.formation || '4-3-3';
    const awayFormation = lineup.away?.formation || '4-3-3';

    let html = `
        <div id="lineupSection" class="lineup-section">
            <div class="formation-label">${homeFormation}</div>
            <div class="pitch">
                <div class="pitch-half home">
                    <div class="penalty-area"></div>
                    <div class="goal-area"></div>
                </div>
                <div class="pitch-half away">
                    <div class="penalty-area"></div>
                    <div class="goal-area"></div>
                </div>
    `;

    // Home team players
    if (lineup.home?.players) {
        lineup.home.players.forEach(player => {
            const clickHandler = player.id ? `onclick="openPlayerModal(${player.id})"` : '';
            html += `
                <div class="player-marker home" style="left: ${player.x}%; top: ${player.y}%;" ${clickHandler}>
                    <div class="player-dot">${player.number}</div>
                    <span class="player-name-tag">${player.name}</span>
                </div>
            `;
        });
    }

    // Away team players
    if (lineup.away?.players) {
        lineup.away.players.forEach(player => {
            const clickHandler = player.id ? `onclick="openPlayerModal(${player.id})"` : '';
            html += `
                <div class="player-marker away" style="left: ${player.x}%; top: ${player.y}%;" ${clickHandler}>
                    <div class="player-dot">${player.number}</div>
                    <span class="player-name-tag">${player.name}</span>
                </div>
            `;
        });
    }

    html += `
            </div>
            <div class="formation-label">${awayFormation}</div>
        </div>
    `;

    return html;
}

function renderStats(stats) {
    const labels = {
        possession: translations.possession || "To'p nazorati",
        shots: translations.shots || 'Zarbalar',
        shots_on_target: translations.shots_on_target || 'Darvozaga',
        corners: translations.corners || 'Burchaklar',
        fouls: translations.fouls || 'Xatolar'
    };

    let html = `<div id="statsSection" class="stats-section" style="display: none;">`;

    // Possession
    const [homePoss, awayPoss] = stats.possession;
    html += `
        <div class="stat-item">
            <span class="stat-value">${homePoss}%</span>
            <div class="stat-bars">
                <div class="stat-bar home" style="width: ${homePoss}%"></div>
                <div class="stat-bar away" style="width: ${awayPoss}%"></div>
            </div>
            <span class="stat-label">${labels.possession}</span>
            <span class="stat-value">${awayPoss}%</span>
        </div>
    `;

    // Other stats
    const statItems = [
        { key: 'shots', label: labels.shots, data: stats.shots },
        { key: 'shots_on_target', label: labels.shots_on_target, data: stats.shots_on_target },
        { key: 'corners', label: labels.corners, data: stats.corners },
        { key: 'fouls', label: labels.fouls, data: stats.fouls }
    ];

    statItems.forEach(stat => {
        if (stat.data) {
            const [home, away] = stat.data;
            const total = home + away || 1;
            const homeWidth = (home / total * 100).toFixed(0);
            const awayWidth = (away / total * 100).toFixed(0);

            html += `
                <div class="stat-item">
                    <span class="stat-value">${home}</span>
                    <div class="stat-bars">
                        <div class="stat-bar home" style="width: ${homeWidth}%"></div>
                        <div class="stat-bar away" style="width: ${awayWidth}%"></div>
                    </div>
                    <span class="stat-label">${stat.label}</span>
                    <span class="stat-value">${away}</span>
                </div>
            `;
        }
    });

    html += '</div>';
    return html;
}

function showMatchTab(tab) {
    const tabs = document.querySelectorAll('.match-tab');
    tabs.forEach(t => t.classList.remove('active'));
    event.target.classList.add('active');

    const lineupSection = document.getElementById('lineupSection');
    const statsSection = document.getElementById('statsSection');

    if (tab === 'lineup') {
        if (lineupSection) lineupSection.style.display = 'block';
        if (statsSection) statsSection.style.display = 'none';
    } else {
        if (lineupSection) lineupSection.style.display = 'none';
        if (statsSection) statsSection.style.display = 'block';
    }
}

function closeMatchModal() {
    document.getElementById('matchModal').classList.remove('active');
}

// Player Modal
async function openPlayerModal(playerId) {
    event.stopPropagation();

    const modal = document.getElementById('playerModal');
    const content = document.getElementById('playerProfileContent');

    modal.classList.add('active');
    content.innerHTML = '<div class="skeleton" style="height: 300px;"></div>';

    const player = await loadPlayer(playerId);
    if (!player) {
        closePlayerModal();
        return;
    }

    const name = currentLang === 'ru' ? player.name_ru : player.name;
    const team = currentLang === 'ru' ? player.team_ru : player.team;
    const position = currentLang === 'ru' ? player.position_ru : player.position_uz;
    const nationality = currentLang === 'ru' ? player.nationality_ru : player.nationality;

    content.innerHTML = `
        <img src="${player.photo}" alt="${name}" class="player-photo" onerror="this.src='https://via.placeholder.com/120'">
        <h2 class="player-name">${name}</h2>
        <div class="player-team">${team}</div>
        <div class="player-position">#${player.number} • ${position}</div>
        
        <div class="player-stats-grid">
            <div class="player-stat-card">
                <div class="player-stat-value">${player.goals}</div>
                <div class="player-stat-label">${translations.goals || 'Gollar'}</div>
            </div>
            <div class="player-stat-card">
                <div class="player-stat-value">${player.assists}</div>
                <div class="player-stat-label">${translations.assists || 'Assistlar'}</div>
            </div>
        </div>
        
        <div class="player-info-list">
            <div class="player-info-item">
                <span class="player-info-label">${translations.age || 'Yoshi'}</span>
                <span class="player-info-value">${player.age}</span>
            </div>
            <div class="player-info-item">
                <span class="player-info-label">${translations.nationality || 'Millati'}</span>
                <span class="player-info-value">${nationality}</span>
            </div>
            <div class="player-info-item">
                <span class="player-info-label">${translations.matches_played || "O'yinlar"}</span>
                <span class="player-info-value">${player.matches}</span>
            </div>
        </div>
    `;
}

function closePlayerModal() {
    document.getElementById('playerModal').classList.remove('active');
}

// News Modal
async function openNewsModal(newsId) {
    const modal = document.getElementById('newsModal');
    const content = document.getElementById('newsDetailContent');

    modal.classList.add('active');

    const news = allNews.find(n => n.id === newsId);
    if (!news) {
        closeNewsModal();
        return;
    }

    const title = currentLang === 'ru' ? news.title_ru : news.title;
    const text = currentLang === 'ru' ? news.content_ru : news.content;
    const timeAgo = getTimeAgo(news.datetime_utc);

    content.innerHTML = `
        <img src="${news.image}" alt="${title}" class="news-detail-image">
        <div class="news-detail-content">
            <h1 class="news-detail-title">${title}</h1>
            <div class="news-detail-meta">
                <span>${translations.source || 'Manba'}: ${news.source}</span>
                <span>${timeAgo}</span>
            </div>
            <p class="news-detail-text">${text}</p>
        </div>
    `;
}

function closeNewsModal() {
    document.getElementById('newsModal').classList.remove('active');
}

// Standings Modal
async function openStandingsModal(leagueId) {
    const modal = document.getElementById('standingsModal');
    const content = document.getElementById('standingsContent');

    modal.classList.add('active');
    content.innerHTML = '<div class="skeleton" style="height: 400px;"></div>';

    const data = await loadStandings(leagueId);
    if (!data || !data.standings) {
        content.innerHTML = `
            <div class="standings-header">
                <h2>${translations.standings || 'Jadval'}</h2>
            </div>
            <div class="empty-state">
                <span class="empty-icon">📊</span>
                <p>Jadval mavjud emas</p>
            </div>
        `;
        return;
    }

    const leagueName = currentLang === 'ru' ? data.league.name_ru : data.league.name;

    let tableRows = data.standings.map(row => {
        const teamName = currentLang === 'ru' ? row.team_ru : row.team;
        return `
            <tr class="pos-${row.pos}">
                <td>${row.pos}</td>
                <td>
                    <div class="team-cell">
                        <span>${row.logo}</span>
                        <span>${teamName}</span>
                    </div>
                </td>
                <td>${row.played}</td>
                <td>${row.won}</td>
                <td>${row.draw}</td>
                <td>${row.lost}</td>
                <td>${row.gd > 0 ? '+' : ''}${row.gd}</td>
                <td class="points">${row.points}</td>
            </tr>
        `;
    }).join('');

    content.innerHTML = `
        <div class="standings-header">
            <h2>${leagueName}</h2>
        </div>
        <table class="standings-table">
            <thead>
                <tr>
                    <th>${translations.pos || '#'}</th>
                    <th>${translations.team || 'Jamoa'}</th>
                    <th>${translations.played || 'O'}</th>
                    <th>${translations.won || 'G'}</th>
                    <th>${translations.draw || 'D'}</th>
                    <th>${translations.lost || 'M'}</th>
                    <th>${translations.gd || 'F'}</th>
                    <th>${translations.points || 'O'}</th>
                </tr>
            </thead>
            <tbody>
                ${tableRows}
            </tbody>
        </table>
    `;
}

function closeStandingsModal() {
    document.getElementById('standingsModal').classList.remove('active');
}

// =============================
// NAVIGATION & UI
// =============================
function setupEventListeners() {
    // Bottom navigation
    const navItems = document.querySelectorAll('.nav-item');
    navItems.forEach(item => {
        item.addEventListener('click', () => {
            const tabName = item.dataset.tab;
            switchTab(tabName);

            // Update active state
            navItems.forEach(n => n.classList.remove('active'));
            item.classList.add('active');
        });
    });

    // Date buttons
    const dateButtons = document.querySelectorAll('.date-btn');
    dateButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            dateButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            // Could filter matches by date here
        });
    });

    // Close modals on backdrop click
    ['matchModal', 'playerModal', 'newsModal', 'standingsModal'].forEach(id => {
        const modal = document.getElementById(id);
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.classList.remove('active');
            }
        });
    });
}

function switchTab(tabName) {
    const tabs = document.querySelectorAll('.tab-content');
    tabs.forEach(tab => tab.classList.remove('active'));

    const activeTab = document.getElementById(`${tabName}Tab`);
    if (activeTab) {
        activeTab.classList.add('active');
    }
}

function updateUI() {
    // Update navigation text
    document.querySelector('#navMatches .nav-text').textContent = translations.matches || "O'yinlar";
    document.querySelector('#navNews .nav-text').textContent = translations.news || 'Yangiliklar';
    document.querySelector('#navLeagues .nav-text').textContent = translations.leagues || 'Ligalar';
    document.querySelector('#navFollowing .nav-text').textContent = translations.following || 'Sevimli';

    // Update date buttons
    document.getElementById('yesterdayBtn').textContent = translations.yesterday || 'Kecha';
    document.getElementById('todayBtn').textContent = translations.today || 'Bugun';
    document.getElementById('tomorrowBtn').textContent = translations.tomorrow || 'Ertaga';

    // Update following tab - 3 til uchun
    let followTitle = 'Sevimli jamoalaringiz';
    let followDesc = 'Hozircha hech narsa tanlanmagan';

    if (currentLang === 'ru') {
        followTitle = 'Ваши избранные команды';
        followDesc = 'Пока ничего не выбрано';
    } else if (currentLang === 'en') {
        followTitle = 'Your favorite teams';
        followDesc = 'Nothing selected yet';
    }

    document.getElementById('followingTitle').textContent = followTitle;
    document.getElementById('followingDesc').textContent = followDesc;
}

// =============================
// UTILITY FUNCTIONS
// =============================
function groupMatchesByLeague(matches) {
    return matches.reduce((acc, match) => {
        const leagueId = match.league_id;
        if (!acc[leagueId]) {
            acc[leagueId] = [];
        }
        acc[leagueId].push(match);
        return acc;
    }, {});
}

function convertToLocalTime(utcString) {
    if (!utcString) return '--:--';

    const date = new Date(utcString);
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

function getTimeAgo(utcString) {
    if (!utcString) return '';

    const date = new Date(utcString);
    const now = new Date();
    const diffMs = now - date;
    const diffHours = Math.floor(diffMs / (1000 * 60 * 60));
    const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));

    if (currentLang === 'ru') {
        if (diffHours < 1) return 'Только что';
        if (diffHours < 24) return `${diffHours} ч. назад`;
        if (diffDays === 1) return 'Вчера';
        return `${diffDays} дн. назад`;
    } else if (currentLang === 'en') {
        if (diffHours < 1) return 'Just now';
        if (diffHours < 24) return `${diffHours}h ago`;
        if (diffDays === 1) return 'Yesterday';
        return `${diffDays}d ago`;
    } else {
        if (diffHours < 1) return 'Hozirgina';
        if (diffHours < 24) return `${diffHours} soat oldin`;
        if (diffDays === 1) return 'Kecha';
        return `${diffDays} kun oldin`;
    }
}

function getDefaultTranslations() {
    return {
        matches: "O'yinlar",
        news: "Yangiliklar",
        leagues: "Ligalar",
        following: "Sevimli",
        today: "Bugun",
        yesterday: "Kecha",
        tomorrow: "Ertaga"
    };
}
