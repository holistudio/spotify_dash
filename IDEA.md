# Spotify Vibe Browser Dashboard

Basic idea: You're looking for music that reflects a certain kind of mood or vibe. Luckily, Spotify users have curated lots of playlists that group songs/tracks not just by particular artists or genres but other descriptive words.

A dashboard can provide an interactive tool for users to see popular songs that match a certain mood and then explore similar artists based on those songs.

## Basic User Story

 1. User selects a couple words describing the mood, style, and/or genre of music they want.
 2. Dashboard displays top X most popular songs and and top X most popular artist that show up in playlists titled with those words.
 3. User can also select an artist from the above list and then a word cloud appears showing frequency of words used for playlists containing their songs
     - Also a bar chart showing the counting frequency for those words
 4. User can filter all results by tempo of songs showing up in the lists (average bpm).

## Behind the Scenes

1. User selects a couple words describing the mood, style, and/or genre of music they want.
2. Dashboard displays top X most popular songs and and top X most popular artist that show up in playlists titled with those words.

Dataset Features:

3. User can also select an artist from the above list and then a word cloud appears showing frequency of words used for playlists containing their songs

Dataset Features:

4. User can filter all results by tempo of songs showing up in the lists (average bpm).

Dataset Features:


## Extra Ideas

Somehow the dashboard can also visualize similar artists with similar ranked frequency of words.
 - Somehow construct feature vectors of all artists based on the frequency of playlist words
 - Then find an appopriate metric for measuring distance between feature vectors
 - Importantly, the feature vectors should try to exclude words of genres so that the resulting mood of the song may end up governining the distance measurements more than other superficial features.

## Appendix of Other Thoughts

Searching for songs to put in the background is typically done with royalty free songs or other music services besides Spotify. This tool assumes that the user will be relatively capable (financially, lawfully) to use the music they are able to pick out using the dashboard.

This dashboard may have one other use case - exploratory data analysis prior to more serious machine learning clustering analysis of songs for the Spotify Playlist Challenge.