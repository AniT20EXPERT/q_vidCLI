import subprocess
import os

def transcode_video(input_path, output_dir):
    resolutions = {
        "480p": "640x480",
        "720p": "1280x720",
        "1080p": "1920x1080"
    }

    base = os.path.splitext(os.path.basename(input_path))[0]
    output_files = {}

    for label, res in resolutions.items():
        output_file = os.path.join(output_dir, f"{base}_{label}.mp4")
        cmd = [
            "ffmpeg", "-y", "-i", input_path,
            "-vf", f"scale={res}",
            "-c:v", "libx264", "-preset", "fast",
            "-c:a", "aac", output_file
        ]
        subprocess.run(cmd, check=True)
        output_files[label] = output_file

    return output_files
