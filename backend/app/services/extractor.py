from pathlib import Path
import ffmpeg


class AudioExtractor:

    def __init__(self):
        self.output_folder = Path("processed_audio")
        self.output_folder.mkdir(exist_ok=True)

    def extract_audio(self, input_file: str):

        input_path = Path(input_file)

        if not input_path.exists():
            raise FileNotFoundError(
                f"Input file does not exist: {input_path}"
            )

        output_path = self.output_folder / f"{input_path.stem}.wav"

        try:
            (
                ffmpeg
                .input(str(input_path))
                .output(
                    str(output_path),
                    ac=1,
                    ar=16000,
                    format="wav"
                )
                .overwrite_output()
                .run(capture_stdout=True, capture_stderr=True)
            )

            return str(output_path)

        except ffmpeg.Error as e:
            print("=" * 60)
            print("FFMPEG ERROR")
            print("=" * 60)

            if e.stdout:
                print("STDOUT:")
                print(e.stdout.decode("utf-8", errors="ignore"))

            if e.stderr:
                print("STDERR:")
                print(e.stderr.decode("utf-8", errors="ignore"))

            raise