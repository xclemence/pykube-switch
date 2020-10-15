
class Cluster(object):
    display_name = ""
    name = ""
    password = ""
    file_name = ""
    server = ""

    def __init__(self, display_name, name, file_name, server, password=""):
        self.display_name = display_name
        self.name = name
        self.file_name = file_name
        self.password = password
        self.server = server
