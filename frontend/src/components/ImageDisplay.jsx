const ImageDisplay = ({ image, loading }) => {
    return (
        <div className="mt-8">
            {loading && <p className="text-gray-700">Generating image...</p>}
            {image && (
                <div className="bg-white shadow-md rounded p-4">
                    <img src={image} alt="Generated" className="max-w-full h-auto rounded" />
                </div>
            )}
            {!image && !loading && <p className="text-gray-700">No image generated yet.</p>}
        </div>
    );
};
export default ImageDisplay;