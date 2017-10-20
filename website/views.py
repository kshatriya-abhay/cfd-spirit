from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from forms.models import Item
from django.http import HttpResponseRedirect

class TestPage(TemplateView):
    template_name = 'test.html';

class ThanksPage(TemplateView):
    template_name = 'thanks.html';


class HomePage(TemplateView):
    template_name = 'index.html';

class Home(TemplateView):
    template_name = 'home.html';

#####################################
#General--------------------------------------------->
#class Pen(TemplateView):
#    template_name = 'General/pen.html';

class Pencil(TemplateView):
    template_name = 'General/pencil.html';

class Sim(TemplateView):
    template_name = 'General/sim.html';

class Notebook(TemplateView):
    template_name = 'General/notebook.html';

class Sheets(TemplateView):
    template_name = 'General/sheets.html';

class Washing_powder(TemplateView):
    template_name = 'General/washing_powder.html';
#General finished--------------------------------------->

#HMC------------>
class Chess_Boards(TemplateView):
    template_name = 'HMC/chess_boards.html';

class TT_table(TemplateView):
    template_name = 'HMC/tt_table.html';

class Cricket_Bats(TemplateView):
    template_name = 'HMC/cricket_bats.html';

class Cricket_Balls(TemplateView):
    template_name = 'HMC/cricket_balls.html';

class Footballs(TemplateView):
    template_name = 'HMC/footballs.html';

class Badminton(TemplateView):
    template_name = 'HMC/badminton.html';

class Washing_Machine(TemplateView):
    template_name = 'HMC/washing_machine.html';

#HMC completed------------------------------------->

#Canteen--------------->

class Chips(TemplateView):
    template_name = 'Canteen/chips.html';

class Snacks(TemplateView):
    template_name = 'Canteen/snacks.html';

class Biscuits(TemplateView):
    template_name = 'Canteen/biscuits.html';

class Beverages(TemplateView):
    template_name = 'Canteen/beverages.html';
#canteen completed------------>

#juice center----------->

class Amul_Products(TemplateView):
    template_name = 'Juice_Center/amul_products.html';

class Fruits(TemplateView):
    template_name = 'Juice_Center/fruits.html';

class Juice(TemplateView):
    template_name = 'Juice_Center/juice.html';

class Soft_Drinks(TemplateView):
    template_name = 'Juice_Center/soft_drinks.html';
#juice center completed------------->

# class AuthRequiredMiddleware(object):
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):

#         response = self.get_response(request)
#         if not request.user.is_authenticated():
#             return HttpResponseRedirect('home')
#         return response
#General-------------------------------------------------------------->
#General-------------------------------------------------------------->
def pen(request):
    all_items = Item.objects.filter(item_type="pen")
    context = {'all_items' : all_items}
    i = "pen"
    i_type = {'i' : i}
    return render(request, 'General/pen.html', context, i_type)
##
def pencil(request):
    all_items = Item.objects.filter(item_type="pencil")
    context = {'all_items' : all_items}
    i = "pencil"
    i_type = {'i' : i}
    return render(request, 'General/pencil.html', context, i_type)
##
def sim(request):
    all_items = Item.objects.filter(item_type="sim")
    context = {'all_items' : all_items}
    i = "sim"
    i_type = {'i' : i}
    return render(request, 'General/sim.html', context, i_type)
##
def files(request):
    all_items = Item.objects.filter(item_type="files")
    context = {'all_items' : all_items}
    i = "files"
    i_type = {'i' : i}
    return render(request, 'General/files.html', context, i_type)
##
def sheets(request):
    all_items = Item.objects.filter(item_type="sheets")
    context = {'all_items' : all_items}
    i = "sheets"
    i_type = {'i' : i}
    return render(request, 'General/sheets.html', context, i_type)
##
def washing_powder(request):
    all_items = Item.objects.filter(item_type="washing_powder")
    context = {'all_items' : all_items}
    i = "washing_powder"
    i_type = {'i' : i}
    return render(request, 'General/washing_powder.html', context, i_type)
