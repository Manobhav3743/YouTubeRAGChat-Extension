document.addEventListener('DOMContentLoaded', async function () {
  // Get the current tab's URL
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  let url = tab.url;

  // Only enable if on a YouTube video page
  if (!url.includes("youtube.com/watch")) {
    document.getElementById('answer').innerText = "Not a YouTube video page.";
    document.getElementById('askBtn').disabled = true;
    return;
  }

  document.getElementById('askBtn').addEventListener('click', async function () {
  const question = document.getElementById('question').value;
  document.getElementById('answer').innerText = "Thinking...";
  try {
    const response = await fetch("http://localhost:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ video_url: url, question: question })
    });
    if (!response.ok) throw new Error("Server error");
    const data = await response.json();
    document.getElementById('answer').innerText = data.answer;
  } catch (e) {
    document.getElementById('answer').innerText = "Error: " + e.message;
  }
});
});