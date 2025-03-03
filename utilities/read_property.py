import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\kirit\\PycharmProjects\\ParaBank Banking\\Configuration\\config.ini")


class Read_Config:
    @staticmethod
    def get_url():
        pro_url = config.get('Home info', 'project')
        return pro_url

    @staticmethod
    def get_first():
        first_name = config.get('Home info', 'first')
        return first_name

    @staticmethod
    def get_last():
        last_name = config.get('Home info', 'last')
        return last_name

    @staticmethod
    def get_address():
        address = config.get('Home info', 'address')
        return address

    @staticmethod
    def get_city():
        city = config.get('Home info', 'city')
        return city

    @staticmethod
    def get_zip():
        zip = config.get('Home info', 'zip')
        return zip

    @staticmethod
    def get_state():
        state = config.get('Home info', 'state')
        return state

    @staticmethod
    def get_ssn():
        ssn = config.get('Home info', 'ssn')
        return ssn

   # @staticmethod
    #def get_username():
     #   username = config.get('Home info', 'username')
      #  return username

    @staticmethod
    def get_password():
        password = config.get('Home info', 'password')
        return password

    @staticmethod
    def get_confirm():
        confirm = config.get('Home info', 'confirm')
        return confirm
