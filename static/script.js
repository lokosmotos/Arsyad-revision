function checkAnswer() {
  const answer = document.getElementById("answer").value;
  if (answer.includes("saya suka membaca buku")) {
    document.getElementById("feedback").style.display = "block";
  }
}
