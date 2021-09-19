# tracklist_search.py
# Version 1.0
# Python 2 or Python 3 (confirm?)
# by Chris Chain

import webbrowser

############### ENTER TRACK LIST ###############

tracklist_raw = """Westbam & Dr Motte - Sunshine (some beatless version?)
Elias Mazian - Don't break it
Earth Trax - Ambient Dance
The Melody - I want your love
The Melody - Tonight is fine
Sansibar - Game over
?
?
JT Company - Don't deal with us (Dusky Edit)
Luca Lozano - Calling all dancers
Coeo - Bliss
Anz - Loos in Twos (NRG)
?
Pangaea - Like This
Windows - Sil
Microglobe - High on Hope (1992 Long Hot Summer Mix)
Last Rhythm - Last Rhythm
Neutron - Poly
Format - Solid Session
?
Subliminal Cuts - Le Voie le soleil
Baby D - Let me be your fantasy"""



############### FORMAT RAW TRACKLIST ###############

def format_tracklist(tracklist_raw, algorithm):
    if algorithm == "Line Split Only":
        tracklist_raw_line_split = tracklist_raw.split("\n")
        tracklist_to_search = tracklist_raw_line_split
    elif algorithm == "Line Split + \'# - Timestamp -\'":
        tracklist_raw_line_split = tracklist_raw.split("\n")
        formatted_tracklist = []
        for line in tracklist_raw_line_split:
            tracklist_formatted_single = line.join(line.split("-", 2)[2:])
            formatted_tracklist.append(tracklist_formatted_single)
        tracklist_to_search = formatted_tracklist
    elif algorithm == "YouTube Standard":
        tracklist_raw_line_split = tracklist_raw.split("\n")
        tracklist_to_search = []
        lines_with_idents = []
        for line in range(0,len(tracklist_raw_line_split)):
            if tracklist_raw_line_split[line] == "Song" \
            and tracklist_raw_line_split[line+2] == "Artist" \
            and tracklist_raw_line_split[line+4] == "Album" \
            and tracklist_raw_line_split[line+6] == "Licensed to YouTube by":
                lines_with_idents.append(line)
                lines_with_idents.append(line+2)
                lines_with_idents.append(line+4)
                lines_with_idents.append(line+6)

                artist = tracklist_raw_line_split[line+3]
                song = tracklist_raw_line_split[line+1]
                search_term = artist + " - " + song
                tracklist_to_search.append(search_term)

    for element in tracklist_to_search:
        print(element)

    return tracklist_to_search


############### SELECT YOUR ALGO TO RUN SCRIPT ###############

algorithm = "Line Split Only"
tracklist_to_search = format_tracklist(tracklist_raw, algorithm)


############### LAUNCH SEARCHES IN WEB BROWSER ###############

def launch_browser(tracklist_to_search):
    for track in tracklist_to_search:
        url = "https://www.google.com.tr/search?q={}".format(track)
        webbrowser.open_new_tab(url)


############### UNCOMMENT TO RUN ###############

launch_browser(tracklist_to_search)