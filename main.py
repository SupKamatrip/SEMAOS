'''Ce programme python SEMAOS a plusieurs focntionnalités:
• Possibilité de lancer un scan du réseau (liste des machines connectées, ports ouverts) à partir du SemaOS. Le
scan du réseau doit être développé par vos soins, le recours à la librairie python de nmap est cependant possible.
• Possibilité de lancer des tests de débits
• Tests à intervalles de temps réguliers du bon fonctionnement de l’accès Internet : ping + latence
• Recueil de l’adresse IP publique du client et lien avec un nom de domaine à l’instar du service DynDNS. A noter
que le serveur DNS qui héberge le nom de domaine dynamique peut être le même que le DNS de la société tel
qu’il est à mettre en place dans la MSPR « TPTE511 – Administrer une solution d’infrastructure ». Le suffixe DNS
PHASE 2 : PRÉSENTATION ORALE COLLECTIVE + ENTRETIEN COLLECTIF
Durée totale par groupe : 30 mn se décomposant comme suit :
10 mn de soutenance orale par l’équipe.
20 mn d’entretien collectif avec le jury (questionnement complémentaire).
Objectif : mettre en avant et démontrer que les compétences visées par ce bloc sont bien acquises.
Jury d’évaluation : 2 personnes (binôme d’évaluateurs) par jury – Ces évaluateurs ne sont pas intervenus durant la période de
formationet ne connaissent pas les apprenants à évaluer.
3
Direction Innovation & Pédagogie – Septembre 2022
de la zone destinée aux entrées DNS dynamiques des Semabox doit correspondre à « cma4.box ».
• Affichage d’un tableau de bord contenant les informations suivantes :
o Adresses IP de la semabox / Nom de la semabox
o IP publique de l’accès Internet / nom dns dynamique
o Etat de la connexion Internet
o Liste des machines détectées sur le réseau
o Résultats du dernier test de débit
'''

