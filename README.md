# face_detection_project

Arcfelismerés / Face detection project

Projekt leírás:
Egy arcfelismerő alkalmazás elkészítése.
Arcdetektálás élő kameraképen, egy személyről. A feladat megvalósításhoz felhasználtam az OpenCV Library-t és a Haar Cascade adatbázist.

Személyi felismerést nem tud a program, csak arcfelismerést.
• Van arc? Hol van arc?
• A megtalált arc köré, egy keretet rajzol az élő kameraképen
• és pluszban a szemeket is megtalálja

OpenCV
• Open Source Computer Vision Library
• ennek a segítségével lehet arcfelismerést megvalósítani
• ezt külön kell telepíteni, hogy működjön az alkalmazás
• pip install opencv-python

Haar Cascade
• viszont a library önmagában nem ismer fel semmit,
• kellenek hozzá betanított adatbázisok, konkrétan a felismerések elvégzésére
• erre szolgálnak a Haar Cascade-ok

Kilépés
• kilépni a 'q' betű lenyomásával lehet

Tervezett fejlesztés
• PyInstaller - Python standalone executable programs
• ez egy önállóan futtatható programot hoz létre (.exe fájl), ami már tartalmazni fogja a python értelmezőt és a szükséges csomagokat
• csak rá kell kattintani az .exe fájlra és fut a program
