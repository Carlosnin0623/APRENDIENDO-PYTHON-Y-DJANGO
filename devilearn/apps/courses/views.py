from django.shortcuts import render
# Create your views here.


def course_list(request):
    courses = [
        {
            'id': 1,
            'level': 'Principiante',
            'rating': 4.8,
            'course_title': 'Python: Fundamentos hasta los detalles',
            'instructor': 'Alison Walsh',
            'course_image': 'images/curso_1.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/68.jpg'

        },

        {
            'id': 2,
            'level': 'Intermedio',
            'rating': 4.9,
            'course_title': 'Django: Aplicaciones robustas',
            'instructor': 'Patty Kutch',
            'course_image': 'images/curso_2.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/20.jpg'
        },

        {
            'id': 3,
            'level': 'Avanzado',
            'rating': 5.0,
            'course_title': 'Django Rest',
            'instructor': 'Alonzo Murray',
            'course_image': 'images/curso_3.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/men/32.jpg'
        },

        {
            'id': 4,
            'level': 'Principiante',
            'rating': 5.0,
            'course_title': 'Fast API',
            'instructor': 'Gregory Harris',
            'course_image': 'images/curso_4.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/men/45.jpg'
        },


    ]
    return render(request, 'courses/courses.html', {
        'courses': courses
    })


def course_detail(request):
   course = {
       'course_title': 'Django Aplicaciones',
       'couse_link': '',
       'info_course': {
           'lessons': 79,
           'duration': 8,
           'instructor': 'Ricardo Cuéllar'
       },
       'course_content':[
           {
               'id': 1,
               'name': 'Introducción al curso',
               'Lessons': [
                   {
                       'name': '¿Que aprenderás en el curso?',
                       'type': 'video'
                   },
                   
                   {
                        'name': '¿Como usar la plataforma?',
                        'type': 'article'
                    },
                   
               ]
           }
       ]
   }
   return render(request, 'courses/courses_detail.html', {
       'course': course
   })


def course_lessons(request):
    pass
