import g4f


mess=[]
while True:
    question = input(" Что скажете?  ")
    if question.strip().lower()=="стоп":
        break
    if question.strip().lower()=="хватит":
        mess=[]
        print("Предлагаю поговорить на другую тему.")
        continue
    mess.append({"role":"user", "content":question})
    
    answer = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=mess
    )
    print(answer)
    mess.append({"role":"assistant", "content":answer})
    
print("До свидания.")
