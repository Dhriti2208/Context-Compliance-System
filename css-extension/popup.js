document.getElementById("scanBtn").addEventListener("click", async () => {

  try {

    const response = await fetch("http://127.0.0.1:8001/analyze");

    const data = await response.json();

    // update counts
    document.getElementById("violations").innerText = data.violations;

    document.getElementById("compliant").innerText = data.compliant;

    // update score
    document.getElementById("score").innerText = data.risk_score;

    // update risk label
    document.getElementById("risk").innerText =
      data.risk_score > 0.5 ? "HIGH RISK" : "LOW RISK";

  } catch (error) {

    console.error(error);

    document.getElementById("score").innerText = "Error";

    document.getElementById("risk").innerText = "Backend not running";

  }

});