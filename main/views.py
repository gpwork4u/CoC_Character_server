from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Character,Account
from random import randint


# Create your views here.
def logout(request):
    del request.session['username']
    return redirect('/')

def user_menu(request):
    login_flag = False
    session_flag = False
    if 'username' in request.session:
        session_flag = True
        username = request.session['username']
    else:
        username = request.POST['username']
        user = Account.objects.get(username=request.POST['username'])
        login_flag = user.password == request.POST['password']
    if login_flag or session_flag:
        request.session['username'] = username
        chars = Character.objects.filter(username=username)
    if 'submit' in request.POST:
        if request.POST['submit'] == 'create':
            create_character(request)
        elif request.POST['submit'] == 'update':
            update_character(request)
    return render(request,"user_menu.html",locals())
def show_character(request):
    char = Character.objects.get(id=request.POST['id'])
    login_flag = char.username == request.session['username']
    if login_flag:
        char = Character.objects.get(id=request.POST['id'])
    return render(request,"character.html",locals())

def menu(request):
    if 'username' in request.session:
        return redirect('user_menu/')
    return render(request,"menu.html",locals())
def update_character(request):
    char = Character.objects.filter(id=request.POST["id"]).first()
    char.Name=request.POST["Name"]
    char.Sex=request.POST["Sex"]
    char.Job=request.POST["Job"]
    char.Age=request.POST["Age"]
    char.Birth_Place=request.POST["Birth_Place"]
    char.Residence=request.POST["Residence"]
    char.STR=request.POST["STR"]
    char.CON=request.POST["CON"]
    char.SIZ=request.POST["SIZ"]
    char.DEX=request.POST["DEX"]
    char.APP=request.POST["APP"]
    char.EDU=request.POST["EDU"]
    char.INT=request.POST["INT"]
    char.POW=request.POST["POW"]
    char.MOV=request.POST["MOV"]
    char.HP=request.POST["HP"]
    char.HP_max=request.POST["HP_max"]
    char.SAN=request.POST["SAN"]
    char.LUCK=request.POST["LUCK"]
    char.MP=request.POST["MP"]
    char.MP_max=request.POST["MP_max"]
    char.Skill_Accounting=request.POST["Skill_Accounting"]
    char.Skill_Anthropology=request.POST["Skill_Anthropology"]
    char.Skill_Appraise=request.POST["Skill_Appraise"]
    char.Skill_Archaecology=request.POST["Skill_Archaecology"]
    char.Skill_Art_Craft=request.POST["Skill_Art_Craft"]
    char.Skill_Charm=request.POST["Skill_Charm"]
    char.Skill_Climb=request.POST["Skill_Climb"]
    char.Skill_Credit=request.POST["Skill_Credit"]
    char.Skill_Cthulhu_Mythos=request.POST["Skill_Cthulhu_Mythos"]
    char.Skill_Disguise=request.POST["Skill_Disguise"]
    char.Skill_Dodge=request.POST["Skill_Dodge"]
    char.Skill_Drive_auto=request.POST["Skill_Drive_auto"]
    char.Skill_Elev_Repair=request.POST["Skill_Elev_Repair"]
    char.Skill_Fast_Talk=request.POST["Skill_Fast_Talk"]
    char.Skill_Fighting=request.POST["Skill_Fighting"]
    char.Skill_Firearms_HandGun=request.POST["Skill_Firearms_HandGun"]
    char.Skill_Firearms_Rifle=request.POST["Skill_Firearms_Rifle"]
    char.Skill_First_Aid=request.POST["Skill_First_Aid"]
    char.Skill_History=request.POST["Skill_History"]
    char.Skill_Intimidate=request.POST["Skill_Intimidate"]
    char.Skill_Jump=request.POST["Skill_Jump"]
    char.Skill_Language_Other=request.POST["Skill_Language_Other"]
    char.Skill_Language_Other_c=request.POST["Skill_Language_Other_c"]
    char.Skill_Language_Owm=request.POST["Skill_Language_Owm"]
    char.Skill_Language_Owm_c=request.POST["Skill_Language_Owm_c"]
    char.Skill_Law=request.POST["Skill_Law"]
    char.Skill_LibraryUse=request.POST["Skill_LibraryUse"]
    char.Skill_Listen=request.POST["Skill_Listen"]
    char.Skill_Locksmith=request.POST["Skill_Locksmith"]
    char.Skill_Mech_Repair=request.POST["Skill_Mech_Repair"]
    char.Skill_Medicine=request.POST["Skill_Medicine"]
    char.Skill_Natural_World=request.POST["Skill_Natural_World"]
    char.Skill_Navigate=request.POST["Skill_Navigate"]
    char.Skill_Occult=request.POST["Skill_Occult"]
    char.Skill_Op_Hv_Machine=request.POST["Skill_Op_Hv_Machine"]
    char.Skill_Persuade=request.POST["Skill_Persuade"]
    char.Skill_Pilot=request.POST["Skill_Pilot"]
    char.Skill_Pilot_c=request.POST["Skill_Pilot_c"]
    char.Skill_Psychology=request.POST["Skill_Psychology"]
    char.Skill_Psychoanalysis=request.POST["Skill_Psychoanalysis"]
    char.Skill_Ride=request.POST["Skill_Ride"]
    char.Skill_Science=request.POST["Skill_Science"]
    char.Skill_Science_c=request.POST["Skill_Science_c"]
    char.Skill_Sleight_of_Hand=request.POST["Skill_Sleight_of_Hand"]
    char.Skill_Spot_Hidden=request.POST["Skill_Spot_Hidden"]
    char.Skill_Stealth=request.POST["Skill_Stealth"]
    char.Skill_Survival=request.POST["Skill_Survival"]
    char.Skill_Survival_c=request.POST["Skill_Survival_c"]
    char.Skill_Swim=request.POST["Skill_Swim"]
    char.Skill_Throw=request.POST["Skill_Throw"]
    char.Skill_Track=request.POST["Skill_Track"]
    char.Damage_Bonus=request.POST["Damage_Bonus"]
    char.Build=request.POST["Build"]
    char.Traits=request.POST["Traits"]
    char.Beliefs=request.POST["Beliefs"]
    char.Personal_Description=request.POST["Personal_Description"]
    char.Significant_People=request.POST["Significant_People"]
    char.Meaningful_Location=request.POST["Meaningful_Location"]
    char.Treasured_Possesions=request.POST["Treasured_Possesions"]
    char.Injuries_Scars=request.POST["Injuries_Scars"]
    char.Phobias_Manias=request.POST["Phobias_Manias"]
    char.Arcane_Tome_Spell_Artifact=request.POST["Arcane_Tome_Spell_Artifact"]
    char.Encounters_with_Strange_Entities=request.POST["Encounters_with_Strange_Entities"]
    char.save()
