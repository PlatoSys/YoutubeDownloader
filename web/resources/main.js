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

function callEndpoint() {
  setTimeout(function(){
      document.querySelector('#dismiss-modal').click();
  }, 1000);
}

function update_progress(percent) {
  percent = parseInt(percent)
  let bar = document.querySelector("#progress");
  let wrapper = document.querySelector('#wrapper-bar');
  bar.style.width = `${percent}%`;
  wrapper.style.opacity = "100%";
}
 function finish_download(){
    document.querySelector('#modal-button').click();
    callEndpoint();
}

window.eel.expose(update_progress);
window.eel.expose(finish_download);


