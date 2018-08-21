from decimal import Decimal
from django.contrib.auth import get_user_model

from questions.models import UserAnswer

User = get_user_model()

users = User.objects.all()
all_user_answers = UserAnswer.objects.all().order_by("user__id")


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
            print "%s has awarded %s points of %s to %s" %(user_a, a_total_awarded, a_points_possible, user_b)
    percent = a_total_awarded / Decimal(a_points_possible)
    print percent, num_question
    if percent == 0:
        percent = 0.00001
    return percent, num_question

match_percentage = "%.2f" % ((Decimal(a[0]) * Decimal(b[0])) ** (1/Decimal(b[1])))
print match_percentage