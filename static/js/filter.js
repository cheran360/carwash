let searchInput = document.getElementById("location");
let dateInput = document.getElementById("inputdate");

const rows = document.querySelectorAll("tbody tr");
searchInput.addEventListener("keyup", function (event) {
  const q = event.target.value.toLowerCase();
  rows.forEach((row) => {
    row.querySelectorAll("td")[1].textContent.toLowerCase().startsWith(q)
      ? (row.style.display = "")
      : (row.style.display = "none");
  });
});

dateInput.addEventListener("change", function (event) {
  console.log(event.target.value);
});
