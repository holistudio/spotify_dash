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

## User Stories

## User Interaction and Design

## Questions

## What This is NOT
