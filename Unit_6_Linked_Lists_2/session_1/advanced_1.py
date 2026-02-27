class SongNode:
    def __init__(self,song,next=None):
        self.song = song
        self.next = next 
    
def print_linked_list(node):
    current = node
    while current:
        print(current.song,end=" -> " if current.next else "")
    print()

top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem",SongNode("Bad Romance")))

def get_artist_frequency(playlist):
    pass 

#Problem 3 Glitching Out

playlist = SOngNode("SOS","ABBA",SongNode("Simple Twist of Fate","Bob Dylan",SongNode("Dreams","Fleetwood Mac","SongNode"("Lovely Day","Bill Withers"))))

print_linked_list(remove_song(playlist,"Dreams"))

#! Problem 4: On Repeat 

def on_repeat(playlist_head):
    pass

#Problem 5: Looped
def loop_length(playlist_head):
    pass

#! Problem 6 
def count_critical_points(song_audio):
    pass