###############HMC
##
def chess_boards(request):
    all_items = Item.objects.filter(item_type="chess_boards")
    context = {'all_items' : all_items}
    i = "chess_boards"
    i_type = {'i' : i}
    return render(request, 'HMC/chess_boards.html', context, i_type)
##
def tt_table(request):
    all_items = Item.objects.filter(item_type="tt_table")
    context = {'all_items' : all_items}
    i = "tt_table"
    i_type = {'i' : i}
    return render(request, 'HMC/tt_table.html', context, i_type)
##
def cricket_bats(request):
    all_items = Item.objects.filter(item_type="cricket_bats")
    context = {'all_items' : all_items}
    i = "cricket_bats"
    i_type = {'i' : i}
    return render(request, 'HMC/cricket_bats.html', context, i_type)
##
def cricket_balls(request):
    all_items = Item.objects.filter(item_type="cricket_balls")
    context = {'all_items' : all_items}
    i = "cricket_balls"
    i_type = {'i' : i}
    return render(request, 'HMC/cricket_balls.html', context, i_type)
##
def footballs(request):
    all_items = Item.objects.filter(item_type="footballs")
    context = {'all_items' : all_items}
    i = "footballs"
    i_type = {'i' : i}
    return render(request, 'HMC/footballs.html', context, i_type)
##
def badminton(request):
    all_items = Item.objects.filter(item_type="badminton")
    context = {'all_items' : all_items}
    i = "badminton"
    i_type = {'i' : i}
    return render(request, 'HMC/badminton.html', context, i_type)
##
def washing_machine(request):
    all_items = Item.objects.filter(item_type="washing_machine")
    context = {'all_items' : all_items}
    i = "washing_machine"
    i_type = {'i' : i}
    return render(request, 'HMC/washing_machine.html', context, i_type)
##
##################################
########################Canteen
def chips(request):
     all_items = Item.objects.filter(item_type="chips")
     context = {'all_items' : all_items}
     i = "chips"
     i_type = {'i' : i}
     return render(request, 'Canteen/chips.html', context, i_type)
 ##
def snacks(request):
     all_items = Item.objects.filter(item_type="snacks")
     context = {'all_items' : all_items}
     i = "snacks"
     i_type = {'i' : i}
     return render(request, 'Canteen/snacks.html', context, i_type)
 ##
def biscuits(request):
     all_items = Item.objects.filter(item_type="biscuits")
     context = {'all_items' : all_items}
     i = "biscuits"
     i_type = {'i' : i}
     return render(request, 'Canteen/biscuits.html', context, i_type)
 ##
def beverages(request):
     all_items = Item.objects.filter(item_type="beverages")
     context = {'all_items' : all_items}
     i = "beverages"
     i_type = {'i' : i}
     return render(request, 'Canteen/beverages.html', context, i_type)

 ############Juice_Center
 ##
def amul_products(request):
     all_items = Item.objects.filter(item_type="amul_products")
     context = {'all_items' : all_items}
     i = "amul_products"
     i_type = {'i' : i}
     return render(request, 'Juice_Center/amul_products.html', context, i_type)
 ##
def fruits(request):
     all_items = Item.objects.filter(item_type="fruits")
     context = {'all_items' : all_items}
     i = "fruits"
     i_type = {'i' : i}
     return render(request, 'Juice_Center/fruits.html', context, i_type)
 ##
def soft_drinks(request):
     all_items = Item.objects.filter(item_type="soft_drinks")
     context = {'all_items' : all_items}
     i = "soft_drinks"
     i_type = {'i' : i}
     return render(request, 'Juice_Center/soft_drinks.html', context, i_type)
 ##
def juice(request):
     all_items = Item.objects.filter(item_type="juice")
     context = {'all_items' : all_items}
     i = "juice"
     i_type = {'i' : i}
     return render(request, 'Juice_Center/juice.html', context, i_type)
 ##
