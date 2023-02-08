# MusicMeta

When you're collecting music from different sources like SoundCloud, Beatport, DJ Pools, etc, it can be a pain to manually set all the track info.

Use this program to collect and assign meta data of your audio files in bulk. The program takes the filename of your tracks and uses the beatport API (https://www.beatport.com/api/v4/catalog/search) to find the most accurate match. Warning, this is not Shazam. The program takes just the name of your file and uses that as a search query on the beatport API. So your filenames need to contain enough information to find the song in the beatport database.

The program can also be used to manually change meta data in a GUI environment. This program makes it much easier to change such data in bulk.

# Known bugs:

- Mutagen separates artists by using a forward slash /. This is problematic when bands like AC/DC are involved since they will be splitted into "two bands": AC and DC by the software.

# Possible future work

- Perhaps I might add more tags later. As of now, the program contains enough tags for DJs.
- The duration of the audio files is read into the program. I might add a function later that uses this information to refine the beatport search. This might narrow the results down to just a single result that could be used to really automatically collect meta data whithout much human intervention.
- I might take the current tags to further refine the beatport search. However, this will cause problems if the tags have been set wrong before.

# Disclaimer

Use at your own discretion. In no way am I promoting illegal downloading of songs. Instead, use it, e.g., to collect meta data for freely downloaded songs from SoundCloud (most if not all of them do not contain this data upon download).
