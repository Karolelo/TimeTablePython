import joblib
class reader:
    @staticmethod
    def read_object(filename):
        loaded_data=joblib.load(filename)
        print(f"loaded object {loaded_data}")
        return loaded_data