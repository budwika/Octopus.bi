from django.shortcuts import render
from .models import School, Class, Student, Subject, Assessment_Areas, Awards, Answers

def dataFetch(request):
    schools = School.objects.all()
    schools_title = "Schools Table"
    schools_headers = ["School ID", "School Name"]
    schools_data = [[school.school_id, school.school_name] for school in schools]

    classes = Class.objects.all()
    classes_title = "Classes Table"
    classes_headers = ["Class ID", "Class Name", "School Name"]
    classes_data = [[class_.class_id, class_.class_name, class_.school.school_name] for class_ in classes]

    students = Student.objects.all()
    students_title = "Students Table"
    students_headers = ["Student ID", "Full Name", "Class Name"]
    students_data = [[student.student_id, student.fullname, student.class_id] for student in students]

    subjects = Subject.objects.all()
    subjects_title = "Subjects Table"
    subjects_headers = ["Subject ID", "Subject"]
    subjects_data = [[subject.subject_id, subject.subject] for subject in subjects]

    assessment_areas = Assessment_Areas.objects.all()
    assessment_areas_title = "Assessment Areas Table"
    assessment_areas_headers = ["Assessment Area ID", "Assessment Area"]
    assessment_areas_data = [[area.assessment_area_id, area.assessment_area] for area in assessment_areas]

    awards = Awards.objects.all()
    awards_title = "Awards Table"
    awards_headers = ["Award"]
    awards_data = [[award.award] for award in awards]

    answers = Answers.objects.all()
    answers_title = "Answers Table"
    answers_headers = ["Answer ID", "Answer"]
    answers_data = [[answer.id, answer.answers] for answer in answers]

    context = {
        'tables': [
            {'title': schools_title, 'headers': schools_headers, 'data': schools_data},
            {'title': classes_title, 'headers': classes_headers, 'data': classes_data},
            {'title': students_title, 'headers': students_headers, 'data': students_data},
            {'title': subjects_title, 'headers': subjects_headers, 'data': subjects_data},
            {'title': assessment_areas_title, 'headers': assessment_areas_headers, 'data': assessment_areas_data},
            {'title': awards_title, 'headers': awards_headers, 'data': awards_data},
            {'title': answers_title, 'headers': answers_headers, 'data': answers_data},
        ]
    }
    return render(request, 'table.html', context)
