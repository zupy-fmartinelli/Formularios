from django.shortcuts import render
from passagens.forms import PassagemForms, PessoaForms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
# Create your views here.
def index(request):
    form = PassagemForms()
    pessoa_form = PessoaForms
    contexto = {'form':form, 'pessoa_form':pessoa_form}
    return render(request, 'index.html', contexto)

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        pessoa_form = PessoaForms(request.POST)
        if form.is_valid():
            contexto = {'form':form, 'pessoa_form':pessoa_form}
            return render(request, 'minha_consulta.html', contexto)
        else:
            print('Form inválido')
            contexto = {'form':form, 'pessoa_form':pessoa_form}
            return render(request, 'index.html', contexto)