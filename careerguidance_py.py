# -*- coding: utf-8 -*-
"""careerguidance.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1s3BlX3t8ZQRiHwHuJC24aADj3TNUK_54
"""

#q/answers.
#must write interested/want in.
qna={
    'hi':'hey',
    'how are you':'fine',
    'what is your name':'my name is chatbot',
    'what is your role':'provide career guidance',
    'interested in experiments what should she/he should choose':'should choose sciences like physics,chemistry and biology',
    'intersted in problem solving what should he/she choose':'should choose math',
    'interested in sports what should he/she choose':'should choose sports',
    'interested in writing what should he/she choose':'should choose writer',
    'interested in engineering what should he/she choose':'should choose engineering',
    'interested in science what should he/she choose':'should choose scientist',
    'interested in sales what should he/she choose':'should choose salesperson',
    'interested in technical things what should he/she choose':'should choose IT field',
    'interested/want in drawing and arts':'should choose graphic designing',
    'interested/want in logical reasoning ':'should choose programing',
    'interested/want in managment ':'should choose project manager',
}
while True:
  qs=input()

  if(qs=='quit'):
    break
  if qs in qna:
    print(qna[qs])
  else:
    print('i dont know')