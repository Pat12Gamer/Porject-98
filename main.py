File1 = input("What is the first file: ")
File2 = input("What is the second file: ")

Que = open(File1,'r+')
Ans = open(File2,'r+')

content_que = Que.readlines()
content_ans = Ans.readlines()


Que.seek(0) 
Que.truncate() 


Ans.seek(0) 
Ans.truncate() 

Que.writelines(content_ans)
Ans.writelines(content_que)
Que.close()
Ans.close()