# MusicMeta by Anteino

When you're collecting music from different sources like SoundCloud, Beatport, DJ Pools, etc, it can be a pain to manually set all the track info.

Use this program to collect and assign meta data of your audio files in bulk. The program takes the filename of your tracks and uses the Beatport API (https://www.beatport.com/api/v4/catalog/search) to find the most accurate match. Since this API is not the fastest in the world, the requests are sent asynchronously.

Warning, this is not Shazam. The program takes just the name of your file and uses that as a search query on the Beatport API. So your filenames need to contain enough information to find the song in the Beatport database.

The program can also be used to manually change meta data in a GUI environment. This program makes it much easier to change such data in bulk.

# How to use

Start the program and use the "Open folder" button to load in a folder containing music. The program will automatically load subfolders as well. You can now start editing the audio tags. You can save the tags to your files at any point using the "Save tags for selected songs" button. As the name suggests, only songs that are selected will have their tags overwritten with the currently inputted data.

Additionally you can click the "Import from Beatport" button to collect track information. On the far right, the drop down menus for each song will be populated with track info from Beatport. The correct track might or might not be in that list. If the correct track is, in fact, in the list you can load its info by clicking it. The buttons under the line edits will be populated with the collected data. A button can be double clicked to move its data to the line edit above it. To move all the data up at once, click the arrow up button on the far left. The track will be automatically selected for saving after clicking one of the options in the drop down menu.

When a song or its correct version cannot be found in the Beatport database, you can click the "Open wiki" button below the drop down menu. THe program will do its best to find the wiki page that belongs to said song and display it in a popup dialog. You don't have to close this dialog manually. When you click the wiki button for another song, the current dialog will be overwritten with the new page.

If your songs were already imported in Rekordbox and analyzed, you can use the key and bpm information assigned by Rekordbox. Export your library to XML from Rekordbox and import this XML with the "Import Rekordbox collection" button. The key and bpm will then be overwritten for all songs that do not have this field set YET. Note that MusicMeta uses Camelot notation and Rekordbox will either use classical notation or camelot depending on your settings.

Make sure that if you select the wrong track in the drop down menu, you manually deselect the song for saving, or you will save the wrong tags to your file.

Lastly, do not try to scroll down in the view while your cursor is on one of the drop down menus. This will cause track info to automatically be loaded in and select the line for saving.

# How to build

<code>PyInstaller .\MusicMeta.spec</code>

# Known bugs:

- Currently, only MP3 files are supported. The program will even break WAV files when trying to edit their tags. So I excluded all extensions but MP3 for now.
- Mutagen separates artists by using a forward slash /. This is problematic when bands like AC/DC are involved since they will be splitted into "two bands": AC and DC by the software.
- The Beatport API has a tag called "mix_name". This can have values like "Original mix", "Pleasurekraft edit", "Extended mix", etc. The problem is that some songs have this mix_name in their title while others don't. But Beatport does not make a difference between this. So I had to choose between always including it in the title or never including it. I chose to always include it in the song title, but I might add a configurator to change this later.
- Some songs will simply not be in the Beatport API. If anyone knows of a more complete or additional API, I might implement it later.
- Two identical wikipedia searches do not always yield identical search results. This non-deterministic behavior is out of my hands unfortunately.

# Possible future work

- Perhaps I might add more tags later. As of now, the program contains enough tags for DJs.
- The duration of the audio files is read into the program. I might add a function later that uses this information to refine the Beatport search. This might narrow the results down to just a single result that could be used to really automatically collect meta data whithout much human intervention.
- I might take the current tags to further refine the Beatport search. However, this will cause problems if the tags have been set wrong before.
- I might add a function to open the wiki page of a certain song (if there exists one) in a popup dialog. Most older or nostalgic songs are not on beatport and having a function to automatically open the wiki page might speed up the manual process significantly.
- Might do the same for discogs since I noticed they're especially complete for older music.

# Disclaimer

Use at your own discretion. In no way am I promoting illegal downloading of songs. Instead, use it, e.g., to collect meta data for freely downloaded songs from SoundCloud (most if not all of them do not contain this data upon download).
