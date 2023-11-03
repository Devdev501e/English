import string
from tkinter import *
from random import randint, choice
import difflib
import pandas as pd
import datetime

#les paramétrages:

liste = [{"question": "Present simple", "reponse": "verb(infinitive)", "auxiliaire": [], "number": 1}, {"question": "Present continuous", "reponse": "verb(ing)", "auxiliaire": ["am", "is", "are"], "number": 2},{"question": "Past simple (Prétérit simple)", "reponse": "verb(ed)", "auxiliaire": [], "number":1},{"question": "Past continuous (Prétérit progressif)", "reponse": "verb(ing)", "auxiliaire": ["was", "were"], "number":2},{"question": "Present perfect Simple", "reponse": "verb(ed)", "auxiliaire": ["have","has"], "number":2},{"question": "Present perfect continuous", "reponse": "been+verb(ing)", "auxiliaire": ["have","has"], "number":3},{"question": "Past perfect simple", "reponse": "verb(ed)", "auxiliaire": ["had"], "number":2},{"question": "Past perfect continuous", "reponse": "been+verb(ing)", "auxiliaire": ["had"], "number":3},{"question": "Future", "reponse": "verb(infinitive)", "auxiliaire": ["will"], "number":2},{"question": "Future continuous", "reponse": "be+verb(ing)", "auxiliaire": ["will"], "number":3},{"question": "Future perfect", "reponse": "²have+verb(ed)", "auxiliaire": ["will"], "number":3}]

liste_prn = ["prn", "pronom", "he", "she", "i", "you", "they", "we", "pronoun"]

liste_resultat=[]

liste_2_resultat=[]

liste_question_already=[]

liste_2_question_already=[]

liste_faute=[0,0]


#import excel:


# Remplacez 'votre_fichier.xlsx' par le nom de votre fichier Excel
nom_fichier = 'verbes.xlsx'



# Lire le fichier Excel et stocker les données dans un DataFrame
df = pd.read_excel(nom_fichier)

# Convertir le DataFrame en une liste de dictionnaires
tableau_donnees = df.to_dict(orient='records')

# Afficher la liste de dictionnaires

print(tableau_donnees)

#crée la fenetre

window = Tk()
window.title("generateur de passport")
window.geometry("1920x1080")

window.config(background='#4065A4')
#frames

frame_1 = Frame(window,bg='#4065A4') #password
frame_2 =Frame(window,bg='#4065A4') #anglais_1
frame_2_fin =Frame(window,bg='#4065A4') #anglais_1
frame_3 =Frame(window,bg='#4065A4') #anglais_2
frame_3_fin =Frame(window,bg='#4065A4') #anglais_2
frame_4 = Frame(window,bg='#4065A4') #notes_views

#crer une sous boite
right_frame_1 = Frame(frame_1, bg='#4065A4')

#création d'une image

width = 300
height = 300
image = PhotoImage(file="biscuit.png").zoom(35).subsample(32)
canvas = Canvas(frame_1, width=width, height=height, bg='#4065A4', bd='0',highlightthickness=0)
canvas.create_image(width/2,height/2,image=image)
canvas.grid(row=0, column=0, sticky=W)



#crée un text
label_title = Label(right_frame_1, text="Mot de passe",font=("Helvetica",20),bg='#4065A4',fg='white')
label_title.pack()

anglais_question = Label(frame_2, text="Question",font=("Helvetica",20),bg='#4065A4',fg='white')
anglais_question.pack(pady=20)

anglais_info = Label(frame_2, text="info",font=("Helvetica",20),bg='#4065A4',fg='white')
anglais_info.pack(pady=20)

anglais_text_info_fin = Label(frame_2_fin, text="info",font=("Helvetica",20),bg='#4065A4',fg='white')
anglais_text_info_fin.pack(pady=20)

anglais_2_question_verbe = Label(frame_3, text="verb",font=("Helvetica",20),bg='#4065A4',fg='white')

anglais_2_question_francais = Label(frame_3, text="translation",font=("Helvetica",20),bg='#4065A4',fg='white')

anglais_2_question_participe = Label(frame_3, text="past participle",font=("Helvetica",20),bg='#4065A4',fg='white')

anglais_2_question_preterit = Label(frame_3, text="past simple",font=("Helvetica",20),bg='#4065A4',fg='white')

