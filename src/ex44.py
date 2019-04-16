class Parent(object):

    def implicit(self):
        print("Parent implicit()")

    def override(self):
        print("Parent override()")

    def altered(self):
        print("Parent altered()")


class Child(Parent):

    def override(self):
        print("Child override()")

    def altered(self):
        print("Child, BEFORE Parent altered()")
        super(Child,self).altered()
        print("Child, AFTER Parent altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

print("-"*10)

dad.override()
son.override()

print("-"*10)

dad.altered()
son.altered()