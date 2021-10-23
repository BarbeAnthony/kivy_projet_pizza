import json


class StorageManager:

    def load_datas(self, data_name):
        file_name = self.get_file_name(data_name)
        try:
            file = open(file_name, "r")
            data_str = file.read()
            file.close()
        except:
            return None
        return json.loads(data_str)

    def save_datas(self, data_name, data_content):
        file_name = self.get_file_name(data_name)
        file = open(file_name, "w")
        file.write(json.dumps(data_content))
        file.close()

    def get_file_name(self, data_name):
        return data_name + ".json"
