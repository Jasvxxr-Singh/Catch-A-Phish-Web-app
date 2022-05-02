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

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password


class Question:
    def __init__(self, q_id: int, sender_address: str, email_subject: str, email_content: str, is_legitimate: bool, reason: str):
        if q_id == "" or not isinstance(q_id, int):
            self.__q_id = None
        else:
            self.__q_id = q_id

        if sender_address == "" or not isinstance(sender_address, str):
            self.__sender_address = None
        else:
            self.__sender_address = sender_address.strip()

        if email_subject == "" or not isinstance(email_subject, str):
            self.__email_subject = None
        else:
            self.__email_subject = email_subject.strip()

        if email_content == "" or not isinstance(email_content, str):
            self.__email_content = None
        else:
            self.__email_content = email_content.strip()
            
        if is_legitimate == "" or not isinstance(is_legitimate, bool):
            self.__is_legitimate = None
        else:
            self.__is_legitimate = is_legitimate

        if reason == "" or not isinstance(reason, str):
            self.__reason = None
        else:
            self.__reason = reason.strip()


    @property
    def question_id(self):
        return self.__q_id

    @property
    def sender_address(self):
        return self.__sender_address

    @property
    def email_subject(self):
        return self.__email_subject

    @property
    def email_content(self):
        return self.__email_content
    
    @property
    def is_legitimate(self):
        return self.__is_legitimate

    @property
    def reason(self):
        return self.__reason



        
    # q_id = -1
    # question = ""
    # option1 = ""
    # option2 = ""
    # correctOption = -1

    """
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
    """
