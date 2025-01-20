const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3001;

// Replace with your Groq API key
const GROQ_API_KEY = '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';
const GROQ_API_URL = 'https://api.groq.com/openai/v1/chat/completions';

app.use(bodyParser.json());

// Proxy endpoint
app.post('/completions', async (req, res) => {
  try {
    const { messages, model } = req.body;

    const response = await axios.post(
      GROQ_API_URL,
      { model, messages },
      {
        headers: {
          Authorization: `Bearer ${GROQ_API_KEY}`,
          'Content-Type': 'application/json',
        },
      }
    );

    res.json(response.data);
  } catch (error) {
    console.error('Error:', error.message);
    res.status(500).json({ error: error.message });
  }
});

app.listen(PORT, () => {
  console.log(`Proxy server running on http://localhost:${PORT}`);
});
