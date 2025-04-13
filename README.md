📼 MKV to MP4 Batch Converter

A lightweight Python script that batch converts .mkv files to .mp4 using ffmpeg. It directly copies the video stream to avoid re-encoding and converts the audio stream to AAC format for better compatibility.
🚀 Features

    🔄 Batch Conversion – processes all .mkv files in a folder.

    ⚡ Fast – skips video re-encoding for speed.

    🎧 Audio Compatibility – re-encodes audio to AAC for broader device support.

    🧹 Simple CLI – just enter your input and output folder paths.

🛠 Requirements

    Python 3.6+

    ffmpeg must be installed and accessible from your system's PATH

You can test if it's installed with:

ffmpeg -version

📦 Installation

    Clone the repo or download the script:

git clone https://github.com/your-username/mkv-to-mp4-converter.git
cd mkv-to-mp4-converter

    (Optional) Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

🧪 Usage

Run the script:

python convert.py

You'll be prompted to enter:

    The input folder containing .mkv files.

    The output folder where .mp4 files will be saved.

Example output:

Enter the folder path containing MKV files: /path/to/input
Enter the folder path to save converted MP4 files: /path/to/output
Converting: myvideo.mkv
 → Output: /path/to/output/myvideo_converted.mp4
✅ Success!

📁 Output Format

Converted files are saved with a _converted suffix:

example.mkv → example_converted.mp4

⚠️ Notes

    If a file with the same name already exists in the output folder, it will be overwritten.

    Video is copied directly, audio is re-encoded to AAC.

📄 License

MIT – do whatever you want, just don't blame me if something breaks. 😄
