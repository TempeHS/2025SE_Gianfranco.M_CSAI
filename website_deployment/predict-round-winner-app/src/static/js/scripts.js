document.addEventListener("DOMContentLoaded", function () {
  const predictionForm = document.getElementById("prediction-form");
  const predictionResult = document.getElementById("prediction-result");
  const trainingForm = document.getElementById("training-form");

  predictionForm.addEventListener("submit", function (event) {
    event.preventDefault();
    const formData = new FormData(predictionForm);

    fetch("/predict", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        predictionResult.innerHTML = `Predicted Winner: ${data.winner}`;
      })
      .catch((error) => {
        console.error("Error:", error);
        predictionResult.innerHTML =
          "ERRORS occurred while making the prediction.";
      });
  });

  trainingForm.addEventListener("submit", function (event) {
    event.preventDefault();
    const formData = new FormData(trainingForm);

    fetch("/train", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        alert(data.message);
        trainingForm.reset();
      })
      .catch((error) => {
        console.error("Error:", error);
        alert("ERRORS occurred while retraining the model.");
      });
  });
});
