# from django.shortcuts import render

# from serpapi import GoogleSearch

# # Create your views here.
# def getnews(request):
    

#     # params = {
#     # "engine": "google_jobs",
#     # "q": "mumbai software developer",
#     # "hl": "en",
#     # "num": "25",
#     # "api_key": "3fb9e0be680fbc384833423e983140627c494f8d1468c6dc9d1282661ede94e6"
#     # }

#     # search = GoogleSearch(params)
#     # results = search.get_dict()
#     # jobs_results = results["jobs_results"]


#     params = {
#     "engine": "google_news",
#     "q": "ai mumbai",
#     "api_key": "3fb9e0be680fbc384833423e983140627c494f8d1468c6dc9d1282661ede94e6"
#     }

#     search = GoogleSearch(params)
#     results = search.get_dict()
#     news_results = results["news_results"]
#     print(news_results)
#     # return render(request,'news/news.html',{'job_list':news_results})
#     return render(request,'news/news.html',{'news_list':news_results})
# # Create your views here.

import requests
from django.shortcuts import render

def getnews(request):
    skillsession = request.session.get('skill', 'python')
    print(skillsession)

    params = {
        "engine": "google_news",
        "q": skillsession,
        "api_key": "3fb9e0be680fbc384833423e983140627c494f8d1468c6dc9d1282661ede94e6"
    }

    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()

    news_results = data.get("news_results", [])
    return render(request,'news/news.html',{'news_list': news_results})





def get_loan_data(request):
    loan_data = [
        {
            'id': 1,
            'title': "Chief Ministers Special Rural Development Fund (CMSRDF)",
            'category': "Agriculture",
            'description': "The primary objective of the program is to generate wage employment and creation of socially and economically useful public assets by involving peoples participation at the grassroots level. The schemes undertaken in the program are varied in nature and are selected by the MLA and NGOs.",
            'apply_src': "",
        },
        {
            'id': 2,
            'title': "National Agriculture Market",
            'category': "Agriculture",
            'description': "e-NAM a pan-India electronic trading portal was launched on 14th April 2016, by the Prime Minister of India, with the aim of networking the existing mandis on a common online market platform as “One Nation One Market” for agricultural commodities in India.",
            'apply_src': "https://www.myscheme.gov.in/schemes/e-nam",
        },
        {
        'id': 3,
        'title': " Kisan Credit Card",
        'category': "Agriculture",
        'description':
        "The Kisan Credit Card (KCC) scheme was introduced in 1998 for issue of Kisan Credit Cards to farmers on the basis of their holdings for uniform adoption by the banks so that farmers may use them to readily purchase agriculture inputs and draw cash for their production needs.",
        'apply_src': "https://www.myscheme.gov.in/schemes/e-nam",
    },
    {
        id: 4,
        'title': "Kalpana Chawla Chatravriti Yojana",
        'category': "Education",
        'description':
        "Launched in 2012-13 by the Govt. of Himachal Pradesh, the Kalpana Chawla Chatravriti Yojana is a scholarship scheme that provides financial assistance to girls from economically weaker sections to pursue higher education without any financial burden, and achieve their career goals.",
        'apply_src': "https://www.myscheme.gov.in/schemes/e-nam",
    },

    {
        id: 5,
        'title':
        "Innovation In Science Pursuit For Inspired Research (INSPIRE) - Internship Ministers Special Rural Development Fund (CMSRDF)",
        'category': "Education",
        'description':
        "INSPIRE INTERNSHIP aims to provide exposure to the top 1% of students at the Class X Board level by organizing Science Camps either during summer or winter which provides an opportunity for them to interact with Science icons from India and abroad, including Nobel Laureates..",

       'apply_src': "https://www.myscheme.gov.in/schemes/e-nam",
    },

    {
        id: 6,
        'title':
        "Chief Special Education And Vocational Training Through Government Institutions Special Rural Development Fund (CMSRDF)",
        'category': "Education",
        'description':
        "In this scheme, Special Education is provided to children with disability between the age group of 6 to 18 years in the Government Special Schools and Vocational Training is provided to special children above the age of 18 years. Only citizens who are permanent residents of Maharashtra are eligible",
        'apply_src': "https://www.myscheme.gov.in/schemes/e-nam",
    },

    {
        id: 7,
        'title': "Chief Ministers Scheme For Wood Carving Artists",
        'category': "Business",
        'description':
        "The scheme “Chief Ministers Scheme for Wood Carving Artists” was launched to sustain the rich tradition of work on wood and is encouraged to propagate with the enhancement of aesthetic sensibilities so that it may be at par with international standards.The primary objective of the program is to generate wage employment and creation of socially and economically useful public assets by involving peoples participation at the grassroots level. The schemes undertaken in the program are varied in nature and are selected by the MLA and NGOs.",
       'apply_src': "https://www.myscheme.gov.in/schemes/e-nam",
    },

    {
        id: 8,
        'title': "Financial Assistance To Disabled For Self Employment",
        'category': "Business",
        'description':
        "The objective of this scheme is to facilitate the self-employment of unemployed disabled persons. Under this scheme, financial assistance is provided to persons with disabilities for self-employment, small-scale business, and agro-based project. This scheme is 100% funded by Govt. of Maharashtra.",
        'apply_src': "https://www.myscheme.gov.in/schemes/e-nam",
    },
    {
        id: 9,
        'title': "New Swarnima Scheme For Women",
        'category': "Business",
        'description':
        "A term loan scheme by the Ministry of Social Justice and Empowerment for women entrepreneurs from backward classes to obtain a loan of up to ₹2,00,000/- @ 5% per annum, thereby providing them social & financial security.  ",
        'apply_src': "https://www.myscheme.gov.in/schemes/e-nam",
    },
    {
        id: 10,
        'title':
        "PM POSHAN - Prime Minister's Overarching Scheme For Holistic Nourishment ",
        'category': "Health",
        'description':
        "PM POSHAN is a centrally sponsored scheme by the Department of School Education & Literacy, Ministry of Education. Under this scheme, one hot cooked meal will be provided to the children studying in Government and Government  aided schools. ",
        'apply_src': "https://www.myscheme.gov.in/schemes/e-nam",
    },
    {
        id: 11,
        'title': "Mukhyamantri Chiranjeevi Swasthya Beema Yojana",
        'category': "Business",
        'description':
        "The state government has announced the implementation of 'Universal Health Coverage' in the state in the budget announcement 2021-22, in compliance of which Chief Minister Chiranjeevi Health Insurance Scheme was started in the state from May 1, 2021.",
        'apply_src': "https://www.myscheme.gov.in/schemes/e-nam",
    },
    {
        id: 12,
        'title': "Ayushman Bharat - Pradhan Mantri Jan Arogya Yojana",
        'category': "Health",
        'description':
        "AB PM-JAY is a health insurance scheme for low-income families in rural and urban areas. The scheme aims to provide affordable healthcare facilities to the Poor. It is the largest health assurance scheme in the world which aims at providing a health cover of ₹ 5,00,000 per family per year.",
       'apply_src': "https://www.myscheme.gov.in/schemes/e-nam",
  },
        
    ]
    return render(request,'loans/loans.html',{'loan_data': loan_data})