class User:

    def __init__(self, user_name: str, password: str):
        if user_name == "" or not isinstance(user_name, str):
            self.__user_name = None
        else:
            self.__user_name = user_name.strip()

        if password == "" or not isinstance(password, str) or len(password) < 7:
            self.__password = None
        else:
            self.__password = password

        self.__read_books = []
        self.__reviews = []
        self.__pages_read = 0

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password


class Questions:
    # q_id = -1
    # question = ""
    # option1 = ""
    # option2 = ""
    # correctOption = -1

    def __init__(self, q_id: int, question: str, option1: str, option2: str, correctoption: int):
        self.option1 = option1 # we could change it into self.__option as a private varibale if u want
        self.option2 = option2
        self.q_id = q_id
        self.question = question
        self.correctoption = correctoption

    def getQ_id(self):
        return self.q_id

    def getQuestion(self):
        return self.question

    def getOption1(self):
        return self.option1

    def getOption2(self):
        return self.option2

    def getCorrectionOption(self):
        return self.correctoption

    def get_correct_option(self):
        if self.correctoption == 1:
            return self.option1
        elif self.correctoption == 2:
            return self.option2
