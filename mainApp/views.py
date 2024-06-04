from django.shortcuts import render,HttpResponse
from .models import Skill,WorkExperience,Education
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'home/index.html')

def calendar(request):
    return render(request,'calendar/calendar.html')
#Video Call with mentors 

@login_required
def profile(request):
    user = request.user
    education = Education.objects.filter(user=user)
    workexp = WorkExperience.objects.filter(user=user)
    skill_info = Skill.objects.filter(user=user)
    print(education)
    print(workexp)
    print(skill_info)
    params = {
        'education':education,
        'workexp':workexp,
        'skill':skill_info
    } 
    return render(request,'profile/profile.html', params)

@login_required
def updateprofile(request):
    return render(request,'profile/updateprofile.html')

@login_required
def updateworkexp(request):
    if request.method == 'POST':
        
        company = request.POST.get('company')
        position = request.POST.get('position')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        brief = request.POST.get('brief')
        
        # Print form data
        print(f"Company: {company}")
        print(f"Position: {position}")
        print(f"Start Date: {start_date}")
        print(f"End Date: {end_date}")
        print(f"Brief: {brief}")
        user = request.user

        WorkExperience.objects.create(
            user=user,
            company=company,
            position=position,
            start_date=start_date,
            end_date=end_date,
            description=brief,
        )
        
        # Do something with the form data, such as saving to a database
        return render(request,'profile/updateprofile.html')
    return render(request,'profile/updateprofile.html')

@login_required
def updateeducation(request):
    if request.method == 'POST':
        institution = request.POST.get('institution')
        degree = request.POST.get('degree')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        user = request.user
       
        # Print form data
        print(f"Institution: {institution}")
        print(f"Degree: {degree}")
        print(f"Start Date: {start_date}")
        print(f"End Date: {end_date}")

        Education.objects.create(
            user=user,
            institution=institution,
            degree=degree,
            start_date=start_date,
            end_date=end_date,
        )
        
        # Do something with the form data, such as saving to a database
        return render(request,'profile/updateprofile.html')
    return render(request,'profile/updateprofile.html')

@login_required
def updateskills(request):
    if request.method == 'POST':
        user = request.user

        skills = request.POST.get('skills')
        
        skills_list = [skill.strip() for skill in skills.split(',') if skill.strip()]  # Split skills by comma and remove any empty or whitespace-only skills
        
        # Print individual skills
        for skill in skills_list:
            print(f"Skill: {skill}")

        for skill_name in skills_list:
                Skill.objects.create(user=user, skill_name=skill_name)

        
        # Do something with the form data, such as saving to a database
        return render(request,'profile/updateprofile.html')
    return render(request,'profile/updateprofile.html')


import requests
from django.shortcuts import render



from serpapi import GoogleSearch



@login_required
def studymaterials(request):
    user = request.user
    skills = Skill.objects.filter(user=user)
    if request.method == 'POST':
        skill_id = request.POST.get('skill_id')
        user = request.user
        skill = Skill.objects.get(id=skill_id,user=user)
        print(skill.skill_name)
        request.session['skill'] = skill.skill_name


        params = {
            "engine": "youtube",
            "search_query": skill.skill_name + "Tutorial Playlist",
            "api_key": "3fb9e0be680fbc384833423e983140627c494f8d1468c6dc9d1282661ede94e6"
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        
        # Print out the results for debugging
        # print(results['playlist_results'])
            
        
        # Print individual skills
        


        return render(request,'resources/studymaterial.html',{'skills':skills,'videos':results['playlist_results']})
    return render(request,'resources/studymaterial.html',{'skills':skills})


    
# def profile(request):
#     try:
#         profile = UserProfile.objects.get(user=request.user)
#     except UserProfile.DoesNotExist:
#         profile = UserProfile.objects.create(user=request.user)
    
#     user = request.user
#     total_quizzes_attempted = Quiz.objects.filter(userinfo=user).count()
#     print(total_quizzes_attempted)
#     education = Education.objects.filter(user=user)
#     workexp = WorkExperience.objects.filter(user=user)
#     skill_info = Skill.objects.filter(user=user)
#     print(skill_info)
#     params = {
#         'profile':profile,
#         'education':education,
#         'workexp':workexp,
#         'skill':skill_info
#     }
#     # return JsonResponse(user_quiz_data,safe=False)
#     return render(request, 'profile.html', params)   