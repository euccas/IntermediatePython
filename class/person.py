class Person:
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln

    @property
    def name(self):
        return self.first_name + ' ' + self.last_name
        # return "{} {}".format(self.first_name, self.last_name)
        # return " ".join(self.first_name, self.last_name)

#>>> trey = Person("Trey", "Hunner")
#>>> trey.name
#'Trey Hunner'
#>>> trey.last_name = "Smith"
#>>> trey.name
#'Trey Smith'