class Camera:
    def camera_feature(self):
        return "48MP Resolution"

class MusicPlayer:
    def music_feature(self):
        return "Dolby Atmos Audio"

class Smartphone(Camera, MusicPlayer):
    def show_features(self):
        print(f"Camera: {self.camera_feature()}")
        print(f"Music: {self.music_feature()}")

phone = Smartphone()
phone.show_features()