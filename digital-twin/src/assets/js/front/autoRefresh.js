function setAutoRefresh() {
    let content = ""
    let setAutoRefresh = localStorage.getItem("autorefresh");
    let elem = document.querySelector("#autorefresh");
    if (setAutoRefresh == "true") {
        parkingMap.startAutoRefresh();
        elem.checked = true;
    } else {
        content = `<input class="form-check-input" type="checkbox" role="switch" id="autorefresh"/>`
        parkingMap.stopAutoRefresh();
        elem.checked = false;
    }
}

$(function () {
    setAutoRefresh()
    $('#autorefresh').change(function () {
        if (this.checked) {
            localStorage.setItem("autorefresh", "true")
            parkingMap.startAutoRefresh();
        } else {
            localStorage.setItem("autorefresh", "false")
            parkingMap.stopAutoRefresh();
        }
    });
    currentTime();
    getServerStatus();
    document.querySelectorAll("#refresh, #refreshModal").forEach((ele) => {
        ele.addEventListener("click", function (e) {
            ele.innerHTML = `<div class="spinner-border spinner-border-sm" role="status"><span class="sr-only">Loading...</span></div> Refreshing`;
            parkingMap.refreshZonas();
        });
    });
})
