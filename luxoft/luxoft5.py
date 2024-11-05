#
# poweredby2dor
#
class ExtraQuestions:
    @staticmethod
    def question2():
        return """
        Interview Question Two:
        What information do you usually include when you open a defect (bug)?
        """

    @staticmethod
    def answer2():
        return """
        Answer:
        When I open a defect I usually start with one or two tags enclosed in brackets so that the type or location of the issue is visible before opening the issue.
        Then I follow the Summary with a brief description of the issue where I try to follow our internal best practices (PAL - Problem Action Location for example).
        And in my description I make sure to include the Steps to Reproduce, Actual and Expected Results, Reproduction Rate, Build or Version that I'm using, Platform if applicable.
        Of course, I do my best to add any possible information available to me about the issue in a structured format or template.
        """

    @staticmethod
    def question3():
        return """
        Interview Question Three:
        What kind of testing have you performed (brief explanation)?
        Most frequently I have worked in the Functional Testing category, like Smoke and Sanity testing which belong to the System testing branch but I have also performed Performance Testing,
        which belongs to the Non Functional Testing category. Smoke and Sanity tests usually cover testing the functionality of the product as a whole system,
        test cases here usually are desgined based on how an end user will use the product.
        """

    @staticmethod
    def answer3():
        return """
        Answer:
        
        """


def main():
    pillars = ExtraQuestions()
    print(pillars.question2())
    print(pillars.answer2())
    print(pillars.question3())
    print(pillars.answer3())


if __name__ == "__main__":
    main()
