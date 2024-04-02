class Something:
    def __enter__(self):
        print("Entering")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting")


with Something() as hello:
    print("I'm inside")
