#!/usr/bin/env python3
"""Fetch Spotify now playing and top tracks data for static site generation."""

import base64
import os
import sys
from datetime import datetime, timezone

import requests
import yaml

# Spotify API endpoints
TOKEN_URL = "https://accounts.spotify.com/api/token"
NOW_PLAYING_URL = "https://api.spotify.com/v1/me/player/currently-playing"
RECENTLY_PLAYED_URL = "https://api.spotify.com/v1/me/player/recently-played?limit=1"
TOP_TRACKS_URL = "https://api.spotify.com/v1/me/top/tracks?time_range=short_term&limit=6"

# Output path
OUTPUT_PATH = "_data/spotify.yml"


def get_access_token():
    """Exchange refresh token for access token."""
    client_id = os.environ.get("SPOTIFY_CLIENT_ID")
    client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")
    refresh_token = os.environ.get("SPOTIFY_REFRESH_TOKEN")

    if not all([client_id, client_secret, refresh_token]):
        print("Error: Missing Spotify credentials in environment variables")
        sys.exit(1)

    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

    response = requests.post(
        TOKEN_URL,
        headers={"Authorization": f"Basic {auth_header}"},
        data={"grant_type": "refresh_token", "refresh_token": refresh_token},
    )

    if response.status_code != 200:
        print(f"Error getting access token: {response.status_code}")
        sys.exit(1)

    return response.json()["access_token"]


def get_now_playing(token):
    """Get currently playing track or most recently played."""
    headers = {"Authorization": f"Bearer {token}"}

    # Try currently playing first
    response = requests.get(NOW_PLAYING_URL, headers=headers)

    if response.status_code == 200 and response.text:
        data = response.json()
        if data.get("is_playing") and data.get("item"):
            track = data["item"]
            return {
                "is_playing": True,
                "track": track["name"],
                "artist": ", ".join(a["name"] for a in track["artists"]),
                "album": track["album"]["name"],
                "album_art": track["album"]["images"][1]["url"] if len(track["album"]["images"]) > 1 else track["album"]["images"][0]["url"],
                "url": track["external_urls"]["spotify"],
            }

    # Fall back to recently played
    response = requests.get(RECENTLY_PLAYED_URL, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data.get("items"):
            track = data["items"][0]["track"]
            return {
                "is_playing": False,
                "track": track["name"],
                "artist": ", ".join(a["name"] for a in track["artists"]),
                "album": track["album"]["name"],
                "album_art": track["album"]["images"][1]["url"] if len(track["album"]["images"]) > 1 else track["album"]["images"][0]["url"],
                "url": track["external_urls"]["spotify"],
            }

    return None


def get_top_tracks(token):
    """Get user's top tracks."""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(TOP_TRACKS_URL, headers=headers)

    if response.status_code != 200:
        print(f"Error getting top tracks: {response.status_code}")
        return []

    data = response.json()
    tracks = []

    for track in data.get("items", []):
        tracks.append({
            "track": track["name"],
            "artist": ", ".join(a["name"] for a in track["artists"]),
            "url": track["external_urls"]["spotify"],
        })

    return tracks


def main():
    print("Fetching Spotify data...")

    token = get_access_token()
    now_playing = get_now_playing(token)
    top_tracks = get_top_tracks(token)

    spotify_data = {
        "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "now_playing": now_playing,
        "top_tracks": top_tracks,
    }

    # Ensure _data directory exists
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    with open(OUTPUT_PATH, "w") as f:
        yaml.dump(spotify_data, f, default_flow_style=False, allow_unicode=True)

    print(f"Spotify data written to {OUTPUT_PATH}")

    if now_playing:
        status = "Playing" if now_playing["is_playing"] else "Last played"
        print(f"{status}: {now_playing['track']} by {now_playing['artist']}")


if __name__ == "__main__":
    main()
