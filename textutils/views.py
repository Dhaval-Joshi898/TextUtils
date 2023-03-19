# I have created this (views.py) file -Dhaval Joshi
#view retuns a http response
from django.http import HttpResponse
from django.shortcuts import render

#def index(request):     #this function takes argument i.e request(1 argument)
  #  return HttpResponse('''<h1>Hello Dhaval Joshi </h1> <a href="https://www.google.com/"> Google</a>''')
#def about(request):     
    #return HttpResponse("About Dhaval Joshi")
#def link(request):
   # return HttpResponse('''<a href="https://www.facebook.com/">Facebook</a>''')

def index(request): 
    #parameter={'name':'Dhaval','place':"India"}
    return render(request,'index.html')       #render take two arguments(request,and html file) it also takes the third argument
                                                # i.e variable (3 argument)  import from django.shortcuts

    #return HttpResponse('''Home ''')

def analyze(request):
    #Get the text and analyze the text.
    #GET display text in url which is not safe and there is limit in url content size.
   # djtext=request.GET.get('text','default')    #request.GET.get('text'this argument is used to get text from textarea name given text and if text is no there in text area it takes default values)
    
    djtext=request.POST.get('text','default')    
    #Check Checkbox values.
   # removepunc=request.GET.get('removepunc','off')     when method was get we used this 
    removepunc=request.POST.get('removepunc','off')    
    fullcaps=request.POST.get('fullcaps','off')    
    fullsmall=request.POST.get('fullsmall','off')   
    newlineremover=request.POST.get('newlineremover','off')   
    extraspaceremover=request.POST.get('extraspaceremover','off')   
    charcount=request.POST.get('charcount','off')   


    #print(djtext) #print the text in text area will show in terminal for debugging
    #print(removepunc) #it will print on if checkbox tick true else defalut or default can be any value(e.g.off)..

    #analyzed=djtext

    #CHeck Which checkbox is ON>
    if removepunc=='on':
                
        Punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=""

        for char in djtext:
            if char  not in Punctuations:
                analyzed=analyzed + char
        
        parameter={'purpose':"Remove Punctuatuion",'analyzed_text':analyzed}
        #Analyzed the text 
        djtext=analyzed
        #return render(request,'analyze.html',parameter)
        
    
 #   elif removepunc=='on' and fullcaps=='on':
                
    #    Punctuations='''"!""#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        """
        analyzed=" "

        for char in djtext:
            if char  not in Punctuations:
                analyzed=analyzed + char
               # analyzed=analyzed + char.upper()

        for i in analyzed:    #djtext is the text written in textarea the box 
            analyzed2=analyzed + i.upper()

        parameter={'purpose':"Remove Punctuatuion And UPPERCASE the text",'analyzed_text':analyzed2}
        #Analyzed the text
        return render(request,'analyze.html',parameter)"""


    
    #elif(fullcaps=='on'):
    if(fullcaps=='on'):
        analyzed=""
        for char in djtext:    #djtext is the text written in textarea the box 
            analyzed=analyzed + char.upper()
        
        parameter={'purpose':"Change Into Capital(UPPERCASE)",'analyzed_text':analyzed}
        #Analyzed the text
        djtext=analyzed
        return render(request,'analyze.html',parameter)

    if(fullsmall=='on'):
        analyzed=''
        for char in djtext:
            analyzed=analyzed+ char.lower()

        parameter={'purpose':"Change into small letter(LOWERCASE)",'analyzed_text':analyzed}
        #Analyzed the text
        djtext=analyzed
        #return render(request,'analyze.html',parameter)

    if(newlineremover=='on'):
        #analyzed=''
        #my logic:-
        b=djtext.splitlines()
        analyzed=print(' '.join(b)) #for debugging
        analyzed=' '.join(b)

    #    """cwh logic
    #     analyzed=''
    #     for char in djtext:
    #      #   print(char)
    #         if char!="\n":# and char!="\r"
    #            # print(char)
    #             analyzed=analyzed+ char
    #             print(analyzed)
    #         else:
    #             print('line break aaya')
        
    #     print(analyzed)"""

            
        parameter={'purpose':"Remove new line",'analyzed_text':analyzed}
        #Analyzed the text
        djtext=analyzed
        #return render(request,'analyze.html',parameter)

    if(extraspaceremover=='on'):
        analyzed=''
        for index,char in enumerate(djtext):
            if not(djtext[index] ==" " and djtext[index+1]==" "):
                analyzed=analyzed+ char
            


        parameter={'purpose':"Remove extra space",'analyzed_text':analyzed}
        #Analyzed the text
        djtext=analyzed
        #return render(request,'analyze.html',parameter)
        
    if(charcount=='on'):
        replaced_djtext=djtext.replace(" ","")
        print(len(djtext))
        analyzed=len(replaced_djtext)    
            

        parameter={'purpose':"Character Count!!",'analyzed_text':analyzed}
        #Analyzed the text
        djtext=analyzed

    return render(request,'analyze.html',parameter) #return for the function
        
    #else:
       # return HttpResponse("ERROR!Please tick the checkbox to remove punctuation.")

def about(request):
    return render(request,'about.html')



































# def capfirst(request):
#     return HttpResponse('''Capitalize First ''')

# def newlineremove(request):
#     return HttpResponse("Remove New line" )

# def spaceremove(request):
#     return HttpResponse("Remove Space")

# def charcount(request):
#     return HttpResponse("count the characters")

   