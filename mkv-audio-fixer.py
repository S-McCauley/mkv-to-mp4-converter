import os
import subprocess

def convert_all_mkv_to_mp4(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".mkv"):
            input_path = os.path.join(input_folder, filename)
            output_filename = filename.rsplit(".", 1)[0] + "_converted.mp4"
            output_path = os.path.join(output_folder, output_filename)

            print(f"Converting: {filename}")
            print(f" → Output: {output_path}")

            cmd = [
                "ffmpeg",
                "-i", input_path,
                "-c:v", "copy",        # copy video (no re-encode)
                "-c:a", "aac",         # re-encode audio to AAC
                "-y",                  # overwrite if exists
                output_path
            ]

            try:
                subprocess.run(cmd, check=True)
                print("✅ Success!\n")
            except subprocess.CalledProcessError:
                print(f"❌ Failed to convert {filename}\n")

if __name__ == "__main__":
    input_folder = input("Enter the folder path containing MKV files: ").strip()
    output_folder = input("Enter the folder path to save converted MP4 files: ").strip()

    if not os.path.isdir(input_folder):
        print("❌ Invalid input folder path.")
    elif not output_folder:
        print("❌ Invalid output folder path.")
    else:
        convert_all_mkv_to_mp4(input_folder, output_folder)
