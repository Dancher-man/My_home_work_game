from django.shortcuts import render
from random import shuffle


def generate_numbers(count_numbers):
    data = list(range(1, 10))
    shuffle(data)
    result = data[:count_numbers]
    return result


class Game:
    secret_numbers = generate_numbers(4)
    print(secret_numbers)

    @staticmethod
    def validation(request):
        try:
            numbers_post = request.POST.get('numbers').split()
            numbers = [int(number) for number in numbers_post]
            context = numbers
            if len(numbers) != 4:
                context = f"The amount of integers should equal to 4"
            elif len(numbers) != len(set(numbers)):
                context = f"The value should be unique"
            for i in numbers:
                if i > 9 or i < 1:
                    context = f"Numbers must be greater than 1 less than 10"
        except:
            context = f"The value should be integer"

        return context

    @staticmethod
    def get_result(secret_number, numbers):
        bulls = 0
        cows = 0
        for i in range(len(numbers)):
            if numbers[i] == secret_number[i]:
                bulls += 1
            elif numbers[i] in secret_number:
                cows += 1
        if bulls == 4:
            context = "winner"
        elif bulls or cows:
            context = f"You got: {bulls} and: {cows}"
        else:
            context = "No identical numbers"
        return context


def index_create(request):
    if request.method == "GET":
        return render(request, "forms.html")
    numbers = Game.validation(request)
    numbers_value = " ".join([str(n) for n in numbers])
    if isinstance(numbers, str):
        context = {
            'result': Game.validation(request)
        }
    else:
        result = Game.get_result(numbers, Game.secret_numbers)
        Game.secret_numbers = generate_numbers(4)
        print(Game.secret_numbers)
        context = {
            'result': result,
            'value': numbers_value
        }

    return render(request, 'forms.html', context)
