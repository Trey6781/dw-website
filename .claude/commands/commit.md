---
description: Review the working tree and commit it with a message in this repo's style
argument-hint: [message hint] [--push]
allowed-tools: Bash(git status:*), Bash(git diff:*), Bash(git log:*), Bash(git add:*), Bash(git commit:*), Bash(git push:*), Bash(git branch:*), Bash(git restore:*)
---

Commit the current work.

Arguments (optional): `$ARGUMENTS`
- Free text is a hint about what the message should say — use it to inform the
  message, not as the message verbatim.
- `--push` means also push the branch when the commit succeeds.

## 1. Look before staging

Run `git status --short` and `git diff` (plus `git diff --staged` if anything
is already staged). Read the actual changes — the message has to describe what
the diff does, not what you assumed it would do.

## 2. Decide what belongs in this commit

- Stage files by name. Never `git add -A` or `git add .` — they sweep in
  scratch files, editor droppings, and unrelated work.
- If the tree holds two unrelated changes, make two commits rather than one
  mixed one.
- Never stage secrets, `.env` files, credentials, or large binaries. If you see
  one, stop and say so instead of committing.

## 3. Write the message in this repo's style

Match what's already in `git log`:

- **Imperative mood, sentence case**: "Add prominent phone number and hours to header"
- **Subject line only.** This repo does not use bodies — don't add one unless
  the change genuinely needs explaining, and then keep it to a sentence or two.
- **No prefixes.** No `feat:`, no `fix:`, no scopes, no ticket numbers.
- Aim for about 50 characters; describe the effect, not the mechanics.

Apply this session's standard attribution trailers, whatever they are — don't
hardcode them here.

## 4. Branch safety

- Never commit directly to `main`. If that's the current branch, create a
  branch first and say which one you made.
- This repo's working branches are named `claude/<topic>`.

## 5. Commit, then report

Commit, then run `git log --oneline -1` and show it.

If `--push` was passed, push with `git push -u origin <current-branch>`. On a
network failure retry up to 4 times, backing off 2s, 4s, 8s, 16s. Do not open
a pull request — that takes a separate, explicit ask.

If nothing is staged and the tree is clean, just say so. Don't invent a commit.
