# Finger Counter using Hand Tracking

<p>This project is a real-time finger-counting application that utilizes computer vision and machine learning techniques to detect and count the number of fingers displayed in front of a camera. It leverages OpenCV for image processing and MediaPipe for hand detection and tracking.</p>
    
## Features   
1-Real-time finger detection and counting using a webcam.<br>
2-Displays corresponding images based on the number of detected fingers.<br>
3-Simple and intuitive user interface.<br>
    

## Requirements
--Python 3.x.<br>
--OpenCV.<br>
--MediaPipe.<br>
--NumPy .<br>
   

## Installation
Clone the repository:<be>
git clone https://github.com/yourusername/finger-counter.git<br>
cd finger-counter<be>
        
#### Create a virtual environment 
python -m venv venv.<br>
source venv/bin/activate # On Windows use `venv\Scripts\activate`.<br>
#### Install the required packages
pip install -r requirements.txt.<br>
   

## Usage
  
 Prepare the images: Place the images you want to display based on the finger count in a folder named <code>images</code>. Make sure the images are named appropriately.<br>
Run the application<br>
    
#### instructions: 
Use your webcam to display different numbers of fingers. The application will detect the number of fingers and display the corresponding image along with the finger count.<br>
   

## File Structure
The main script to run the finger counter application.<br>
Contains the <code>handDetector</code> class for hand detection and tracking using MediaPipe.<br>
 Folder containing images to be displayed based on the detected finger count.<br>
List of required Python packages.<br>
