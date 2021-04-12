function download() {
  let url = document.getElementById("url").value
  let format = document.getElementById("format").value
  eel.download({url, format})
  postData().then(data => console.log(data))
}






async function postData(url = 'https://httpbin.org/post', data = {}) {

  const response = await fetch(url, {
    method: 'POST',
    mode: 'cors',
    cache: 'no-cache',
    headers: {
      'Content-Type': 'application/json'
    },
    referrerPolicy: 'no-referrer',
    body: JSON.stringify(data)
  });
  return response.json();
}
