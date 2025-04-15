function RunSentimentAnalysis() {
    // Get the text input from the user
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    // Get the system response div
    const systemResponseDiv = document.getElementById("system_response");

    // Clear previous results and show a loading message
    systemResponseDiv.innerHTML = "Analyzing emotions... Please wait.";

    // Check if the input is empty
    if (!textToAnalyze.trim()) {
        systemResponseDiv.innerHTML = "Please enter some text to analyze.";
        return;
    }

    // Send a POST request to the Flask server
    fetch('/detect_emotion', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: textToAnalyze }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Server error: ${response.status} ${response.statusText}`);
        }
        return response.json();
    })
    .then(data => {
        // Display the response in the system_response div
        if (data.error) {
            systemResponseDiv.innerHTML = `<span style="color: red;">Error: ${data.error}</span>`;
        } else {
            // Format the response as normal text
            let formattedResponse = "<strong>Detected Emotions:</strong><br>";
            data.forEach(emotion => {
                const label = (emotion.label || "Unknown").toUpperCase(); // Convert label to uppercase
                const score = (emotion.score !== undefined && emotion.score !== null) 
                    ? (emotion.score * 100).toFixed(2) 
                    : "0.00";
                formattedResponse += `- <strong>${label}</strong>: ${score}%<br>`;
            });
            systemResponseDiv.innerHTML = formattedResponse;
        }
    })
    .catch(error => {
        // Display error message in case of network or server issues
        systemResponseDiv.innerHTML = `<span style="color: red;">Error: ${error.message}</span>`;
    });
}