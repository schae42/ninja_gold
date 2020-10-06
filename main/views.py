from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random

# Create your views here.
def index(request):
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0
        print("Total Gold = 0")
        request.session['activities'] = []
    return render(request, 'index.html')

def process(request):
    if request.method == "POST":
        print("*"*25, "PROCESS MONEY METHOD", "*"*25)

        if request.POST['building'] == 'farm':
            request.session['message'] = ''
            number = random.randrange(10,21)
            time = datetime.now().strftime("%Y/%m/%d %I:%M %p")
            request.session['total_gold'] += number
            print(f"Gold increased by {number}.")
            print(f"Total Gold = {request.session['total_gold']}")
            temp_list = request.session['activities']
            temp_list.append(f"<div class='won'>Earned {number} gold from the farm! ({time})</div>")
            request.session['activities'] = temp_list

            for i in range(len(request.session['activities'])-1, -1, -1):
                request.session['message'] += request.session['activities'][i]
            print("\nSESSION SUMMARY:")
            for val in request.session.keys():
                print("\n", val, request.session[val])
            print("*"*25, "END PROCESS MONEY METHOD", "*"*25)



        elif request.POST['building'] == 'cave':
            request.session['message'] = ''
            number = random.randrange(5,11)
            time = datetime.now().strftime("%Y/%m/%d %I:%M %p")
            request.session['total_gold'] += number
            print(f"Gold increased by {number}.")
            print(f"Total Gold = {request.session['total_gold']}")
            temp_list = request.session['activities']
            temp_list.append(f"<div class='won'>Earned {number} gold from the farm! ({time})</div>")
            request.session['activities'] = temp_list

            for i in range(len(request.session['activities'])-1, -1, -1):
                request.session['message'] += request.session['activities'][i]
            print("\nSESSION SUMMARY:")
            for val in request.session.keys():
                print("\n", val, request.session[val])
            print("*"*25, "END PROCESS MONEY METHOD", "*"*25)


        elif request.POST['building'] == 'house':
            request.session['message'] = ''
            number = random.randrange(2,6)
            time = datetime.now().strftime("%Y/%m/%d %I:%M %p")
            request.session['total_gold'] += number
            print(f"Gold increased by {number}.")
            print(f"Total Gold = {request.session['total_gold']}")
            temp_list = request.session['activities']
            temp_list.append(f"<div class='won'>Earned {number} gold from the farm! ({time})</div>")
            request.session['activities'] = temp_list

            for i in range(len(request.session['activities'])-1, -1, -1):
                request.session['message'] += request.session['activities'][i]
            print("\nSESSION SUMMARY:")
            for val in request.session.keys():
                print("\n", val, request.session[val])
            print("*"*25, "END PROCESS MONEY METHOD", "*"*25)


        elif request.POST['building'] == 'casino':
            if request.session['total_gold'] > 0:
                request.session['message'] = ''
                number = random.randrange(-50,51)
                time = datetime.now().strftime("%Y/%m/%d %I:%M %p")
                request.session['total_gold'] += number
                if number > 0:
                    print(f"Gold increased by {number}.")
                    temp_list = request.session['activities']
                    temp_list.append(f"<div class='won'>Earned {number} gold from the farm! ({time})</div>")
                    request.session['activities'] = temp_list
                if number < 0:
                    print(f"Gold decreased by {abs(number)}.")
                    temp_list = request.session['activities']
                    temp_list.append(f"<div class='lost'>Entered a casino and lost {abs(number)} gold....Ouch! ({time})</div>")
                    request.session['activities'] = temp_list         
                print(f"Total Gold = {request.session['total_gold']}") 

                for i in range(len(request.session['activities'])-1, -1, -1):
                    request.session['message'] += request.session['activities'][i]
                print("\nSESSION SUMMARY:")
                for val in request.session.keys():
                    print("\n", val, request.session[val])
                print("*"*25, "END PROCESS MONEY METHOD", "*"*25)

            elif request.session['total_gold'] <= 0:
                request.session['message'] = ''
                temp_list = request.session['activities']
                temp_list.append(f"<div>You have no gold to gamble. Please come back to the casino when you have more money.</div>")
                request.session['activities'] = temp_list       
                print(f"Total Gold = {request.session['total_gold']}")
                print("You have no gold to gamble. Please come back to the casino when you have more money.")

                for i in range(len(request.session['activities'])-1, -1, -1):
                    request.session['message'] += request.session['activities'][i]
                print("\nSESSION SUMMARY:")
                for val in request.session.keys():
                    print("\n", val, request.session[val])
                print("*"*25, "END PROCESS MONEY METHOD", "*"*25)

        return redirect("/")
    
    else:
        print("*"*25, "PROCESS MONEY METHOD", "*"*25)
        return redirect("/")


def reset(request):
    print("*"*25, "RESET METHOD", "*"*25)
    print("Current game is ending. Gold count will reset to 0.")
    request.session.clear()
    print("SESSION SUMMARY:")
    for val in request.session.keys():
        print(val, request.session[val], "\n")
    print("*"*25, "END RESET METHOD", "*"*25)
    return redirect("/")