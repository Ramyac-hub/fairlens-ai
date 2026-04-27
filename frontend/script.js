async function sendMessage(message) {
  const res = await fetch("https://fairlens-ai-6.onrender.com", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      message: message
    })
  });

  const data = await res.json();
  return data.reply;
}