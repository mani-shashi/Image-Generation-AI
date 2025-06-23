import { useState } from 'react';
import axios from 'axios';
const PromptForm = ({ setImage, setLoading }) => {
    const [prompt, setPrompt] = useState('');
    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!prompt.trim()) return;
        setLoading(true);
        try {
            const response = await axios.post('http://localhost:3001/api/generate', { prompt });
            setImage(response.data.image);
        } catch (error) {
            console.error('Error generating image:', error);
            alert('Failed to generate image');
        } finally {
            setLoading(false);
        }
    };
    return (
        <div className="w-full max-w-md">
            <form onSubmit={handleSubmit} className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
                <div className="mb-4">
                    <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="prompt">
                        Text Prompt
                    </label>
                    <input
                        className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        id="prompt"
                        type="text"
                        placeholder="Enter a description..."
                        value={prompt}
                        onChange={(e) => setPrompt(e.target.value)}
                    />
                </div>
                <div className="flex items-center justify-between">
                    <button
                        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                        type="submit"
                        disabled={loading}
                    >
                        {loading ? 'Generating...' : 'Generate Image'}
                    </button>
                </div>
            </form>
        </div>
    );
};
export default PromptForm;