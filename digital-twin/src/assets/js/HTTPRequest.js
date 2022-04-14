class HTTPRequest{

    
    static async POST(url, data) {
        let xhr = new XMLHttpRequest();
        xhr.withCredentials = true;
        xhr.open("POST", url);
        
        xhr.setRequestHeader("content-type", "application/x-www-form-urlencoded");
        xhr.setRequestHeader("cache-control", "no-cache");

        xhr.onload = () => callback(xhr.responseText);

        xhr.send(data); 
        
    }
}