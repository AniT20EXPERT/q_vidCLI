import os
from transcoder import transcode_video
from utils import get_video_metadata
from quality_metrics import detect_blurriness
import matplotlib.pyplot as plt
import statistics

INPUT_VIDEO = "input/sample.mp4"
OUTPUT_DIR = "output/"


def generate_report(video_outputs):
    print("\n Video Analysis Report\n")

    report_lines = [
        "# Video Analysis Report",
        ""
    ]

    for label, path in video_outputs.items():
        meta = get_video_metadata(path)
        blur_scores = detect_blurriness(path)
        avg_blur = round(statistics.mean(blur_scores), 2)

        codec = meta['streams'][0]['codec_name']
        width = meta['streams'][0]['width']
        height = meta['streams'][0]['height']
        bitrate = meta['format'].get('bit_rate', 'N/A')

        print(f" {label.upper()} — {os.path.basename(path)}")
        print(f"   • Codec: {codec}")
        print(f"   • Resolution: {width}x{height}")
        print(f"   • Bitrate: {bitrate} bps")
        print(f"   • Avg Blur Score: {avg_blur}\n")

        report_lines.append(f"## {label.upper()} — `{os.path.basename(path)}`")
        report_lines.append(f"- **Codec:** {codec}")
        report_lines.append(f"- **Resolution:** {width}x{height}")
        report_lines.append(f"- **Bitrate:** {bitrate} bps")
        report_lines.append(f"- **Average Blur Score:** {avg_blur}")
        report_lines.append("")

        # Plot blurriness
        plt.plot(blur_scores, label=label)

    # Save plot
    blur_plot_path = os.path.join(OUTPUT_DIR, "blur_plot.png")
    plt.title("Blurriness Scores Across Frames")
    plt.xlabel("Frame Sample")
    plt.ylabel("Laplacian Variance")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(blur_plot_path)
    plt.close()

    # Add plot to report
    report_lines.append("![Blur Score Plot](blur_plot.png)")
    report_lines.append("")

    # Write Markdown report
    with open(os.path.join(OUTPUT_DIR, "report.md"), "w") as f:
        f.write("\n".join(report_lines))


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    outputs = transcode_video(INPUT_VIDEO, OUTPUT_DIR)
    generate_report(outputs)
