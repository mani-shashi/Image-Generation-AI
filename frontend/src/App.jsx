import PromptForm from './components/PromptForm';
import ImageDisplay from './components/ImageDisplay';
import { useState } from 'react';
function App() {
    const [image, setImage] = useState(null);
    const [loading, setLoading] = useState(false);
    return (
        <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center">
            <h1 className="text-4xl font-bold mb-8">Text-to-Image Generator</h1>
            <PromptForm setImage={setImage} setLoading={setLoading} />
            <ImageDisplay image={image} loading={loading} />
        </div>
    );
}
export default App;