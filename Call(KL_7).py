class Helper:
    def __init__(self, work):
        self.work = work
    def __call__(self, new_work):
        return f'I will help you with your {self.work}. Afterwards I will help you with {new_work}'
helper = Helper('homework')
res = helper('cleaning')
print(res)