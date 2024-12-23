from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_obj = Book.objects.all()
    for b in books_obj:
        b.pub_date = b.pub_date.strftime("%Y-%m-%d")
    context = {
        'books': books_obj
    }
    return render(request, template, context)


def show_book_date(request, date):
    date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    content_for_paginator = sorted(Book.objects.values_list('pub_date'))

    dates = {}
    dates_for_context = {}
    i = 1
    for d in content_for_paginator:
        dates[d[0].strftime("%Y-%m-%d")] = i
        dates_for_context[i] = d[0].strftime("%Y-%m-%d")
        i += 1

    paginator = Paginator(content_for_paginator, 1)
    page = paginator.get_page(dates[date])

    book_obj = Book.objects.filter(pub_date=date_obj).values()
    for b in book_obj:
        b['pub_date'] = str(b['pub_date'])

    next = dates_for_context[page.number + 1] if page.number + 1 <= len(dates_for_context) else ''
    last = dates_for_context[page.number - 1] if page.number - 1 >= 1 else ''

    template = 'books/book.html'
    context = {
        'book': book_obj[0],
        'page': page,
        'next_date': next,
        'last_date': last
    }
    return render(request, template, context)

