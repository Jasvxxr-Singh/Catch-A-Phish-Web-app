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
        self.__option1 = option1
        self.__option2 = option2
        self.__q_id = q_id
        self.__question = question
        self.__correctoption = correctoption

    def getQ_id(self):
        #print("helllllo")
        return self.__q_id

    def getQuestion(self):
        #print("in queston")
        return self.__question

    def getOption1(self):
        return self.__option1

    def getOption2(self):
        return self.__option2

    def getCorrectionOption(self):
        return self.__correctoption

    def get_correct_option(self):
        if self.__correctoption == 1:
            return self.__option1
        elif self.__correctoption == 2:
            return self.__option2
