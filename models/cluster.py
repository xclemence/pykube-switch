class Cluster:
    display_name = ""
    name =  ""
    password = ""
    file_name = ""

    def __init__(self, display_name, name, file_name, password=""):
        self.display_name = display_name
        self.name = name
        self.file_name = file_name
        self.password = password

