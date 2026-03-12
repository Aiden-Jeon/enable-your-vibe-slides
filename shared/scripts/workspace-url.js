/**
 * workspace-url.js
 * Fetches the workspace URL from /api/config and substitutes
 * data-workspace-url / data-workspace-profile placeholders.
 */
(function () {
  var FALLBACK_URL = "https://<workspace-url>.cloud.databricks.com";
  var FALLBACK_PROFILE = "<workspace-profile>";

  function applyValues(url, profile) {
    document.querySelectorAll("[data-workspace-url]").forEach(function (el) {
      el.textContent = url;
    });
    document.querySelectorAll("[data-workspace-profile]").forEach(function (el) {
      el.textContent = profile;
    });
    // Replace href placeholders: data-workspace-href="/ml/playground"
    // → href="https://<workspace>/ml/playground"
    document.querySelectorAll("[data-workspace-href]").forEach(function (el) {
      var path = el.getAttribute("data-workspace-href");
      el.href = url + path;
    });
  }

  function extractProfile(url) {
    try {
      var hostname = new URL(url).hostname; // e.g. "e2-demo-field-eng.cloud.databricks.com"
      return hostname.split(".")[0];         // e.g. "e2-demo-field-eng"
    } catch (_) {
      return FALLBACK_PROFILE;
    }
  }

  function ensureProtocol(url) {
    if (url && !/^https?:\/\//.test(url)) {
      return "https://" + url;
    }
    return url;
  }

  fetch("/api/config")
    .then(function (res) { return res.json(); })
    .then(function (data) {
      if (data.workspace_url) {
        var url = ensureProtocol(data.workspace_url);
        applyValues(url, extractProfile(url));
      } else {
        applyValues(FALLBACK_URL, FALLBACK_PROFILE);
      }
    })
    .catch(function () {
      applyValues(FALLBACK_URL, FALLBACK_PROFILE);
    });
})();
