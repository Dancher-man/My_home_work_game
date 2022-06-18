from django.shortcuts import render
from random import shuffle


def generate_numbers(count_numbers):
    data = list(range(1, 10))
    shuffle(data)
    result = data[:count_numbers]
    print(result)
    return result


secret_numbers = generate_numbers(4)


def validation(numbers, numbers_str):
    pass


# Create your views here.
def index_create(request):
    context = {}
    if request.method == "GET":
        return render(request, "forms.html")
    else:
        if request.method == "POST":
            print(request.POST.get('numbers'))
            try:
                numbers_post = request.POST.get('numbers').split()
                numbers = [int(number) for number in numbers_post]
                print(numbers)
                if len(numbers) != 4:
                    context = {
                        'result': f"The amount of integers should equal to 4"
                    }
                elif len(numbers) != len(set(numbers)):
                    context = {
                        'result': f"The value should be unique"
                    }
                for i in numbers:
                    if i > 9 or i < 1:
                        context = {
                            'result': f"Numbers must be greater than 1 less than 10"
                        }
            except:
                context = {
                    'result': f"The value should be integer"
                }
    return render(request, 'forms.html', context)
# def index_create(request):
#     context = {}
#     if request.method == "GET":
#         return render(request, "create_index.html")
#     else:
#         if request.POST.get('choice') == 'add':
#             query = int(request.POST.get('first_number')) + int(request.POST.get('second_number'))
#             context = {
#                 'result': f"Result: {request.POST.get('first_number')} + {request.POST.get('second_number')} = {query}"
#             }
#         elif request.POST.get('choice') == 'subtract':
#             query = int(request.POST.get('first_number')) - int(request.POST.get('second_number'))
#             context = {
#                 'result': f"Result: {request.POST.get('first_number')} - {request.POST.get('second_number')} = {query}"
#             }
#         elif request.POST.get('choice') == 'multiply':
#             query = int(request.POST.get('first_number')) * int(request.POST.get('second_number'))
#             context = {
#                 'result': f"Result: {request.POST.get('first_number')} * {request.POST.get('second_number')} = {query}"
#             }
#         elif request.POST.get('choice') == 'divide':
#             query = int(request.POST.get('first_number')) / int(request.POST.get('second_number'))
#             context = {
#                 'result': f"Result: {request.POST.get('first_number')} / {request.POST.get('second_number')} = {query}"
#             }
#     return render(request, 'create_index.html', context)
