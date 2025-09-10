async function translateText() {
    const text = document.getElementById('inputText').value;
    if (!text) {
        alert('Please enter some text!');
        return;
    }
    
    const response = await fetch('/translate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text })
    });
    
    if (response.ok) {
        const result = await response.json();
        document.getElementById('result').innerText = `Translation: ${result.translation}`;
    } else {
        document.getElementById('result').innerText = 'Error: Could not translate.';
    }
}