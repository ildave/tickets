from os import listdir
from os.path import isfile, join
path = "./tickets"
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

dida = {}

with open('tickets.txt', 'r') as f:
    for line in f:
        n, d = line.split("=")
        dida[n] = d.rstrip()

with open("tickets.html", 'a') as f:
    i = 1
    f.write('''<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I miei concerti</title>
    <style>
        body {
            background-color: #DAA520;
        }
        .container {
            text-align: center;
            padding: 10px;
            background-color: #143D60;
            max-width: 500px;
            margin: 50px auto;
            border-radius: 15px;
        }
        .image {
            border-radius: 15px;
            max-width: 100%;
            height: auto;
            max-width: 500px;
            cursor: pointer;
            margin-bottom: 20px;
        }
        .caption {
            margin-top: 10px;
            color: #DAA520;
            font-weight: bold;

        }
        /* Stili per la finestra modale */
        .modal {
            display: none;
            position: fixed;
            z-index: 1;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgba(0,0,0,0.8);
        }
        .modal-content {
            margin: 15% auto;
            display: block;
            max-width: 90%;
        }
        .close {
            position: absolute;
            top: 20px;
            right: 35px;
            color: #fff;
            font-size: 40px;
            font-weight: bold;
            cursor: pointer;
        }
    </style>
</head>
<body>''') 

    for file in onlyfiles:
        f.write('<div class="container">')
        f.write('<img src="tickets/'+file+'" alt="'+file+'" class="image" id="image'+str(i)+'">')
        f.write('<div class="caption">'+dida[file]+'</div>')
        f.write('</div>')
        i = i + 1
    i = 1;
    for file in onlyfiles:
        f.write('<div id="myModal'+str(i)+'" class="modal">')
        f.write('<span class="close">&times;</span>')
        f.write('<img class="modal-content" id="imgModal'+str(i)+'">')
        f.write('</div>')
        i = i + 1
    
    f.write('''<script>
        
        // Funzione per aprire la finestra modale
        function openModal(imageSrc, n) {
            console.log(imageSrc, n, "imgModal"+n);
            var modal = document.getElementById("myModal"+n);
            modal.style.display = "block";
            var modalImg = document.getElementById("imgModal"+n);
            modalImg.src = imageSrc;
            console.log(modalImg.src);
        }

        // Aggiungi eventi di click alle immagini
        document.querySelectorAll('.image').forEach(item => {item.onclick = function() {
            var id = this.id;
            var n = id.replace('image', '');
            openModal(this.src, n);}
            });
    

        document.querySelectorAll('.close').forEach(item => {
            item.onclick = function() {
                console.log(this);
                this.parentElement.style.display = "none";
            }
        });
    </script>''')
    f.write('</body></html>')
