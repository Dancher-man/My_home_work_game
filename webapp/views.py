from django.shortcuts import render


# Create your views here.
def index_create(request):
    context = {}
    if request.method == "GET":
        return render(request, "forms.html")

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
