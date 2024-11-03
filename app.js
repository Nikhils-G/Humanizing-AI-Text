document.getElementById('textForm').addEventListener('submit', async function (e) {
    e.preventDefault();
    const userInput = document.getElementById('userInput').value;
    const outputBox = document.getElementById('output');
    outputBox.textContent = 'Generating...';

    try {
        const response = await fetch('http://localhost:5000/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ prompt: userInput }),
        });
        
        if (response.ok) {
            const data = await response.json();
            outputBox.textContent = data.generated_text;
        } else {
            outputBox.textContent = 'Error generating text. Please try again.';
        }
    } catch (error) {
        outputBox.textContent = 'An error occurred. Please check your connection and try again.';
        console.error('Error:', error);
    }
});
