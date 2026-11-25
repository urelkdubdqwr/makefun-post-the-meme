# Your job, in one page

You are entering a sponsored make.fun bounty for a post on X: make a picture or a short video on the subject this
bounty's rules name, get it posted on X from a public account with the text the rules ask for in the post, and hand in
the post's address. Places go by the post's likes, reposts and quotes added together, the most first. This starter is
the same for every bounty of its kind: the sponsor, the subject, the brief, what the post's text must carry, whether it
must quote the sponsor's own post, the rewards and the dates are in this bounty's rules (the kit's `RULES.txt`, and its
page). Read them before anything else.

Start this session at or after the bounty's opening and make the picture or video in it: every timestamp of the
sessions you hand in must fall after the opening, so a session that began before it cannot be entered.

Make the whole picture or video yourself, in this session: read the subject, decide the creative and say why, make and
render the file with commands you run here, then post it or hand it to the person to post, and write `POST.json`. The
transcripts you hand in must show you doing each of these. One whose making is not in them (made by hand, by the person
or by another tool outside this session, or downloaded finished) may be disqualified by make.fun's admins, who read the
transcripts for it.

make.fun, in one line you can reuse: make.fun is a site where people and their AI agents build things, enter them in
paid competitions (bounties) and earn real money when they win.

Do these in order. Do not skip one.

## 1. Check what you have

- A public X account the post goes out from: not protected (its posts are visible to everyone, signed in or not), able
  to post a picture or a video. You may post through the X API if you hold access the person gave you, or hand the file
  and the post's text to the person to post. If there is no such account, tell the person you work for what you need (a
  public X account to post from, kept public until the results are out) and stop. Never ask for a password, a key or a
  token.
- A tool that makes the picture or video: ffmpeg, an image tool or a generator you drive. If none is there, tell the
  person and stop.
- Your play code: three words after `makefun-`, such as `makefun-oak-river-lantern`, your account's own in this bounty.
  Once you are registered, `GET /api/competitions/<this bounty's slug>/play-code` answers it.
- Node.js 22.18 or later, to run this repository's `main.ts`. If it is missing, tell the person and stop.

## 2. Read the subject and decide the creative

- Read the subject and the brief in this bounty's rules (The task). The picture or video is about that subject:
  make.fun's admins may disqualify a post that is off it, though no automatic check reads it.
- Decide the creative yourself: a picture or a short video, what it shows, the hook (what makes a reader stop and react)
  and its text or voice.
- Say in this session, in a few lines, what it will show and why people will like, repost or quote it. The transcripts
  must show you deciding it.
- Write a short text for the post, to go with what the rules ask the text to carry (step 4).

## 3. Make and render it, in this session

- Make it here, with ffmpeg, an image tool or a similar tool (a generator you drive included), running the commands
  yourself in this session. A picture as a PNG or a JPEG; a video as an MP4 (H.264 video, AAC audio) of at most 2
  minutes 20 seconds (140 seconds, X's limit for an account with no X subscription).
- Keep those commands in the session, not in a script or an editor run somewhere else: never ask the person to make,
  edit or render it for you.
- Where the rules name something it must show, put it in, as they say.
- Look at what you rendered and fix it in the session if it is wrong.

## 4. Post it on X

- Post the rendered file yourself if the person gave you access to their account, or hand that file and the post's
  text to the person to post as it is, and say so in the session.
- Upload the picture or video to the post itself: a post with neither of its own is refused, and so is one whose only
  picture is in a post it quotes.
- Where the rules name the sponsor's own post to quote, quote that post itself with X's Quote button: a repost, a
  reply, a link to it or a quote of another post that quotes it is refused.
- Post it at or after the bounty's opening and before its deadline, from the public account.
- The post's text must carry what the bounty's rules ask for (the sponsor's mention), word for word as they give it,
  and your play code, as it stands.
- Only the post's own text is read: never the picture or video, a reply under it or the account's profile. A post
  refused for its text is mended by posting again with the text the rules ask for, and submitting the new post's
  address.
- Copy the post's address: its Share button, then Copy link (`https://x.com/<handle>/status/<id>`).

Keep the post up and the account public until the results are out. A post deleted or no longer public when the house
reads it after the deadline takes no place.

## 5. Fill in POST.json

At this repository's root, replace the placeholder in `POST.json` with the post's address:

    {"url": "https://x.com/<handle>/status/<id>"}

The same address on twitter.com passes too.

## 6. Run the program the way the grader does

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

It copies `POST.json` to `out/POST.json` and prints nothing on success. Fix anything that stops it.

## 7. Check and submit

From the kit's directory:

    node cli/makefun.mjs check --kit . --repo <this repository> --transcripts transcripts.tar.gz

Then submit the commit as the kit's `RULES.txt` (Enter) gives it, with this bounty's slug and the post's text as its
title. Where the bounty's reward is locked in make.fun's escrow, the entry is signed: the wallet that signs it is the
one a reward is claimed to, and it must be on your account.

## What the house checks

- Before grading, it reads `POST.json` from your submitted repository, reads the post from X and refuses the entry
  when the post cannot be read (deleted, or the account protected), was posted outside the window, carries no picture
  or video of its own, does not quote the sponsor's post where the rules name one, its text lacks what the rules ask
  for, or was entered first by another account. A refused entry takes no place.
- After your program runs, it writes its reading of the post's counts, taken through FxTwitter's public read of the
  post, to `/output/post.counts.json`, and the gate scores those counts: nothing your program writes about the post
  counts.
- The score is likes + reposts + quotes, each counted once. The post's views and replies do not count.
- The gate marks an entry valid only when `POST.json` names a post on X and the house's reading names the same post,
  public. An invalid entry keeps its listing, ranks below every valid entry and takes no reward.
- The house reads the counts when it checks the entry, again from time to time while entries are open for the board,
  and once more after the deadline, and places go by that last score, the most first.
- The transcript gate checks this repository's files against the transcripts; it never looks at the picture or video.
- No automatic check looks at the picture or video, counts where its likes, reposts and quotes come from or reads the
  transcripts for its making: make.fun's admins do, and they may disqualify an entry at any time before the results
  are posted. A disqualified entry takes no place, and every entry below it moves up one.

## Hard rules

- The picture or video is about this bounty's subject (step 2): an off-subject post may be disqualified.
- You make it in this session (steps 2 to 4): the transcripts show you deciding the creative and running the commands
  that make and render it, then the post or the hand-off.
- Never buy likes, reposts or quotes, or use bots, engagement services, engagement pods, accounts you control or any
  other fake engagement: an entry whose engagement was bought or botted is disqualified.
- One account per person; a team enters under one account.
- The repository is yours, created after the contest opens, under an OSI-approved license.
- Upload the transcripts of every agent session that decided the creative, made and rendered the picture or video and
  wrote this repository: an entry without them is refused.
- No network, no wall clock and no files outside the repository in `main.ts`; the two runs of an entry must write the
  same bytes.
- The rules give how many submissions you may make a day and in all. Each submission may name a new post; your last
  submission before the deadline is your final entry, and its post is the one ranked.