anglais_2_info = Label(frame_3, text="info",font=("Helvetica",20),bg='#4065A4',fg='white')

anglais_2_info_fin = Label(frame_3_fin, text="info",font=("Helvetica",20),bg='#4065A4',fg='white')
anglais_2_info_fin.pack()




#champ input
password_entry = Entry(right_frame_1, font=("Helvetica", 20), bg='#4065A4', fg='white')
password_entry.pack()

anglais_entry = Entry(frame_2, font=("Helvetica", 20), bg='#4065A4', fg='white')
anglais_entry.pack(pady=20)

anglais_2_entry_participe = Entry(frame_3, font=("Helvetica", 20), bg='#4065A4', fg='white')


anglais_2_entry_preterite = Entry(frame_3, font=("Helvetica", 20), bg='#4065A4', fg='white')




#def

def execute_both_commands(frame):
    notes_creator()
    open_frame(frame)






def notes_creator():
    frame_anglais_1 = Frame(frame, bg='#4065A4',width=200, height=100, bd=3, relief=SUNKEN)
    frame_anglais_1.grid(row=0, column=0,padx=10, pady=10)
    label = Label(frame_anglais_1, width=20, height=2, text="Anglais_1")
    label.grid(row=0, column=1)



    frame_anglais_2 = Frame(frame, bg='#4065A4',width=200, height=100, bd=3, relief=SUNKEN)
    frame_anglais_2.grid(row=1, column=0,padx=10, pady=10)
    label = Label(frame_anglais_2, width=20, height=2, text="Anglais_2")
    label.grid(row=0, column=1)


    list_notes_anglais_1 = []

    list_notes_anglais_2 = []

    list_notes = get_notes()

    for i in range(0, len(list_notes)):
        if get_notes()[i]['Exercices'] == "Anglais_1":

            frame_direction = frame_anglais_1
            list_notes_anglais_1.append(list_notes[i]['Notes'])
        else:
            frame_direction = frame_anglais_2
            list_notes_anglais_2.append(list_notes[i]['Notes'])

        frame_infos_i = Frame(frame_direction, bg='#4065A4', bd=3, relief=SUNKEN)  # password
        frame_infos_i.grid(row=i+1, column=1)
        frame_times_i = Frame(frame_direction, bg='#4065A4', bd=3, relief=SUNKEN)  # password
        frame_times_i.grid(row=i+1, column=2)
        frame_notes_i = Frame(frame_direction, bg='#4065A4', bd=3, relief=SUNKEN)  # password
        frame_notes_i.grid(row=i+1, column=3)

        label = Label(frame_notes_i,width=4, height=3, text=f"{list_notes[i]['Notes']}%")
        label.pack()
        moth=""
        mois=list_notes[i]['Dates'][3:5]
        moth_liste=['January','February','March','April','May','June','July','August','September','October','November','December']
        moth =  moth_liste[int(mois)-1]

        label = Label(frame_times_i,width=25, height=3, text=f"{list_notes[i]['Dates'][0:2]} {moth} {list_notes[i]['Dates'][6:10]} at {get_notes()[i]['Times']}")
        label.pack()

        label = Label(frame_infos_i,width=30, height=3, text=f"{list_notes[i]['Commentaire']}",wraplength=200)
        label.pack()

    moyenne_anglais_1 = "{:.1f}".format((sum(list_notes_anglais_1) / len(list_notes_anglais_1)))
    moyenne_anglais_2 = "{:.1f}".format((sum(list_notes_anglais_2) / len(list_notes_anglais_2)))

    frame_infos_moyenne_angalais_1 = Frame(frame_anglais_1, bg='#4065A4', bd=3, relief=SUNKEN)
    frame_infos_moyenne_angalais_1.grid(row=len(list_notes)*2, column=1)
    frame_times_moyenne_angalais_1 = Frame(frame_anglais_1, bg='#4065A4', bd=3, relief=SUNKEN)
    frame_times_moyenne_angalais_1.grid(row=len(list_notes)*2, column=2)
    frame_notes_moyenne_angalais_1 = Frame(frame_anglais_1, bg='#4065A4', bd=3, relief=SUNKEN)
    frame_notes_moyenne_angalais_1.grid(row=len(list_notes)*2, column=3)

    label = Label(frame_infos_moyenne_angalais_1, text="Moyenne des notes")
    label.pack()

    label = Label(frame_times_moyenne_angalais_1, text="zqfdqzdqz")
    label.pack()

    label = Label(frame_notes_moyenne_angalais_1, text=f"{moyenne_anglais_1}%")
    label.pack()

    frame_infos_moyenne_angalais_2 = Frame(frame_anglais_2, bg='#4065A4', bd=3, relief=SUNKEN)
    frame_infos_moyenne_angalais_2.grid(row=len(list_notes)*2, column=1)
    frame_times_moyenne_angalais_2 = Frame(frame_anglais_2, bg='#4065A4', bd=3, relief=SUNKEN)
    frame_times_moyenne_angalais_2.grid(row=len(list_notes)*2, column=2)
    frame_notes_moyenne_angalais_2 = Frame(frame_anglais_2, bg='#4065A4', bd=3, relief=SUNKEN)
    frame_notes_moyenne_angalais_2.grid(row=len(list_notes)*2, column=3)

    label = Label(frame_infos_moyenne_angalais_2, text="Moyenne des notes")
    label.pack()

    label = Label(frame_times_moyenne_angalais_2, text="zqfdqzdqz")
    label.pack()

    label = Label(frame_notes_moyenne_angalais_2, text=f"{moyenne_anglais_2}%")
    label.pack()


