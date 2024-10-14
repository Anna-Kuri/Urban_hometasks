import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return self.nickname

    def __eq__(self, otherUser):
        return self.nickname == otherUser.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def __contains__(self, word):
        return word.lower() in self.title.lower()


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and hash(user.password) == hash(password):
                self.current_user = user
                return

    def register(self, nickname, password, age):
        newUser = User(nickname, password, age)

        for user in self.users:
            if user == newUser:
                print(f"Пользователь {nickname} уже существует")
                return

        self.users.append(newUser)

        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        videoTitles = [video.title for video in self.videos]

        for newVideo in args:
            if newVideo.title not in videoTitles:
                self.videos.append(newVideo)

    def get_videos(self, searchWord):
        matchedVideos = []

        for video in self.videos:
            if searchWord in video:
                matchedVideos.append(video)

        return matchedVideos

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if title == video.title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста, покиньте страницу")
                    return
                while video.time_now < video.duration:
                    time.sleep(1)
                    print(video.time_now + 1, end=" ", flush=True)
                    video.time_now += 1
                print("Конец видео")
                video.time_now = 0


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')