const express = require('express');
const axios = require('axios');
const router = express.Router();
const PYTHON_API_URL = process.env.PYTHON_API_URL || 'http://localhost:8000';
router.post('/generate', async (req, res) => {
    try {
        const { prompt } = req.body;
        const response = await axios.post(`${PYTHON_API_URL}/generate`, { prompt });
        res.json(response.data);
    } catch (error) {
        console.error('Error proxying request:', error.message);
        res.status(500).json({ error: 'Failed to generate image' });
    }
});
module.exports = router;