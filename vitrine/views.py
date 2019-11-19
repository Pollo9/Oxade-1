from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound,Http404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from .models import *

def index_vitrine(request):

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'index_vitrine.html'
	return render(request,template,context)

def contact(request):

	if request.POST.get('envoyer'):
		Nom =  request.POST.get('prenom') + " " + request.POST.get('nom')
		commentaire =  request.POST.get('message')
		tel = request.POST.get('tel')
		subject = Nom + " - Ebrain contact"
		emailFrom = request.POST.get('mail')

		message ='%s \n\n Voici le mail pour répondre à %s : %s \n Voici le téléphone pour répondre à %s : %s' %(commentaire, Nom, emailFrom, Nom,tel)
		emailTo =[settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
		confirm_message = "Merci, Votre message à bien été envoyé !"
		print('email envoyé')

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))
	context = locals()

	template = 'contact.html'
	return render(request,template,context)

def conduite_du_changement(request):

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'offres/conduite_du_changement.html'
	return render(request,template,context)

def evenements(request):

	events = Bdd_evenement.objects.all()

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))


	context = locals()
	template = 'evenements.html'
	return render(request,template,context)

def digitalisation(request):

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'offres/digitalisation.html'
	return render(request,template,context)

def experience_client(request):

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'offres/experience_client.html'
	return render(request,template,context)

def fusions_et_acquisitions(request):

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'offres/fusions_et_acquisitions.html'
	return render(request,template,context)

def gestion_de_projets(request):

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'offres/gestion_de_projets.html'
	return render(request,template,context)

def reglementaire(request):
	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))
	context = locals()
	template = 'offres/reglementaire.html'
	return render(request,template,context)

def securite(request):

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'offres/securite.html'
	return render(request,template,context)

def transformation(request):

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'offres/transformation.html'
	return render(request,template,context)


def mentions_legales(request):

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'mentions_legales.html'
	return render(request,template,context)

def banque(request):

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'secteurs/banque.html'
	return render(request,template,context)

def assurance(request):

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'secteurs/assurance.html'
	return render(request,template,context)

def energie(request):

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'secteurs/energie.html'
	return render(request,template,context)

def secteur_public(request):

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'secteurs/secteur_public.html'
	return render(request,template,context)

def telecommunications(request):

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'secteurs/telecommunications.html'
	return render(request,template,context)

def transport_et_logistique(request):

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'secteurs/transport_et_logistique.html'
	return render(request,template,context)

def a_propos(request):

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'a_propos.html'
	return render(request,template,context)


def nous_rejoindre(request):

	if request.POST.get("sv"):
		Bdd_mail.objects.create(mail=request.POST.get("mail"))

	context = locals()
	template = 'nous_rejoindre.html'
	return render(request,template,context)


