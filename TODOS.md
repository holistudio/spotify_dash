# TODOS

## Data Collection

 - [x] Download Spotify Million Playlist Dataset.
 - [x] Download Spotify Tracks Dataset.
 - [x] Count number of unique songs in datasets.
 - [ ] Investigate Spotify Web API for additional track features (e.g., `energy`, `valence`).

## Data Cleaning

 - [x] Parse playlist titles to extract mood/vibe keywords.
 - [x] Identify and exclude common articles/stop words from playlist titles.
 - [ ] Handle missing values for numerical attributes of songs.
    - [x] For now, use only songs in the Tracks Dataset that can be found in the first 100,000 playlists in the Millon Playlist dataset.
 - [x] Merge datasets to create a comprehensive song/playlist/artist table.
 - [ ] Decide on how to handle songs with multiple artists
 - [ ] For Tableau
    - [ ] Dataset 1: Rows of different words, columns of track_ids, each cell value = word frequency count for each track 
    - [ ] Dataset 2: Rows of different words, columns of artists
    - [ ] Dataset 3: Rows of track_ids, columns of artist numerical features

## EDA


 - [ ] Determine how to rank songs based on a list of "mood words" (e.g., frequency in relevant playlist titles, popularity).
    - [x] Analyze distribution (mean, min, max) frequency of playlist words for all songs/tracks
    - [x] Decide on a cut-off threshold for "common enough" words to consider in ranking songs.
 - [ ] Analyze the distribution of numerical audio features (e.g., tempo, energy, valence).
 - [ ] Explore relationships between mood words and audio features.
 - [ ] Preview Tableau dashboards
    - [ ] Using Dataset 1: Identify top X most popular songs and artists for given mood words.
    - [ ] Using Dataset 2: Analyze word frequency in playlists containing specific artists' songs.

## Dashboard

 - [ ] Design Tableau dashboard layout (left half for search/ranked lists, right half for word cloud/artist details, tertiary panel for filters).
 - [ ] Implement search functionality for mood keywords.
 - [ ] Display top X most popular songs and artists based on search.
 - [ ] Create interactive word cloud visualization for artist-specific playlist words.
 - [ ] Develop bar chart for word frequency.
 - [ ] Implement filters for tempo and other numerical audio features.
 - [ ] Ensure dashboard is visually appealing and user-friendly.
