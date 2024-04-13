import axios from "https://cdn.jsdelivr.net/npm/axios@1.3.6/+esm";

function handleFile(file) {
  axios.post("/api/data", file).then(function (response) {
    console.log(response.data);
  });
  window.location.replace("result.html");
}

document.getElementById("file").addEventListener("change", function (event) {
  const file = event.dataTransfer.files[0];
  handleFile(file);
});

const dropzone = document.getElementById("dropzone");

dropzone.addEventListener("click", function (event) {
  event.preventDefault();
});

dropzone.addEventListener("dragover", function (event) {
  event.preventDefault();
  dropzone.classList.add("dragover");
});

dropzone.addEventListener("dragleave", function (event) {
  event.preventDefault();
  dropzone.classList.remove("dragover");
});

dropzone.addEventListener("drop", function (event) {
  event.preventDefault();
  dropzone.classList.remove("dragover");
  const file = event.dataTransfer.files[0];

  if (file.type === "text/csv" || file.type === "application/json") {
    handleFile(file);
  } else {
    alert("Перетащите CSV или JSON файл.");
  }
});
