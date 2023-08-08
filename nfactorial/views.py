from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, nfactorial school!")

def add(request, first, second):
    result = first + second
    return HttpResponse(f"the sum of {first} and {second} is {result}.")

def upper(request, text):
    return HttpResponse(text.upper())

def palindrome(request, word):
    is_palindrome = word.lower() == word.lower()[::-1]
    return HttpResponse(f"{word} is {'a palindrome' if is_palindrome else 'not a palindrome'}.")


def calculator(request, first, operation, second):
    if operation == 'add':
        result = first + second
    elif operation == 'sub':
        result = first - second
    elif operation == 'mult':
        result = first * second
    elif operation == 'div':
        if second != 0:
            result = first / second
        else:
            return HttpResponse("error: cannot divide by zero.")
    else:
        return HttpResponse("error: invalid operation.")
    return HttpResponse(f"result: {result}")

