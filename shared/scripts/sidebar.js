(function () {
  var sections = [
    { number: '00', dir: '00-home', title: 'Welcome', subtitle: '세션 소개', type: 'lecture', part: 1 },
    { number: '01', dir: '01-ai-foundation', title: 'AI Foundation', subtitle: 'Claude AI 기초', type: 'lecture', part: 1 },
    { number: '02', dir: '02-claude-code-features', title: 'Claude Code Features', subtitle: 'Claude Code 사용법', type: 'lecture+demo', part: 1 },
    { number: '03', dir: '03-mcp-architecture', title: 'MCP Architecture', subtitle: 'MCP 아키텍처', type: 'lecture+hands-on', part: 1 },
    { number: '04', dir: '04-genie-mcp', title: 'MCP', subtitle: 'Genie MCP 서버 만들기', type: 'hands-on', part: 2 },
    { number: '05', dir: '05-skills', title: 'Skills', subtitle: '개념에서 실전까지', type: 'lecture+hands-on', part: 2 },
    { number: '06', dir: '06-agents', title: 'Agents', subtitle: '나만의 에이전트 만들기', type: 'lecture+hands-on', part: 2 },
    { number: '07', dir: '07-hooks', title: 'Hooks', subtitle: '이벤트 기반 자동화', type: 'lecture+hands-on', part: 2 },
    { number: '08', dir: '08-ai-dev-kit', title: 'AI Dev Kit', subtitle: 'Databricks AI Dev Kit', type: 'lecture+demo', part: 2 },
    { number: '09', dir: '09-google-slides', title: 'Google Slides', subtitle: 'Vibe Coding으로 슬라이드 자동화', type: 'lecture+demo', part: 3 }
  ];

  function detectCurrentSection() {
    var path = window.location.pathname;
    for (var i = 0; i < sections.length; i++) {
      if (path.indexOf(sections[i].dir) !== -1) return sections[i].dir;
    }
    return null;
  }

  function buildSidebar() {
    var current = detectCurrentSection();
    var list = document.querySelector('.sidebar-sections');
    if (!list) return;

    var partNames = { 1: 'AI Literacy', 2: 'Vibe with Databricks', 3: 'Vibe for SA' };
    var currentPart = 0;

    sections.forEach(function (s) {
      if (s.part !== currentPart) {
        currentPart = s.part;
        var divider = document.createElement('li');
        divider.className = 'sidebar-part-divider';
        divider.textContent = 'Part ' + s.part + ': ' + partNames[s.part];
        list.appendChild(divider);
      }

      var li = document.createElement('li');
      if (s.dir === current) li.className = 'current';

      li.innerHTML =
        '<a href="../../sections/' + s.dir + '/index.html">' +
          '<span class="section-num">' + s.number + '</span>' +
          '<span class="section-detail">' +
            '<span class="section-title">' + s.title + '</span>' +
            '<span class="section-subtitle">' + s.subtitle + '</span>' +
          '</span>' +
        '</a>';

      list.appendChild(li);
    });
  }

  function initSidebar() {
    var toggle = document.getElementById('sidebar-toggle');
    var sidebar = document.getElementById('sidebar');
    var overlay = document.getElementById('sidebar-overlay');
    if (!toggle || !sidebar || !overlay) return;

    function open() {
      sidebar.classList.add('open');
      overlay.classList.add('active');
      toggle.classList.add('active');
    }

    function close() {
      sidebar.classList.remove('open');
      overlay.classList.remove('active');
      toggle.classList.remove('active');
    }

    toggle.addEventListener('click', function () {
      sidebar.classList.contains('open') ? close() : open();
    });

    overlay.addEventListener('click', close);

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') close();
    });

    buildSidebar();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSidebar);
  } else {
    initSidebar();
  }
})();
