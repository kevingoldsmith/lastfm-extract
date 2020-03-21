#!/usr/bin/env python

import pylast

network = pylast.LastFMNetwork(api_key=api_key, api_secret=api_secret, username=username, password_hash=password_hash)
user = network.get_user(username)
recents = user.get_recent_tracks()
