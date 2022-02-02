from allennlp.predictors.predictor import Predictor

predictor =Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/bidaf-model-2017.09.15-charpad.tar.gz")

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# allennlp-------------------------------
def allennlpMethod(Ques):
    
    with open('akbar-birbal-potOfWit.txt', 'r',encoding="utf8") as file:
        data2 = file.read().replace('\n', '')
    passage=data2
    result=predictor.predict(passage=passage,question=Ques)
    return result['best_span_str']



#html interface
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('try1.html')

@app.route('/process', methods=['POST','GET'])
def my_form_post():
    text = request.args.get('jsdata')
    
    flag=True
    print("My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
    while(flag==True):
        user_response = text
        
        user_response=user_response.lower()
        if(user_response!='bye'):
            if(user_response=='thanks' or user_response=='thank you' ):
                flag=False
                return jsonify({'output' : "You'r welcome"})
                print("You are welcome..")
            else:
                if(greeting(user_response)!=None):
                    return jsonify({'output' :greeting(user_response)})
                    print("ROBO: "+greeting(user_response))
                else:
                    print("ROBO: ",end="")
                    return jsonify({'output' :allennlpMethod(user_response)})
                    
        else:
            flag=False
            print("ROBO: Bye! take care..")
    
    return jsonify({'output' :"Bye.Take Care!"})

if __name__ == '__main__':
   app.run(host='0.0.0.0',debug=True)