def get_notes():
    data_results = 'Data_results.xlsx'

    # Lire le fichier Excel et stocker les données dans un DataFrame
    df = pd.read_excel(data_results)

    # Convertir le DataFrame en une liste de dictionnaires
    tableau_donnees_notes = df.to_dict(orient='records')

    # Afficher la liste de dictionnaires


    return tableau_donnees_notes

def whirte_data_results(notes, exercice,commentaire):
    excel_Data_results = 'Data_results.xlsx'
    df_existing = pd.read_excel(excel_Data_results)
    liste_time = get_time()
    new_data = {

        'Exercices': [exercice],
        'Commentaire': [commentaire],
        'Dates': [liste_time[0]],
        'Times': [liste_time[1]],
        'Notes': [notes]
    }
    df_new = pd.DataFrame(new_data)

    # Concaténez les deux DataFrames en ajoutant les nouvelles données à la suite des données existantes
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)

    # Écrivez le DataFrame résultant dans le même fichier Excel sans l'index
    df_combined.to_excel(excel_Data_results, index=False)



def get_time():

    liste_time=[]
    date_actuelle = datetime.datetime.now()
    format_1 = date_actuelle.strftime("%d-%m-%Y")
    format_2 = date_actuelle.strftime("%H:%M:%S")
    liste_time.append(format_1)
    liste_time.append(format_2)
    return liste_time

def open_frame(frame):
    frame_1.pack_forget()
    frame_2.pack_forget()
    frame_2_fin.pack_forget()
    frame_3.pack_forget()
    frame_3_fin.pack_forget()
    frame_4.pack_forget()
    frame.pack(expand=YES)
