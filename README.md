<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Finger Counter using Hand Tracking</title>
</head>
<body>
    <h1>Finger Counter using Hand Tracking</h1>
    <p>This project is a real-time finger counting application that utilizes computer vision and machine learning techniques to detect and count the number of fingers displayed in front of a camera. It leverages OpenCV for image processing and MediaPipe for hand detection and tracking.</p>
    
    <h2>Features</h2>
    <ul>
        <li>Real-time finger detection and counting using a webcam.</li>
        <li>Displays corresponding images based on the number of detected fingers.</li>
        <li>Simple and intuitive user interface.</li>
    </ul>

    <h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li>OpenCV</li>
        <li>MediaPipe</li>
        <li>NumPy (optional)</li>
    </ul>

    <h2>Installation</h2>
    <ol>
        <li><p>Clone the repository:</p>
        <pre><code>git clone https://github.com/yourusername/finger-counter.git
cd finger-counter</code></pre></li>
        
        <li><p>Create a virtual environment (optional but recommended):</p>
        <pre><code>python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`</code></pre></li>
        
        <li><p>Install the required packages:</p>
        <pre><code>pip install -r requirements.txt</code></pre></li>
    </ol>

    <h2>Usage</h2>
    <ol>
        <li><p>Prepare the images: Place the images you want to display based on the finger count in a folder named <code>images</code>. Make sure the images are named appropriately (e.g., <code>1.png</code>, <code>2.png</code>, etc.).</p></li>
        <li><p>Run the application:</p>
        <pre><code>python main.py</code></pre></li>
        <li><p>Instructions: Use your webcam to display different numbers of fingers. The application will detect the number of fingers and display the corresponding image along with the finger count.</p></li>
    </ol>

    <h2>File Structure</h2>
    <ul>
        <li><code>main.py</code>: The main script to run the finger counter application.</li>
        <li><code>Module.py</code>: Contains the <code>handDetector</code> class for hand detection and tracking using MediaPipe.</li>
        <li><code>images/</code>: Folder containing images to be displayed based on the detected finger count.</li>
        <li><code>requirements.txt</code>: List of required Python packages.</li>
    </ul>

</body>
</html>
