from dataclasses import dataclass


@dataclass
class Form:
    name: str
    id: int

    def get_id(self):
        return self.id

    def set_id(self, new_id):
        self.id = new_id



form = Form("Scott", 112)


print(form.get_id())
print(form)
form.set_id(2245)

print(form)