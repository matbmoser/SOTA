class HTTPRequest{

    static async POST(url, data, tag) {
        var xhr = new XMLHttpRequest();
        xhr.withCredentials = true;
  
        xhr.addEventListener("readystatechange", function () {
          if (this.readyState === 4) {
            callback(this.responseText, tag);
          }
        });
  
        xhr.open("POST", url);
        xhr.setRequestHeader("content-type", "application/x-www-form-urlencoded");
        xhr.setRequestHeader("cache-control", "no-cache");
  
        xhr.send(data);
    }
    static async GET(url, data, tag){

      var xhr = new XMLHttpRequest();
      xhr.withCredentials = true;

      xhr.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
          callback(this.responseText, tag);
        }
      });

      xhr.open("GET", url);
      xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

      xhr.send(data);
    }
}