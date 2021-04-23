function download() {
  let url = document.getElementById("url").value;
  let format = document.getElementById("format").value;
  eel.download({ url, format });
  postData().then((data) => console.log(data));
}

async function postData(url = "https://httpbin.org/post", data = {}) {
  const response = await fetch(url, {
    method: "POST",
    mode: "cors",
    cache: "no-cache",
    headers: {
      "Content-Type": "application/json",
    },
    referrerPolicy: "no-referrer",
    body: JSON.stringify(data),
  });
  return response.json();
}

function update_progress(percent) {
  let bar = document.querySelector("#progress");
  bar.style.display = 'flex';
  bar.style.width = `${percent}%`;
  if (percent === 100){
    bar.style.display = 'none'
  }
}

window.eel.expose(update_progress);
