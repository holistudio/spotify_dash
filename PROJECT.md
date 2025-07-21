# Project Requirements Document (PRD)

A project requirements document (PRD) for this project

---
Status: DRAFT
Owner: Dan
Designer: Dan
Developer: Dan
Target Release Date: 2025-08-03
---

## Goals and Objectives

**Premise:** You're looking for music that reflects a certain kind of vibe or mood. Luckily, Spotify users have curated lots of playlists that group songs/tracks not just by particular artists or genres but other descriptive words. 

**End product:** A Tableau dashboard that visualizes relevant data regarding songs/tracks and artists that relate to certain vibes/moods (text descriptions) specified by the user.

**Ideally:** The dashboard will help user find songs that match a specific vibe and belong to a variety of genres (i.e., "transcend genre")

## Background and Strategic Fit

**Challenges:**

Finding a song based on a vibe/mood/feeling remains a challenge.
 - Direct search in Spotify is typically good finding a specific song or artist.
 - In contrast typing moods in Spotify yields individual playlist results, which requires additional steps in browsing and listening to various songs across multiple playlists (of course this kind of exploration can be fun! but also time-consuming).
 - Creating your own Spotify playlist with songs that match the mood could work because Spotify recommends similar songs at the bottom of each list. But in my personal experience, the song recommendations appear more biased towards similar genres (e.g., Spotify recommends only movie soundtracks for a playlist populated with movie soundtrack songs when I am also looking for instrumental music in general, not just those used in movies)

**Opportunities:** 

- Spotify has an [API](https://developer.spotify.com/documentation/web-api) to look up track/artist information and [numerical attributes pertaining to mood]((https://developer.spotify.com/documentation/web-api/reference/get-audio-features)):
   - `popularity`
   - `energy`
   - `valence` 
   - `tempo`
   - `danceability`
   - `acousticness`
   - `instrumentalness`
   - `liveness`

- Datasets appear to exist for Spotify songs and playlists
   - [Spotify Million Playlist Dataset](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge)
   - [Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)
   - [Most Streamed Spotify Songs 2023](https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023)

## Assumptions

 - Assume user is familiar with interactive dashboards.
 - Behind the scenes of Tableau dashboard should be "simple" - one static Excel/csv table from which data is visualized will do.

## User Stories

 1. User selects a couple words describing the mood, style, and/or genre of music they want.
 2. Dashboard displays top X most popular songs and and top X most popular artist that show up in playlists titled with those words.
 3. User can also select an artist from the above list and then a word cloud appears showing frequency of words used for playlists containing their songs
     - Also a bar chart showing the counting frequency for those words
 4. User can filter all results by tempo of songs showing up in the lists (average bpm) or other numerical features (TBD based on Web API).

## User Interaction and Design

Likely a single dashboard with two vertical halves:
 - The left half has a search bar and shows a ranked list of songs and corresponding artists based on the search query.
 - The right half shows either a word cloud or ranked list of words for a particular artist.
   - Ideally, this right half display is based on the artist of the songs the user clicks on the left half.
   - But can also just be based on another standalone search bar for artist.

A tertiary panel on the right side has a list of filters for the numerical attributes of the songs.

## Questions

 - How do I get access to the Web API? Do I need an API key?
 - What restrictions are there to the API? How frequently can I use it?
 - What are the ranges for the numerical attributes of each Spotify track/song?
 - How many unique songs are there on the above datasets?
 - How many songs have null/missing values for the numerical attributes?
 - What are the unique list of words used in Spotify playlists?
    - What general list of "articles" ("a", "the", "I") should be excluded from analysis of playlist titles?
 - What are the most/least used words in Spotify playlist titles?
    - How long does it take to then find all playlists that contain a given song? And then count the frequency of words?
 - What are the list of possible `genre` a song can have?
    - Does excluding words on the `genre` list consequently remove too many words for the "vibe" results on the dashboard to be meaningful?


## What This is NOT

 - This does not have to reflect the current real-time state of the Spotify songs.
 - This is not a machine learning/self-supervised learning clustering exercise nor a full recommender system per se (though that could make for interesting future work).