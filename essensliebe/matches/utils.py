from decimal import Decimal
from django.contrib.auth import get_user_model
from django.db.models import Q
from questions.models import UserAnswer, Question

def get_match(user_a, user_b):
    q1 = Q(useranswer__user=user_a)
    q2 = Q(useranswer__user=user_b)
    question_set = Question.objects.filter(q1 | q2).distinct()
    a_points = 0
    b_points = 0
    a_total_points = 0
    b_total_points = 0 
    questions_in_common = 0 
    for question in question_set:
        try:
            a = UserAnswer.objects.get(user=user_a, question=question)
        except:
            a = None
        try:
            b = UserAnswer.objects.get(user=user_b, question=question)
        except:
            b = None
        if a and b:
            questions_in_common = 1
            if a.their_answer == b.my_answer:
                b_points += a.their_points
            b_total_points += a.their_points

            if b.their_answer== a.my_answer:
                a_points += b.their_points
            a_total_points += b.their_points

    if questions_in_common > 0: 
        a_decimal = a_points / Decimal(a_total_points)
        b_decimal = b_points / Decimal(b_total_points)
        if a_decimal == 0:
            a_decimal = 0.000001
        if b_decimal == 0:
            a_decimal = 0.000001
        match_percentage = (Decimal(a_decimal)) * Decimal(b_decimal)) ** (1/Decimal(questions_in_common))
        return match_percentage,questions_in_common

    else:
        return 0.0, 0

def get_points(user_a, user_b):
    a_answers = UserAnswer.objects.filter(user=user_a)[0]
    b_answers = UserAnswer.objects.filter(user=user_b)[0]
    a_total_awarded = 0
    a_points_possible = 0
    num_question = 0

    for a in a_answers:
        for b in b_answers:
            if a.question.id == b.question.id:
                a_pref = a.their_answer
                b_answer = b.my_answer
                if a_pref == b_answer:
                    '''
                    awards points for correct answer
                    '''
                    a_total_awarded += a.their_points
                '''
                assigning total points
                '''
                a_points_possible += a.their_points
            print ("%s has awarded %s points of %s to %s" % (user_a, a_total_awarded, a_points_possible, user_b))
    percent = a_total_awarded / Decimal(a_points_possible)
    print (percent, num_question)
    if percent == 0:
        percent = 0.00001
    return percent, num_question

