# QuestEcho changelog

## 1.9.4
- One addon for all three clients: retail, WLK 3.3.5a and Turtle 1.12 now run the
  same code. Only the .toc file differs, because 1.12 and 3.3.5a need their own
  version-specific toc to recognise the folder.
- Fixed no sound after pausing or after clearing the queue while the status bar kept
  running: the guard that prevents overlapping playback was never cleared when a
  line was stopped, so replaying the same file was silently refused.
- Fixed the settings checkboxes showing as green blocks on retail: colouring now goes
  through SetColorTexture, restoring the gold mark.

## 1.9.3
- Retail 12.0 support: IsAddOnLoaded moved into C_AddOns, so the two remaining direct
  calls are now routed through the safe wrapper (one of them broke initialisation).
- The sound channel setting is honoured again, with a three-step fallback
  (configured channel -> Master -> single argument) so playback cannot fail silently.
- The Echo button sits next to the Back button again on modern clients.

## 1.9.2
- Runs on the 1.18 (Turtle), 3.3.5a and 2.4.3 clients from one build.
- Voice playback, pause, clear and captions work on all of them.
- The Echo button sits in the quest log, and is always available: press it to hear the
  quest on screen, or be told it has no line. It is placed beside the log's own map
  button where that exists, and beside the close button where it does not.
- The quest log's frame names differ per client, so the detail panel, the anchor and the
  quest title are each located by trying the known names and then, failing that, by
  looking through the log's own frames - the title is additionally recognised by its
  text resolving through the voice pack.
- Captions always match the voice: they come from the same pack the line is spoken
  from, so changing the interface language cannot desynchronise them.
- The status bar position is remembered between sessions.
- Fixed the minimap icon.

## 1.9.1
- Chinese and English voice packs, with captions in the language you hear.

## 1.9.0
- First release.
