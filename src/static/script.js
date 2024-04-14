function handleFile(file) {
  window.open("/result", "_blank");
}

if (document.getElementById("file")) {
  document.getElementById("file").addEventListener("change", function (event) {
    const file = event.target.files[0];
    handleFile(file);
  });
}

if (document.getElementById("download-csv")) {
  document
    .getElementById("download-csv")
    .addEventListener("click", function () {
      window.open("/download");
    });
}

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
