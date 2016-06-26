# Youtube_bulk_Downloader
This is a python script to download youtube videos in bulk. 


The process is quite easy:

Whenever you find some video worth downloading just open the terminal and type this command:

###$echo "YoutubeLink" >> /PathToFile/download.txt

Repeat above command as much as you like. Once you are full with your bucket list you can view it in download.txt 


Now to download just type in command line

###$python /Youtube_bulk_Downloader/bd.py

Downloads will begin and you can track the progress in the commandline

Don't worry of duplicate downloads they are taken care of.

##Alternatively 
You can add the path to download.txt to your environment 
For example :
path to my download.txt is /media/thalursc1/downloads/download.txt

In CLI type:
$gedit ~./bash_profile 

Add this line to the ./bash_profile 
export YT = /media/thalursc1/downloads/download.txt

and now close the file after saving. 

In new CLI type in:
$source ~./bash_profile 

Now to add links to your file you can simply type 
$echo "youtube-link" >> "$YT"


 
 