def create_character(request):
    Character.objects.create(username=request.session["username"],\
                         Name=request.POST["Name"],\
                         Sex=request.POST["Sex"],\
                         Job=request.POST["Job"],\
                         Age=request.POST["Age"],\
                         Birth_Place=request.POST["Birth_Place"],\
                         Residence=request.POST["Residence"],\
                         STR=request.POST["STR"],\
                         CON=request.POST["CON"],\
                         SIZ=request.POST["SIZ"],\
                         DEX=request.POST["DEX"],\
                         APP=request.POST["APP"],\
                         EDU=request.POST["EDU"],\
                         INT=request.POST["INT"],\
                         POW=request.POST["POW"],\
                         MOV=request.POST["MOV"],\
                         HP=request.POST["HP"],\
                         HP_max=request.POST["HP_max"],\
                         SAN=request.POST["SAN"],\
                         LUCK=request.POST["LUCK"],\
                         MP=request.POST["MP"],\
                         MP_max=request.POST["MP_max"],\
                         Skill_Accounting=request.POST["Skill_Accounting"],\
                         Skill_Anthropology=request.POST["Skill_Anthropology"],\
                         Skill_Appraise=request.POST["Skill_Appraise"],\
                         Skill_Archaecology=request.POST["Skill_Archaecology"],\
                         Skill_Art_Craft=request.POST["Skill_Art_Craft"],\
                         Skill_Charm=request.POST["Skill_Charm"],\
                         Skill_Climb=request.POST["Skill_Climb"],\
                         Skill_Credit=request.POST["Skill_Credit"],\
                         Skill_Cthulhu_Mythos=request.POST["Skill_Cthulhu_Mythos"],\
                         Skill_Disguise=request.POST["Skill_Disguise"],\
                         Skill_Dodge=request.POST["Skill_Dodge"],\
                         Skill_Drive_auto=request.POST["Skill_Drive_auto"],\
                         Skill_Elev_Repair=request.POST["Skill_Elev_Repair"],\
                         Skill_Fast_Talk=request.POST["Skill_Fast_Talk"],\
                         Skill_Fighting=request.POST["Skill_Fighting"],\
                         Skill_Firearms_HandGun=request.POST["Skill_Firearms_HandGun"],\
                         Skill_Firearms_Rifle=request.POST["Skill_Firearms_Rifle"],\
                         Skill_First_Aid=request.POST["Skill_First_Aid"],\
                         Skill_History=request.POST["Skill_History"],\
                         Skill_Intimidate=request.POST["Skill_Intimidate"],\
                         Skill_Jump=request.POST["Skill_Jump"],\
                         Skill_Language_Other=request.POST["Skill_Language_Other"],\
                         Skill_Language_Other_c=request.POST["Skill_Language_Other_c"],\
                         Skill_Language_Owm=request.POST["Skill_Language_Owm"],\
                         Skill_Language_Owm_c=request.POST["Skill_Language_Owm_c"],\
                         Skill_Law=request.POST["Skill_Law"],\
                         Skill_LibraryUse=request.POST["Skill_LibraryUse"],\
                         Skill_Listen=request.POST["Skill_Listen"],\
                         Skill_Locksmith=request.POST["Skill_Locksmith"],\
                         Skill_Mech_Repair=request.POST["Skill_Mech_Repair"],\
                         Skill_Medicine=request.POST["Skill_Medicine"],\
                         Skill_Natural_World=request.POST["Skill_Natural_World"],\
                         Skill_Navigate=request.POST["Skill_Navigate"],\
                         Skill_Occult=request.POST["Skill_Occult"],\
                         Skill_Op_Hv_Machine=request.POST["Skill_Op_Hv_Machine"],\
                         Skill_Persuade=request.POST["Skill_Persuade"],\
                         Skill_Pilot=request.POST["Skill_Pilot"],\
                         Skill_Pilot_c=request.POST["Skill_Pilot_c"],\
                         Skill_Psychology=request.POST["Skill_Psychology"],\
                         Skill_Psychoanalysis=request.POST["Skill_Psychoanalysis"],\
                         Skill_Ride=request.POST["Skill_Ride"],\
                         Skill_Science=request.POST["Skill_Science"],\
                         Skill_Science_c=request.POST["Skill_Science_c"],\
                         Skill_Sleight_of_Hand=request.POST["Skill_Sleight_of_Hand"],\
                         Skill_Spot_Hidden=request.POST["Skill_Spot_Hidden"],\
                         Skill_Stealth=request.POST["Skill_Stealth"],\
                         Skill_Survival=request.POST["Skill_Survival"],\
                         Skill_Survival_c=request.POST["Skill_Survival_c"],\
                         Skill_Swim=request.POST["Skill_Swim"],\
                         Skill_Throw=request.POST["Skill_Throw"],\
                         Skill_Track=request.POST["Skill_Track"],\
                         Damage_Bonus=request.POST["Damage_Bonus"],\
                         Build=request.POST["Build"],\
                         Traits=request.POST["Traits"],\
                         Beliefs=request.POST["Beliefs"],\
                         Personal_Description=request.POST["Personal_Description"],\
                         Significant_People=request.POST["Significant_People"],\
                         Meaningful_Location=request.POST["Meaningful_Location"],\
                         Treasured_Possesions=request.POST["Treasured_Possesions"],\
                         Injuries_Scars=request.POST["Injuries_Scars"],\
                         Phobias_Manias=request.POST["Phobias_Manias"],\
                         Arcane_Tome_Spell_Artifact=request.POST["Arcane_Tome_Spell_Artifact"],\
                         Encounters_with_Strange_Entities=request.POST["Encounters_with_Strange_Entities"])

def show_create_page(request):
    username = request.session['username']
    return render(request,'create_char.html',locals())

def show_regist_page(request):
    return render(request,"regist.html",locals())

def user_regist(request):
    Account.objects.create(username=request.POST['username'],\
                           password=request.POST['password'],\
                           email=request.POST['email'])
    return

def validate_username(request):
    print('test')
    username = request.GET.get('username',None)
    data = {
        'is_taken': Account.objects.filter(username=username).exists()
    }
    return JsonResponse(data)