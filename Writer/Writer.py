import joblib
class writer:
    @staticmethod
    def save_object(obj,filename):
        joblib.dump(obj, filename)
        print(f"Object saved to {filename}")