def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range (randint(password_min,password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


def swich():
   anglais_info.config(text="")
   if len(liste_question_already)==len(liste):
       nombre_de_true = 0
       nombre_de_false = 0
       for valeur in liste_resultat:
           if valeur:
               nombre_de_true += 1
           else:
               nombre_de_false += 1

       frame_2.pack_forget()
       frame_2_fin.pack(expand=YES)
       j= nombre_de_true/len(liste_resultat)*100


       if j>50:
         anglais_text_info_fin.config(text=f" Well done you have {int(j)}%")
         whirte_data_results(int(j), "Anglais_1","well done you did a great work, carry on")
       else:
           anglais_text_info_fin.config(text=f" Try again you have {int(j)}%")
           whirte_data_results(int(j), "Anglais_1", "you must work more to get better results")

       anglais_entry.delete(0, END)
       liste_resultat.clear()
       liste_question_already.clear()

       return
   else:
     number_question = randint(0, 10)
     while number_question in liste_question_already:
         number_question = randint(0, 10)

     liste_question_already.append(number_question)
     print(number_question)
     print(liste_question_already[-1])
     anglais_question.config(text=liste[liste_question_already[-1]]["question"])
     anglais_button_swicth.pack_forget()
     anglais_button.pack(pady=20, fill=X)


def filtrage(reponse_utilisateur,filtrage_number):
    numbers = 0

    for k in range(0,filtrage_number):
        i = 0
        reponse_utilisateur_traitement = ""
        for lettre in reponse_utilisateur:  # permet de filtrer la réponse des +
            i += 1
            if ((lettre == "+" and i < len(reponse_utilisateur) and reponse_utilisateur[i] != "+") or (
                    lettre == " " and i < len(reponse_utilisateur) and reponse_utilisateur[i] != " ")) and i != 1:
                if lettre == "+" and reponse_utilisateur[i] != " ":
                    numbers += 1
                    reponse_utilisateur_traitement += "+"
                elif lettre == " " and reponse_utilisateur[i] != "+":
                    numbers += 1
                    reponse_utilisateur_traitement += "+"

            if lettre != "+" and lettre != " ":
                reponse_utilisateur_traitement += lettre
        reponse_utilisateur = reponse_utilisateur_traitement
        if k !=filtrage_number-1:
            numbers = 0

    return [numbers,reponse_utilisateur]

def separation(reponse_utilisateur_traitement,auxiliaire):
    reponse_utilisateur_traitement_after=""
    pronom = ""
    nimbers2 = 0
    for lettre in reponse_utilisateur_traitement:  # permet de retirer les auxiliaires

        if lettre != "/" and nimbers2 >= auxiliaire:
            reponse_utilisateur_traitement_after += lettre
        if lettre == "+":
            nimbers2 += 1
        if nimbers2 == 0:
            pronom += lettre
    return [pronom,reponse_utilisateur_traitement_after]
def verifier_question():
    if anglais_entry.get() != "":
        reponse_utilisateur = anglais_entry.get()
        reponse_utilisateur = reponse_utilisateur.lower()
        numbers = 0



        reponse_utilisateur_traitement = ""  #prn+am/is/are+verb(infinitive)
        reponse_utilisateur_traitement_after = ""
        auxiliaire = []
       #auxiliaire_vrai = []
        auxiliaire_bol = FALSE
        pronom=""

        list_t = filtrage(reponse_utilisateur, 2)
        numbers = list_t[0]
        reponse_utilisateur_traitement=list_t[1]



        reponse_utilisateur=""
        if(liste[liste_question_already[-1]]["auxiliaire"]!=[] and liste[liste_question_already[-1]]["number"]==numbers):
            nimbers2 = 0
            for lettre in reponse_utilisateur_traitement:               #permet de recupere les auxiliaires

                if nimbers2 == 1 and lettre != "/"and lettre != "+":
                    reponse_utilisateur+=lettre
                elif lettre == "/":
                    auxiliaire.append(reponse_utilisateur)
                    reponse_utilisateur = ""
                elif nimbers2 > 1:
                    auxiliaire.append(reponse_utilisateur)
                    break
                if lettre == "+":
                    nimbers2 += 1

            list_sans_auxiliaires = separation(reponse_utilisateur_traitement,2)
            pronom = list_sans_auxiliaires[0]
            reponse_utilisateur_traitement_after=list_sans_auxiliaires[1]



            print(pronom)
            print(auxiliaire)
            print("reponse_utilisateur_traitement_after = ", reponse_utilisateur_traitement_after)

            if pronom in liste_prn:
                if len(auxiliaire) == len(
                        liste[liste_question_already[-1]]["auxiliaire"]):  # verifie la taille des listes auxiliaires

                    auxiliaire_vrai = [x for x in liste[liste_question_already[-1]]["auxiliaire"]]
                    for k in range(0, len(auxiliaire)):  # verifie les auxiliaires

                        correspondance_proche = difflib.get_close_matches(auxiliaire[k], auxiliaire_vrai, n=1,
                                                                          cutoff=0.95)
                        if correspondance_proche:
                            auxiliaire_vrai.remove(correspondance_proche[0])
                            print("liste a suprimer = ", auxiliaire_vrai)

                    if auxiliaire_vrai == []:
                        auxiliaire_bol = TRUE
                    else:
                        print("auxiliaire faux ")
                        auxiliaire_bol = FALSE
                else:
                    print("auxiliaire faux ")
                    auxiliaire_bol = FALSE
            else:
              print("pronom pas bon")
              auxiliaire_bol = FALSE

        elif liste[liste_question_already[-1]]["number"] != numbers:
             print("trop d'espace")
             auxiliaire_bol=FALSE
        else:
            list_sans_auxiliaires = separation(reponse_utilisateur_traitement, 1)
            pronom = list_sans_auxiliaires[0]
            reponse_utilisateur_traitement_after = list_sans_auxiliaires[1]
            if pronom in liste_prn:

             auxiliaire_bol = TRUE
            else:
             print("pronom pas bon")
             auxiliaire_bol = FALSE


        print(auxiliaire_bol)
        print("reponse_utilisateur_traitement_after",reponse_utilisateur_traitement_after)
        print("liste[liste_question_already[-1]]",liste[liste_question_already[-1]]["reponse"])
        comparateur = difflib.SequenceMatcher(None, reponse_utilisateur_traitement_after, liste[liste_question_already[-1]]["reponse"])
        if float(comparateur.ratio()) >= 0.95 and auxiliaire_bol:
            anglais_info.config(text="well donne")
            anglais_button.pack_forget()
            anglais_button_swicth.pack(pady=20, fill=X)
            anglais_entry.delete(0, END)
            liste_resultat.append(TRUE)
            anglais_question.config(text="")

        else:
            anglais_info.config(text=reponse_utilisateur_traitement)
            liste_resultat.append(FALSE)
    else:
        anglais_info.config(text="pas de réponse")

def swich_2():

    if len(liste_2_question_already) == 10:
        frame_3_fin.pack(expand=YES)
        frame_3.pack_forget()
        nombre = 0
        for bol in liste_2_resultat:
            if bol:
                nombre += 1

        nombre = nombre/len(liste_2_resultat)*100


        if nombre > 50:
            anglais_2_info_fin.config(text=f" Well done you have {int(nombre)}%")
            whirte_data_results(int(nombre), "Anglais_2", "well done you did a great work, carry on")
        else:
            anglais_2_info_fin.config(text=f" Try again you have {int(nombre)}%")
            whirte_data_results(int(nombre), "Anglais_2", "you must work more to get better results")

        liste_2_resultat.clear()
        liste_2_question_already.clear()
        return

    liste_faute[0] = 0
    anglais_2_entry_preterite.delete(0, END)
    anglais_2_entry_participe.delete(0, END)
    numbers_2 = randint(0,len(tableau_donnees)-1)
    while numbers_2 in liste_2_question_already:
        numbers_2 = randint(0,len(tableau_donnees)-1)
    liste_2_question_already.append(numbers_2)
    anglais_2_question_verbe.config(text=tableau_donnees[liste_2_question_already[-1]]["Infinitive"])
    anglais_2_question_francais.config(text=f"({tableau_donnees[liste_2_question_already[-1]]['Traduction']})")
    anglais_2_button_swicth.pack_forget()
    anglais_2_button.pack()
    anglais_2_info.config(text="")


def verifier_question_2():

    user_response_preterite = anglais_2_entry_preterite.get()
    user_response_participle = anglais_2_entry_participe.get()

    user_response_preterite = user_response_preterite.lower()
    user_response_participle = user_response_participle.lower()

    comparateur_preterite = difflib.SequenceMatcher(None, user_response_preterite, tableau_donnees[liste_2_question_already[-1]]['preterite'])
    comparateur_participe = difflib.SequenceMatcher(None, user_response_participle, tableau_donnees[liste_2_question_already[-1]]['Participe'])

    if user_response_preterite != "" and user_response_participle != "":
         if comparateur_preterite.ratio()>= 0.95 and comparateur_participe.ratio() >= 0.95:
              anglais_2_info.config(text="well done")
              anglais_2_button.pack_forget()
              anglais_2_button_swicth.pack()
              liste_2_resultat.append(TRUE)
         else :

              liste_2_resultat.append(FALSE)
              liste_faute[0] += 1

         if comparateur_preterite.ratio()< 0.95:
             anglais_2_info.config(text="the past simple is not correct")
             anglais_2_entry_preterite.delete(0, END)



         if  comparateur_participe.ratio() < 0.95:

             anglais_2_info.config(text="the past participle is not correct")

             anglais_2_entry_participe.delete(0, END)


         if comparateur_preterite.ratio() < 0.95 and comparateur_participe.ratio() <0.95:

            anglais_2_info.config(text="no one is correct try again")
            anglais_2_entry_preterite.delete(0, END)
            anglais_2_entry_participe.delete(0, END)
         if liste_faute[0] == 3:
             liste_faute[0] = 0
             anglais_2_info.config(text="you have tried too much times")
             anglais_2_entry_preterite.delete(0, END)
             anglais_2_entry_participe.delete(0, END)
             anglais_2_entry_preterite.insert(0, tableau_donnees[liste_2_question_already[-1]]['preterite'])
             anglais_2_entry_participe.insert(0, tableau_donnees[liste_2_question_already[-1]]['Participe'])
             anglais_2_button.pack_forget()
             anglais_2_button_swicth.pack()
    else:
        anglais_2_info.config(text="the blank is empty")





#button
password_button = Button(right_frame_1,text="Générer", font=("Helvetica", 20), bg='#4065A4', fg='white',command=generate_password)
password_button.pack(fill=X)

anglais_button = Button(frame_2,text="OK", font=("Helvetica", 20), bg='#4065A4', fg='white',command=verifier_question)


anglais_button_swicth = Button(frame_2,text="Next", font=("Helvetica", 20), bg='#4065A4', fg='white',command=swich)
anglais_button_swicth.pack(pady=20,fill=X)

anglais_2_button = Button(frame_3,text="OK", font=("Helvetica", 20), bg='#4065A4', fg='white',command=verifier_question_2)

anglais_2_button_swicth = Button(frame_3,text="Next", font=("Helvetica", 20), bg='#4065A4', fg='white',command=swich_2)


#frame activator

frame_1.pack(expand=YES)
right_frame_1.grid(row=0, column=1, sticky=E)
frame_2.pack_forget()

#frame 3 création

anglais_2_question_verbe.pack(pady=1)
anglais_2_question_francais.pack(pady=1)
anglais_2_question_preterit.pack(pady=20)
anglais_2_entry_preterite.pack(pady=20)
anglais_2_question_participe.pack(pady=20)
anglais_2_entry_participe.pack(pady=20)
anglais_2_button_swicth.pack(pady=10)
anglais_2_info.pack(pady=10)



#frame 4 création

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_mousewheel(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

def on_arrow_scroll(event):
    if event.keysym == "Up":
        canvas.yview_scroll(-1, "units")
    elif event.keysym == "Down":
        canvas.yview_scroll(1, "units")

# Créez une frame principale au lieu de Tk()



# Créez un canvas de taille spécifique
canvas = Canvas(frame_4, height=700, width=1400)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(frame_4, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)

# Créez un cadre de taille spécifique
frame = Frame(canvas, height=200, width=100)
canvas.create_window((0, 0), window=frame, anchor=NW)

frame.bind("<Configure>", on_frame_configure)
frame.bind("<MouseWheel>", on_mousewheel)
canvas.bind("<MouseWheel>", on_mousewheel)
frame_4.bind("<MouseWheel>", on_mousewheel)
frame.bind("<Up>", on_arrow_scroll)
frame.bind("<Down>", on_arrow_scroll)




# Ajoutez votre contenu au cadre








#barre de menu
menu_bar = Menu(window)
#créet un premier menu
file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Password", command=lambda: open_frame(frame_1))
file_menu.add_command(label="Anglais_1", command=lambda: open_frame(frame_2))
file_menu.add_command(label="Anglais_2", command=lambda: open_frame(frame_3))
file_menu.add_command(label="notes", command=lambda: execute_both_commands(frame_4))
file_menu.add_command(label="Quitter", command=window.quit)

menu_bar.add_cascade(label="Fichier", menu=file_menu)

#configuer notre fenetre pour ajouter le menu bar
window.config(menu=menu_bar)

#date

date_actuelle = datetime.datetime.now()

# Format 1 : AAAA-MM-JJ HH:MM:SS
format_1 = date_actuelle.strftime("%d-%m-%Y")
format_2 = date_actuelle.strftime("%H:%M:%S")
print("Format 1 : AAAA-MM-JJ HH:MM:SS")
print(format_1)





window.mainloop()