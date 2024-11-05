#
# poweredby2dor
#
class OOPPillars:
    @staticmethod
    def encapsulation():
        return """
        Encapsulation:
        The concept of encapsulation involves bundling the data (attributes) and methods (functions) that operate on the data into a single unit, known as a class.
        It hides the internal state of the object and requires all interactions to be performed through well-defined interfaces.
        """

    @staticmethod
    def inheritance():
        return """
        Inheritance:
        Inheritance is a mechanism where a new class inherits properties and behaviors from an existing class (superclass or base class).
        It allows for code reuse and the creation of a hierarchy of classes, promoting a more organized and efficient structure.
        """

    @staticmethod
    def polymorphism():
        return """
        Polymorphism:
        Polymorphism allows objects of different types to be treated as objects of a common type.
        There are two types of polymorphism: compile-time (method overloading) and runtime (method overriding).
        Method overloading enables a class to have multiple methods with the same name but different parameters.
        Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass.
        """

    @staticmethod
    def abstraction():
        return """
        Abstraction:
        Abstraction involves simplifying complex systems by modeling classes based on the essential properties and behaviors they share.
        It provides a way to provide a simple interface for the complex underlying systems.
        Abstract classes and interfaces are used to achieve abstraction in OOP.
        """


def main():
    pillars = OOPPillars()
    print(pillars.encapsulation())
    print(pillars.inheritance())
    print(pillars.polymorphism())
    print(pillars.abstraction())


if __name__ == "__main__":
    main()
