import psycopg2
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView


def test(request, name):
    """

    Args:
        request:
        name:

    Returns:

    """

    # query = f'SELECT email from auth_user where username="{name}";'
    #
    # conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host='postgres')
    # cursor = conn.cursor()
    #
    # query = "SELECT email FROM auth_user where username='canary';"
    # cursor.execute(query)
    # results = cursor.fetchall()[0][0]

    return render(request, 'test1/test1.html')
    # return HttpResponse(f'<p>Hello, {results}!</p>')
    # return JsonResponse({"name": name})


def get_email(request, name):
    query = f'SELECT email from auth_user where username="{name}";'

    conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host='postgres')
    cursor = conn.cursor()

    # x = 4/0 # causes Error 500: Internal server error

    query = f"SELECT email FROM auth_user where username='{name}';"
    cursor.execute(query)
    email = cursor.fetchall()[0][0]

    return JsonResponse({"email": email})