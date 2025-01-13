document.getElementById("calculate-btn").addEventListener("click", function () {
    // Get height and weight values
    const height = parseFloat(document.getElementById("height").value);
    const weight = parseFloat(document.getElementById("weight").value);

    // Validate inputs
    if (isNaN(height) || isNaN(weight) || height <= 0 || weight <= 0) {
        document.getElementById("result").innerText = "Please enter valid height and weight.";
        return;
    }

    // Calculate BMI
    const bmi = (weight / ((height / 100) ** 2)).toFixed(2);

    // Determine BMI category
    let category = "";
    if (bmi < 18.5) {
        category = "Underweight";
    } else if (bmi >= 18.5 && bmi < 24.9) {
        category = "Normal weight";
    } else if (bmi >= 25 && bmi < 29.9) {
        category = "Overweight";
    } else {
        category = "Obesity";
    }

    // Display result
    document.getElementById("result").innerText = `Your BMI is ${bmi} (${category}).`;
});
