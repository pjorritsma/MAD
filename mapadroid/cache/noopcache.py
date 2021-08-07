class NoopCache:
    def set(self, key, value, ex=None):
        pass

    def get(self, key):
        pass

    def exists(self, key):
        return False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass
