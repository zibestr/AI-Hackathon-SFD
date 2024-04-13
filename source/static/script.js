// async function handleFile(file) {
//     await axios.post("/get_file", file).then(function (response) {
//       console.log(response.data);
//      });
//   window.open("result.html", "_blank");
// }

document.getElementById("/get_file").addEventListener("change", function (event) {
  window.open("/send", "_blank");
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
    window.open("/send", "_blank");
  } else {
    alert("Перетащите CSV или JSON файл.");
  }
});
