import unittest

from scripts.render_video import format_srt_time, validate_project


class RenderVideoTests(unittest.TestCase):
    def test_format_srt_time_rounds_milliseconds_and_carries(self):
        self.assertEqual(format_srt_time(61.9996), "00:01:02,000")

    def test_validate_project_requires_german_scene_assets(self):
        project = {
            "language": "de",
            "scenes": [
                {"image": "bilder/01.png", "audio": "audio/01.wav", "subtitle": "Ein klarer Satz."}
            ],
        }
        self.assertEqual(validate_project(project), project["scenes"])

    def test_validate_project_rejects_missing_scenes(self):
        with self.assertRaisesRegex(ValueError, "mindestens eine Szene"):
            validate_project({"language": "de", "scenes": []})


if __name__ == "__main__":
    unittest.main()
