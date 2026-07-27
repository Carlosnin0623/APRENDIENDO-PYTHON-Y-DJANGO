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
            'level': 'Principiante',
            'rating': 5.0,
            'course_title': 'Beginner Guide to Successful Company Management:Business And More',
            'instructor': 'Patty Kutch',
            'course_image': 'images/curso_2.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/20.jpg'
        },

        {
            'id': 3,
            'level': 'Principiante',
            'rating': 5.0,
            'course_title': 'A Fascinating Theory of Probability. Practice Application. How to Outplay...',
            'instructor': 'Alonzo Murray',
            'course_image': 'images/curso_3.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/men/32.jpg'
        },

        {
            'id': 4,
            'level': 'Principiante',
            'rating': 5.0,
            'course_title': 'Introduction: Machine Learning and LLM. Implementation in Modern Software',
            'instructor': 'Gregory Harris',
            'course_image': 'images/curso_4.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/men/45.jpg'
        },


    ]
    return render(request, 'courses/courses.html', {
        'courses': courses
    })


def course_detail(request):
    pass


def course_lessons(request):
    pass
