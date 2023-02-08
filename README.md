# MusicMeta

When you're collecting music from different sources like SoundCloud, Beatport, DJ Pools, etc, it can be a pain to manually set all the track info.

Use this program to collect and assign meta data of your audio files in bulk. The program takes the filename of your tracks and uses the Beatport API (https://www.beatport.com/api/v4/catalog/search) to find the most accurate match. Since this API is not the fastest in the world, the requests are sent asynchronously.

Warning, this is not Shazam. The program takes just the name of your file and uses that as a search query on the Beatport API. So your filenames need to contain enough information to find the song in the Beatport database.

The program can also be used to manually change meta data in a GUI environment. This program makes it much easier to change such data in bulk.

# Known bugs:

- Currently, only MP3 files are supported. The program will even break WAV files when trying to edit their tags. So I excluded all extensions but MP3 for now.
- Mutagen separates artists by using a forward slash /. This is problematic when bands like AC/DC are involved since they will be splitted into "two bands": AC and DC by the software.
- The Beatport API has a tag called "mix_name". This can have values like "Original mix", "Pleasurekraft edit", "Extended mix", etc. The problem is that some songs have this mix_name in their title while others don't. But Beatport does not make a difference between this. So I had to choose between always including it in the title or never including it. I chose to always include it in both filename as well as song title.
- Some songs will simply not be in the Beatport API. If anyone knows of a more complete or additional API, I might implement it later.

# Possible future work

- Perhaps I might add more tags later. As of now, the program contains enough tags for DJs.
- The duration of the audio files is read into the program. I might add a function later that uses this information to refine the Beatport search. This might narrow the results down to just a single result that could be used to really automatically collect meta data whithout much human intervention.
- I might take the current tags to further refine the Beatport search. However, this will cause problems if the tags have been set wrong before.

# Disclaimer

Use at your own discretion. In no way am I promoting illegal downloading of songs. Instead, use it, e.g., to collect meta data for freely downloaded songs from SoundCloud (most if not all of them do not contain this data upon download).
