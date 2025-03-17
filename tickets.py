from os import listdir
from os.path import isfile, join

def write_container(f, i):
    f.write('<div class="container">')
    f.write('<img src="tickets/'+file+'" alt="'+file+'" class="image" id="image'+str(i)+'">')
    f.write('<div class="caption">'+dida[file]+'</div>')
    f.write('</div>')

def write_modal(f, i):
    f.write('<div id="myModal'+str(i)+'" class="modal">')
    f.write('<span class="close">&times;</span>')
    f.write('<img class="modal-content" id="imgModal'+str(i)+'">')
    f.write('</div>')

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
    <link href="https://mastodon.uno/@ildave" rel="me">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="manifest" href="/site.webmanifest">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I miei concerti</title>
    <style>
        body {
            background-color: #DAA520;
        }
        .father {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            padding: 20px;
            align-items: flex-start;
        }
        .container {
            text-align: center;
            padding: 10px;
            background-color: #143D60;
            max-width: 390px;
            margin: 50px auto;
            border-radius: 15px;
        }
        .image {
            border-radius: 15px;
            height: auto;
            max-width: 330px;
            cursor: pointer;
            margin-bottom: 20px;
        }
        .caption {
            margin-top: 10px;
            color: #DAA520;
            font-weight: bold;

        }
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
        .mastodon {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 75px;
            background-color: #143D60;
            color: #DAA520;
            border: 1px solid #DAA520;
            border-radius: 0px 5px 0px 0px;
            font-weight: bold;
        }
        .mastodon a {
            color: #DAA520;
        }
        @media (max-width: 768px) {
            .father {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
<div class="mastodon"><a href="https://mastodon.uno/@ildave" rel="me">Mastodon</a></div>
<div class="father">
''') 

    for file in onlyfiles:
        write_container(f, i)
        i = i + 1
    f.write("</div>") #chiudo .father
    i = 1;
    for file in onlyfiles:
        write_modal(f, i)
        i = i + 1
    
    f.write('''<script>
        
        function openModal(imageSrc, n) {
            console.log(imageSrc, n, "imgModal"+n);
            var modal = document.getElementById("myModal"+n);
            modal.style.display = "block";
            var modalImg = document.getElementById("imgModal"+n);
            modalImg.src = imageSrc;
            console.log(modalImg.src);
        }

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
