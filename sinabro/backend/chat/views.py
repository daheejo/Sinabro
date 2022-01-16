from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
from .models import Message, SuvMessage, TmpUser
from .apps import ChatConfig
from .deep_model.data_process import sentence_to_char_index
import time



# Create your views here.
def index(request):
    if request.method == 'POST':
        new_message = Message.objects.create(
            send_text=request.POST['contents']
        )

        speak = sentence_to_char_index([request.POST['contents']], ChatConfig.vocab, False)
        result = ChatConfig.model.inference([speak])

        for sentence in result:
            response = ''
            for index in sentence:
                if index == 0:
                    break
                response += ChatConfig.reverse_vocab[index]
            bot_new_message = Message.objects.create(
                                            send_text=response,
                                            user=False
                                            )
        return redirect('/chat/')

    latest_message_list = Message.objects.order_by('pub_date')

    context = {
        'latest_message_list':latest_message_list,
    }

    return render(request, 'chat/index.html', context)

def delete(reuqest):
    Message.objects.all().delete()

    return redirect('/chat/')

q = ['''안녕! 이제 테스트를 진행해볼 건데, 질문에 대해서\n
    전혀 없음은 0,\n
    며칠동안은 1,\n
    1주일 이상은 2,\n
    거의 매일은 3,\n
    을 누르면 돼!\n
    (ex>1. 맞아 나는 집에서 보통 그렇게 느껴)그럼 시작해볼까?''',
    'Q1.매사에 흥미나 즐거움이 없는 편이야?',
    'Q2 그럼 기분이 가라앉거나 우울하거나 희망이 없다고 느끼는 날은? 많아?',
    'Q3 그렇구나, 그럼 잠들이 어렵거나 자주 깨거나 아니면 잠을 너무 많이 자기도 해?',
    'Q4 음.. 피곤하다고 느끼거나 기운이 거의 없다고 느낀 적은?',
    'Q5 그래도 맛있는 거 먹으면 기분이 풀리잖아, 식욕이 너무 줄거나 늘진 않았어?',
    'Q6 조심스럽지만, 스스로가 실패자로 느껴지거나 가족을 실망시켰다고 느낀적은 있어?',
    'Q7 책을 읽거나 tv를 보는 것처럼 일상적인 일에 집중하기 어렵다는 생각은?',
    'Q8 다른 사람들이 눈치 챌 정도로 평소보다 말과 행동이 느리거나, 혹은 너무 안절부절해서 가만히 앉아있을 수 없었던 적은?',
    'Q9 차라리 죽는 것이 낫겠다고 생각하거나 어떻게든 자해를 하려고 생각한 적은? ',
    '우리가 결과를 보여줄게! :)',]

def survey(request):

    if request.method == 'POST':
        if '0' in request.POST['contents']:
            new_message = SuvMessage.objects.create(
            send_text=request.POST['contents'],
            score = 0
            )
        elif '1' in request.POST['contents']:
            new_message = SuvMessage.objects.create(
            send_text=request.POST['contents'],
            score = 1
            )
        elif '2' in request.POST['contents']:
            new_message = SuvMessage.objects.create(
            send_text=request.POST['contents'],
            score = 2
            )
        elif '3' in request.POST['contents']:
            new_message = SuvMessage.objects.create(
            send_text=request.POST['contents'],
            score = 3
            )
        else:
            return redirect('/chat/survey/')

        

        speak = sentence_to_char_index([request.POST['contents']], ChatConfig.vocab, False)
        
        response = q[SuvMessage.objects.filter(user=1).count()]

        bot_new_message = SuvMessage.objects.create(
                                        send_text=response,
                                        user=False
                                        )
        return redirect('/chat/survey/')
        
    if SuvMessage.objects.filter(user=1).count() == 0:
        response = q[SuvMessage.objects.filter(user=1).count()]

        bot_new_message = SuvMessage.objects.create(
                                        send_text=response,
                                        user=False
                                        )

    latest_message_list = SuvMessage.objects.order_by('pub_date')
    context = {
        'latest_message_list':latest_message_list,
        'num_a':SuvMessage.objects.filter(user=1).count(),
    }


    return render(request, 'chat/survey.html', context)

def survey_delete(reuqest):
    SuvMessage.objects.all().delete()

    return redirect('/chat/survey/')

def survey_result(request):
    # make result
    score = 0
    for a in SuvMessage.objects.filter(user=1):
        score += a.get_score()
    if score <= 4:
        result_txt = '우울하지 않고 건강하네!'
    elif score <= 9:
        result_txt = '가벼운 우울증이 있어, 괜찮아?'
    elif score <= 14:
        result_txt = '중간 정도의 우울중이네, 괜찮아?'
    elif score <= 19:
        result_txt = '중간 정도의 우울중이네, 치료를 받아보는 것은 어때?'
    else:
        result_txt = '심한 우울증이 있어, 치료를 받는 게 좋을 것 같아'

    context = {'score':score,
               'result_txt' : result_txt}
    SuvMessage.objects.all().delete()
    return render(request, 'chat/survey_result.html', context)