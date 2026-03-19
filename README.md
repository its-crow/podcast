podgasm

RSS-first podcast downloader with queues, playlists, and yt-dlp
integration.

Lightweight CLI tool for managing podcast feeds, downloading episodes,
and organizing audio locally.

------------------------------------------------------------------------

Features

-   RSS-only parsing (Atom rejected)
-   Feed management (add / remove / rename)
-   SQLite-backed episode tracking
-   Flexible downloads (latest / all / by ID / since date)
-   Parallel downloads
-   Queue system
-   Playlist support (M3U export)
-   Full-text search (FTS5 optional)
-   OPML import/export
-   yt-dlp integration (audio + video)
-   Per-feed and global download directories

------------------------------------------------------------------------

Installation

pipx: pipx install .

pip: pip install .

Command: podcast

------------------------------------------------------------------------

Quick Start

Initialize: podcast init

Add a feed: podcast add-feed tdz https://example.com/rss.xml

Refresh: podcast refresh –feed tdz

Download latest: podcast download –feed tdz

------------------------------------------------------------------------

Commands

Feeds: podcast list-feeds podcast add-feed podcast remove-feed podcast
rename-feed podcast refresh –feed podcast refresh –all

Downloads: podcast download –feed podcast download-title –feed –title
“keyword”

Options: –latest N –all –ids 1,2,3 –since YYYY-MM-DD –jobs N

Search: podcast search –feed tdz –query “keyword” podcast search-all
–query “keyword” –fts

Queue: podcast queue-add –feed tdz –episode-id 12 podcast queue-list
podcast queue-download podcast queue-remove –queue-id 1 podcast
queue-reset

Playlists: podcast playlist create mylist podcast playlist add mylist
–episode-id 12 podcast playlist show mylist podcast playlist export
mylist –out playlist.m3u

yt-dlp: podcast download-yt –link podcast download-yt –link –video

OPML: podcast opml import feeds.opml podcast opml export feeds.opml

Settings: podcast set –download-dir ~/pods podcast set –download-yt-dir
~/yt podcast set –change-feed-dir tdz –dir ~/custom/tdz podcast set
–unset-feed-dir tdz podcast set –show

Utility: podcast info podcast clean podcast dirs podcast –changes
podcast –version

------------------------------------------------------------------------

Storage

Config: PODFILE.ini

Database: SQLite

Audio: //.mp3

------------------------------------------------------------------------

Notes

-   RSS only (Atom feeds rejected)
-   SQLite used for persistence
-   Optional FTS5 search support
-   SSL verification disabled by default in code

------------------------------------------------------------------------

Version

0.3

------------------------------------------------------------------------

Changelog

podcast –changes
