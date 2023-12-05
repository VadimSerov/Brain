import json
import g4f


mess=[]
while True:
    question = input("(Исключения: стоп, хватит, записать, прочитать) Что скажете?  ")
    if question.strip().lower()=="стоп":
        break
    if question.strip().lower()=="хватит":
        mess=[]
        print("Предлагаю поговорить на другую тему.")
        continue
    if question.strip().lower()=="записать":
        filename=input("имя файла для записи: ").strip()
        if filename != "":
            with open(filename+".json", "w") as file:
                json.dump(mess, file)
        continue
    if question.strip().lower()=="прочитать":
        filename=input("имя файла для чтения: ").strip()
        if filename != "":
            with open(filename+".json", "r") as file:
                mess = json.load(file)
        print("Возможно у нас теперь другая тема разговора.")
        continue
    mess.append({"role":"user", "content":question})
    
    answer = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=mess
    )
    print(answer)
    mess.append({"role":"assistant", "content":answer})
    
print("До свидания.")
