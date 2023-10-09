# Advanced_calculator

import math


class CustomError(Exception):
    def __init__(self, message):
        self.message = message


def validate_positive_number(func):
    def wrapper(instance, num1, num2):
        if num1 <= 0 or num2 <= 0:
            raise CustomError("the number must to be positive")
        return func(instance, num1, num2)
    return wrapper


class MathOperation:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


class AddOperation(MathOperation):
    @validate_positive_number
    def perform(self, num1, num2):
        return num1 + num2


class SustractOperation(MathOperation):
    @validate_positive_number
    def perform(self, num1, num2):
        return num1 - num2


class MultiplicationOperation(MathOperation):
    @validate_positive_number
    def perform(self, num1, num2):
        return num1 * num2


class DivisionOperation(MathOperation):
    @validate_positive_number
    def perform(self, num1, num2):
        if num2 == 0:
            raise CustomError("Division by zero is not allowed")
        return num1 / num2


class FloorDivisionOperation(MathOperation):
    @validate_positive_number
    def perform(self, num1, num2):
        if num2 == 0:
            raise CustomError("Division by zero is not allowed")
        return num1 // num2


class RemainderOperation(MathOperation):
    @validate_positive_number
    def perform(self, num1, num2):
        return num1 % num2


class SquereRootOperation:
    def perform(self, num1):
        return math.sqrt(num1)


class ExponentitationOperation(MathOperation):
    @validate_positive_number
    def perform(self, num1, num2):
        return num1 ** num2


class AdvancedCalculator:
    def enter_number(self):
        print("Welcome to the advanced calculator!")
        while True:
            try:
                n1 = float(input("Enter the first number: "))
                op = input("Enter the operation (+|-|*|/|//|sqrt|^|%): ")

                if op == "+":
                    n2 = float(input("Enter the second number: "))
                    operation = AddOperation(n1, n2)
                    result = operation.perform(n1, n2)
                elif op == "-":
                    n2 = float(input("Enter the second number: "))
                    operation = SustractOperation(n1, n2)
                    result = operation.perform(n1, n2)
                elif op == "*":
                    n2 = float(input("Enter the second number: "))
                    operation = MultiplicationOperation(n1, n2)
                    result = operation.perform(n1, n2)
                elif op == "/":
                    n2 = float(input("Enter the second number: "))
                    operation = DivisionOperation(n1, n2)
                    result = operation.perform(n1, n2)
                elif op == "//":
                    n2 = float(input("Enter the second number: "))
                    operation = FloorDivisionOperation(n1, n2)
                    result = operation.perform(n1, n2)
                elif op == "sqrt":
                    operation = SquereRootOperation()
                    result = operation.perform(n1)
                    print("sqrt root resut:", result)
                elif op == "^":
                    n2 = float(input("Enter the exponent: "))
                    operation = ExponentitationOperation(n1, n2)
                    result = operation.perform(n1, n2)
                elif op == "%":
                    n2 = float(input("Enter the remainder: "))
                    operation = RemainderOperation(n1, n2)
                    result = operation.perform(n1, n2)
                else:
                    print("Operation not valid :(")
                    continue
                print("Result:", result)
                while True:
                    choice = input(
                        "Do you want to perform another calculation? (yes/no): ")

                    if choice.lower() == "no":
                        print("Thanks for using the advanced calculator!")
                        return
                    elif choice.lower() == "yes":
                        break
                    else:
                        print("Invalid choice. Exiting.")

            except ValueError:
                print("Invalid input. Please enter a valid number.")
            except CustomError as e:
                print(e.message)


calculator = AdvancedCalculator()
calculator.enter_number()
