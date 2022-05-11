from django.shortcuts import render
from django.views.generic import View

#addition view
class Addview(View):
    def get(self,request):
        return render(request,'add.html')
    def post(self, request):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        sum=int(n1)+int(n2)
        data={'sumofnum':sum,'number1':n1,'number2':n2}
        return render(request,"add.html",data)

#subtraction view
class Subtratcview(View):
    def get(self,request):
        return render(request,"sub.html")
    def post(self,request):
        num1=request.POST.get('n1')
        num2=request.POST.get('n2')
        sub=int(num1)-int(num2)
        data={'result':sub,'number1':num1,'number2':num2}
        return render(request,'sub.html',data)

#square
class Square(View):
    def get(self,request):
        return render(request,'square.html')
    def post(self,request):
        n=int(request.POST.get('num'))
        sq=n**2
        data={'result':sq,'numbers':n}
        return render(request, 'square.html',data)

#cube
class Cube(View):
    def get(self,request):
        return render(request,'cube.html')
    def post(self,request):
        num=int(request.POST.get('n'))
        cubes=num**3
        data={'result':cubes,'numbers':num}
        return render(request,'cube.html',data)

#factorial
class Factorial(View):
    def get(self,request):
        return render(request,'fact.html')
    def post(self,request):
        n=int(request.POST.get('num'))
        f=1
        for i in range(1,n+1):
            f=f*i
        data={'result':f,'num':n}
        return render(request, 'fact.html',data)
#prime
class PrimeView(View):
    def get(self,request):
        return render(request,'prime.html')
    def post(self,request):
        primes=[]
        nonprimes=[]
        number1=int(request.POST.get('num1'))
        number2 = int(request.POST.get('num2'))
        for i in range(number1,(number2+1)):
            for j in range(2,i):
                if i % j == 0:
                   nonprimes.append(i)
                   break
            else:
                primes.append(i)

        data={'prime_result':primes,'nonprime_result':nonprimes,'n1':number1,'n2':number2}
        return render(request, 'prime.html', data)


#wrdcount
class WordCount(View):
    def get(self,request):
        return render(request,'wordcount.html')
    def post(self,request):
            word = request.POST.get('wrd')
            d={}

            lwrd = word.lower()
            new_word = lwrd.rstrip("\n").split(" ")

            for wrd in new_word:
                if wrd not in d:
                    d.update({wrd:1})
                else:
                    values=d[wrd]
                    values+=1
                    d.update({wrd:values})
            # print(d)
        # word=''.join(filter(str.isalnum, request.POST.get('wrd')))
        # s=len(word)
        # s=0
        # for wd in word:
        #     s=s+1
        # data={'result':s,'w':word}
            data={'result':d}
            return render(request, 'wordcount.html',data)

class IndexView(View):
    def get(self,request):
        return render(request,'home.html')